from os import system
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
    stylesheet = (driver.execute_script('return document.styleSheets[0]["href"];'))
    driver.get(stylesheet)
    split_current_url = driver.current_url
    length = len(split_current_url)
    filename = split_current_url[length-1]
    if 'css' in filename[-3:]:
        print "That's a css file already: %s" % filename
    else:
        filename += '.css' 
    css = driver.page_source
    new_css_file = open(filename, "w")
    new_css_file.write(css)
    new_css_file.close()
    return stylesheet_urls


