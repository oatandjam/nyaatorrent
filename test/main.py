import os, subprocess, sys

def dl_choice(*args):
    for arg in args:
        rent = (nyaa_rss['entries'][arg]['link'])
        cmd = ("wget " +rent +" -P " +location)
        subprocess.call((cmd), shell=True)
dl_choice(5)