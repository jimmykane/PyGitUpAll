# coding=utf-8

import os
import sys
import json
import biplist


"""
Utility and Helpers
"""


def read_projects_from_json(projects_file):
    file_handler = os.path.join('.', projects_file)
    try:
        with open(file_handler) as json_file:
            projects = json.load(json_file)
    except Exception as e:
        return False
    return projects


def read_projects_from_sourcetree():
    sourcetree_projects_dir = {
        "darwin": "Library/Application Support/SourceTree"
    }

    # Here this func should be responsible to check fo os and add paths
    browser_plist = biplist.readPlist(
        os.path.join(os.path.expanduser('~'), sourcetree_projects_dir[sys.platform], "browser.plist"))
    # Ugly hack for now and no other way
    strings = []
    for object in browser_plist['$objects']:
        if type(object) is str:
            strings.append(object)
    repos = {}
    for string in strings:
        if '/' in string:
            repos.update({
            string.rpartition('/')[2]: {'name': string.rpartition('/')[2], 'git_url': None, 'absolute_path': string}})

    return repos

