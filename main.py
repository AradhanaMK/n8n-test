from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI Example", version="1.0")

# ------------------------------
#   HOME ROUTE
# ------------------------------
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


# ------------------------------
#   QUERY PARAMETERS
# ------------------------------
@app.get("/greet/")
def greet(name: str = "User"):
    return {"message": f"Hello {name}!"}


# ------------------------------
#   PATH PARAMETER
# ------------------------------
@app.get("/square/{number}")
def square_number(number: int):
    return {"number": number, "square": number * number}


# ------------------------------
#   CALCULATOR (POST)
# ------------------------------
class CalcRequest(BaseModel):
    a: float
    b: float
    operation: str   # add, sub, mul, div

@app.post("/calculator")
def calculator(req: CalcRequest):
    if req.operation == "add":
        result = req.a + req.b
    elif req.operation == "sub":
        result = req.a - req.b
    elif req.operation == "mul":
        result = req.a * req.b
    elif req.operation == "div":
        if req.b == 0:
            return {"error": "Division by zero not allowed"}
        result = req.a / req.b
    else:
        return {"error": "Invalid operation. Use add, sub, mul, div."}

    return {
        "a": req.a,
        "b": req.b,
        "operation": req.operation,
        "result": result
    }
