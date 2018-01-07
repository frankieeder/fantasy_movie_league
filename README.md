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

In Terminal, run either all_weeks.py (which runs all sidecar files), or one of the sidecar files (of the format week_<quarter>_<year>_<week>.py) to compute the best bracket for the specific week to which that sidecar file corresponds.

To add a new week, run new_week.py and input the necessary strings. This will also add the new week you make to all_weeks.py


Raw strings from Fantasy Movie League Insider, Box Office Report, and the Fantasy
Movie League are located in the files that accompany fml.py, the primary code file.
Accompanying files each correspond to a week, formatted as <year>_<quarter>_<week>.py
Running a file will parse and compute the best cineplex (predictions) for that week.
