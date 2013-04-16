import os
from selenium import webdriver
from sys import argv

# maybe use kwargs for better modeling, e.g. known_good_site=, broken_site=
site_one = argv[1]
site_two = argv[2]
sites_to_compare = [site_one, site_two]
driver = webdriver.Chrome()
file_mappings = {"site_one_css": "", "site_two_css": ""}
i=0

for site in sites_to_compare:
    driver.get(site) 
    stylesheet = (driver.execute_script('return document.styleSheets[0]["href"];'))
    driver.get(stylesheet)
    current_url = driver.current_url
    split_current_url = current_url.split('/')
    length = len(split_current_url)
    filename = split_current_url[length-1]
    if 'css' in filename[-3:]:
        print "That's a css file already: %s" % filename
    elif '?' in filename:
        print "Query strings won't be necessary." 
        filename = filename.split('?')
        filename = filename[0]
        filename += '.css' 
    else:
        filename += '.css' 
    css = driver.page_source
    new_css_file = open(filename, "w")
    new_css_file.write(css)
    new_css_file.close()
    if i == 0:
        file_mappings["site_one_css"] = filename
    else:
        file_mappings["site_two_css"] = filename 
    i+=1

os.system('diff %s %s' % (file_mappings['site_one_css'], file_mappings['site_two_css']))
