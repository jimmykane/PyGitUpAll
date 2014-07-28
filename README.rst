PyGitUpAll |Build Status|
=========================

Git-Up all your projects!

How this works
--------------

``git-up-all`` requires a projects.json containing a list of projects/repos to keep update
Running git-up-all will go to each project/repo and try to git-up and report back with
the results for each project.

Setup
-----

 - Install via ``pip install git-up-all``
 - Create a ``projects.json`` containing a list of projects (see example below)
 - Run ``git-up-all`` on that folder containing the projects.json


projects.json
-------------

This file should contain a list with projects/repos as below:

.. code-block:: javascript
    {
        "gitup": {
            "name": "PyGitUp",
            "git_url": "https://github.com/msiemens/PyGitUp.git",
            "absolute_path": "/Users/jimmykane/projects/pygitup"
        },
        "gitupall": {
            "name": "PyGitUpAll",
            "git_url": "https://github.com/jimmykane/PyGitUpAll.git",
            "absolute_path": "/Users/jimmykane/projects/pygitupall"
        }
    }


Version
-------
This is a pre-release. It's packaged for testing purposes only.

.. |Build Status| image:: https://travis-ci.org/jimmykane/PyGitUpAll.svg?branch=master
   :target: https://travis-ci.org/jimmykane/PyGitUpAll