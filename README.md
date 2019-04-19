# Subscene-API (unmaintained)
Unofficial Python API for Subscene subtitle database.

_NOTE_: this project is no longer maintained - use [my fork of Subliminal](https://github.com/mamins1376/subliminal)
 to with the added bonus of a nicely designed API. Use `develop` branch for subscene support until it gets merged
with the upstream repository.

## Usage

1. Clone the repo:

    `$ git clone https://github.com/mamins1376/Subscene-API subscene`

2. Install dependencies:

    `$ cd subscene && sudo pip install -r requirements.txt`

3. Fire it:
```
$ python3
>>> import subscene
>>> film = subscene.search('Ex Machina')
>>> subtitle = film.subtitles[42]
>>> subtitle.url
'http://subscene.com/subtitles/ex-machina/arabic/1141161'
>>> subtitle.zipped_url
'http://subscene.com/subtitle/download?mac=xR_n9E9cIdBzvp4ayAVHV8N7lDHHWIpZarWcT4l_j0SG4x_qSGFVHKG26EdRzUUL0'
```

Have Fun!
