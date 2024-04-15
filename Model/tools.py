import requests
import traceback
import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


class ResponseFormatError(Exception):
    """Custom exception to indicate incorrect response format."""
    def __init__(self, message, status_code=None, headers=None):
        self.message = message
        self.status_code = status_code
        self.headers = headers
        super().__init__(message)


def response_to_json(url):
    """
    Goal is to call an API, and get a JSON response returned

    Parameters:
        url: The url with which to reach API

    Returns:
        API Response in JSON format
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type:
            return response.json()
        else:
            raise ResponseFormatError("Expected JSON response format, but got different.",
                                      status_code=response.status_code,
                                      headers=response.headers)
    except requests.HTTPError as e:
        traceback.print_exc()
        print(f"HTTP error occurred: {e}")  # More specific message about HTTP errors
        return None
    except requests.RequestException as e:
        traceback.print_exc()
        print(f"Network-related error occurred: {e}")
        return None
    except ResponseFormatError as e:
        traceback.print_exc()
        print(f"Response format error: {e}")
        return None
    except Exception as e:  # Generic exception should be last
        traceback.print_exc()
        print(f"An unexpected error occurred: {e}")
        return None
