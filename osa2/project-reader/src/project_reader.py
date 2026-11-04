import re
from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # TOML-merkkijono Pythonin sanakirjaksi
        data = tomli.loads(content)
        tiedot = data["project"]

        name = tiedot["name"]
        description = tiedot.get("description", "")
        project_license = tiedot.get("license", "")
        authors = [author["name"] for author in tiedot.get("authors", [])]
        dependencies = self._nimet(tiedot.get("dependencies", []))
        dev_dependencies = self._nimet(
            data.get("dependency-groups", {}).get("dev", [])
        )

        return Project(
            name,
            description,
            project_license,
            authors,
            dependencies,
            dev_dependencies,
        )

    def _nimet(self, riippuvuudet):
        # "flask>=3.1.3" -> "flask"
        return [re.split(r"[<>=!~;\[ ]", r)[0] for r in riippuvuudet]