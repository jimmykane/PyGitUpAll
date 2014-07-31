PyGitUpAll |Build Status|
=========================

Git-Up all your projects!

Why use ``git-up-all`` ?
------------------------

 - Tired of going into each repo and ``pulling/rebasing/stashing`` in order to update
 - Tired of updating all branches over all the repos you have following the above tactics?
 - Need one custom action for sourcetree for eg? Just add ``git-up-all --sourcetree`` and you are good to go

How it works
------------

1. Reads a json file (or SourceTree list OSX) containing the list of repos you want to keep updated (could also be sourced controlled).

2. Iterates over each folder containing the repos provided and executes git-up as a module

3. Prints results for each repo

- Note that it will skip any fails and leaves it up to the user to manually resolve the conflicts. Currently it wont check if the repo is inside arebse or no.


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




Changelog
---------

v0.3.0 (*2014-08-01*)
~~~~~~~~~~~~~~~~~~~~~~~

- (BETA) Support for reading from SourceTree on OSX systems for now. Run with ``--sourcetree``
- Logic fixes


v0.2.0.1 (*2014-07-29*)
~~~~~~~~~~~~~~~~~~~~~~~
- This is a pre-release. I will start most of the work in this section after tests are done


@TODO
-----

- Check repo status (rebase etc)
- Check for branch ``origin`` validity
- Patch ``PyGitUp`` to use dir paths as arguments let it do the chdir kind or the work is chdir is not needed
- Add the tests finally
- Rethink about structure and integration with ``PyGitUp``

Acknowledgements
----------------

Thanks to the original port of GitUp in python (PyGitUp) by msiemens

 - git: https://github.com/msiemens/PyGitUp.git

.. |Build Status| image:: https://travis-ci.org/jimmykane/PyGitUpAll.svg?branch=master
   :target: https://travis-ci.org/jimmykane/PyGitUpAll