# Importing dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
import time
import numpy as np
import json
from selenium import webdriver

def init_browser():
    # splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    # Mars News Titles
    browser = init_browser()
    mars_collection = {}
    
    # Mars News Url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_collection["news_title"] = soup.find('div', class_="content_title").text()
    mars_collection["news_snip"] = soup.find('div', class_="rollover_description_inner").text()

    # Mars Feature Image
    url_feature_image = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url_feature_image)
    response = browser.html
    soup2 = BeautifulSoup(response, 'html.parser')
    images = soup2.find_all('a', class_="fancybox")
    pic_source = []
    for image in images:
        picture = image['data-fancybox-href']
        pic_source.append(picture)

    mars_collection["featured_image_url"] = "https://www.jpl.nasa.gov" + pic_source[2] 

   
    # Mars Facts
    url_facts = "https://space-facts.com/mars/"
    df_facts = pd.read_html(url_facts)[0]
    mars_df.columns=["Description","Value"]
    mars_df.set_index("Description", inplace=True)
    mars_df

    # # Mars Hemispheres
    hemisphere_image_urls = []

    # Cerberus Hemispheres
    url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_cerberus)
    response_cerberus = browser.html
    soup4 = BeautifulSoup(response_cerberus, 'html.parser')
    cerberus_img = soup4.find_all('div', class_="wide-image-wrapper")

    for img in cerberus_img:
        pic_cerberus = img.find('li')
        cerberus_full_img = pic_cerberus.find('a')['href']
    cerberus_title = soup4.find('h2', class_='title').get_text()
    cerberus_hem = {"Title": cerberus_title, "url": cerberus_full_img}

    hemisphere_image_urls.append(cerberus_hem)

    # Schiaparelli Hemisphere

    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_cerberus)
    response_schiaparelli = browser.html
    soup5 = BeautifulSoup(response_schiaparelli, 'html.parser')
    schiaparelli_img = soup5.find_all('div', class_="wide-image-wrapper")

    for img in schiaparelli_img:
        pic_schiaparelli = img.find('li')
        schiaparelli_full_img = pic_schiaparelli.find('a')['href']
    shiaparelli_title = soup5.find('h2', class_='title').get_text()
    shiaparelli_hem = {"Title": shiaparelli_title, "url": schiaparelli_full_img}
    
    hemisphere_image_urls.append(shiaparelli_hem)

    # Syrtis Hemisphere

    url_syrtis = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')
    browser.visit(url_syrtis)
    response_syrtis = browser.html
    soup6 = BeautifulSoup(response_syrtis, 'html.parser')
    syrtris_img = soup6.find_all('div', class_="wide-image-wrapper")

    for img in syrtris_img:
        pic_syrtris = img.find('li')
        syrtris_full_img = pic_syrtris.find('a')['href']
    syrtris_title = soup6.find('h2', class_='title').get_text()
    syrtris_hem = {"Title": syrtris_title, "url": syrtris_full_img}

    hemisphere_image_urls.append(syrtris_hem)

    # Valles Marineris Hemisphere

    url_valles = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')
    browser.visit(url_valles)
    response_valles = browser.html
    soup7 = BeautifulSoup(response_valles, 'html.parser')
    valles_img = soup7.find_all('div', class_="wide-image-wrapper")

    for img in valles_img:
        pic_valles = img.find('li')
        valles_full_img = pic_valles.find('a')['href']
    valles_title = soup7.find('h2', class_='title').get_text()
    valles_hem = {"Title": valles_title, "url": valles_full_img}
    
    hemisphere_image_urls.append(valles_hem)

    ## Collection of information
    mars_collection["hemisphere_image"] = hemisphere_image_urls

    return mars_collection
