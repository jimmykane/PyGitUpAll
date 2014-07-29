#!/usr/bin/python
# coding=utf-8


class Project(object):

    project_properties = [
        'name',
        'git_url',
        'absolute_path'
    ]

    def __new__(cls, project_settings):
        if not sorted(project_settings.keys()) == sorted(cls.project_properties):
            return None
        return cls
