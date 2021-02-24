# Web Scraping - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

The task here is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did.

## Step 1 - Scraping

Complete a initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* I created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all of the scraping and analysis tasks:

### NASA Mars News

* I scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that I can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* I visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* I used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Facts

* I visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* I used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* I visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* I set up splinter to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Then I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. I created a Python dictionary to store the data using the keys `img_url` and `title`.

* Next, I appended the dictionary with the image url string and the hemisphere title to a list. This list contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```
- - -

## Step 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* I started by converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executes all of your scraping code from above and returns one Python dictionary containing all of the scraped data.

* Next, I created a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * It stores the return value in Mongo as a Python dictionary.

* I created a root route `/` that queries the Mongo database and passes the mars data into an HTML template to display the data.

* I created a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.  
Thi is how the final product looks like:

![final_page](Images/final_page.gif)


Feel free to reach out to me if you have any questions.

### Marina Ercoli
E-mail: maercoli@hotmail.com


#### Copyright

Trilogy Education Services © 2020. All Rights Reserved.
