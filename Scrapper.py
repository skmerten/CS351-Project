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

parsedContennt = BeautifulSoup(page.content, 'html.parser')
jobResults = parsedContennt.find(id='ResultsContainer')


jobs = jobResults.find_all('section', class_='card-content')

with open('Scrapper_Data.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter= ',')
    for jobs in jobss:
        jobTitle = jobs.find('h2', class_='title')
        jobCompany = jobs.find('div', class_='company')
        jobLocation = jobs.find('div', class_='location')
        if None in (jobTitle, jobCompany, jobLocation):
            continue
        title = jobTitle.text.strip()
        company = jobCompany.text.strip()
        location = jobLocation.text.strip()

        dataWriter.writerow([title, company, location])
