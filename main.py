try:
    from rich.console import Console
    from rich.text import Text
    from rich.prompt import Prompt
    from rich.table import Table
    import feedparser as fp
    import os
    import subprocess
except ImportError:
    print("Please make sure that all missing dependancies are installed!")
    quit() 
#DOWNLOAD PATH
location = ("/downloads/nyaatorrents/")
nyaa_rss = fp.parse('https://nyaa.si/?page=rss')
print(nyaa_rss['feed']['link'])
entries = nyaa_rss['entries']

console = Console()

def torrent_table():
    table = Table(title="Nyaa.si Torrents")
    table.add_column(style="green")
    table.add_column("Name")
    table.add_column("Link", style="blue")
    for entry in entries:
        table.add_row(str(entries.index(entry)),entry['title'],entry['link'])
    console.print(table)
torrent_table()

torrent_dl = Prompt.ask("Enter the the number of the torrent(s) you would like to download seperated by a comma")
torrent_dl = torrent_dl.split(",")
def torrent_download(*args):
    i=0
    for item in arg:
        print("Downloading " +str(arg))
        print(entries[int(item[i])]['link'])
        print(i)
        i = i + 1
        #cmd = ("wget " +link +" -P " +location)
        #subprocess.call((cmd), shell=True)
torrent_download(torrent_dl)


print("Downloads complete!")

exit=input("Press any key to exit...")
