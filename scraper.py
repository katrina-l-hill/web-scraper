# step 5: need to parse the raw HTML data to make it easier to read.
# import Beautiful Soup

from bs4 import BeautifulSoup

# step 1: import requests

import requests


# step 2: add URL for Wikipedia website of choice

URL = "https://en.wikipedia.org/wiki/Environmental_justice"

# step 3: make a request to the URL using the requests.get() function. Pass in the URL for the website of choice. Variable "page" is common to use

page = requests.get(URL)

# step 4: print the contents of the page of the URL you are requesting. This will return a lot of raw data in HTML form.

# print(page.content)

# step 6: create a BeautifulSoup instance that passes in two parameters
# For the parameters, BeautifulSoup wants to know what is the string it will parse (some string in some form) and what kid of parsing is to be done (the built-in string html.parser).
#

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

# # print the type of soup: it's an instance

# print(type(soup))

# do finds on soup using a criteria you want to use for finding. i.e., find what?
# give it a keyword argument
# find only finds one thing
results = soup.find(class_="vector-body")
# print(results.prettify())

# step 7: perform a find on previously found items. Find all instead of just one.
# Use "results" as the basis for the find.

titles = results.find_all("h3")
print(titles)

# step 8: iterate through the data with a for loop
# this returns list-like data

for title in titles:
    print(title.text)


# shortcut for find_all:
# returns all the anchor tags

anchors = results("a")
print(type(results))  # prints the type of results --> class
print(anchors)

# Iterables can be list comprehensions

links = [anchor["href"] for anchor in anchors]
print(links)


# def get_citations_needed_count(url):
#     pass


# def get_citations_needed_report(url):
#     pass
