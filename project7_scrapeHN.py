#In this project we will be scraping Hacker news website to grab all the top rated stories so the stories that have over 100 upvotes!

#Ok fist thing is to download beautiful soup cuz its our web scraping tool
# pip3 install beautifulsoup4
#We also need request library - allows us to grab HTML files 
#pip3 install requests

import requests 
from bs4 import BeautifulSoup
import pprint #makes it so when we print things to the terminal it looks better

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a')  #need the >a becuasee the link sits under the a line think of it as a subfolder
subtext = soup.select('.subtext')   #A note the '.' means it is a class so we are grabbing the score and titleline classes
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

#USing beautiful soup we can keep getting attributes 

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) #This is standards for sorting items we get to use lambda fuctions

#If we didn't use enumerate then we couldnt grab both links and subtext items
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):  #we used enumerate cuz we have 2 lists (links and subtext) but we are only enumerating over links so we need the idx(index) so we can access the subtext in our loop
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote): #if votes exists basically - if true
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points}) #here we use a dicionary to combine the title and link to article
    return sort_by_votes(hn)
    

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
















