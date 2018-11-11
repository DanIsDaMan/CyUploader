#Import module needed for copying the .deb files from "adddebs" to "debs"
from shutil import copyfile
#Import module needed for delays, especially in printLetterByLetter()
import time
#Needed for stuff in printLetterByLetter()
import sys
#Needed for a lot of stuff, compressing Packages, running git.bat to stage, commit, & push,
#Deleting the files from "adddebs after they have been copied, getting the name of the current working directory,
#And iterating through all the .deb files in "adddebs".
#So this module is really useful.
import os

#NOTE : Put .deb files to be added in a folder called "adddebs",
#and make another folder called "debs". This one will be the desination.

#Creates the cool effect of printing out a string letter by letter.
#Someone showed this to me so I'm not really sure how it works.
def printLetterByLetter(string):
    #Iterates through the string.
    for char in string:
        #I guess this outputs each letter in the string?
        sys.stdout.write(char)
        #Not sure at all why this is needed.
        sys.stdout.flush()
        #Sets the speed this is done at.
        time.sleep(0.02)

#NOTE : THIS WILL NOT WORK YET UNLESS YOU DECOMPRESS YOUR "Packages.bz2" FILE TO "Packages".
#Get the path of the repo folder.
#This path is my specific path.
#path = str("C:\\Users\\hamid\\OneDrive\\Desktop\\DanIsDaMan.github.io\\adddebs")
#This path will work for anyone as long as this program is in the root of the repo folder.
path = str(os.getcwd() + "\\adddebs")
#For every file in the adddebs folder, i.e. Every new .deb file.
for file in os.listdir(path):
    file = str(file)
    #Slices off the ".deb" from the end of the file names.
    #Needed for the name that shows up on the repo.
    tweakName = str(file[0:-4])
    #All this stuff creates the metadata to be put in the Packages file.
    #Creates package name.
    package = str("Package: com.dan." + tweakName)
    #Creates main name to show up on the repo.
    name = str("Name: " + tweakName)
    #Asks for version number and creates format for it.
    version = str(input("Version Number for " + "\"" + str(tweakName) + "\":\n"))
    version = str("Version: " + version)
    #Gets the size of the .deb file.
    #This is the single line way of doing it, uses lots of brackets,
    #size = str((float(((os.path.getsize(os.getcwd() + "\\adddebs\\" + str(fileName)))/1000))) + "kb")
    #I like it but I didn't think other people would, so I broke it down.
    #Gets size from the file in bytes,
    size = float(os.path.getsize(os.getcwd() + "\\adddebs\\" + str(file)))
    #Divides size in bytes by 1000 to create size in kb,
    size = float(size/1000)
    #Creates correct format.
    size = str("Size: " + str(size) + "kb")
    #Creates architecture. SHould always be the same.
    architecture = str("Architecture: iphoneos-arm")
    #Asks for a description of what "Name of tweak/app/ect.".
    description = str(input("Description for " + "\"" + str(tweakName) + "\":\n"))
    description = str("Description: " + description)
    #Asks who is the maintainer of "Name of tweak/app/ect.".
    maintainerName = str(input("Name of Maintainer:\n"))
    #Asks for the email of the maintainer of "Name of tweak/app/ect.".
    maintainerEmail = str(input("Maintainer's Email Address:\n"))
    maintainer = str("Maintainer: " + maintainerName + " <" + maintainerEmail + ">")
    #Asks who is the author of "Name of tweak/app/ect." and formats it.
    authorName = str(input("Name of Author:\n"))
    #Asks for the email of the author of "Name of tweak/app/ect.".
    authorEmail = str(input("Author's Email Address:\n"))
    author = str("Author: " + authorName + " <" + authorEmail + ">")
    #Asks for what section "Name of tweak/app/ect." will be in.
    section = str(input("Section:\n"))
    section = str("Section: " + section)
    #Asks for hashsums for "Name of tweak/app/ect.".
    MD5sum = str(input("MD5sum:\n"))
    MD5sum = str("MD5sum: " + MD5sum)
    SHA1sum = str(input("SHA1sum:\n"))
    SHA1sum = str("SHA1sum: " + SHA1sum)
    SHA256sum = str(input("SHA256sum:\n"))
    SHA256sum = str("SHA256sum: " + SHA256sum)
    #Gets filepath for "Name of tweak/app/ect."
    filePath = str("debs//" + file)
    filePath = str("Filename: " + file)
    #makes a little blank fille to create a line gap in the Packages file.
    filler = str(" ")
    #Not needed beacuse I figured Python can edit it without renaming it.
    #Rename "Packages" to "Packages.txt" so that Python can edit it.
    #os.rename((os.getcwd() + "\\Packages"), (os.getcwd() + "\\Packages.txt"))
    #NOTE : THIS WILL NOT WORK YET UNLESS YOU DECOMPRESS YOUR "Packages.bz2" FILE TO "Packages".
    with open("Packages", "a") as Packages:
        #Adds all the metadata to "Packages".
        Packages.write(filler + "\n")
        Packages.write(package + "\n")
        Packages.write(tweakName + "\n")
        Packages.write(version + "\n")
        Packages.write(size + "\n")
        Packages.write(architecture + "\n")
        Packages.write(description + "\n")
        Packages.write(maintainer + "\n")
        Packages.write(author + "\n")
        Packages.write(section + "\n")
        Packages.write(MD5sum + "\n")
        Packages.write(SHA1sum + "\n")
        Packages.write(SHA256sum + "\n")
        Packages.write(filePath + "\n")
        #Closes the file.
        Packages.close()
    #Gets filepaths to move the .deb file and delete it from "adddebs".
    #Gets the filepath of the .deb file from inside "adddebs".
    filePathOld = str(os.getcwd() + "\\adddebs\\" + file)
    #Makes a new filepath inside "debs" to move the .deb file to.
    filePathNew = str(os.getcwd() + "\\debs\\" + file)
    #Copies the .deb file from "adddebs" to "debs".
    copyfile(filePathOld, filePathNew)
    #Removes the .deb file from "adddebs".
    os.remove(filePathOld)
    #Gves a messsage that the .deb file was added successfully.
    success = str("Successfully added " + file + " to your cydia repo!\n")
    printLetterByLetter(success)
#Compresses "Packages" to "Packages.bz2".
#Checks if "Packages.bz2" already exists.
#If it doesn't exist, it will go on and compress "Packages".
#If it does exist, it will say that it failed to compress it.
if not "Packages.bz2" in os.listdir(os.getcwd()):
    #After checking that "Packages.bz2" doesn't exist, it checks if anything is left in "adddebs".
    #I think they should be the other way around to be honest...
    if not os.listdir(os.getcwd() + "\\adddebs"):
        #Uses os.system() to run "bzip2.exe" on "Packages" to compress it.
        os.system(os.getcwd() + "\\bzip2.exe " + os.getcwd() + "\\Packages")
        #After compressing "Packages", it checks if "Packages.bz2" exists.
        #If it does exist, it will say that is successfully compressed it.
        #If it doesn't exist, it will say that it failed to compress it.
        if "Packages.bz2" in os.listdir(os.getcwd()):
            printLetterByLetter("Successfully compressed \"Packages\" to \"Packages.bz2\".\n")
            time.sleep(1)
        else:
            printLetterByLetter("Failed to compress \"Packages\" to \"Packages.bz2\".\n")
            time.sleep(1)
else:
    printLetterByLetter("Failed to compress \"Packages\" to \"Packages.bz2\".\n")
    time.sleep(1)
#This allows it to be automatically stage, commit, and push to Github.
#NOTE : "git.bat" MUST BE IN THE ROOT OF THE REPO FOLDER FOR THIS TO WORK.
#Creates the "end" variable to track if a valid answer was recieved to continue or loop.
end = False
while end == False:
    #Asks whether or not you would like to push changes now.
    pushOrNot = str(input("Would you like to push changes now?(Y/N)\n"))
    #Makes the answer uppercase so it will be easier to check.
    pushOrNot = pushOrNot.upper()
    #Checks if answer was "Y", "N", or neither of them.
    if pushOrNot == "Y":
        #If the answer was "Y", then it will run "git.bat",
        #Which will ask for a commit message then automatically stage, commit, and push to Github.
        os.system(os.getcwd() + "\\git.bat")
        #Then it will say that changes were succesfully pushed to Github.
        printLetterByLetter("Changes have successfully been pushed to Github!\n")
        time.sleep(1)
        #Sets "end" to True so it doesn't loop.
        end = True
    elif pushOrNot == "N":
        #If the answer was "N", it will say tht it won't push changes yet.
        printLetterByLetter("Okay. I won't push changes yet.\n")
        time.sleep(1)
        #Sets "end" to True so it doesn't loop.
        end = True
    else:
        #If the answer wasn't "Y" or "N", it will say "what did you say?",
        printLetterByLetter("What did you say?\n")
        #Then it will set "end" to False so that it loops.
        end = False
        
        
    


'''
#This is the base for the stuff that will be written to the "Packages" file
Package: com.danS.Tweak
Name: SpringThing 
Version: 4.0.4
Size: 63kb
Architecture: iphoneos-arm
Description: A dope respring animation. Trust me. U want this.
Maintainer: Danyaal <danyaal45@gmail.com>
Author: Danyaal <danyaal45@gmail.com>
Section: Test
MD5sum:111111111111111111111111
SHA1sum:11111111111111111111111
SHA256sum:111111111111111111111
Filename: debs//SpringThing.deb
'''
