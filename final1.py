import urllib.request as urllib
from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
#import urllib
#import urllib.request
from requests.exceptions import ConnectionError
import json
import re


try:
	url = "https://timesofindia.indiatimes.com/city/hyderabad/of-17-elected-mps-10-face-criminal-cases/articleshow/69489675.cms"
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()    # rip it out

	# get text
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split(".\n"))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	text = re.sub('[^a-zA-Z0-9\n\.]', ' ', text)

	print(text)
	
	
except HTTPError as e:
		print('The server couldn\'t fulfill the request.')
		print('Error code: ', e.code)
		#worksheet.write(row, column1,e.code) 
		#row+=1
		#writer = csv.writer(csv_out)
		#writer.writerows(e.code)
		#worksheet.write(row,1,e.code)
		#workbook.save('Excel_Workbook.xls')
		#row+=1
		#if e.code == 404  or e.code == 403 or e.code == 500:
			#filtered_url.remove(f)
except URLError as e:
		print('We failed to reach a server.')
		print('Reason: ', e.reason)
		#worksheet.write(row,column2,e.reason)
		#row+=1
		#writer = csv.writer(csv_out)
		#writer.writerows(f)
		#worksheet.write(row,2,f)
		#workbook.save('Excel_Workbook.xls')
		#row+=1
except (ConnectionError, TimeoutError) as e:
		print(e)

		
			