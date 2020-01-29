from bs4 import BeautifulSoup


def lazysize_images(html):
    soup = BeautifulSoup(html, 'lxml')
    for node in soup.find_all('img'):
        src = node.attrs.pop('src', None)
        if src:
            node.attrs['data-src'] = src
            cl = node.attrs.get('class', [])
            cl.append('lazyload')
            node.attrs['class'] = cl
    body = soup.find('body')
    return body.decode_contents() if body else str(soup)
