import csv
import logging
import requests
from bs4 import BeautifulSoup
import re

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

results = []


def create_screenshots(context, name_image):
    logging.info('Init save screenshot ' + name_image)
    context.driver.save_screenshot("screenshots/" + name_image)
    logging.info('End save screenshot ' + name_image)


def save_results(name, result, description_error):
    result = {
        'name': name, 'result': result, 'description_error': description_error
    }
    results.append(result)


def save_csv(name):
    logging.info('Init Create report ' + name)
    with open('reports/' + name, 'w', newline='') as file_csv:
        fields = ['name', 'result', 'description_error']
        writer_csv = csv.DictWriter(file_csv, fieldnames=fields)
        writer_csv.writeheader()
        for result in results:
            writer_csv.writerow(result)
    logging.info('End Create report ' + name)


def extract_paragraph_with_text(url, search_text):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.getText()
    phrases = re.split(r'[.!?]', text)

    find_phrase = ''

    for phrase in phrases:
        if search_text in phrase:
            find_phrase = phrase.strip()
            break
    logging.info('Paragraph ' + str(find_phrase))
    return find_phrase


def find_year_in_text(text):
    pattern = r"\b\d{4}\b"
    return re.findall(pattern, text)
