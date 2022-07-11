from bleach import clean
from bs4 import BeautifulSoup

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

def cleanExternalLinks(content):
  html = BeautifulSoup(content, features = "html5lib")
  anchors = html.find_all('a')
  
  for anchor in anchors:
    if anchor["href"].find('http') != -1:
      anchor["target"] = "_blank"

  return html

class ExternalTargets(BasePlugin):
  def on_post_template(self, content, **kwargs):
    return cleanExternalLinks(content)

  def on_page_content(self, content, **kwargs):
    return cleanExternalLinks(content)