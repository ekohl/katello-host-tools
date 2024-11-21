import os.path
from katello.utils import ConfigParser
from katello.constants import REPOSITORY_PATH, ZYPPER

class EnabledReport(object):
    def __generate(self):
        if not os.path.exists(self.repofile):
            return {"enabled_repos": {"repos": []}}

        config = ConfigParser()
        config.read(self.repofile)
        enabled_sections = [section for section in config.sections() if config.getboolean(section, "enabled")]
        enabled_repos = [{"repositoryid": section, "baseurl": [self._format_str(config.get(section, "baseurl"))]} for section in enabled_sections]
        return {"enabled_repos": {"repos": enabled_repos}}

    def __init__(self, repo_file=REPOSITORY_PATH):
        """
        :param path: A .repo file path used to filter the report.
        :type path: str
        """
        self.repofile = repo_file
        self.content = self.__generate()

    def __str__(self):
        return str(self.content)

    def _format_str(self, repo_url):
        """
        returns a formatted string

        :param repo_url: a repo URL that you want to format
        :type path: str
        """

        if ZYPPER:
            return self._cut_question_mark(repo_url)
        else:
            return repo_url;

    def _cut_question_mark(self, repo_url):
        """
        returns a string where everything after the first occurence of ? is truncated

        :param repo_url: a repo URL that you want to modify
        :type path: str
        """
        return repo_url[:repo_url.find('?')]
