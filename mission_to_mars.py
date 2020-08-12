from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import re
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'driver/chromedriver.exe'}
    #browser = Browser('chrome', **executable_path, headless=False)
    return Browser("chrome", **executable_path, headless=False)

def scrape_news():
    ### NASA Mars Program News
    #set up browswer, parser, and scrape page into soup
    browser = init_browser()
    browser.visit('https://mars.nasa.gov/news/')
    time.sleep(5)
    soup = bs(browser.html, 'lxml')
    # get latest news articles
    news_title = soup.find_all('div', class_='content_title')[1].text
    news_article = soup.find('div', class_='article_teaser_body').text
    # Close the browser after scraping
    browser.quit()
    # Store data in a dictionary
    news_dict = {
        "news_title": news_title,
        "news_article": news_article,
    }
    # Return results
    return news_dict


def scrape_f_image():
    ### JPL Mars Space Images - Featured Image
    # run browser with url of NASA Mars program
    browser = init_browser()
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    # find and click FULLIMAGE button
    FullImageButton = browser.find_by_id('full_image')
    FullImageButton.click()
    # find and click the "more info" button
    moreInfoButton = browser.find_link_by_partial_text('more info')
    moreInfoButton.click()
    time.sleep(5)
    # set up parser
    soup = bs(browser.html, 'lxml')
    # get url of the featured image_
    f_image_url = soup.select_one('figure.lede a img').get("src")
    f_title = soup.select_one('figure.lede a img').get("title")
    # Store data in a dictionary
    f_image_dict = {
        "f_image_url": f_image_url,
        "f_title":f_title,}
    # Close the browser after scraping
    browser.quit()
    # Return results
    return f_image_dict

def scrape_tweet():
    ### Mars Weather - from Tweeter
    #set up browswer, parser, and scrape pagls e into soup
    browser = init_browser()
    browser.visit('https://twitter.com/marswxreport?lang=en')
    time.sleep(5)
    soup = bs(browser.html, 'lxml')
    # get latest Mars weather tweet
    pattern = re.compile(r'sol')
    weather_tweet = soup.find("span", text=pattern).text
    # Close the browser after scraping
    browser.quit()
    # Return results
    return weather_tweet 

def scrape_images():
    ### Mars Hemispheres Images
    # run browser with url of Mars Hemispheres site
    browser = init_browser()
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    
    # find and visit each of the 4 sites and pick up the pictures' url and put them in dictionary
    #Create dictionary for mars hemisphere images
    Hem_Img_Dict = []
    
    for i in range(0,4):
        # navigate to the specific page
        link = browser.find_by_css("a.product-item h3")[i]
        print(link.text)
        link.click()                 
        # scrape
        soup = bs(browser.html, 'lxml')   # set up parser 
        image_ulr = soup.find('img', class_="wide-image")['src']   # get image's ulr
        title = soup.find('h2').text                               # get title
        # put in dictionary
        image_dict = {"Image_ULR": image_ulr,   
                    "Title":title}            
        Hem_Img_Dict.append(image_dict)       # append dict to list
        # navigate to previous page      
        browser.back()      
    # Close the browser after scraping
    browser.quit()
    # Return results
    return Hem_Img_Dict

def scrape_table():
    ### Mars Facts Table (with Pandas)
    # pandas to read the tables of the designed url
    tables = pd.read_html('https://space-facts.com/mars/')
    # pick the right table and modify
    df= tables[0]
    df.columns = ['Features','Values']
    df=df.set_index('Features')
    # return results
    return df