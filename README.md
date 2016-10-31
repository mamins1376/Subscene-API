# Subscene-API
Unofficial Python API for Subscene subtitle database.

## Usage

1. Clone the repo:

    `$ git clone https://github.com/mamins1376/Subscene-API subscene`

2. Install dependencies:

    `$ cd subscene && sudo pip install -r requirements.txt`

3. Fire it:
```
$ python3
>>> from subscene import Subscene
>>> subscene = Subscene()
>>> film = subscene.search('Ex Machina')
>>> subtitle = film.subtitles[42]
>>> subtitle.page
'http://bbsub.ir/subtitles/ex-machina/arabic/1141161'
>>> subtitle.get_zip_link()
'http://bbsub.ir/subtitle/download?mac=xR_n9E9cIdBzvp4ayAVHV8N7lDHHWIpZarWcT4l_j0SG4x_qSGFVHKG26EdRzUUL0'
```

Have Fun!
