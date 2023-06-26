import json

class Displayer:
    def read_json(self, filename):
        with open(filename, 'r') as js:
            data = json.load(js)

        return data
    
    def display_data(self, data_dict):
        print()
        print("-------------------------------------------------------------------------------------")
        print()
        artist_name = data_dict["artist_name"]
        print(f"Displaying studio discography of {artist_name}")
        print()

        albums_list = data_dict["albums_info"]

        for dictionary in albums_list:

            name = dictionary["album_name"]
            print(f"Album name: {name}")

            date = dictionary["date"]
            print(f"Date of issue: {date}")

            if "label" in dictionary.keys():
                label = dictionary["label"]
                print(f"Label: {label}")
            if "format" in dictionary.keys():
                format = dictionary["format"]
                print(f"Format(s): {format}")
        

            print()
    
        print("-------------------------------------------------------------------------------------")
        print()

