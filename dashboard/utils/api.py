import requests
import time

API_URL = "http://127.0.0.1:8000"


def check_api_status():
    """
    Check whether the FastAPI server is running.
    Returns True if online, otherwise False.
    """

    try:
        requests.get(API_URL)
        return True
    except:
        return False


def predict_purchase(payload):
    """
    Send prediction request to FastAPI.
    Returns prediction result and response time.
    """

    start = time.time()

    response = requests.post(
        f"{API_URL}/predict",
        json=payload
    )

    end = time.time()

    response.raise_for_status()

    result = response.json()

    response_time = round(end - start, 3)

    return result, response_time
