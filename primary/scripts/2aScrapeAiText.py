# FINAL CODE to Scrape the-good-ai.com's AI example essays.

#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from numpy import random
from time import sleep
import os

# Set up Splinter's browser
browser = Browser('chrome')


#create variables to save with so don't overwrite previously generated text
total_counter =  len(os.listdir('../rawData/aiEssays/')) +2 
genre_count = 8
llm = 'the-good-ai'

#develop base_url
base_url = 'https://www.the-good-ai.com'
query1 = '/examples/'
query2 = '?category='

#loop through each genre type
genre = ['memoir', 'math', 'physics', 'philosophy', 'engineering', 'finance', 'economics', 'chemistry', 'biology', 'music', 'technology', 'comparative', 'history', 'literature', 'art', 'geography', 'religion']

for word in genre:
    
    genre_count = genre_count + 1
    track_genre = word

    #specify the url for each genre
    url_genre = f'{base_url}{query1}{query2}{word}'

    #pause the analysis for about 20 seconds
    wait = random.normal(3, .5, 1)[0]
    sleep(wait)

    #visit the url for each genre
    browser.visit(url_genre)
    sleep(3)

    # save and Parse the html for each genre
    html = browser.html
    html_soup = soup(html, 'html.parser')   
    
    #get information about essays for a given genre
    links = html_soup.find_all('a')

    #save and extract all links for a given genre page
    post_link = []
    for link in links:
        post_link.append(link['href'])

    #filter out links to just include links to essays
    search_term = '/post/'
    to_click = []
    for link in post_link:
        if search_term in link:
            to_click.append(f'{base_url}{link}')
    
    #go to each link (essay) and extract relevant information
    for page in to_click:
        #pause the analysis for appx 15 sec
        wait = random.normal(3, .5, 1)[0]
        sleep(wait)

        #visit the page
        try: 
            browser.visit(page)
            sleep(3)
            #save and parse the html for given essay
            html = browser.html
            html_soup = soup(html, 'html.parser') 
            
            #extract the title
            title = html_soup.find('span', class_ = 'fancy highlighted').text

            #create list w/ title
            essay_text = []
            essay_text.append(f'{title}\n')

            #extract the paragraphs and add to list
            paragraphs = html_soup.find_all('p')
            for paragraph in paragraphs:
                essay_text.append(f'{paragraph.text}')

            #combine title
            final_essay = ''.join(essay_text)
            final_essay

            #increase counter
            total_counter = total_counter + 1

            #save the full document as text
            save_path = f'../rawData/aiEssays/eid{genre_count}-{llm}_{total_counter}.txt'
            with open(save_path, 'w') as f:
                f.write(final_essay)
                
        except Exception as e:
            print(f'error occurred with {page} {e}')


        
browser.quit()


