from playwright.sync_api import sync_playwright
import configparser
import os

def read_properties_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['Settings']


def run():
    properties = read_properties_file('config.ini')
    pdf_download_url = properties['pdf_download_url']
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(pdf_download_url)

    page.wait_for_timeout(2000)  
    with page.expect_download() as download_info:
        page.click('text="Download a Printable PDF of this Cheat Sheet"')
    download = download_info.value
    download.save_as(download.suggested_filename)

    filename = os.path.basename(download.suggested_filename)
    if os.path.exists(filename):
        print("PDF file is downloaded successfully.")
    else:
        print("PDF file is not downloaded.")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run()
