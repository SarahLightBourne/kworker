from typing import Dict, List


class Category:
  URL = "https://kwork.ru/projects"

  def __init__(self, name: str, params: Dict) -> None:
    self.name, self.params = name, params
    self.projects_cache: List[str] = None
