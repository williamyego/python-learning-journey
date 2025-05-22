# Networked Programs

## 🌐 Introduction to Networked Programs
Python can connect to web servers, fetch content over the internet, and handle data using standard internet protocols.

---

## Reading Web Pages with `urllib`

### Example:
```
import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
```
## Using `beautifulsoup`
````
import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
    print(tag.contents[0])
````

