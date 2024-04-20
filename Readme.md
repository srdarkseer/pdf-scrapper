##  README.md

**Astro-ph PDF Downloader**

This Python script downloads and extracts information from PDF files.

**Requirements:**

* Python 3.x
* `requests` library: Install with `pip install requests`
* `beautifulsoup4` library: Install with `pip install beautifulsoup4`
* `PyPDF2` library: Install with `pip install PyPDF2`

**Instructions:**

1. Download and install the required libraries (listed above).
2. Save the script as `astro_ph_downloader.py`.
3. Run the script from your terminal: `python astro_ph_downloader.py`

**Script Functionality:**

* The script first creates a directory named `downloaded_pdfs` to store downloaded PDFs.
* It then retrieves the HTML content of the arXiv astrophysics homepage.
* The script parses the HTML content to extract links to all PDF files on the page.
* It iterates through the extracted links and attempts to download each PDF using the `requests` library.
* Downloaded PDFs are saved with filenames derived from their URLs.
* For each successfully downloaded PDF, the script attempts to extract metadata using the `PyPDF2` library. 
* The extracted information includes author, creator, producer, subject, title, and number of pages.
* Information is printed to the console for each processed PDF.

**Error Handling:**

* The script includes error handling to catch download failures and exceptions during PDF processing.
* Download errors and exceptions encountered while reading PDFs are printed to the console.

**Note:**

* This script retrieves information from the first page of the arXiv astrophysics archive. 
* To download PDFs from other pages, modifications to the scraping logic would be necessary.
* Be aware of arXiv's terms of service when using their data.

**Further Development:**

* The script can be extended to download PDFs from specific arXiv categories (e.g., astro-ph.GA for Galaxies) using the category codes in the URL.
* Extracted metadata can be saved to a file for further analysis.

I hope this README provides a clear explanation of the script's functionality!
