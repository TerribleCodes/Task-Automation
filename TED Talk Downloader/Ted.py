import requests
from bs4 import BeautifulSoup
import re
import sys


if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Enter a TED Talk URL")

r = requests.get(url)
result = ''

print("Gathering Resources...")

soup = BeautifulSoup(r.content, features="lxml")

for value in soup.findAll("script"):
    if(re.search("talkPage.init", str(value))) is not None:
        result = str(value)

res_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = res_mp4.split('"')[0]
print("Downloading video from: "+mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
print("Storing the video in..."+file_name)

r = requests.get(mp4_url)
with open(file_name, 'wb') as f:
    f.write(r.content)

print("Download Completed")
