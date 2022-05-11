from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="vector-body")
    ptags = results.find_all("p")
    output = 0
    for ptag in ptags:
        tag_content = ptag.text
        if "citation needed" in tag_content:
            output += 1
    return output


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="vector-body")
    ptags = results.find_all("p")
    output = ""
    for ptag in ptags:
        tag_content = ptag.text
        if "citation needed" in tag_content:
            output += tag_content
            output += "\n\n"
    return output


URL = "https://en.wikipedia.org/wiki/Environmental_racism"
print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))
