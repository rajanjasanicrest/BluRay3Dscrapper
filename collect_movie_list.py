# import json

# # Load existing JSON data
# with open("data/DVD-1998.json", "r", encoding="utf-8") as f:
#     existing_data = json.load(f)

# # Use a set to track unique (title, sku) pairs
# seen = []
# unique_data = []
# for item in existing_data:
#     if item:
#         bluray_url = item.get("blu_ray_url", "")


#         if bluray_url not in seen:
#             seen.append(bluray_url)
#             unique_data.append(item)  # Keep only unique entries

#         # if 'production_year' in item.keys():
#         #     unique_data.append(item)

# # Save the filtered unique data back to the JSON file
# with open("data/DVD-1998.json", "w", encoding="utf-8") as f:
#     json.dump(unique_data, f, indent=4)

# print("Duplicates removed based on title and SKU.")


from playwright.sync_api import sync_playwright
from get_agents import get_agent
from get_proxies import get_proxies_credentials_list
import random
import json
import os
from getMovieList import getMovieList
import logging

logger = logging.getLogger(__name__)  # Use __name__ without quotes
logger.setLevel(logging.INFO)

def get_random_proxy():
    # Randomly select a proxy from the pool
    proxies_list = get_proxies_credentials_list()
    return random.choice(proxies_list)


def visit_bluray_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True
        )  # Set headless=True for background execution
        context = browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent=get_agent(),
        )
        context.add_cookies([
            {
                "name": "country",
                "value": "us",
                "domain": ".blu-ray.com",
                "path": "/",
                "max_age": 30 * 24 * 60 * 60
            },
            {
                "name": "listlayout_7",
                "value": "simple",
                "domain": ".blu-ray.com",
                "path": "/",
                "max_age": 30 * 24 * 60 * 60
            },
        ])

        release_years = list(range(2009, 2025))

        for year in release_years:
            print('*'*50)
            print('scrapping for year ', year)
            
            try:
                page = context.new_page()
                movies_list = []
                try:
                    with open(f'movie_list/{year}-list.json', 'r', encoding='utf-8') as f:
                        movies_list = json.load(f)
                except Exception as e:
                    print(e)
                    print('scrapping for the first time')

                if not movies_list:
                    movies_list = getMovieList(page, year)
                    with open(f'movie_list/{year}-list.json', 'w', encoding='utf-8') as f:
                        json.dump(movies_list, f, indent=4, ensure_ascii=False)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    visit_bluray_website()