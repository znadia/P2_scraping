import requests
from bs4 import BeautifulSoup


def get_links_books(links_cat):
    """
    Fonction qui récupère sous forme de dictionnaire les urls des
    livres de chaque categorie, elle prend en parametre l'url
    d'une categorie. {"categorie" : ["url_book", "url_book"]}
    """
    links = {}

    for link_cat_list_key, link_cat_list_values in links_cat.items():
        for link_cat in link_cat_list_values:
            pages_category = BeautifulSoup(requests.get(
                link_cat).text, 'html.parser').findAll("h3")

            # récupère les urls des livres par categories
            for page in pages_category:
                a = page.find("a")
                book = a["href"].strip('../../../')
                category_name = link_cat_list_key.split('_')[0]
                url_book = ('https://books.toscrape.com/catalogue/' + book)

                try:
                    links[category_name].append(url_book)
                    print("book url: ", book)

                except KeyError:
                    links[category_name] = [url_book]
                    print("book url: ", book)

    print("------ all book urls have been retrieved ------\n")

    return links
