class ProductAPIConfig:
    PRODUCT_API_URL = "https://api.rainforestapi.com/request"
    # PRODUCT_API_URL = "https://jsonplaceholder.typicode.com/todos/1"


class ProductReviewMongodbConfig:
    MONGODB_NAME = "amazon_products"
    MONGODB_COLLECTION_NAME = "amazon_products"


class ProductReviewSummaryMongodbConfig:
    MONGODB_NAME = "product_review_summaries"
    MONGODB_COLLECTION_NAME = "product_review_summaries"
