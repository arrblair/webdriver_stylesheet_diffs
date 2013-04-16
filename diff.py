from selenium import webdriver
from sys import argv


site_one = argv[1]
site_two = argv[2]
sites_to_compare = [site_one, site_two]
driver = webdriver.Chrome()
stylesheet_urls = []

for site in sites_to_compare():
    driver.get(site) 
    stylesheets.append((driver.execute_script('return document.styleSheets[0]["href"];')))    
    return stylesheet_urls
