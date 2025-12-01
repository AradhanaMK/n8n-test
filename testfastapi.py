from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    values: list[int]

@app.post("/largest")
def get_largest_number(numbers: Numbers):
    if not numbers.values:
        raise HTTPException(status_code=400, detail="List of numbers cannot be empty.")
    largest = max(numbers.values)
    return {"largest": largest}

# Additional future improvements can include separating request model and business logic into separate modules.