from bs4 import BeautifulSoup
import json

class Parser:
    def __init__(self, sourse):
        self.sourse = sourse

    def parse(self, file_name = "result.json", params = {'parse_label': True, 'parse_format': True}):
        albums_info = []
        with open(self.sourse, 'r', encoding="utf8") as f:
            page = f.read()
            soup = BeautifulSoup(page, 'html.parser')
            artist_name = soup.find("title").text.split()
            final_name = ""
            for i in range(len(artist_name)):
                if artist_name[i] == 'discography':
                    for y in range(i):
                        final_name += artist_name[y] + " "

            full_table = soup.find("table", attrs={"class": "wikitable plainrowheaders"})
            album = full_table.find_all("th", attrs={"scope": "row"})
            for a in album:
                if params['parse_label'] and params['parse_format']:
                    albums_info.append({"album_name": a.text[:-1], "date": None, "label": None, "format": None})
                elif params['parse_label'] and not params['parse_format']:
                    albums_info.append({"album_name": a.text[:-1], "date": None, "label": None})
                elif not params['parse_label'] and params['parse_format']:
                    albums_info.append({"album_name": a.text[:-1], "date": None, "format": None})
                elif not params['parse_label'] and not params['parse_format']:
                    albums_info.append({"album_name": a.text[:-1], "date": None})

            optional_info_list = full_table.find_all("ul")
            tmp = []
            for i in optional_info_list:
                if i.text.find("Released") != -1:
                    tmp.append(i.text)
            for i in range(len(tmp)):
                data = tmp[i].split('\n')[0].split(':')[1].strip()
                if data[-1] == ']':
                    data = data[:data.rfind('[')]
                if data[-1] == ')':
                    data = data[:data.rfind('(')]
                albums_info[i]['date'] = data.strip()
            if params['parse_label']:
                for i in range(len(tmp)):
                    if len(tmp[i].split('\n')) > 1:
                        albums_info[i]['label'] = tmp[i].split('\n')[1].split(':')[1].strip()
            if params['parse_format']:
                for i in range(len(tmp)):
                    if len(tmp[i].split('\n')) > 2:
                        albums_info[i]['format'] = tmp[i].split('\n')[2].split(':')[1].strip()
            final = {"artist_name": final_name[:-1], "albums_info": albums_info}
            with open(file_name, "w") as g:
                json.dump(final, g, indent= 4, ensure_ascii=False)
