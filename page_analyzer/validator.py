import validators
from page_analyzer.url_formatter import formate

def validate(url):
    errors = {}
    normalized_url = formate(url)
    if not url:
        errors['without_url'] = 'URL обязателен'
    if url and (not validators.url(normalized_url)
                or len(normalized_url) > 255):
        errors['incorrect_url'] = 'Некорректный URL'
    return errors
