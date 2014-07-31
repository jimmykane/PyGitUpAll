#!/usr/bin/python
# coding=utf-8

import os
import sys
import docopt

from git import Repo
from git.repo.fun import is_git_dir
from PyGitUp.git_wrapper import GitError
from PyGitUp.gitup import GitUp
from PyGitUpAll.utils import read_projects_from_json, read_projects_from_sourcetree
from PyGitUpAll.project import Project
from termcolor import colored


PROJECTS_FILE = "projects.json"


class GitUpAll(object):

    start_dir = os.getcwd()

    def git_up_all(self, sourcetree=False):

        if sourcetree:
            print(colored("Loading projects from ", attrs=["bold"]) + colored("SourceTree" + "\n", color="green"))
            projects = read_projects_from_sourcetree()
        else:
            print(colored("Loading projects from ", attrs=["bold"]) + colored(PROJECTS_FILE + "\n", color="green"))
            projects = read_projects_from_json(PROJECTS_FILE)

        if not projects:
            print(colored("Could not read projects\n", color="red"))
            return False


        for project_name, project_settings in projects.iteritems():
            # Check if we are able to initialize settings to an object
            project = Project(project_settings)
            print(colored("- Working on: " + project.name + " @" + project.absolute_path, attrs=["underline"]))
            if not project:
                print (colored("Could not create project " + project_name, color="red"))
                continue

            # Check if a dir exists or clone
            if not os.path.isdir(project.absolute_path):
                print ("Project is not directory or not initialized repo. Cloning from url")
                project.repo = Repo.clone_from(url=project.git_url, to_path=project.absolute_path)
                print (colored("Repository cloned", color="green"))


            # Check if dir is empty and if yes clone
            if os.listdir(project.absolute_path) == []:
                print ("Project is not initialized repo. Cloning from url")
                project.repo = Repo.clone_from(url=project.git_url, to_path=project.absolute_path)
                print (colored("Repository cloned", color="green"))

            # Check if the is not git and if not skip
            if not is_git_dir(os.path.join(self.start_dir, ".git")):
                print (colored("Project path is not a git dir and contains files. Skipping", color="red"))
                continue

            self.sync_repository(project)

            print(colored("Repository " + project.name + " updated\n", color="green", attrs=["bold"]))


    @classmethod
    def sync_repository(cls, project):

        # ugly chdir. Will try to patch pygitup
        os.chdir(project.absolute_path)
        try:
            # Creates a new object
            GitUp().run()
        except GitError:
            print (colored("Could not update repository: " + project.name, color="red"))
        finally:
            os.chdir(cls.start_dir)


def run():
    if '--sourcetree' in sys.argv:
        GitUpAll().git_up_all(sourcetree=True)
    else:
        GitUpAll().git_up_all(sourcetree=False)


if __name__ == "__main__":
    run()