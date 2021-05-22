from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import os
from PIL import Image, ImageDraw, ImageFont
import random
import pyautogui


def get_soup(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})
    return BeautifulSoup(r.content, 'html.parser')


def create_driver():
    chrome_profile_location = '/Users/deepak.sahu/Downloads/'
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-data-dir={chrome_profile_location}')
    return webdriver.Chrome(
        executable_path='/Users/deepak.sahu/Downloads/chromedriver'
    )


def get_quotes():
    quotes = []
    soup = get_soup('https://versionweekly.com/news/instagram/best-unique-instagram-captions-for-girls-in-2020/')
    for item in soup.find_all('ol'):
        for quote in item.find_all('li'):
            try:
                quote = quote.text.replace('”', '')
                quote = quote.replace('“', '')
                quotes.append(quote)
            except UnicodeEncodeError:
                pass
    return quotes[4:]


def generate_image(quote):
    x1 = 1500
    y1 = 1500

    fnt = ImageFont.truetype('/Users/deepak.sahu/venv/lib/python3.7/site-packages/reportlab/fonts/Adriana.ttf', 150)
    img = Image.new('RGBA', (x1, y1), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    sum = 0
    for letter in quote:
        sum += d.textsize(letter, font=fnt)[0]
    average_length_of_letter = sum / len(quote)
    number_of_letters_for_each_line = (x1 / 1.618) / average_length_of_letter
    incrementer = 0
    fresh_sentence = ''

    for letter in quote:
        if letter == '-':
            fresh_sentence += '\n\n' + letter
        elif incrementer < number_of_letters_for_each_line:
            fresh_sentence += letter
        else:
            if letter == ' ':
                fresh_sentence += '\n'
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer += 1

    dim = d.textsize(fresh_sentence, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1 / 2 - x2 / 2)
    qy = (y1 / 2 - y2 / 2)
    d.text((qx, qy), fresh_sentence, align="center", font=fnt, fill=(100, 100, 100))

    location = os.getcwd() + f'\\quotes\\{quote.split()[0]}_{random.randint(0, 1000)}.png'
    img.save(location)
    title = quote
    tags = ', '.join(title.split())
    desc = f'A very inspirational quote: {quote}'
    return quote_image(location, title, tags, desc)


class quote_image:
    def __init__(self, location, title, tags, desc):
        self.location = location
        self.title = title
        self.tags = tags
        self.desc = desc


class bot:
    def __init__(self, quote):
        self.quote = quote
        self.driver = create_driver()

    def upload(self):
        template_link = ''

        self.driver.get(template_link)
        element = self.driver.find_element_by_css_selector('#work_title_en')
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(self.quote.title)

        element = self.driver.find_element_by_css_selector('#work_tag_field_en')
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(self.quote.tags)

        element = self.driver.find_element_by_css_selector('#work_description_en')
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(self.quote.desc)

        self.driver.find_element_by_css_selector(
            '#add-new-work > div > div.duplicate > div.upload-button-wrapper.replace-all-images').click()
        time.sleep(1.5)
        pyautogui.typewrite(self.quote.location)
        time.sleep(1)
        pyautogui.hotkey('ENTER')
        time.sleep(20)
        self.driver.find_element_by_css_selector('#rightsDeclaration').click()
        self.driver.find_element_by_css_selector('#submit-work').click()

        time.sleep(23)
        self.driver.close()


def run():
    WIDTH = 2376
    HEIGHT = 2024
    img = Image.new('RGB', (WIDTH, HEIGHT))
    for quote in get_quotes():
        print(f'Uploading: {quote}')
        design = generate_image(quote)
        print(design)
        # Load the user photo (read-mode). It should be a 250x250 circle
        user_photo = Image.open('user_photo.png', 'r')

        # Paste the user photo into the working image. We also use the photo for\
        # its own mask to keep the photo's transparencies
        img.paste(user_photo, COORD_PHOTO, mask=user_photo)

        # Finally, save the created image
        img.save(f'{img_name}.png')
        # bot(design).upload()
run()