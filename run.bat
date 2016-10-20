python greenhat.py 5 2016-10-01

"echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt;
git add realwork.txt;
GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update';
git push;"
