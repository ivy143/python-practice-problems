# Web scraper for job listings
import requests
from bs4 import BeautifulSoup
import csv
def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = []

    for job_card in soup.find_all('div', class_='job-card'):
        title = job_card.find('h2', class_='job-title').text.strip()
        company = job_card.find('div', class_='company-name').text.strip()
        location = job_card.find('div', class_='job-location').text.strip()
        job_listings.append({
            'title': title,
            'company': company,
            'location': location
        })

    return job_listings
def save_to_csv(job_listings, filename):
    keys = job_listings[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(job_listings)
# Example usage
url = 'https://example.com/jobs'  # Replace with a real job listings URL
job_listings = scrape_job_listings(url)
save_to_csv(job_listings, 'job_listings.csv')
print("Job listings have been saved to job_listings.csv")
# Note: The above URL is a placeholder. To run this code, replace it with a valid job listings webpage URL and ensure the HTML structure matches the selectors used in the code.