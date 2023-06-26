if __name__ == "__main__":
    from download import Downloader
    from parse import Parser
    from data import Displayer
else:
    from .download import Downloader
    from .parse import Parser
    from .data import Displayer

def process(url, file_name = "result.json", params = {'parse_label': True, 'parse_format': True}):
    
    downloader = Downloader(url)
    discography_is_present = downloader.save()
    if discography_is_present:
        parser = Parser("page.html")
        parser.parse(file_name, params)
        displayer = Displayer()
        data = displayer.read_json(file_name)
        displayer.display_data(data)

#We can also try Amon_Amarth, Iron_Maiden, Five_Finger_Death_Punch
url_amon = "https://en.wikipedia.org/wiki/Amon_Amarth"
url_im = "https://en.wikipedia.org/wiki/Imagine_Dragons"
par_am = {'parse_label': False, 'parse_format': False}
par_im = {'parse_label': True, 'parse_format': False}

process(url_amon, params=par_am)
# process(url_im, params=par_im)