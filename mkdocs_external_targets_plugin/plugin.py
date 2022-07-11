from bs4 import BeautifulSoup

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

class ExternalTargets(BasePlugin):
  def on_page_content(self, content, **kwargs):
    html = BeautifulSoup(content)
    anchors = html.find_all('a')
    
    for anchor in anchors:
      if anchor["href"].find('http') != -1:
        anchor["target"] = "_blank"

    return html