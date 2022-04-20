import requests
import urllib.request
import os
import re
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

thread = input("Enter thread's full link: ")

#get thread board
boardStart = thread.find('org/', 0)
boardStart += 4
boardEnd = thread.find('/', boardStart)

board = thread[boardStart:boardEnd]
print('board: ' + str(board))

#get thread name
threadStart = thread.find('thread/', 0)
threadStart += 7
threadStart = thread.find('/', threadStart) + 1
threadEnd = len(thread)

threadName = thread[threadStart:threadEnd]
print('thread name: ' + str(threadName))

#get path
path = os.getcwd() + '/' + threadName

print(str(os.path.isdir(threadName)))

if os.path.isdir(threadName) == False:
    os.mkdir(path)

#get html source
r = requests.get(thread)
htmlSource = r.text

soup = BeautifulSoup(htmlSource, "html.parser")

c = 0
varOld = ''

for link in soup.findAll('a'):

    var = link.get('href')

    if ".webm" in var or ".gif" in var or ".png" in var or ".jpg" in var or ".jpeg" in var:

        if varOld != var: #not copying duplicates
        
            fileName = var.replace('//i.4cdn.org/' + board + '/', '')
            fullFileName = path + '/' + fileName

            url = 'https:' + var
            
            #check if file already exists (duplicate thread or something)
            if os.path.isfile(fullFileName) == True:
                print(Fore.WHITE + str(url) + Fore.RED + ' - already exists. skipping file.')
            else:
                urllib.request.urlretrieve(url, fullFileName)
                print(Fore.WHITE + str(url) + Fore.GREEN + ' - downloaded.')

        varOld = var

print(Fore.WHITE + 'finished.')
