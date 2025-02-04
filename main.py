import math
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import asyncio

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
async def root():
    return {"message": "Number Classification API is running"}

# Global exception handler for non-integer inputs
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "number": request.query_params.get("number", "unknown"),
            "error": True
        }
    )

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n <= 0:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

def is_armstrong_number(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

async def get_fun_fact(number: int) -> str:
    """Fetch a fun fact about the number from Numbers API."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://numbersapi.com/{number}")
            return response.text if response.status_code == 200 else "No fun fact available"
    except Exception:
        return "No fun fact available"

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Number to classify")):
    """Classify a number and return its properties."""
    # Validate input is an integer
    try:
        number = int(number)
    except ValueError:
        raise ValueError(f"Invalid input: {number}")
    
    properties = []
    
    # Determine number properties
    if number % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")
    
    if is_prime(number):
        properties.append("prime")
    
    if is_perfect_number(number):
        properties.append("perfect")
    
    if is_armstrong_number(number):
        properties.append("armstrong")
    
    # Get digit sum
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Get fun fact
    fun_fact = await get_fun_fact(number)
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect_number(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)