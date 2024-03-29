import os
import traceback
import subprocess
try:
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.table import Table
    from rich import box
    import feedparser as fp
except ImportError:
    traceback.print_exc()
    input("Press enter to install missing packages")
    import pip
    pip.main(['install', '--user', 'rich', 'feedparser'])
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.table import Table
    from rich import box
    import feedparser as fp
    quit()

# Initialise download path
path = (os.path.expanduser('~')+"/nyaatorrents/downloads/")
if not os.path.exists(path):
    os.makedirs(path)

dirname = os.path.dirname(path)

try:
    nyaa_rss = fp.parse('https://nyaa.si/?page=rss')
except:
    print("Could not establish connection to nyaa.si.\nPlease make sure you are connected to the internet and try again.")
    exit()
else:
    print(nyaa_rss['feed']['link'])
    entries = nyaa_rss['entries']


def torrent_table():
    console = Console()
    table = Table(title="Nyaa.si Torrents", box=box.ROUNDED)
    table.add_column(style="green")
    table.add_column("Name")
    table.add_column("Link", style="blue")
    for entry in entries:
        table.add_row(str(entries.index(entry)), entry['title'], entry['link'])
    console.print(table)


torrent_table()

torrent_dl = Prompt.ask(
    "Enter the the number of the torrent(s) you would like to download seperated by a comma")
torrent_dl = tuple(torrent_dl.split(","))
print(torrent_dl)


def torrent_download():
    link = (entries[int(item)]['link'])
    cmd = ("wget " + link + " -P " + dirname)
    subprocess.call((cmd), shell=True)


for item in torrent_dl:
    torrent_download()
print("Downloads complete!")
exit()
