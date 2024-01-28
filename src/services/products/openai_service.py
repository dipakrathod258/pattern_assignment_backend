from src.config.product_config import OPENAI_API_KEY

import openai
import logging


def summarise_product_reviews(prompt_messages):
    """This function uses OPENAI API and summarises the customer reviews received & returns it"""
    try:
        logging.info(f"#src #services #product #openai_service.py #summarise_product_reviews #prompt_messages:"
                     f" {prompt_messages}")
        openai.api_key = OPENAI_API_KEY
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
            prompt=prompt_messages,
            max_tokens=150,  # Adjust as needed
            temperature=0.7  # Adjust as needed
        )

        # prepare summary of the customer reviews
        product_review_summary = response['choices'][0]['text']
        if product_review_summary:
            return product_review_summary
        else:
            return None
    except Exception as err:
        logging.error(f"#src #services #product #openai_service.py #summarise_product_reviews #ERROR: {str(err)}")
        return None
