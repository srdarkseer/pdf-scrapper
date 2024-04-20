import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import os

def download_and_save_pdf(url, session):
    try:
        response = session.get(url)
        response.raise_for_status()  # Check if the download was successful

        # Generate a safe filename from the URL
        filename = url.split('/')[-1]
        filepath = os.path.join('downloaded_pdfs', filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)
        return filepath
    except requests.HTTPError as e:
        print(f"Failed to download {url}: {str(e)}")
        return None

# Create a directory to store downloaded PDFs
if not os.path.exists('downloaded_pdfs'):
    os.mkdir('downloaded_pdfs')

# Make a GET request to the website
url = "https://arxiv.org/archive/astro-ph"
session = requests.Session()  # Use a session object for connection pooling
response = session.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the links to the PDF files
list_of_pdf = set()
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith(".pdf"):
        list_of_pdf.add(href)

# Download the PDF files
pdf_paths = []
for pdf_url in list_of_pdf:
    filepath = download_and_save_pdf(pdf_url, session)
    if filepath:
        pdf_paths.append(filepath)

# Extract information from the downloaded PDF files
for pdf_path in pdf_paths:
    try:
        with open(pdf_path, 'rb') as f:
            pdf_file = PdfReader(f)
            metadata = pdf_file.metadata  # Corrected to access metadata
            number_of_pages = len(pdf_file.pages)
            print(f"PDF file: {pdf_path}")
            print(f"Author: {metadata.get('/Author', 'Unknown')}")
            print(f"Creator: {metadata.get('/Creator', 'Unknown')}")
            print(f"Producer: {metadata.get('/Producer', 'Unknown')}")
            print(f"Subject: {metadata.get('/Subject', 'Not specified')}")
            print(f"Title: {metadata.get('/Title', 'Untitled')}")
            print(f"Number of pages: {number_of_pages}\n")
    except Exception as e:
        print(f"Error reading {pdf_path}: {str(e)}")
