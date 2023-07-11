import warnings

import click
import html2text
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

warnings.filterwarnings("ignore")
from minichain.utils.disk_cache import disk_cache


@disk_cache
def markdown_browser(url):
    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Initialize WebDriver with options (Chrome in this example)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # Load the webpage
    driver.get(url)
    # Get the HTML of the page after JavaScript execution
    html = driver.page_source
    # Close the driver
    driver.quit()
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Convert HTML to markdown
    markdown = html2text.html2text(str(soup))
    return markdown


@click.command()
@click.argument("url")
def main(url):
    print(url)
    print(markdown_browser(url))


if __name__ == "__main__":
    main()
