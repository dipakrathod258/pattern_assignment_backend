def get_product_review_response(vendor_response) -> dict:
    """This function prepares the final API response to be returned"""
    product_top_reviews = vendor_response['product']['top_reviews']
    return product_top_reviews


def get_product_review_summarise_response(asi_number, doc_inserted_id, product_review_summary) -> dict:
    """This function prepares the final API response to be returned"""
    formatted_response = {
        "product_asin_number": asi_number,
        "product_review_summary": product_review_summary,
        "doc_inserted_id": doc_inserted_id
    }
    return formatted_response
