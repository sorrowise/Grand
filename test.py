from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import os


def get_date_string(n, startdate):
	d = startdate - timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn
argv = ['5','2010-10-01']
startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))
curdate = get_date_string(5,startdate)

#print "echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt"
#print "GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update'"
print "echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update'; git push;"
