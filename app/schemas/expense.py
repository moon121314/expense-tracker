from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)


class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str