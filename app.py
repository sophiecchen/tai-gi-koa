#index page

#here be setup
#when have a new computer, py -m pip install Flask
from flask import Flask, render_template, request, redirect, url_for

#functions to interact with OS
import os

#for the random song function
import random

app = Flask(__name__)



#main page
#these can use the post and get methods
#get happens initially, post happens after search submit
@app.route("/", methods=["POST", "GET"])
@app.route("/home/", methods=["POST", "GET"])
@app.route("/index/", methods=["POST", "GET"])
def home():
    #if search submit
    if request.method == "POST":
        search = request.form["searchIn"]
        #send this information to the collection page (with already searched results)
        if search == "":
            return redirect("/collection/")
        else:
            return redirect("/collection/search=" + search)
    else:
        #the main page
        return render_template("index.html", title="Tâi-gí-koa")

#random function
@app.route("/randomSong/")
def randomSong():
    songDirs = os.listdir(".\\koa\\")
    randIndex = random.randrange(0, len(songDirs))
    return redirect("/collection/" + songDirs[randIndex]) 



#find all songs that match a keyword
def searchKey(keyword):
    #all of the songs in a list
    songDirs = os.listdir(".\\koa\\")
    songMatches = []

    #search for the keyword in each song
    for song in songDirs:
        keyPath = ".\\koa\\" + song + "\\keys.txt"
        if os.path.isfile(keyPath):
            with open(keyPath, 'r', encoding="utf8") as keyFile:
                #checks for everything in lowercase
                if keyword.lower() in keyFile.read():
                    songMatches.append(song)

    #an array
    return songMatches

#finds certain information about a song in the info file
def findInfo(koaInfoPath, infoToFind):
    #with automatically takes care of closing the file!
    with open(koaInfoPath, 'r', encoding="utf8") as infoFile:
        #an array of all the content in the file, line by line
        content = infoFile.readlines()

        for i in range(0, len(content), 3):
            if infoToFind in content[i]:
                return content[i+1]
        
        return ""

#collection page
#url for no search and search
@app.route("/collection/", methods=["POST", "GET"])
@app.route("/collection/search=", methods=["POST", "GET"])
@app.route("/collection/search=<query>", methods=["POST", "GET"])
@app.route("/collection/search=/page=<page>", methods=["POST", "GET"])
@app.route("/collection/search=<query>/page=<page>", methods=["POST", "GET"])
#so that the default query is nothing and the default page is 1
def collection(query="", page=1):
    #if searching on the collection page (not from home)
    if request.method == "POST":
        #query value from form!
        query = request.form["searchCol"]
        #refresh url!
        return redirect("/collection/search=" + query)

    #split into array of different words
    searchWords = query.split(' ')

    #dictionary
    songMatches = {}

    #add the matching songs for each word
    for word in searchWords:
        for song in searchKey(word):
            if (song in songMatches.keys()):
                songMatches[song] += 1
            else:
                songMatches[song] = 0
    
    #make dictionary of song matches with all info
    for song in songMatches:
        koaInfoPath = ".\\koa\\" + song + "\\info.txt"
        songMatches[song] = [songMatches[song], findInfo(koaInfoPath, "hantitle").strip('\n'), findInfo(koaInfoPath, "pojartist").strip('\n'), findInfo(koaInfoPath, "hanartist").strip('\n')]

    #songMatches.items(): list of tuples of key-value pairs
    #key=lambda x:x[1]: compare the values not the keys!
    #reverse=True: sort from most to least
    songListSort = sorted(songMatches.items(), key=lambda x:x[1], reverse=True)

    #change list of tuples into dictionary
    songMatches = dict(songListSort)

    #matches = dictionary of songmatches
    #matchKeys = list of songmatch keys
    #page = the page number
    #numPages = the number of pages that will be needed
    return render_template("collection.html", title="Collection | Tâi-gí-koa", query=query, matches=songMatches, matchKeys=list(songMatches.keys()), page=int(page), numSongs=len(songMatches), numPages=len(songMatches)//20+1)



#returns the song lyrics at a certain path
def openSong(koaPath):
    #returns song if song file exists and "" if it does not
    if os.path.isfile(koaPath):
        with open(koaPath, 'r', encoding="utf8") as koaFile:

            #replace \n with <br> because flask autoescapes html tags...
            return koaFile.read().replace("\n", "<br>")
    else:
        return ""

#individual song page
#returns the html file with appropriate content
@app.route("/collection/<koaName>/")
def koa(koaName):
    #searches for the song
    #use \\ for a literal \
    koaInfoPath = ".\\koa\\" + koaName + "\\info.txt"

    if os.path.isfile(koaInfoPath):
        #open title file here! find title and artists
        pTitle = findInfo(koaInfoPath, "pojtitle").strip('\n')
        hTitle = findInfo(koaInfoPath, "hantitle").strip('\n')
        pArtist = findInfo(koaInfoPath, "pojartist").strip('\n')
        hArtist = findInfo(koaInfoPath, "hanartist").strip('\n')
        video = findInfo(koaInfoPath, "video").strip('\n')

        #open the lyrics here
        pKoaPath = ".\\koa\\" + koaName + "\\" + findInfo(koaInfoPath, "pojkoa").strip('\n')
        pKoa = openSong(pKoaPath)

        hKoaPath = ".\\koa\\" + koaName + "\\" + findInfo(koaInfoPath, "hankoa").strip('\n')
        hKoa = openSong(hKoaPath)

        return render_template("koa.html", pojTitle=pTitle, hanTitle = hTitle, pojArtist = pArtist, hanArtist = hArtist, pojKoa=pKoa, hanKoa=hKoa, video=video)
    else:
        #if does not exist
        return redirect("/notfound/")



#about page
@app.route("/about/")
def about():
    return render_template("about.html", title="About | Tâi-gí-koa") 



#run!
if __name__ == "__main__":
    app.run(debug=True)
