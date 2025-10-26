from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_linkedin_jobs(keyword, num_jobs=5):
    """Scrape job listings from LinkedIn based on a keyword."""

    print(f"🔎 Searching LinkedIn for: {keyword}")
    options = Options()
    options.add_argument("--headless=new")   # Headless mode for automation
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    search_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword.replace(' ', '%20')}"
    driver.get(search_url)
    time.sleep(4)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_cards = soup.find_all("div", class_="base-card")[:num_jobs]

    jobs = []
    for card in job_cards:
        try:
            title = card.find("h3", class_="base-search-card__title").get_text(strip=True)
            company = card.find("h4", class_="base-search-card__subtitle").get_text(strip=True)
            link = card.find("a", class_="base-card__full-link")["href"]
            jobs.append({"title": title, "company": company, "link": link})
        except AttributeError:
            continue

    driver.quit()
    print(f"✅ Scraped {len(jobs)} job listings successfully.")
    return jobs
