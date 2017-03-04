import os
from html.parser import HTMLParser
from urllib import parse
import requests
from bs4 import BeautifulSoup
import queue

# Each Website Crawling is a separate project (folder)
def create_project_dir(directory):
  if not os.path.exists(directory):
    print('create project directory ' + directory)
    os.makedirs(directory)
  else: 
    print('directory {} already exists'.format(directory))

# Create queue and crawled files (if not created)
def create_data_files(directory, base_url):
  queue=directory+'/queue.txt'
  crawled=directory+'/crawled.txt'
  # create file queue.txt
  if not os.path.isfile(queue): 
    print('create file {}'.format(queue))
    write_file(queue, base_url)
  else: 
    print('file {} already exists'.format(queue))
  # create file crawled.txt
  if not os.path.isfile(crawled):
    print('create file {}'.format(crawled))
    write_file(crawled, '')  # didn't crawl any url yet
  else: 
    print('file {} already exists'.format(crawled))

#  basic file operations
def write_content(path, data):
  f = open (path, 'w')
  f.write(data)
  f.close()

def append_content(path, data):
  with open(path,'a') as f: 
    f.write(data+'\n')

def delete_content(path):
  with open(path, 'w'):
    pass

# extract unique urls in file and return a set
def convert_set(file_name):
  results=set()  # set only hold unique elements
  with open(file_name, 'rt') as f: 
    for line in f:
      results.add(line.replace('\n', ''))  
  return results

# clear old file and replace with unique urls in the set
def set_to_file(links, filename): 
  delete_content(filename) # delete contents in old file
  for link in sorted (links):
    append_content(filename, link)
  
# use requests and BS to parse the website
def bsCrawl(url):
  http='http://'+url
  r=requests.get(http)
  data=r.text
  soup=BeautifulSoup(data, 'lxml')   # parse the requested html
  for link in soup.find_all('a'):
    print(link.get('href'))


# define threading Class
class MyThread(threading.Thread):
  def __init__(self):
    super().__init__(self):
  def run(self): 
    while (1): 
      pass

def worker(q): 
  url=q.get()
  bsCrawl(url)
  q.task_done()

if __name__=='__main__':
  threads=[]
  n_queue=5
  n_thread=3
  q=queue.Queue(n_queue)
  for i in range(n_thread): 
    t=MyThread(name=i, target='worker', args=(q)
    t.start()

  q.join()
  















  


