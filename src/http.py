import requests

def get_html(url: str) -> str:
    try:
        response = requests.get(url)
        return response.text
    except Exception:
        print("Error while fetching requested webpage, check the url provided or your internet connection")
