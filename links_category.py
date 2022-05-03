import requests
from bs4 import BeautifulSoup


def get_links_category(url):
    """
    Fonction qui récupère sous forme de dictionnaire les urls de chaque
    categorie ainsi que les paginations, elle prend en parametre l'url
    du site. {"categorie" : ["url_cat", "url_cat"]}
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if response.ok:
        first_ul = soup.find('ul', {"class": "nav-list"})
        category_ul = first_ul.find('ul')
        list_category = category_ul.find_all('li')

        links_category = {}
        link = 'https://books.toscrape.com/catalogue/category/books/'

        # récupère les urls des categories
        for page in list_category:
            a_category = page.find("a")
            name_category = a_category["href"].split('/')[3]
            url_category = (link + name_category + '/index.html')
            links_category[name_category] = [url_category]
            pages_next = BeautifulSoup(requests.get(
                url_category).text, 'html.parser').find(
                    "li", {"class": "current"})
            print("Category url: ", name_category)

            if pages_next is None:
                pass

            else:
                pages = str(pages_next.text).strip().split(' ')
                nbr_page = int(pages[3])

                # récupère les urls des pagination des categories
                for i in range(2, nbr_page + 1):
                    url_next_page_cat = (
                        link + name_category + '/page-' + str(i) + '.html')
                    links_category[name_category].append(url_next_page_cat)
                    print("     category pagination")

    print("------ all category urls have been retrieved ------\n")

    return links_category
