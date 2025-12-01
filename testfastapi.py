from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request model
class NumberList(BaseModel):
    numbers: List[float]

@app.get("/")
def home():
    return {"message": "FastAPI Largest Number API"}

# POST API to find largest number
@app.post("/largest")
def find_largest_number(data: NumberList):
    if not data.numbers:
        return {"error": "List cannot be empty"}

    largest_number = max(data.numbers)
    return {
        "numbers": data.numbers,
        "largest": largest_number
    }
