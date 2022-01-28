from helium import *
import time
from docx import Document
from docx.shared import Inches

document = Document()

start_chrome('some url', headless = True)

time.sleep(5)
article_list = find_all(S('a'))

href_list = [article.web_element.get_attribute('href') for article in article_list]

for href in href_list:
    if href.startswith('some substring'):
        go_to(href)
        time.sleep(5)
        paragraph_list = find_all(S('p'))
        for paragraph in paragraph_list:
            document.add_paragraph(paragraph.web_element.text)

document.save('Extract.docx')