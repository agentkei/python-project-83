import validators


def validate(url):
    error = {}
    if url is False:
        error['without_url'] = 'URL обязателен'
    if url is True and (not validators.url(url, public=False)
                        or len(url) > 255):
        error['incorrect_url'] = 'Некорректный URL'
    else:
        return error
