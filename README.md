# Subscene-API
Unofficial Python API for Subscene subtitle service using BeautifulSoup4 library.

## Usage
```
$ git clone https://github.com/mamins1376/Subscene-API SubsceneAPI
$ python3
>>> from SubsceneAPI import Subscene
>>> subscene = Subscene()
>>> film = subscene.Search('Ex Machina')
>>> subtitle = film.subtitles[42]
>>> subtitle.page
'http://bbsub.ir/subtitles/ex-machina/arabic/1141161'
>>> subtitle.getZipLink()
>>> subtitle.zipped
'http://bbsub.ir/subtitle/download?mac=xR_n9E9cIdBzvp4ayAVHV8N7lDHHWIpZarWcT4l_j0SG4x_qSGFVHKG26EdRzUUL0'
```

Have Fun!
