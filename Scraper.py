'''import requests
website_url = requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,"lxml")
print(soup.prettify())
My_table = soup.find("table",{"class":"wikitable sortable"})
links = My_table.findAll("a")
Countries = []
for link in links:
    Countries.append(link.get("title"))
    
print(Countries)
import pandas as pd
df = pd.DataFrame()
df["Country"] = Countries
df'''

'''
import wikipedia
print(wikipedia.WikipediaPage(title = 'Metropolis (1927 film)').summary)
# get the section of a page. In this case the Plot description of Metropolis
section = wikipedia.WikipediaPage('Metropolis (1927 film)').section('Plot')

# that will return fairly clean text, but the next line of code
# will help clean that up.
section = section.replace("\\n","").replace("\\","")'''

'''
import wikipedia
import numpy as np

# you'll need to get the exact names of the titles of the pages beforehand
example_titles = ['Algol (film)','Dr. Jekyll and Mr. Hyde (1920 Haydon film)',
 'Figures of the Night', 'The Invisible Ray (1920 serial)', 'The Man from Beyond',
 'Black Oxen','Aelita','The Hands of Orlac (1924 film)']

# create a list of all the names you think/know the section might be called
possibles = ['Plot','Synopsis','Plot synopsis','Plot summary', 
             'Story','Plotline','The Beginning','Summary',
            'Content','Premise']
# sometimes those names have 'Edit' latched onto the end due to 
# user error on Wikipedia. In that case, it will be 'PlotEdit'
# so it's easiest just to make another list that acccounts for that
possibles_edit = [i + 'Edit' for i in possibles]
#then merge those two lists together
all_possibles = possibles + possibles_edit

# now for the actual fetching!
for i in example_titles:
# load the page once and save it as a variable, otherwise it will request
# the page every time.
# always do a try, except when pulling from the API, in case it gets confused
# by the tttle.
    try:
        wik = wikipedia.WikipediaPage(i[0])
    except:
        wik = np.NaN

# a new try, except for the plot
    try:
        # for all possible titles in all_possibles list
        for j in all_possibles:
            # if that section does exist, i.e. it doesn't return 'None'
            if wik.section(j) != None:
                #then that's what the plot is! Otherwise try the next one!
                plot_ = wik.section(j).replace('\n','').replace("\'","")
    # if none of those work, or if the page didn't load from above, then plot
    # equals np.NaN
    except:
        plot= np.NaN'''
        
import wikipedia
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd

# first pull the HTML from the page that links to all of the pages with the links.
# in this case, this page gives the links list pages of sci-fi films by decade.
# just go to https://en.wikipedia.org/wiki/Lists_of_science_fiction_films
# to see what I'm pulling from.
html = requests.get('https://en.m.wikipedia.org/wiki/List_of_colleges_and_universities_in_Massachusetts')

#turn the HTML into a beautiful soup text object
b = BeautifulSoup(html.text, 'lxml')
b.prettify()
My_table = b.find("table",{"class":"wikitable sortable"})
links = My_table.findAll("a")
colleges = []
for link in links:
    colleges.append(link.get("title"))
df = pd.DataFrame()
df["college"] = colleges

print(df)

'''
# create an mpty list where those links will go.
links = []

# in this case, all of the links we're in a '<li>' brackets.
for i in b.find_all(name = 'li'):
    # pull the actual link for each one
    for link in i.find_all('a', href=True):
        links.append(link['href'])
# the above code ends up pulling more links than I want,
# so I just use the ones I want
links = links[1:11]
# add same prefix URL to different suffixes
university_links = ['https://en.wikipedia.org' + i for i in links]

# create two new lists, one for the title of the page, 
# and one for the link to the page
film_titles = []
film_links = []
# for loop to pull from each category page with list of universities.
# to follow along as an exampe
for university in university_links:
    print(f'Collecting films from {university}')
    html = requests.get(university)
    b = BeautifulSoup(html.text, 'lxml')
    # get to the table on the page
    for i in b.find_all(name='table', class_='wikitable'):
        # get to the row of each film
        for j in i.find_all(name='tr'):
            #get just the title cell for each row.
            # contains the title and the URL
            for k in j.find_all(name='i'):
                # get within that cell to just get the words
                for link in k.find_all('a', href=True):
                    # get the title and add to the list
                    film_titles.append(link['title'])
                    # get the link and add to that list
                    film_links.append(link['href'])
    #be a conscientious scraper and pause between scrapes
    time.sleep(1)
print(f'Number of university Links Collected: {len(film_links)}')
print(f'Number of university Collected: {len(film_titles)}')
# remove film links that don't have a description page on Wikipedia
new_film_links = [i for i in film_links if 'redlink' not in i]
# same goes for titles
new_film_titles = [i for i in film_titles if '(page does not exist)' not in i]
print(f'Number of Film Links with Wikipedia Pages: {len(new_film_links)}')
print(f'Number of Film Titles with Wikipedia Pages: {len(new_film_titles)}')
#use this list to fetch from the API
title_links = list(zip(new_film_titles, new_film_links))
print(title_links)'''