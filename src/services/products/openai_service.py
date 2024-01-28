from src.config.product_config import OpenAIAPIConfig

import openai
import logging
import json


def get_prompt_message(product_reviews) -> list:
    prompt_messages = [review['body'] for review in product_reviews]
    return prompt_messages


def summarise_product_reviews(product_reviews) -> str:
    """This function uses OPENAI API and summarises the customer reviews received & returns it"""
    try:
        logging.info(f"#src #services #product #openai_service.py #summarise_product_reviews #product_reviews:"
                     f" {product_reviews}")
        prompt_messages = get_prompt_message(product_reviews)

        openai.api_key = OpenAIAPIConfig.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
            prompt=prompt_messages,
            max_tokens=150,
            temperature=0.7
        )

        # prepare summary of the customer reviews
        product_review_summary = response['choices'][0]['text']

        logging.info(f"#src #services #product #openai_service.py #summarise_product_reviews #product_review_summary:"
                     f" {product_review_summary}")
        if product_review_summary:
            return product_review_summary.strip()
        else:
            return ""
    except Exception as err:
        logging.error(f"#src #services #product #openai_service.py #summarise_product_reviews #ERROR: {str(err)}")
        return ""
