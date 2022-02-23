import requests
import urllib.request
import os

thread = input("Enter thread's full link: ") #ex: https://boards.4channel.org/wsg/thread/4346206/webms-with-sound-for-other-boards

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
os.mkdir(path)


r = requests.get(thread)
htmlSource = r.text

link_part1 = '<a href="//i.4cdn.org/' + board + '/'
xt1 = '.webm'
xt2 = '.gif'

counter = htmlSource.count(link_part1)
indexStart = 0
i = 1

while i <= counter:

    #gets 1st index
    indexStart = htmlSource.find(link_part1, indexStart + 1)
    
    #check closest extension
    end1 = htmlSource.find(xt1, indexStart)
    end2 = htmlSource.find(xt2, indexStart)

    if end1 > end2:
        indexEnd = end2
        size = len(xt2)
    else:
        indexEnd = end1
        size = len(xt1)

    indexStart += 11
    indexEnd += size
    url = htmlSource[indexStart:indexEnd]

    fileName = url.replace('i.4cdn.org/' + board + '/', '')

    url = 'https://' + url
    
    print(url)
    print(fileName)

    fullFileName = path + '/' + fileName
    
    urllib.request.urlretrieve(url, fullFileName)

    i += 1
