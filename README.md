# Unit-12-Web-Scraping-Challenge - Mission to Mars
Web Scraping, Flask, and MongoBD 
'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17832_hires.jpg'
https://cdn.mos.cms.futurecdn.net/pCubQdszKKbYMnAjpSx6LP-650-80.jpg.webp

## Part 1 : Web Scraping
<img align="right" src="Screenshot (152)">
The first part of the assignment is to scrape mars information from various NASA website. The information that we gather are in texts, urls of pictures, urls of webpages, and tables formats. The initial scraping is performed in Jupyter Notebook using BeautifulSoup, Pandas, and Requests/Splinter. Additionally we use request, re, time libraries.


The sites that we visit are :
* Mars News : 
  * https://mars.nasa.gov/news/
  * We grab news title and new headline from this site
* JPL Mars Space Images - Featured Image
  * https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
  * We obtain the ulr of high resolution image from this site
* Mars Weather
  * https://twitter.com/marswxreport?lang=en
  * From MarsWeather twitter, we get information about mars weather 
* Mars Facts
  * https://space-facts.com/mars/
  * From this site grab the table that contain mars fact
  * We use pandas to do this 
* Mars Hemispheres
  * https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
  * we take the four pictures that the site has as well as the information about each of the mars hemisphere

## Part 2 : MongoDB and Flask Application

