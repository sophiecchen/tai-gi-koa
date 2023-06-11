#deletes a song

#functions to interact with OS and delete all files in a directory
import os, shutil

if __name__ == "__main__":
    print("This command deletes the directory and all associated files for a song.")

    outer = True
    while (outer):
        name = input("Enter the song's title in POJ or 'q' to quit this command: ")

        #allows user to leave if command was run accidentally
        if (name == 'q'):
            break

        path = "C:\\Users\\sophi\\OneDrive\\Documents\\Tâi-gí-koa\\koa\\" + name

        #if the song does infact exist (checks for directory)
        if os.path.isdir(path):
            
            #checks to make sure that the user indeed wants to delete the song
            makeSure = True
            while (makeSure):
                check = input("Are you sure you want to delete " + name + "? This action cannot be undone. Enter 'y' to delete and 'n' to keep " + name + ": ")

                if (check == 'n'):
                    makeSure = False
                elif (check == 'y'):
                    makeSure = False
                    shutil.rmtree(path)
                    print("Song deleted successfully.")
    
        else:
            print("Sorry, this song does not exist.")
        

        #allows the user to continue input without running command again
        repeat = True
        while (repeat):
            again = input("Would you like to delete another song? Enter 'y' for yes and 'n' for no: ")

            if (again == 'n'):
                repeat = False
                outer = False
            elif (again == 'y'):
                repeat = False