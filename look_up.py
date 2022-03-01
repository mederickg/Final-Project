from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



#StockX Search Function
def OpenAndSearch_StockX(search): 
   
    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://stockx.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="home-search"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)

    #returns user with a link to the website
    print(driver.current_url)



#footlocker Search Function
def OpenAndSearch_FootLocker(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://www.footlocker.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="HeaderSearch_search_query"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)
    #returns user with a link to the website
    print(driver.current_url)


#finishline Search Function
def OpenAndSearch_FinishLine(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://www.finishline.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="searchBarSearchBox"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)
    #returns user with a link to the website
    print(driver.current_url)


#goat Search Function
def OpenAndSearch_Goat(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    #goat website is built in a way that wont let me "click" the 
    #search button with chromedriver so I have to try and create my own url
    url = "https://www.goat.com/search?query=" + search

    # opens website
    driver.get(url) 
    #returns user with a link to the website
    print(driver.current_url)



#nike Search Function
def OpenAndSearch_Nike(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://www.nike.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="VisualSearchInput"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)

    #returns user with a link to the website
    print(driver.current_url)

#adidas Search Function
def OpenAndSearch_Adidas(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    #creates custom url for search
    url = "https://www.adidas.com/us/search?q=" + search

    # opens website
    driver.get(url) 

    #returns user with a link to the website
    print(driver.current_url)

#DSW search function
def OpenAndSearch_DSW(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    url = "https://www.dsw.com/en/us/browse/" + search

    # opens website
    driver.get(url) 

    #returns user with a link to the website
    print(driver.current_url)

   
 
#amazon search function
def OpenAndSearch_Amazon(search): 
  
    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://www.amazon.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)

    #returns user with a link to the website
    print(driver.current_url)


#ebay search function
def OpenAndSearch_Ebay(search): 

    #Opens a Chromepage and allows function to search on it
    s=Service("/Users/mederickschool/Desktop/Python Enviroment/chromedriver") 
    driver= webdriver.Chrome(service=s)

    # opens website
    driver.get("https://www.ebay.com/") 

    # clicks on search box byt finding xpath in the html sourcecode
    # then types in users input
    # finally presses "enter" to submit query

    search_box = driver.find_element(By.XPATH, '//*[@id="gh-ac"]') 
    search_box.send_keys(search)
    search_box.send_keys(Keys.ENTER)

    #returns user with a link to the website
    print(driver.current_url)


#runs all search functions
def OpenAndSearch_All(search): 

    OpenAndSearch_FootLocker(search)
    OpenAndSearch_Goat(search)
    OpenAndSearch_Nike(search)
    OpenAndSearch_Adidas(search)
    OpenAndSearch_DSW(search)
    OpenAndSearch_Amazon(search)
    OpenAndSearch_Ebay(search)
    OpenAndSearch_FinishLine(search)
