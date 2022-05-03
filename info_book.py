import requests
from bs4 import BeautifulSoup


def get_book(url_book):
    """
    Fonction qui récupère sous forme de dictionnaire les informations d'un
    livre, elle prend en parametre l'url d'un livre en chaine de caractere
    """
    response = requests.get(url_book)
    soup = BeautifulSoup(response.text, 'html.parser')

    information_book = {}

    # récupère le titre
    information_book['title'] = soup.find('h1').text

    # récupère l'URL du livre
    information_book['url'] = url_book

    # récupère la catégorie
    path = soup.select('ul.breadcrumb')
    for category_book in path:
        information_book['category'] = category_book.select('li')[
            2].text.strip()

    # récupère la description
    information_book['descriptilon'] = soup.select('article > p')[0].text

    # récupère le nombre d'étoile
    information_book['review_rating'] = soup.find(
        "p", class_="star-rating").get("class")[1]

    # récupère les informations
    product_information = soup.select('table')
    for info in product_information:
        information_book['universal_product_code'] = info.select('td')[0].text
        information_book['price_excluding_tax'] = info.select('td')[2].text
        information_book['price_including_tax'] = info.select('td')[3].text
        information_book['number_available'] = info.select('td')[5].text

    # récupère l'image
    img_book = soup.select('img')[0]
    information_book['image_url'] = "https://books.toscrape.com/" + \
        img_book.get('src').strip('../../')

    return information_book
