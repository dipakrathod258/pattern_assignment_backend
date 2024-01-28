from pydantic import BaseModel


class ProductReviewData(BaseModel):
    asi_number: str
