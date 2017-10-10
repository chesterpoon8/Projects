# Project

For use in Google Chrome as default browser

This project I built at work trying to unify provider schedules in the NYU Emergency Dept.  It compiles the schedule information for all three platforms to be readable on tableau server where it is disseminated to staff.  It's crude, but something I'm very proud of as my first project in Python having read a book on Python only a month ago.

It uses selenium to download all the schedules and openpyxl to work with the data to be read by an existing tableau desktop file.  Ultimately, it's automatically refreshed and uploaded to Tableau server.
