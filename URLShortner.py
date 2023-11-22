import pyshorteners
url = input('Enter the url\n')
def shortner(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortner(url)


