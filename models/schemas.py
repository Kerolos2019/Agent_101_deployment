from pydantic import BaseModel, Field
from typing import List, Optional


# ── Step 1: Search Query Generation ──────────────────────────────────────────

class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(
        ...,
        title="Suggested search queries to be passed to the search engine",
        min_length=1,
        max_length=10,
    )


# ── Step 2: Search Results ────────────────────────────────────────────────────

class SingleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="The page URL")
    content: str
    score: float
    search_query: str


class AllSearchResults(BaseModel):
    results: List[SingleSearchResult]


# ── Step 3: Scraped Product Data ──────────────────────────────────────────────

class ProductSpec(BaseModel):
    specification_name: str
    specification_value: str


class SingleExtractedProduct(BaseModel):
    page_url: str = Field(..., title="The original URL of the product page")
    product_title: str = Field(..., title="The title of the product")
    product_image_url: str = Field(..., title="The URL of the product image")
    product_url: str = Field(..., title="The URL of the product")
    product_current_price: float = Field(..., title="The current price of the product")
    product_original_price: Optional[float] = Field(
        default=None,
        title="The original price before discount. None if no discount",
    )
    product_discount_percentage: Optional[float] = Field(
        default=None,
        title="The discount percentage. None if no discount",
    )
    in_stock: bool = Field(
        ...,
        title="Whether the product is currently in stock and available to buy",
    )
    product_specs: List[ProductSpec] = Field(
        ...,
        title="The most important specs to compare (1-5 items)",
        min_length=1,
        max_length=5,
    )
    agent_recommendation_rank: int = Field(
        ...,
        title="Recommendation rank out of 5 (higher is better)",
    )
    agent_recommendation_notes: List[str] = Field(
        ...,
        title="Notes on why this product is or isn't recommended",
    )


class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]


# ── Crew Inputs ───────────────────────────────────────────────────────────────

class CrewInputs(BaseModel):
    product_name: str
    websites_list: List[str]
    country_name: str
    no_keywords: int = 10
    language: str = "English"
    score_th: float = 0.10
    top_recommendations_no: int = 10
