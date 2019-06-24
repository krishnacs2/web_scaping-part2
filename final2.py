import nltk   
import urllib.request as urllib
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = urllib.urlopen(url).read()    
soup = BeautifulSoup(html)
text = soup.get_text()
raw = nltk.clean_html(text)  
print(raw)