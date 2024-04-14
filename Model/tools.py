import requests
import traceback
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

class ResponseFormatError(Exception):
    def __init__(self, message, status_code=None, headers=None):
        self.message = message
        self.status_code = status_code
        self.headers = headers
        super().__init__(message)


def response_to_json(url):
    """
    :param url: The url with which to reach API
    :return: JSON

    Goal is to call an API, and get a JSON response returned
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            content_type = response.headers.get("Content-Type")
            if content_type and "application/json" in content_type:
                return response.json()
            else:
                raise ResponseFormatError("Can't get JSON format of response."
                                          , status_code=response.status_code
                                          , headers=response.headers)
        else:
            raise Exception(f'Request unfulfilled (didn\'t get code 200), or JSON not possible.')

    except requests.RequestException as e:
        # print(e, "request exception")
        traceback.print_exc()
        return None
        # traceback.format_exc()
        # print("End of exception\n\n")
