PyGitUpAll |Build Status|
=========================

Git-Up all your projects!

Why use ``git-up-all`` ?
------------------------

 - Tired of going into each repo and ``pulling/rebasing/stashing`` in order to update
 - Tired of updating all branches over all the repos you have following the above tactics?
 - Need one custom action for sourcetree for eg?

How it works
------------

1. Reads a json file containing the list of repos you want to keep updated (could also be sourced controlled)

2. Iterates over each folder containing the repos provided and executes git-up as a module

3. Prints results for each repo

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


@TODO
-----

- Check for branch ``origin`` validity
- Patch ``PyGitUp`` to use dir paths as arguments let it do the chdir kind or the work is chdir is not needed
- Add the tests finally
- Rethink about structure and integration with ``PyGitUp``


Version
-------
This is a pre-release. I will start most of the work in this section after tests are done


Acknowledgements
----------------

Thanks to the original port of GitUp in python (PyGitUp) by msiemens

 - git: https://github.com/msiemens/PyGitUp.git

.. |Build Status| image:: https://travis-ci.org/jimmykane/PyGitUpAll.svg?branch=master
   :target: https://travis-ci.org/jimmykane/PyGitUpAll
