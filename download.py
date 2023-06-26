import requests
from bs4 import BeautifulSoup
import os
class Downloader:
    def __init__(self, url, params = None, file_path = "page.html", method = 'GET'):
        self.url = url
        self.params = params
        self.file_path = file_path
        self.method = method
    
    def get_html(self):
        true_link = "https://en.wikipedia.org" 
        response = requests.get(self.url)
        contents = response.content
        soup = BeautifulSoup(contents, 'html.parser')
        for link in soup.find_all('a', href = True):
            string = "discography"
            if string in link['href']:
                true_link += link['href']
                break
        if(true_link == "https://en.wikipedia.org"):
            return None
        true_response = requests.get(true_link)
        return true_response.content
    
    def save(self):
        content = self.get_html()
        if content == None:
            print("This artist has no separate discography page on wikipedia.org")
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
            return False
        else:
            with open (self.file_path, 'wb') as f:
                f.write(content)
            return True