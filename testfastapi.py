from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class NumberList(BaseModel):
    numbers: list


def calculate_largest_number(numbers: list) -> float:
    if not numbers:
        raise ValueError("The list cannot be empty.")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numbers.")
    return max(numbers)

@app.post("/largest-number/")
async def get_largest_number(number_list: NumberList):
    try:
        largest_number = calculate_largest_number(number_list.numbers)
        return {"largest_number": largest_number}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Note: You would typically have test functions below this line to ensure the correctness of your logic.