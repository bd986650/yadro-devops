import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

BASE_URL = "https://tools-httpstatus.pickup-services.com/status/"


class HttpStatusError(Exception):
    pass


def make_request(status_code: int) -> None:
    url = f"{BASE_URL}{status_code}"

    logging.info(f"Sending request to {url}")

    response = requests.get(url, timeout=5)

    code = response.status_code
    body = response.text.strip()

    if 100 <= code < 400:
        logging.info(
            f"SUCCESS | status_code={code} | body={body}"
        )
    elif 400 <= code < 600:
        raise HttpStatusError(
            f"ERROR | status_code={code} | body={body}"
        )
    else:
        raise HttpStatusError(
            f"Unexpected status code: {code}"
        )


def main() -> None:
    status_codes = [100, 200, 301, 404, 500]

    for code in status_codes:
        try:
            make_request(code)
        except HttpStatusError as error:
            logging.error(error)
        except requests.RequestException as error:
            logging.error(f"Request failed: {error}")


if __name__ == "__main__":
    main()