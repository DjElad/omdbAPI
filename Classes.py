import requests
import json


class Movie:

    def __init__(self, title, year, typ):
        self.typ = typ
        self.year = year
        self.title = title

    def get_type(self):
        return self.typ

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year


class OmdbSdk:

    def __init__(self, api):
        self.api = api

    def get_movie(self, typ, title, page=None):

        r = requests.get('http://www.omdbapi.com/?apikey='+self.api, params={
            's': title,
            'type': typ
        })
        r_dict = json.loads(r.text)
        print(r_dict)
        for page in range(1, int(int(r_dict['totalResults']) / 10 + 2)):
            r = requests.get('http://www.omdbapi.com/?apikey=' + self.api, params={
                's': title,
                'y': '',
                'type': typ,
                'page': page
            })
            r_dict = json.loads(r.text)
            print(f"\npage {page}:\n")
            for i in r_dict['Search']:
                yield Movie(i['Title'], i['Year'], i['Type'])


omdb = OmdbSdk("37e4a2ab")

for movie in (omdb.get_movie("movie", "Batman")):
    print(movie.get_title())

