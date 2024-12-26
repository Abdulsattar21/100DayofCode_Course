from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", rel="noreferrer") #class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

# this is the same as the previous loop:
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])


# print(article_texts)
# print(article_links)
# print(article_upvotes)




soup.find_all(name="td")
all = soup.select(selector="td a", class_="title")

print(all)
print(len(all))



with open("website.html", errors="ignore") as file:
    contents = file.read()

# so if we want to use xml format instead of HTML we need to import it and write "lxml" instead of "html.parser"

soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title.string)
# print(soup.name)
# print(soup)
# print(soup.prettify()) # everything looks good

# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText()) # to get the text
#     print(tag.get("href")) # getting the links

# heading = soup.find(name = "h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a") # you  can do this for name and class
print(company_url)

"""
There is a difference between find and find_all searching
"""
