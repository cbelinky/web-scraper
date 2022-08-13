import requests
import pandas as pd
from bs4 import BeautifulSoup


def create_list(x, y):
    """
    Extracts the text from each item in a list created by the .find_all function of bs4 and
        stores the text in a second list

            Args:
                x (list): a list of all the tags or strings that match a particular criteria

                y (list): a second list to store the text retrieved from each item in the
                    first list

            Side effects:
                populates second list
    """
    for i in x:
        x = i.text
        y.append(x)


year = input("Enter a year: ")

# url definition
url = str("https://www.boxofficemojo.com/year/world/" + year)
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# Filter by film title
title = soup.find_all("a", class_="a-link-normal")[17:67]

# Filter by rank
rank = soup.find_all(
    "td",
    class_="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column",
)[:50]

# Filter by worldwide box office revenue
revenue = soup.find_all("td", class_="a-text-right mojo-field-type-money")[0:150:3]

film_titles = []
film_ranks = []
box_office_earnings = []

create_list(title, film_titles)
create_list(rank, film_ranks)
create_list(revenue, box_office_earnings)

# using populated lists to create a dataframe using pandas
df = pd.DataFrame(
    {
        "Rank": film_ranks,
        "Release Group": film_titles,
        "Worldwide Box Office": box_office_earnings,
    }
)

df.to_csv(str(year + "data.csv"), index=False)

print("Success!")
