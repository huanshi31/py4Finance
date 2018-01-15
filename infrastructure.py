#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:16:23 2018

@author: huanshi
"""
#==============================================================================
# ipython inline functions
#==============================================================================
#Huans-MacBook:~ huanshi$ ipython
#Python 2.7.13 |Anaconda custom (x86_64)| (default, Dec 20 2016, 23:05:08) 
#Type "copyright", "credits" or "license" for more information.
#
#IPython 5.3.0 -- An enhanced Interactive Python.
#?         -> Introduction and overview of IPython's features.
#%quickref -> Quick reference.
#help      -> Python's own help system.
#object?   -> Details about 'object', use 'object??' for extra details.
#
#In [1]: %lsmagic
#Out[1]: 
#Available line magics:
#%alias  %alias_magic  %autocall  %autoindent  %automagic  %bookmark  %cat  %cd  %clear  %colors  %config  %cp  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %man  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
#
#Available cell magics:
#%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
#
#Automagic is ON, % prefix IS NOT needed for line magics.
#
#In [2]: import numpy as np
#
#In [3]: %time np.sin(np.arange(10000))
#CPU times: user 2.04 ms, sys: 623 µs, total: 2.67 ms
#Wall time: 2.36 ms
#Out[3]: 
#array([ 0.        ,  0.84147098,  0.90929743, ...,  0.43692413,
#        0.99297289,  0.63608696])
#
#In [4]: %prun np.sin(np.arange(10000))
#         3 function calls in 0.001 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {numpy.core.multiarray.arange}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 
#In [5]: %bookmark current
#
#In [6]: %bookmark -l
#Current bookmarks:
#current -> /Users/huanshi
#l       -> /Users/huanshi/Documents/GitHub/py4Finance
#now     -> /Users/huanshi/Documents/GitHub/py4Finance
#
#In [7]: %bookmark?
#Docstring:
#Manage IPython's bookmark system.
#
#%bookmark <name>       - set bookmark to current dir
#%bookmark <name> <dir> - set bookmark to <dir>
#%bookmark -l           - list all bookmarks
#%bookmark -d <name>    - remove bookmark
#%bookmark -r           - remove all bookmarks
#
#You can later on access a bookmarked folder with::
#
#  %cd -b <name>
#
#or simply '%cd <name>' if there is no directory called <name> AND
#there is such a bookmark defined.
#
#Your bookmarks persist through IPython sessions, but they are
#associated with each profile.
#File:      ~/Desktop/MyFiles/anaconda/lib/python2.7/site-packages/IPython/core/magics/osm.py

#==============================================================================
# Huans-MacBook:~ huanshi$ conda
# usage: conda [-h] [-V] command ...
# 
# conda is a tool for managing and deploying applications, environments and packages.
# 
# Options:
# 
# positional arguments:
#   command
#     info         Display information about current conda install.
#     help         Displays a list of available conda commands and their help
#                  strings.
#     list         List linked packages in a conda environment.
#     search       Search for packages and display their information. The input
#                  is a Python regular expression. To perform a search with a
#                  search string that starts with a -, separate the search from
#                  the options with --, like 'conda search -- -h'. A * in the
#                  results means that package is installed in the current
#                  environment. A . means that package is not installed but is
#                  cached in the pkgs directory.
#     create       Create a new conda environment from a list of specified
#                  packages.
#     install      Installs a list of packages into a specified conda
#                  environment.
#     update       Updates conda packages to the latest compatible version. This
#                  command accepts a list of package names and updates them to
#                  the latest versions that are compatible with all other
#                  packages in the environment. Conda attempts to install the
#                  newest versions of the requested packages. To accomplish
#                  this, it may update some packages that are already installed,
#                  or install additional packages. To prevent existing packages
#                  from updating, use the --no-update-deps option. This may
#                  force conda to install older versions of the requested
#                  packages, and it does not prevent additional dependency
#                  packages from being installed. If you wish to skip dependency
#                  checking altogether, use the '--force' option. This may
#                  result in an environment with incompatible packages, so this
#                  option must be used with great caution.
#     upgrade      Alias for conda update. See conda update --help.
#     remove       Remove a list of packages from a specified conda environment.
#     uninstall    Alias for conda remove. See conda remove --help.
#     config       Modify configuration values in .condarc. This is modeled
#                  after the git config command. Writes to the user .condarc
#                  file (/Users/huanshi/.condarc) by default.
#     clean        Remove unused packages and caches.
#     package      Low-level conda package utility. (EXPERIMENTAL)
# 
# optional arguments:
#   -h, --help     Show this help message and exit.
#   -V, --version  Show the conda version number and exit.
# 
# other commands, such as "conda build", are available when additional conda
# packages (e.g. conda-build) are installed
#==============================================================================

