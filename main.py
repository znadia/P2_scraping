import csv
import urllib.request
import os

from links_category import get_links_category
from links_books import get_links_books
from info_book import get_book


books_toscrape = "https://books.toscrape.com/index.html"

links_category = get_links_category(books_toscrape)
urls_book = get_links_books(links_category)

headers = ['title',
           'url',
           'category',
           'descriptilon',
           'review_rating',
           'universal_product_code',
           'price_excluding_tax',
           'price_including_tax',
           'number_available',
           'image_url']


def downloads_img(dic):
    """
    Fonction qui télécharge l'image d'un livre, elle prend en paramètre
    le dictionnaire qui contient les informations du livre
    """
    img = 'img'

    if not os.path.exists(img):
        os.mkdir(img)

    img_url = dic['image_url']
    title_url = dic['title'].replace("/", "-")
    f = open(img + '/' + title_url + '.jpg', 'wb')
    f.write(urllib.request.urlopen(img_url).read())
    f.close()
    print("     the image upload is successful")


#   Création d'un dossier pour stocker les fichiers CSV
category = "category_csv"

if not os.path.exists(category):
    os.mkdir(category)

"""
Cette étape permet de créer les fichiers CSV, elle parcourt les dictionnaires
créer précédemment afin d'en extraire les informations
"""
for cat, urls in urls_book.items():
    print("-- Creation of the", cat, "file --")
    with open(category + '/' + cat + ".csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for url in urls:
            writer.writerow(get_book(url))
            print("     book information: ", get_book(url)['title'])
            downloads_img(get_book(url))

print("********* All information has been successfully retrieved *********")
