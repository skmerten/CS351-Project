# Package Import
import requests
# Excel Drivers
import xlwt
from xlwt import Workbook

# Create Excel workbook to log locations with miatas
wb = Workbook()
sheet1 = wb.add_sheet('Data')
    # Set row counter
row = 0

# URL Data
jobKeyword = 'Software Engineer'
jobLocation = 'San Diego'

URL_BASE = 'https://www.monster.com/jobs/search/?q='
URL_CRITERIA = jobKeyword + '&where=' + jobLocation
URL = URL_BASE + URL_CRITERIA


# GET URL
page = requests.get(URL)


wb.save('Scrapped Data.xls')