# Package Import
import re
import requests
from bs4 import BeautifulSoup
import html5lib
# CSV Library
import csv

# URL Data
jobKeyword = 'Software Engineer'
jobLocation = 'San Diego'

jobTypeDict = {
    "J" : r"(?i)(java)\b",
    "N" : r"(?i)(\.?)(net)\b",
    "F" : r"(?i)(full)\s?(stack)"
}


# URL Construct
URL_BASE = 'https://www.monster.com/jobs/search/?q='
URL_CRITERIA = jobKeyword + '&where=' + jobLocation
URL = URL_BASE + URL_CRITERIA + '&stpage=1&page=3'


# GET Webpage at URL
page = requests.get(URL)

# Parse into more manageable content
parsedContent = BeautifulSoup(page.content, 'html5lib')

# Filter content for Job Listings
jobResults = parsedContent.find(id='ResultsContainer')
jobs = jobResults.find_all('section', class_='card-content')

jobFilter = input("Enter 'A' to search for all jobs or:\nEnter 'J' for Java jobs\nEnter 'N' for .Net jobs\nEnter 'F' for Fullstack jobs\n")

# Open CSV file for input
with open('Scrapper_Data.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter= ',')
    
    foundTrigger = False
    #Loop through each job entry
    for job in jobs:
        # Find HTML element for the Job title, Company, and Location
        jobTitle = job.find('h2', class_='title')
        
        if jobFilter != 'A':
            jobTypeSearch = re.search(jobTypeDict[jobFilter], str(jobTitle))
            if jobTypeSearch == None:
                continue
        jobCompany = job.find('div', class_='company')
        jobLocation = job.find('div', class_='location')
        jobDesc = str(job.find(id='JobDescription'))

        # Check to see if any fields are blank. Causes problems otherwise
        if None in (jobTitle, jobCompany, jobLocation):
            continue

        # Strip white spaces from parsed strings
        title = jobTitle.text.strip()
        company = jobCompany.text.strip()
        location = jobLocation.text.strip()

        # Write data to a new row in the CSV file
        dataWriter.writerow([title, company, location])
        foundTrigger = True
        print("Title: " + title + "\nCompany: " + company + "\nLcoation: " + location +"\n\n")
if (not foundTrigger):
    print('   No jobs found with provided criteria.')