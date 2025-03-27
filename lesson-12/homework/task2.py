import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sqlite3


def set_up_database():
    with sqlite3.connect('jobs.db') as con:
        cur = con.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS Jobs (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,company TEXT,location TEXT,description TEXT, application_link TEXT)')
        con.commit()


def scrape_jobs():
    chrome_options = Options()
    chrome_options.add_argument("--window-position=0, 0")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://realpython.github.io/fake-jobs")
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Extract job listings
    jobs = []
    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip() if job.find("h2", class_="title") else "N/A"
        company = job.find("h3", class_="company").text.strip() if job.find("h3", class_="company") else "N/A"
        location = job.find("p", class_="location").text.strip() if job.find("p", class_="location") else "N/A"
        description = job.find("div", class_="description")
        description_text = description.text.strip() if description else "N/A"
        link = job.find("a", class_="card-footer-item")
        application_link = link['href'] if link else "N/A"

        jobs.append((title, company, location, description_text, application_link))

    return jobs


add = "Insert into Jobs(title, company, location, description, application_link) VALUES (?, ?, ?, ?, ?) "


def save_jobs(jobs):
    with sqlite3.connect('jobs.db') as con:
        cur = con.cursor()
        cur.executemany(add, jobs)

def filter_by_title(title):
    with sqlite3.connect('jobs.db') as con:
        cur = con.cursor()
        jobs = cur.execute("SELECT * FROM Jobs WHERE title LIKE ?", (title+'%',))
        return jobs
def filter_by_company(company):
    with sqlite3.connect('jobs.db') as con:
        cur = con.cursor()
        jobs = cur.execute('SELECT * FROM Jobs WHERE company LIKE ?', (company+'%',))
        return jobs
def filter_by_location(location):
    with sqlite3.connect('jobs.db') as con:
        cur = con.cursor()
        jobs = cur.execute('SELECT * FROM Jobs WHERE location LIKE ?', (location+'%',))
        return jobs
def write_to_csv(jobs, filename='jobs.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('title', 'company', 'location', 'description', 'application_link'))
        for job in jobs:
            writer.writerow(job)

if __name__ == '__main__':
    # set_up_database()
    # jobs_list = scrape_jobs()
    # save_jobs(jobs_list)
    software = filter_by_title("Software Engineer")
    write_to_csv(software)
