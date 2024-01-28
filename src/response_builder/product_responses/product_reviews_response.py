def get_product_review_response(vendor_response) -> dict:
    """This function prepares the final API response to be returned"""
    product_top_reviews = vendor_response['product']['top_reviews']
    return product_top_reviews
