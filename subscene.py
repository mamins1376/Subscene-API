#! coding: utf-8
from bs4 import BeautifulSoup
import urllib.request
import re


class Subscene:

  SITE_DOMAIN = 'http://bbsub.ir'

  SEARCH_TYPE_EXACT = 0
  SEARCH_TYPE_TVSERIE = 1
  SEARCH_TYPE_POPULAR = 2
  SEARCH_TYPE_CLOSE = 3

  __SEARCH_TYPE_LOOKUP = {
      SEARCH_TYPE_EXACT: 'Exact',
      SEARCH_TYPE_TVSERIE: 'TV-Series',
      SEARCH_TYPE_POPULAR: 'Popular',
      SEARCH_TYPE_CLOSE: 'Close'
  }

  class Subtitle:

    def __init__(self, title, page, language, owner, comment, ziplink=False):
      self.title = str(title)
      self.page = str(page)
      self.language = str(language)
      self.owner = dict(owner)
      self.comment = str(comment)
      if ziplink:
        self.getZipLink()

    def __str__(self):
      return self.title

    def fromRow(row):
      title = row.find('td', 'a1').a.find_all('span')[1].text
      title = re.sub(r'^\s+', '', title)
      title = re.sub(r'\s+$', '', title)

      page = Subscene.SITE_DOMAIN + row.find('td', 'a1').a.get('href')

      language = row.find('td', 'a1').a.find_all('span')[0].text
      language = re.sub(r'\s+', '', language)

      owner = {}
      owner_username = row.find('td', 'a5').a.text
      owner['username'] = re.sub(r'\s+', '', owner_username)
      owner_page = row.find('td', 'a5').a.get('href')
      owner['page'] = Subscene.SITE_DOMAIN + owner_page

      comment = row.find('td', 'a6').div.text
      comment = re.sub(r'^\s+', '', comment)
      comment = re.sub(r'\s+$', '', comment)

      subtitle = Subscene.Subtitle(title, page, language, owner, comment)
      return subtitle

    def getZipLink(self):
      soup = Subscene._Subscene__get_soup(Subscene, self.page)
      self.zipped = Subscene.SITE_DOMAIN + \
          soup.find('div', 'download').a.get('href')

  class Film:

    def __init__(self, title, year, imdb, cover, subtitles):
      self.title = str(title)
      self.year = int(year)
      self.imdb = str(imdb)
      self.cover = str(cover)
      self.subtitles = tuple(subtitles)

    def __str__(self):
      return self.title

    def fromURL(url):
      soup = Subscene._Subscene__get_soup(Subscene, url)

      content = soup.find('div', 'subtitles byFilm')
      header = content.find('div', 'box clearfix')

      cover = header.find('div', 'poster').img.get('src')

      title = header.find('div', 'header').h2.text
      title = re.sub(r'^\s+', '', title[:-12])
      title = re.sub(r'\s+$', '', title)

      imdb = header.find('div', 'header').h2.find('a', 'imdb').get('href')

      year = header.find('div', 'header').ul.li.text
      year = int(re.findall(r'[0-9]+', year)[0])

      subtitles = []
      rows = content.find('table').tbody.find_all('tr')
      for row in rows:
        if row.td.a is None:
          continue

        subtitle = Subscene.Subtitle.fromRow(row)
        subtitles.append(subtitle)

      film = Subscene.Film(title, year, imdb, cover, subtitles)
      return film

  def Search(self, term, search_type=SEARCH_TYPE_CLOSE):
    url = "{}/subtitles/title?q={}&l=".format(Subscene.SITE_DOMAIN, term)

    soup = self.__get_soup(url)

    if self.__section_exist(soup, Subscene.SEARCH_TYPE_EXACT):
      return self.__get_first(soup, Subscene.SEARCH_TYPE_EXACT)

    if search_type == Subscene.SEARCH_TYPE_EXACT:
      return None

    if self.__section_exist(soup, Subscene.SEARCH_TYPE_TVSERIE):
      return self.__get_first(soup, Subscene.SEARCH_TYPE_TVSERIE)

    if search_type == Subscene.SEARCH_TYPE_TVSERIE:
      return None

    if self.__section_exist(soup, Subscene.SEARCH_TYPE_POPULAR):
      return self.__get_first(soup, Subscene.SEARCH_TYPE_POPULAR)

    if search_type == Subscene.SEARCH_TYPE_POPULAR:
      return None

    if self.__section_exist(soup, Subscene.SEARCH_TYPE_CLOSE):
      return self.__get_first(soup, Subscene.SEARCH_TYPE_CLOSE)

    return None

  def __get_soup(self, url):
    url = re.sub('\s', '+', url)

    html_doc = urllib.request.urlopen(url).read()
    html_doc = html_doc.decode("utf-8")
    soup = BeautifulSoup(html_doc, 'html.parser')

    return soup

  def __section_exist(self, soup, section):
    tag_text = Subscene.__SEARCH_TYPE_LOOKUP[section]
    headers = soup.find('div', 'search-result').find_all('h2')
    for header in headers:
      if tag_text in header.text:
        return True
    return False

  def __get_first(self, soup, section):
    tag_text = Subscene.__SEARCH_TYPE_LOOKUP[section]
    headers = soup.find('div', 'search-result').find_all('h2')
    for header in headers:
      if tag_text in header.text:
        tag = header
        break

    film_url = tag.findNext('ul').find('li').div.a.get('href')
    film_url = Subscene.SITE_DOMAIN + film_url

    film = Subscene.Film.fromURL(film_url)
    return film
