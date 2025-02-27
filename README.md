# Number Classification API

## Project Overview

This is a comprehensive mathematical classification and analysis API for integer inputs. It takes a number and returns interesting mathematical proterties about the number, along with a fun fact.

## 🚀 Features

- **Number Classification**: Identifies mathematical properties of integers
- **Fun Facts**: Retrieves interesting trivia about numbers
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **Async Processing**: Non-blocking request handling

## 🛠 Prerequisites

- Python 3.9+
- pip
- Virtual Environment (recommended)

To install these, follow the steps below...

P.s. The steps below are for installing on an Ubuntu-based Linux machine. <br><br>

**1\.Installing Python 3.9+**

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

Verify the installation by running:

```bash
python3 --version
```

It should ouput something like, `Python 3.12.3` <br><br>

**2\. Installing Pip**

```bash
sudo apt install -y python3-pip
```

Verify Intall:

```
pip3 --version
```

It should ouput something like:

```bash
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

## 📦 Dependencies

- FastAPI
- Uvicorn
- httpx
- Python Standard Library

## 🔧 Installation

### 1. Clone Repository
```bash
git clone https://github.com/NonsoEchendu/number-classification-api.git
cd number-classification-api
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Deployment
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

It should look like this if it starts successfully: 

![terminal-app-successful](<Screenshot 2025-02-04 at 18.04.37.png>)

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
curl "http://localhost:8000/api/classify-number?number=153"
```

#### Successful Response (200 OK)
```json
{
    "number": 153,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
      "odd",
      "armstrong"
    ],
    "digit_sum": 9,
    "fun_fact": "153 is the ordinal number of the coat of arms of Komi Republic in the State Heraldic Register of the Russian Federation."
}
```

On browser, here's how it looks:

![alt text](<Screenshot 2025-02-04 at 18.25.12.png>)


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

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/license/MIT).

## 🤝 Contributing

Contributions are welcome! To contribute do the following:

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## 💡 Future Improvements

- Web Interface: Provide a dashboard to allow users input desired numbers and view the fun fact and other information.