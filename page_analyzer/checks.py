from bs4 import BeautifulSoup


def get_check(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    h1 = soup.h1.string if soup.h1 else ''
    title = soup.title.string if soup.title else ''
    if soup.find('meta', {'name': 'description'}):
        description = soup.find('meta', {'name': 'description'})['content']
        if len(description) > 255:
            description = f'{description[:254]}'
    else:
        description = ''
    return h1, title, description
