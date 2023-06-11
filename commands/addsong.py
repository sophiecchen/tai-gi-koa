#adds a song

#functions to interact with OS
import os

if __name__ == "__main__":
    print("This command adds a new song directory and creates the info.txt file.")
    outer = True

    while (outer):
        pojTitle = input("Enter the title in POJ or 'q' to quit this command: ")
        
        #allows user to leave if command was run accidentally
        if (pojTitle == 'q'):
            break

        newPath = "C:\\Users\\sophi\\OneDrive\\Documents\\Tâi-gí-koa\\koa\\" + pojTitle

        if os.path.isfile(newPath):
            print("Sorry, this song already exists.")
        else:
            hanTitle = input("Enter the title in Hanji: ")
            pojArtist = input("Enter the artist name in POJ: ")
            hanArtist = input("Enter the artist name in Hanji: ")
            video = input("Enter the Youtube video ID: ")

            #creates the song folder
            os.makedirs(newPath)
            
            #creates info file
            with open(newPath + "\\info.txt", 'w', encoding="utf8") as infoFile:
                infoFile.write('pojtitle\n' + pojTitle + '\n\nhantitle\n' + hanTitle + '\n\npojartist\n' + pojArtist + '\n\nhanartist\n' + hanArtist + '\n\npojkoa\n' + pojTitle + ".txt\n\nhankoa\n" + hanTitle + ".txt\n\nvideo\n" + video)
            print("Info file created successfully.")
            
            #creates keys file (everything lowercase)
            with open(newPath + "\\keys.txt", 'w', encoding="utf8") as keysFile:
                keysFile.write(pojTitle.lower() + '\n' + hanTitle.lower() + '\n' + pojArtist.lower() + '\n' + hanArtist.lower())
            print("Keys file created successfully.")

            #asks whether POJ lyric file should be created
            pojAdd = True
            while (pojAdd):
                pojPref = input("Would you like to make a POJ lyric file? Enter 'y' for yes and 'n' for no: ")

                if (pojPref == 'n'):
                    pojAdd = False
                elif (pojPref == 'y'):
                    pojAdd = False
                    with open(newPath + "\\" + pojTitle + ".txt", 'w', encoding="utf8") as pojFile:
                        pojFile.write("Lyrics to be added.")
                    print("POJ lyric file created successfully.")

            #asks whether Hanji lyric file should be created
            hanAdd = True
            while (hanAdd):
                hanPref = input("Would you like to make a Hanji lyric file? Enter 'y' for yes and 'n' for no: ")

                if (hanPref == 'n'):
                    hanAdd = False
                elif (hanPref == 'y'):
                    hanAdd = False
                    with open(newPath + "\\" + hanTitle + ".txt", 'w', encoding="utf8") as hanFile:
                        hanFile.write("Lyrics to be added.")
                    print("Hanji lyric file created successfully.")                    

            print("Song added successfully.")


        #allows the user to continue input without running command again
        repeat = True
        while (repeat):
            again = input("Would you like to add another song? Enter 'y' for yes and 'n' for no: ")

            if (again == 'n'):
                repeat = False
                outer = False
            elif (again == 'y'):
                repeat = False