from requests import get
from re import findall


def GoogleImageGrabber(quert: str, limit: int = 20) -> list[str]:
    pages = limit // 20 + 1
    results = []

    for page in range(1, pages+1):
        request = get(f"https://www.google.com/search?q={quert}&tbm=isch&start={page}")

        assert request.status_code == 200, '\n'.join(["Failed get request",
                                                      f"Responce code: {request.status_code}",
                                                      "Response:",
                                                      request.text])

        assert (result := findall(r'https://encrypted-tbn0\.gstatic\.com/images\S+;s', request.text)), \
            "Not found images"

        results.extend(result)

    return results[:limit]
