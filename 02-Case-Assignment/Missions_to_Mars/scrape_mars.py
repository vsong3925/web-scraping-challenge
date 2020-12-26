from splinter import Browser
from bs4 import BeautifulSoup 
from webdriver_manager.chrome import ChromeDriverManager

#%% Connect to the browser

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

#%% Scrape NASA Mars News

def scrape_news():
    browser = init_browser()
    
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    results = soup.find_all('li', class_='slide')
    
    news_list = []
        
    for result in results:
        title = result.find('h3').text
        paragraph = result.find('div', class_='article_teaser_body').text
            
        listings = {'title': title, 'paragraph': paragraph}
        news_list.append(listings)
        
    return news_list

#%%