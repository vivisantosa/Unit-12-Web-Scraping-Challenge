# UofT SCS Data Analytics Boot Camp
#  Unit-12-Web-Scraping-Challenge
#  Author:	Vivianti Santosa -->

# MARS MISSION SCRAPING FUNCTION  

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import re

def init_browser():
    executable_path = {'executable_path': 'driver/chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    # Collect and store data in a dictionary
    mars_data = {
        "mars_news" : scrape_news(),
        "f_image_dict" : scrape_f_image(),
        "weather_tweet" : scrape_tweet(),
        "hem_img_dict" : scrape_images(),
        "mars_table" : scrape_table(),}
    # Return results
    return mars_data


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

    # Store data in a dictionary
    news_dict = {
        "news_title": news_title,
        "news_article": news_article,}    
    # Close the browser after scraping
    browser.quit()  
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
    featured_image = soup.select_one('figure.lede a img').get("src")
    f_image_url = f'https://www.jpl.nasa.gov{featured_image}'
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
    
    # get the extra information about Mars Hemisphere
    soup = bs(browser.html, 'html.parser')
    extra_info=soup.find_all('div', class_="item")

    # find and visit each of the 4 sites and pick up the pictures' url and put them in dictionary
    #Create dictionary for mars hemisphere images
    Hem_Img_Dict = []
    
    for i in range(0,4):
        # navigate to the specific page
        link = browser.find_by_css("a.product-item h3")[i]
        link.click()                 
        # scrape
        soup = bs(browser.html, 'lxml')   # set up parser 
        image_ulr = browser.find_link_by_text('Sample').first['href']    # get image's ulr
        title = soup.find('h2').text                                     # get title
        info= extra_info[i].find('p').text
        print(info)                                   # get the info paragraph
        site_url = 'https://astrogeology.usgs.gov' + extra_info[i].find("a")["href"] # get the site url
        # put in dictionary
        image_dict = {  "Image_ULR": image_ulr,   
                        "Title":title,
                        "Info" :info,
                        "site" :site_url,}            
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
    # df=df.set_index('Features')
    # return results
    
    return df.to_html(index=False, classes="table table-striped")