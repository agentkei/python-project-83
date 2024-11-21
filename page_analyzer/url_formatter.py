from urllib.parse import urlparse


def formate(url):
    if url:
        norm_url = urlparse(url)
        norm_url = f"{norm_url.scheme}://{norm_url.netloc}"
        return norm_url
    return ''
