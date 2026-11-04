class Project:
    def __init__(
        self, name, description, project_license, authors,
        dependencies, dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = project_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _listaa(self, items):
        if len(items) == 0:
            return "-"
        return "\n".join(f"- {item}" for item in items)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self._listaa(self.authors)}"
            f"\n\nDependencies:\n{self._listaa(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n"
            f"{self._listaa(self.dev_dependencies)}"
        )