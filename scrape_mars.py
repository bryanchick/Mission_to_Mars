import pandas as pd
import requests
from bs4 import BeautifulSoup


# Dealing with the headline

def get_images():
    # your functin should bulild this list of dictionaries
    # return it as a dict, having a key of images
    
    return {"images": [
        {"title": "Valles Marineris Hemisphere", "img_url": "..."},
        {"title": "Cerberus Hemisphere", "img_url": "..."},
        {"title": "Schiaparelli Hemisphere", "img_url": "..."},
        {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]

    
    }

def get_mars_headline():
    url = "https://mars.nasa.gov/api/v1/news_items/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    resp = requests.get(url).json()
    first_item = resp.get('items')[0]
    return {"item_title": first_item.get('title'), 
            "item_desc": first_item.get('description')
           }

def get_mars_facts_table():
    tables = pd.read_html("https://space-facts.com/mars/") # list of tables, even if there's 1
    table_we_want = tables[0]
    table_we_want.columns = ['Thing', "Metric"]
    formatted =  table_we_want.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    return {"html_table_facts": formatted}


def scrape_master():
    print('scraping stuff')
    facts_table_dict = get_mars_facts_table()
    headlines_dict = get_mars_headline()
    image_dict = get_images()
    merged_dict = {**facts_table_dict, **headlines_dict, **image_dict}
    print('done merging')
    # merged dict will be the new data in mongodb
    return merged_dict