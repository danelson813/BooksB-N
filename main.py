# BooksB&N/main.py
from helpers.helpers import get_soup, parse_books
import pandas as pd
from tqdm import tqdm


# set variables
results = {}
finished_list = []
fin_list = []

for i in tqdm(range(1, 6)):
    url = f"https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page={i}"
    soup = get_soup(url)
    books = soup.select_one('ol.product-shelf-list').select('li')
    fin_list = parse_books(books, finished_list)

# pandas manipulations
df = pd.DataFrame(fin_list)
df.to_csv("data/List of Books.csv", index=False)
