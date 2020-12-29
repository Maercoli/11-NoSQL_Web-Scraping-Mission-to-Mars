# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "/Users/Marina/Desktop/chromedriver_win32/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    ####################
    #### Mars News ####
    ####################
    
    ### URL of NASA Mars News to be scrape ###
    url_1 = "https://mars.nasa.gov/news"
    browser.visit(url_1)                    
    
    # Scrape page into Soup
    html_1 = browser.html                   
    soup = bs(html_1, 'html.parser')  

    # Retrieve all elements that contain news title
    results = soup.find_all("div", class_="content_title")
    
    # Get the lastest news title
    news_title = results[1].get_text()
    
    # Get the latest news paragrapgh
    news_p = soup.find("div", class_="article_teaser_body").text
    

    #########################
    ## Mars Featured Image ##
    #########################

    ### URL of JPL Mars Space Images to be scrape ###
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2) 

    # Search for "Full image" and "click"
    browser.find_by_id('full_image').click()

    # Search for "More info" and "click"
    browser.links.find_by_partial_text('more info').click()

    # Scrape page into Soup
    html_2 = browser.html
    soup = bs(html_2, 'html.parser')

    # Search for image source
    results = soup.find_all('figure', class_='lede')
    relative_img_path = results[0].a['href']
    featured_img = 'https://www.jpl.nasa.gov' + relative_img_path


    ###############################
    ######### Mars Facts #########
    ###############################

    ### URL of Mars Facts to be scrape ###
    url_3 = "https://space-facts.com/mars/"
    
    # Use Pandas to scrape data
    tables = pd.read_html(url_3, match="Equatorial Diameter")[0]

    # Rename table colunms
    df = tables.rename(columns={0: " ", 1: "Mars"})
    
    # Convert the dataframe to html string
    mars_facts_table = df.to_html(index=False, header=True, border=0)
    
    ### Mars Hemispheres
    ### URL of JPL Mars Space Images to be scrape ###
    url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # HTML object
    browser.visit(url_4) 

    # Store data in a list
    hemisphere_image_urls = []

    # Get a List of All the Hemispheres
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
        
        # Find and click on each element on the list
        browser.find_by_css("a.product-item h3")[item].click()
        
        # Get Hemisphere Title
        hemisphere["title"] = browser.find_by_css("h2.title").text

        # Find Sample Image Anchor Tag, Extract <href> and store full img_url
        sample_element = browser.links.find_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]   
        
        # Append Hemisphere Object to List
        hemisphere_image_urls.append(hemisphere)
        
        # Navigate Backwards
        browser.back()
    
    hemisphere_image_urls

    ##############################
    # Store data in a dictionary #
    ##############################

    mars_data = { 
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_img,
        "mars_facts": mars_facts_table,
        "hemispheres": hemisphere_image_urls
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
