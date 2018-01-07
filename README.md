CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Quick Start


INTRODUCTION
------------

An object-oriented version of the knapsack problem, fantasy_movie_league parses third-party box-office projections and computes the highest-earning Fantasy Movie League bracket for a given week.

Fantasy Movie League rules can be found here: https://fantasymovieleague.com/howtoplay


REQUIREMENTS
------------

 * Python 3.


QUICK START
-----------

In Terminal, run either all_weeks.py (which runs all sidecar files), or one of the sidecar files to compute the best bracket for the specific week to which that sidecar file corresponds.

To add and run a new week sidecar file, run new_week.py and input the necessary strings. This will also add the new week you make to all_weeks.py for later use.

If desired, you can use the interactive interpreter to further investigate possible earnings. Sidecar files are imported as modules in all_weeks.py, so to investigate the variables between weeks, simply run all_weeks.py in interactive mode and access the variables through the syntax "sidecar_file_name"."vairable_name".

All functions and classes are stored in fml.py.
