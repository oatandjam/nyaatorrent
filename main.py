import feedparser as fp
from colorama import init
init()
from colorama import Fore, Back, Style
import subprocess
import os
from vars import loc
import sys

ans = input("would you like install the packages colorama and feedparser (y/n)? ")

if (ans == "y"):
    subprocess.call("pip install colorama")
    subprocess.call("pip install feedparser")

elif (ans == "n"):
    print("Understandable")
    exit()


d = fp.parse('https://nyaa.si/?page=rss')

print(d['feed']['title'])
print(d.feed.subtitle)
print(d['feed']['link'])

print(Fore.RED + 'test!')
x = (len(d['entries']))

print(d['entries'][0]['title'])

i=0
for i in range(x):
    print(Fore.GREEN +str(i) +(" ") +Style.RESET_ALL +((d['entries'][i]['title'] +"      " +Fore.GREEN + (d['entries'][i]['link']) +Style.RESET_ALL)))
    
    i=i+1

i=0
print("                                                             ")

t = int(input("Enter the the number of the torrent you want to download: "))

print(t)

print((d['entries'][t]['link']))

rent = (d['entries'][t]['link'])

cmd = ("wget " +rent +" -P " +loc)
subprocess.call(cmd)

#exit=input("Press Any Key To Exit...")