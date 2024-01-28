import time

from config.http_configs import HttpStatusCodes
from config.product_config import AmazonRainforestConfig
from connections.mongo_connections import insert_doc_to_mongodb
from response_builder.product_responses.product_reviews_response import get_product_review_response, \
    get_product_review_summarise_response
from services.products.constants import ProductAPIConfig, ProductReviewMongodbConfig, ProductReviewSummaryMongodbConfig

import requests
import logging

from src.services.products.openai_service import summarise_product_reviews


def make_request_amazon_rainforest(asi_number):
    """
    :param asi_number: This function receives ASIN Number
    :return: Calls the Rainforest API and sends the response as it is received from Vendor
    """
    logging.info(f"#src #services #products #product_marketplace_services #get_product_reviews"
                 f" #make_request_amazon_rainforest asi_number: {asi_number}")
    url = ProductAPIConfig.PRODUCT_API_URL
    params = {
        'api_key': AmazonRainforestConfig.AMAZON_RAINFOREST_API_KEY,
        'type': 'product',
        'asin': asi_number,
        'amazon_domain': 'amazon.com'
    }
    logging.info(f"#src #services #products #product_marketplace_services #get_product_reviews"
                 f" #make_request_amazon_rainforest url: {url} params: {params}")

    response = requests.get(url, params)
    logging.info(f"#src #services #products #product_marketplace_services #get_product_reviews"
                 f" #make_request_amazon_rainforest response:"
                 f" {response}")
    return response


def get_product_reviews(request_payload):
    """
    :param request_payload: The payload received in API request that contains ASIN Number
    :return: Gets the product review details from Amazon Rainforest API and returns it
    """
    try:
        logging.info(f"#src #services #products #product_marketplace_services #get_product_reviews request_payload: "
                     f"{request_payload}")

        asi_number = request_payload.asi_number
        logging.info(f"#src #services #products #product_marketplace_services #get_product_reviews asi_number: "
                     f"{asi_number}")

        # Make API request to Amazon Rainforest
        response = make_request_amazon_rainforest(asi_number)

        response_status_code = response.status_code
        vendor_response = response.json()

        mongodb_doc = {
            "product_asin": asi_number,
            "vendor_response": vendor_response
        }

        if response.status_code == HttpStatusCodes.HTTP_200_SUCCESS:
            # Inserting API response first in MongoDB before returning

            doc_inserted_id = insert_doc_to_mongodb(ProductReviewMongodbConfig.MONGODB_NAME,
                                                    ProductReviewMongodbConfig.MONGODB_COLLECTION_NAME, mongodb_doc)
            logging.info(
                f"#src #services #products #product_marketplace_services #get_product_reviews doc_inserted_id: "
                f"{doc_inserted_id} for ASIN: {asi_number}")

            if not vendor_response['request_info']['success']:
                return {"status_code": vendor_response['request_info']['http_status_code'],
                        "error_message": vendor_response['request_info']['message']}

            product_review_response = get_product_review_response(vendor_response)
            return {"status_code": response_status_code, "data": product_review_response}
        return {"status_code": response_status_code, "error_message": response.text}
    except Exception as err:
        logging.error(f"#src #services #products #product_marketplace_services #get_product_reviews ERROR: {str(err)} "
                      f"for ASIN Number: {request_payload.asi_number}")
        return {"status_code": HttpStatusCodes.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": "Server Error. Please"
                                                                                                " Contact Admin"}


def get_product_summarised_reviews(request_payload):
    """This function accepts ASIN Numbers pf the product -> calls Amazon API & gets product details -> summarises
    customer reviews and returns it"""
    try:
        logging.info(
            f"#src #services #products #product_marketplace_services #get_product_reviews request_payload: "
            f"request_payload STARTS...")

        response = get_product_reviews(request_payload)

        if 'data' in response.keys():
            product_reviews = response['data']

            product_review_summary = summarise_product_reviews(product_reviews)

            asi_number = request_payload.asi_number
            mongodb_doc = {
                "product_asin": request_payload.asi_number,
                "product_review_summary": product_review_summary,
                "is_product_review_summarised": True
            }
            doc_inserted_id = insert_doc_to_mongodb(ProductReviewSummaryMongodbConfig.MONGODB_NAME,
                                                    ProductReviewSummaryMongodbConfig.MONGODB_COLLECTION_NAME, mongodb_doc)
            if product_review_summary:
                logging.info(
                    f"#src #services #products #product_marketplace_services #get_product_reviews doc_inserted_id: "
                    f"{doc_inserted_id} for ASIN: {asi_number}")
                response_data = get_product_review_summarise_response(asi_number, doc_inserted_id, product_review_summary)
                return {"status_code": HttpStatusCodes.HTTP_200_SUCCESS, "data": response_data}
            else:
                return {"status_code": HttpStatusCodes.HTTP_200_SUCCESS, "data": "Could not summarise reviews of this "
                                                                                 "product"}
        else:
            error_response = {
                "product_review_summary": response['error_message']
            }
            return {"status_code": response['status_code'], "data": error_response}
    except Exception as err:
        logging.error(f"#src #services #products #product_marketplace_services #get_product_summarised_reviews ERROR: "
                      f"{str(err)} for ASIN Number: {request_payload.asi_number}")
        return {"status_code": HttpStatusCodes.HTTP_500_INTERNAL_SERVER_ERROR, "data": "Internal Server Error. Please "
                                                                                       "contact admin"}
