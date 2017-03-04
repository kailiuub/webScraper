Functions: 

1. Parse the info on booking.com webpage by three levels. Extract important information about hotels around one specified area. 

2. Create a PostgreSQL data in the local machine and save the extracted data in the database. 

3. Use multithreading and queue to speed up the web scraping process. 


How to set up chromium server

For Linux

1. Check you have installed latest version of chrome brwoser-> "chromium-browser -version"
2. If not, install latest version of chrome "sudo apt-get install chromium-browser"
3. get appropriate version of chrome driver from http://chromedriver.storage.googleapis.com/index.html
4. Unzip the chromedriver.zip
5. Move the file to /usr/bin directory sudo mv chromedriver /usr/bin
6. Goto /usr/bin directory and you would need to run something like "chmod a+x chromedriver" to mark it executable.
7. finally you can execute the code.

import os
from selenium import webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print driver.page_source.encode('utf-8')
driver.quit()
display.stop()
