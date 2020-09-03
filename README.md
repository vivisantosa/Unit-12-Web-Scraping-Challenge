# Unit-12-Web-Scraping-Challenge - Mission to Mars
### Web Scraping, Flask, and MongoBD 
<img src="https://cdn.mos.cms.futurecdn.net/pCubQdszKKbYMnAjpSx6LP-650-80.jpg.webp" width="1080"><br>

Author: Vivianti Santosa
Date: 2020-08-16
#### 'https://vivisantosa.github.io/Unit-12-Web-Scraping-Challenge/index.html'
<br> (un-dynamic webpage - sample)

## Part 1 : Web Scraping
The first part of the assignment is to scrape mars information from various NASA website. The information that we gather are in texts, urls of pictures, urls of webpages, and tables formats. The libraries that we use are BeautifulSoup, Pandas, and Requests/Splinter, as well as request, re, time. To make it easier, the initial scraping is performed in Jupyter Notebook.

The sites that we scraped are :
* Mars News : 
  * https://mars.nasa.gov/news/
  * From this site, we grab news title and new headline 
* JPL Mars Space Images - Featured Image
  * https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
  * We obtain the ulr of high resolution image from this site
* Mars Weather
  * https://twitter.com/marswxreport?lang=en
  * The information about mars weather is obtained from MarsWeather twitter.
* Mars Facts
  * https://space-facts.com/mars/
  * Mars Facts have information about Mars that is presented in table form
  * Pandas is used to get and transform the table
* Mars Hemispheres
  * https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
  * This is a site about Mars hemisphere, where images, and information about each of them is pulled. 
<img align="right" src="/Images/Screenshot (161).png" width="480">
Once routes to all of the scraped  information is determined, the codes are transformed into a python script in a file called scrape_mars.py. 
I decided to create small function definitions that will execute all of your scraping code for each of the websites.  Another function definition called scrape_info calls the other functions, gathers the data, and bundles it into one Python dictionary containing all of the scraped data (called mars_data).

## Part 2 : MongoDB and Flask Application

Using PyMongo the data is then loaded into MondoDB. It is set up, so that when a new scrape is performed, the latest information will overwrite the previous information on Mongo DB.

Two flask apps are created to operate the two routes are set up to handle the information flow from the database to the “display” file. The routes are :
* Root route “/” that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Scrape root - “/scrape” that will import your scrape_mars.py script and call your scrape function.

Last but not least the information, the images, and the tables, are displayed in an interactive HTML page. The file “index.html” takes the mars_data dictionary and displays all of the data in the appropriate HTML elements. On the right is the screenhoot of the webpage. Below is the sample (un-dynamic) of the webpage.<br>
https://vivisantosa.github.io/Unit-12-Web-Scraping-Challenge/templates/mars_index.html


