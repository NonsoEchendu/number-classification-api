# Number Classification API

## Project Overview

This FastAPI-based microservice provides comprehensive mathematical classification and analysis for integer inputs.

## 🚀 Features

- **Number Classification**: Identifies mathematical properties of integers
- **Fun Facts**: Retrieves interesting trivia about numbers
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **Async Processing**: Non-blocking request handling

## 🛠 Prerequisites

- Python 3.9+
- pip
- Virtual Environment (recommended)

## 📦 Dependencies

- FastAPI
- Uvicorn
- httpx
- Python Standard Library

## 🔧 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Development Mode
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Production Deployment
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 🌐 API Endpoints

### Root Endpoint
- **GET /** 
  - Returns service health check
  - Response: `{"message": "Number Classification API is running"}`

### Number Classification
- **GET /api/classify-number**
  - Parameters: `number` (integer)
  - Returns comprehensive number analysis

#### Example Request
```bash
curl "http://localhost:8000/api/classify-number?number=371"
```

#### Successful Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## 🔍 Number Properties Analyzed

- Parity (Odd/Even)
- Prime Number
- Perfect Number
- Armstrong Number
- Digit Sum

## 📋 Error Handling

- Non-integer inputs trigger 400 Bad Request
- Graceful error responses with descriptive messages

## 🐳 Docker Support

### Build Docker Image
```bash
docker build -t number-classification-api .
```

### Run Docker Container
```bash
docker run -p 8000:8000 number-classification-api
```

## 🔐 Security

- CORS configured for all origins
- Input validation
- Async architecture prevents blocking

## 🧪 Testing

### Run Tests
```bash
# Add testing command (placeholder)
pytest
```

## 📝 License

[Add your license information]

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## 📞 Support

For issues or questions, please [add contact method or issue tracker link]