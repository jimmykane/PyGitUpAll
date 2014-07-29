#!/usr/bin/python
# coding=utf-8


class Project(object):

    __allowed_properties = [
        'name',
        'git_url',
        'absolute_path'
    ]

    def __new__(cls, project_settings):
        # Check if project settings are a go for setting attributes
        if not sorted(project_settings.keys()) == sorted(cls.__allowed_properties):
            return None

        # Create attributes from provided dict
        for allowed_property in cls.__allowed_properties:
            setattr(cls, allowed_property, project_settings[allowed_property])

        return cls