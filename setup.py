# coding=utf-8
from setuptools import setup, find_packages

setup(
    name="git-up-all",
    version="0.1.4",
    packages=find_packages(exclude=["tests"]),
    scripts=['PyGitUpAll/gitupall.py'],
    install_requires=['GitPython==0.3.2.RC1', 'git-up==1.1.4',
                      'termcolor==1.1.0'],

    # Tests
    test_suite="nose.collector",
    tests_require='nose',

    # Executable
    entry_points={
        'console_scripts': [
            'git-up-all = gitupall:run'
        ]
    },

    zip_safe=False,

    # Metadata
    author="Dimitrios Kanellopoulos",
    author_email="jimmykane9@gmail.com",
    description="Run git-up trough a json list of repos",
    license="GPLv3",
    keywords="git git-up git-up-all",
    url="https://github.com/jimmykane/PyGitUpAll",
    download_url='https://github.com/jimmykane/PyGitUpAll/tarball/0.1.4',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Version Control",
        "Topic :: Utilities"
    ],

    long_description=open('README.rst').read()
)
