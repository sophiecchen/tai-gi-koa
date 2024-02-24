# Tâi-gí-koa
This repository contains the code for Tâi-gí-koa, a website that displays Taiwanese song lyrics in two writing systems. View the website [here](https://tai-gi-koa.vercel.app/).

To run locally, type py "index.py" in terminal and view the website locally on http://127.0.0.1:5000.

Commands for song maintenance:
* addsong: addsong.py adds a new song directory and creates the info.txt file
* deletesong: deletesong.py deletes the directory and all associated files for a song

Structure:
* Each song is made of a directory, info.txt file, and a keyword.txt file (all lowercase)
* Each song should also contain (optional) lyric files
* Actual lyrics and lyric files must be added manually. Any song modifications must be done manually.
