#!/usr/bin/python
# coding=utf-8

import os
import sys
import docopt

from git import Repo, exc
from git.repo.fun import is_git_dir
from PyGitUp.git_wrapper import GitError
from PyGitUp.gitup import GitUp
from PyGitUpAll.utils import read_projects_from_json, read_projects_from_sourcetree
from PyGitUpAll.project import Project
from termcolor import colored


PROJECTS_FILE = "projects.json"


class GitUpAll(object):

    def __init__(self):
        self.start_dir = os.getcwd()

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

        results = {}
        for project_name, project_settings in projects.iteritems():

            """
            This nees to be rewritten and tested!
            """
            # Check if we are able to initialize settings to an object
            project = Project(project_settings)
            if not project:
                print (colored("Could not read project " + project_name, color="red"))
                continue
            print(colored("- Working on: " + project.name + " @" + project.absolute_path, attrs=["underline"]))

            # Check if a dir exists or clone
            if (not os.path.isdir(project.absolute_path) or os.listdir(project.absolute_path) == []) and project.git_url:
                print ("Project is not directory or not initialized repo. Cloning from url")
                project.repo = Repo.clone_from(url=project.git_url, to_path=project.absolute_path)
                print (colored("Repository cloned", color="green"))

            # Check if the is not git and if not skip
            if not is_git_dir(os.path.join(project.absolute_path, ".git")) and not project.git_url:
                print (colored("Project path is not a git dir and has no info. Skipping", color="red"))
                continue

            # @todo probably should be moved
            if self.sync_repository(project):
                results.update({project.name: True})
            else:
                results.update({project.name: False})
            print(colored("- Finished on: " + project.name + " @" + project.absolute_path, attrs=["underline"]) + "\n")


        self.print_results(results)


    def sync_repository(self, project):

        result = False
        # ugly chdir. Will try to patch pygitup
        os.chdir(project.absolute_path)
        try:
            # Creates a new object all the time
            GitUp().run()
            result = True
        except (GitError, exc.GitCommandError, BaseException) as e:
            print (colored("Could not update repository: " + project.name, color="red"))
        finally:
            os.chdir(self.start_dir)
            return result


    def print_results(self, results):
        total = len(results)
        successes = 0
        fails = 0
        for name, success in results.iteritems():
            if success:
                print (colored(name, color="green"))
                successes += 1
            else:
                print (colored(name, color="red"))
                fails += 1

        print(colored("Total: " + str(total) + " projects", attrs=['bold'], color="green"))
        print(colored("Successful: " + str(successes) + " projects", attrs=['bold'], color="green"))
        print(colored("Fails: " + str(fails) + " projects", attrs=['bold'], color="red"))
        print(colored("Ration: " + str(float(successes)/float(total) * 100.0)[:4] + "% success", attrs=['underline'], color="green"))





def run():
    if '--sourcetree' in sys.argv:
        GitUpAll().git_up_all(sourcetree=True)
    else:
        GitUpAll().git_up_all(sourcetree=False)


if __name__ == "__main__":
    run()