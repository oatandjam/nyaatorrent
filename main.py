import subprocess, os, sys
try:
    from colorama import Fore, Back, Style, init
except ImportError:
    print("Installing Colorama...")
    subprocess.call("(python3 -m pip install colorama==0.4.1)", shell=True)
finally:
    from colorama import Fore, Back, Style, init
    
try:
    import feedparser as fp
except ImportError:
    print("Installing Feedparser")
    subprocess.call("(python3 -m pip install feedparser==6.0.0)", shell=True)
finally:
    import feedparser as fp

#DOWNLOAD PATH
location = ("~/Downloads/nyaatorrents/")

d = fp.parse('https://nyaa.si/?page=rss')

print(d['feed']['link'])

x = (len(d['entries']))

for i in range(x):
    print(Fore.GREEN +str(i) +(" ") +Style.RESET_ALL +((d['entries'][i]['title'] +"      " +Fore.GREEN + (d['entries'][i]['link']) +Style.RESET_ALL)))
print("\n")
t = str(input("Enter the the number of the torrent(s) you want to download (example: 1,2,3): "))

print(t)
trn = t.split(',')
trnlth = len(trn)

for i in range(trnlth):
    print((d['entries'][int(trn[i])]['link']))
for i in range(trnlth):
    rent = (d['entries'][int(trn[i])]['link'])
    cmd = ("wget " +rent +" -P " +location)
    subprocess.call((cmd), shell=True)
print("Download(s) complete!")
exit=input("Press Any Key To Exit...")
