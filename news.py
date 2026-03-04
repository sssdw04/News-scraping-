import requests
from bs4 import BeautifulSoup
import json

articles_data = []

url = "https://english.onlinekhabar.com/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a", href=True):
    text = link.get_text()

    
    if "election" in text.lower() or "vote" in text.lower():
        article_url = link["href"]

        article_page = requests.get(article_url)
        article_page.encoding = "utf-8"
        article_soup = BeautifulSoup(article_page.text, "html.parser")

        #headline
        headline_tag = article_soup.find("h1")
        if headline_tag:
            headline = headline_tag.get_text(strip=True)
        else:
            headline = "No headline found"

        #newsbody
        paragraphs = article_soup.find_all("p")
        body = ""
        for p in paragraphs:
            body += p.get_text(strip=True) + " "

        #summarize
        sentences = body.split(". ")
        summary = ". ".join(sentences[:3])

       
        articles_data.append({
            "source": "Onlinekhabar",
            "headline": headline,
            "summary": summary,
            "url": article_url
        })

        break   


url = "https://nagariknews.nagariknetwork.com/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a", href=True):

    text = link.get_text()

    if "निर्वाचन" in text or "चुनाव" in text:

        article_url = link["href"]

        article_page = requests.get(article_url)
        article_page.encoding = "utf-8"
        article_soup = BeautifulSoup(article_page.text, "html.parser")

        headline_tag = article_soup.find("h1")

        if headline_tag:
            headline = headline_tag.get_text(strip=True)
        else:
            headline = "No headline found"

        paragraphs = article_soup.find_all("p")

        body = ""
        for p in paragraphs:
            body += p.get_text(strip=True) + " "

        sentences = body.split(". ")
        summary = ". ".join(sentences[:3])

        articles_data.append({
            "source": "Nagarik News",
            "headline": headline,
            "summary": summary,
            "url": article_url
        })

        break


url = "https://www.setopati.com/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a", href=True):

    text = link.get_text()

    if "निर्वाचन" in text or "चुनाव" in text:

        article_url = link["href"]

        article_page = requests.get(article_url)
        article_page.encoding = "utf-8"
        article_soup = BeautifulSoup(article_page.text, "html.parser")

        headline_tag = article_soup.find("h1")

        if headline_tag:
            headline = headline_tag.get_text(strip=True)
        else:
            headline = "No headline found"

        paragraphs = article_soup.find_all("p")

        body = ""
        for p in paragraphs:
            body += p.get_text(strip=True) + " "

        sentences = body.split(". ")
        summary = ". ".join(sentences[:3])

        articles_data.append({
            "source": "Setopati",
            "headline": headline,
            "summary": summary,
            "url": article_url
        })

        break

#save to json file
with open("newsarticles1.json", "w", encoding="utf-8") as file:
    json.dump(articles_data, file, indent=4, ensure_ascii=False)


print("News saved to newsarticles1.json")