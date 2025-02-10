#this script belongs to Morris Zuniga date: 07/01/2024.
#this script uses beautifulSoup to scrape data from a web page
#in This case we are scraping my github page for my name "Morris Zuniga" 
#and writing the information found to a csv file

from bs4 import BeautifulSoup
import requests
import csv

# URL of the webpage to scrape
url = 'https://github.com/MorrisAZ'  

response = requests.get(url)


response.encoding = response.apparent_encoding

#parsing the HTML page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting from the <title> tag within the <head> tag 
#this was found by examining the web page and locating where the name could be found on page
title = soup.find('title').text.strip()
print("Page Title:", title)

# Search for the specific name in the entire HTML document
name_to_search = "Morris A. Zuniga"
name_tags = soup.find_all(string=lambda text: text and name_to_search in text)

#prepapring data to write to csv file
csv_data = [[tag.strip()] for tag in name_tags]
csv_file = 'found_names.csv'


# Writing data to CSV file and saving to same directory the python script is found
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Found Name'])  # header of csv file
    writer.writerows(csv_data)  # Write data

print(f"Data has been written to {csv_file}")

