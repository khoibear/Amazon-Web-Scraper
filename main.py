import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
amazonURL = "https://www.amazon.com/Nutricost-Whey-Protein-Concentrate-Unflavored/product-reviews/B01KITQG0A/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber={page}"
htmlElements = "//div[@class='a-section review aok-relative']"

with open('reviews.txt', 'w', encoding='utf-8') as f:
    #Number of Amazon review pages to scrap
    for page in range(1, 3):
        url = amazonURL
        browser.get(url)
        time.sleep(5)
        elements = browser.find_elements(By.XPATH, htmlElements)
        for element in elements:
            text = element.text
            html = element.get_attribute('innerHTML').encode('utf-8')
            rating = re.search(r'<span class="a-icon-alt">(.+?)</span>', html.decode()).group(1)
            lines = text.split('\n')
            review = [line for line in lines if "found this helpful" not in line and "Helpful" not in line and "Report" not in line and "Verified Purchase" not in line]
            review_text = '\n'.join(review)
            f.write("Rating: " + rating + '\n')
            f.write(review_text + '\n')
            f.write("=" * 50 + '\n')
        print(f"Page {page} done")

browser.quit()
