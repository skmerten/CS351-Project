# Package Import
import requests
from bs4 import BeautifulSoup
# Excel Drivers
import csv

# URL Data
jobKeyword = 'Software Engineer'
jobLocation = 'San Diego'

URL_BASE = 'https://www.monster.com/jobs/search/?q='
URL_CRITERIA = jobKeyword + '&where=' + jobLocation
URL = URL_BASE + URL_CRITERIA


# GET URL
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')


job_elems = results.find_all('section', class_='card-content')

with open('Scrapper_Data.csv', 'w', newline='') as csvfile:
    #dataWriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    dataWriter = csv.writer(csvfile, delimiter= ',')
    for job_elem in job_elems:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        if None in (title_elem, company_elem, location_elem):
            continue
        title = title_elem.text.strip()
        company = company_elem.text.strip()
        location = location_elem.text.strip()

        dataWriter.writerow([title, company, location])
