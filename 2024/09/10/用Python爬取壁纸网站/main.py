from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time


def getDetail(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), features="lxml")
    detailLst = bsObj.findAll("a", {"class": "wallpapers__link"})
    return ["https://wallpaperscraft.com" + i.attrs["href"] for i in detailLst]


def getImg(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), features="lxml")
    imgUrl = bsObj.findAll("img", {"class": "wallpaper__image"})[0].attrs["src"]
    return imgUrl, imgUrl.split("/")[-1]


for num in range(1, 11):
    try:
        target = f"https://wallpaperscraft.com/catalog/anime/3840x2400/page{num}"
        detailLst = getDetail(target)
        print("\033[91mDownloading from:\033[0m", target)
        for details in detailLst:
            time.sleep(5)
            address, name = getImg(details)
            print("Downloading:", name)
            urlretrieve(address, "downloaded\\" + name)
            print("Done.")
    except:
        pass
