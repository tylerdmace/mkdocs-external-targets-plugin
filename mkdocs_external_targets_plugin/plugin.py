import uuid
from bs4 import BeautifulSoup

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

def cleanExternalLinks(content):
  html = BeautifulSoup(content, features = "html5lib")
  anchors = html.find_all('a')

  for anchor in anchors:
    if len(anchor["href"].split("?")) > 1:
      anchor["href"] += "&"
    else:
      anchor["href"] += "?"

    anchor["href"] += f'cb={uuid.uuid4()}'

    if anchor["href"].find('http') != -1:
      anchor["target"] = "_blank"

  return html.prettify()

class ExternalTargets(BasePlugin):
  def on_post_page(self, content, **kwargs):
    return cleanExternalLinks(content)