import requests
from bs4 import BeautifulSoup


def scrape_jobs():

    url = "https://boards.greenhouse.io/embed/job_board?for=stripe"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    postings = soup.find_all("div", class_="opening")

    for post in postings:

        title = post.find("a").text.strip()
        link = post.find("a")["href"]

        jobs.append({
            "company": "Stripe",
            "title": title,
            "link": link
        })

    return jobs