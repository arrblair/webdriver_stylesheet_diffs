from selenium import webdriver
from sys import argv

# maybe use kwargs for better modeling, e.g. known_good_site=, broken_site=
site_one = argv[1]
site_two = argv[2]
sites_to_compare = [site_one, site_two]
driver = webdriver.Chrome()
stylesheet_urls = []

for site in sites_to_compare():
    driver.get(site) 
    stylesheet_urls.append((driver.execute_script('return document.styleSheets[0]["href"];')))    
    return stylesheet_urls
