from bs4 import BeautifulSoup
from tabulate import tabulate


def parse_source(source, quantity):
    soup = BeautifulSoup(source, 'html.parser')
    rows = soup.find_all("tr")

    data = []
    for index, row in enumerate(rows):

        if index == quantity + 1:
            break

        cols = row.find_all("td")

        # don't check out headers
        if len(cols) > 0:
            game_name = cols[2].text.split('\n')[1]
            discount = cols[3].text.strip()
            price = cols[4].text.strip()
            obj = {
                'name': game_name,
                'discount': discount,
                'price': price
            }
            data.append(obj)
    # print(data)
    return data
            

def show_table(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))