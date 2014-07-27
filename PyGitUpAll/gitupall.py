#!/usr/bin/python
# coding=utf-8

import sys
import os

from git import Repo
from PyGitUp.git_wrapper import GitError
from PyGitUp.gitup import GitUp
from PyGitUpAll.utils import read_projects_from_json
from termcolor import colored


PROJECTS_FILE = 'projects.json'


class GitUpAll(object):
    def git_up_all(self):

        current_dir = os.getcwd()
        projects = read_projects_from_json(PROJECTS_FILE)
        if not projects:
            print(colored("Could not read ", color="red") + colored(PROJECTS_FILE, color="red", attrs=['bold']))
            return False

        print(colored("Loaded projects from ", attrs=['bold']) + colored(PROJECTS_FILE, color="green"))

        for project_name, project_settings in projects.iteritems():
            print(
                colored('- Working on: ', attrs=['bold']) + colored(
                    str(project_name + " " + project_settings['absolute_path']),
                    attrs=['underline']))
            if not os.path.isdir(project_settings['absolute_path']):
                print ("Directory not found. Cloning from url")
                repo = Repo.clone_from(url=project_settings['git_url'], to_path=project_settings['absolute_path'])
                print (colored("Repository cloned", color='green'))
            # Workaround for now
            os.chdir(project_settings['absolute_path'])
            # Check, if we're in a git repo
            self.sync_repository(project_settings)
            os.chdir(current_dir)
            print(colored('Repository updated', color="green", attrs=['bold']))


    @staticmethod
    def sync_repository(project_settings):
        try:
            GitUp().run()
        except GitError:
            print (colored("Could not update repository: " + project_settings['name'], color='red'))
            return False


def run():
    GitUpAll().git_up_all()


if __name__ == '__main__':
    run()