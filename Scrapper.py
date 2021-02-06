# Package Import
import re
import requests
from bs4 import BeautifulSoup
# Excel Drivers
import csv

# URL Data
jobKeyword = 'Software Engineer'
jobLocation = 'San Diego'

# URL Construct
URL_BASE = 'https://www.monster.com/jobs/search/?q='
URL_CRITERIA = jobKeyword + '&where=' + jobLocation
URL = URL_BASE + URL_CRITERIA


# GET Webpage at URL
page = requests.get(URL)

# Parse into more manageable content
parsedContennt = BeautifulSoup(page.content, 'html.parser')

# Filter content for Job Listings
jobResults = parsedContennt.find(id='ResultsContainer')
jobs = jobResults.find_all('section', class_='card-content')

# Open CSV file for input
with open('Scrapper_Data.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter= ',')

    #Loop through each job entry
    for job in jobs:
        # Locate Job's Title
        jobTitle = job.find('h2', class_='title')
        jobCompany = job.find('div', class_='company')
        jobLocation = job.find('div', class_='location')
        jobPostDate = str(job.find('time'))
        date = re.search(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', jobPostDate)
        if None in (jobTitle, jobCompany, jobLocation):
            continue
        title = jobTitle.text.strip()
        company = jobCompany.text.strip()
        location = jobLocation.text.strip()

        dataWriter.writerow([title, company, location, date])
