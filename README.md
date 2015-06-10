# lmastracker
A hastily thrown-together django project for storing and browsing details of
who did what on LMAS projects.

The Ultimate Source of Truth is the castcrews.txt file in the root folder. The
idea is that anybody can edit this file and Joe will merge the changes and
import the new data on the server using the import_castcrews.py management script.
