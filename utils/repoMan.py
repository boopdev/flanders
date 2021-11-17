import git
from os import PathLike, makedirs
from os.path import exists
from typing import Any, Dict, Union
import json

class RepositoryManagementHelper(object):
    def __init__(self, repositoryPath : PathLike):
        self.repo_path = repositoryPath

        self.ensure_repo_path()

    def ensure_repo_path(self) -> None:
        """
        Ensures that the directory for repositories actually exists, since its in 
        .gitignore and im too lazy to find out how to do a lower-level exclusion.
        """
        makedirs(self.repo_path, exist_ok=True)

    def getRepositoryList(self):
        pass

    def getRepositoryConfig(self, dirExtension : str) -> Union[Dict[str, Any], None]:
        """Returns the dict containing the data from the repository meta file

        :param dirExtension: The user-defined name of the repository
        :type dirExtension: str
        :return: The json data related to the provided repository, if not found, this returns `None`
        :rtype: Dict[str, Any] or `None`
        """
        if not exists(self.repo_path + f"/{dirExtension}/flandersRepo.json"):
            return None

        with open(self.repo_path + f"/{dirExtension}/flandersRepo.json", "r") as meta_file:
            data = json.load(meta_file)

        return data

    def cloneRepository(self, dirExtension : str, url : str) -> None:
        """Clones a repository from a url

        :param url: The url for the repository
        :type url: str
        """
        x = git.Repo.clone_from(url, to_path = self.repo_path + f"/{dirExtension}")
        

if __name__ == "__main__":
    test_repo = "https://github.com/boopdev/flanders-ext-test"
    rmh = RepositoryManagementHelper(r"C:\Users\steel\Desktop\flanders\repositories")
    rmh.cloneRepository("testBoopdev", test_repo)
