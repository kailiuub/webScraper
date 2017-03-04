import requests
from bs4 import BeautifulSoup
import lxml
import re
import time

# Accept URL and Parsing HTML
class Parsing:
  def __init__(self, url='https://buffalo.craigslist.org/'):
    self.url=url
  # request response and convert it to soup object
  def request(self):
    self.r=requests.get(self.url)
    data=self.r.text
    self.soup=BeautifulSoup(data, 'lxml')    

  def getLink(self): 
    links=set()
    pattern=re.compile("^http")
    for link in self.soup.find_all('a'):
      href=link.get('href')
      if re.match(pattern, str(href)):
        links.add(link.get('href'))
    return links

if __name__=="__main__":
  t=time.time()
  # first level link search
  links=set()
  par=Parsing()
  par.request()
  links=par.getLink() 
  # save 1st level links to database
  '''for link in links:
    print(link)'''
  
  # second level link search
  links2=set()
  for link in links: 
    par2=Parsing(link)
    par2.request()
    temp=par2.getLink()
    if temp: 
      links2=links2.union(temp)  # add all http links to the set links2
  # save 2st level links to DB
  '''for link in links2:
    print(link)'''

  # third level link search
  links3=set()
  for link in links2:
    par3=Parsing(link)
    par3.request()
    temp=par3.getLink()
    if temp:
      links3=links3.union(temp)
  # save 3rd level links to DB
  for link in links3:
    print(link)

  print("consumed time: {}".format(time.time()-t))




    
