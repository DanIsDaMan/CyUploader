from shutil import copyfile
import time
import sys
import os

#NOTE : Put .deb files to be added in a folder called "adddebs",
#and make another folder called "debs". This one will be the desination.

def printLetterByLetter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


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
    package = str("Package: com.dan." + tweakName)
    version = str(input("Version Number for " + "\"" + str(tweakName) + "\":\n"))
    version = str("Version: " + version)
    #size = str((float(((os.path.getsize(os.getcwd() + "\\adddebs\\" + str(fileName)))/1000))) + "kb")
    size = float(os.path.getsize(os.getcwd() + "\\adddebs\\" + str(file)))
    size = float(size/1000)
    size = str("Size: " + str(size) + "kb")
    architecture = str("Architecture: iphoneos-arm")
    description = str(input("Description for " + "\"" + str(tweakName) + "\":\n"))
    description = str("Description: " + description)
    maintainerName = str(input("Name of Maintainer:\n"))
    maintainerEmail = str(input("Maintainer's Email Address:\n"))
    maintainer = str("Maintainer: " + maintainerName + " <" + maintainerEmail + ">")
    authorName = str(input("Name of Author:\n"))
    authorEmail = str(input("Author's Email Address:\n"))
    author = str("Author: " + authorName + " <" + authorEmail + ">")
    section = str(input("Section:\n"))
    section = str("Section: " + section)
    MD5sum = str(input("MD5sum:\n"))
    MD5sum = str("MD5sum: " + MD5sum)
    SHA1sum = str(input("SHA1sum:\n"))
    SHA1sum = str("SHA1sum: " + SHA1sum)
    SHA256sum = str(input("SHA256sum:\n"))
    SHA256sum = str("SHA256sum: " + SHA256sum)
    fileName = str("debs//" + file)
    fileName = str("Filename: " + file)
    filler = str(" ")
    #Rename "Packages" to "Packages.txt" so that Python can edit it.
    #os.rename((os.getcwd() + "\\Packages"), (os.getcwd() + "\\Packages.txt"))
    with open("Packages", "a") as Packages:
        Packages.write(filler + "\n")
        Packages.write(package + "\n")
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
        Packages.write(fileName + "\n")
        Packages.close()
    filePathOld = str(os.getcwd() + "\\adddebs\\" + file)
    filePathNew = str(os.getcwd() + "\\debs\\" + file)
    copyfile(filePathOld, filePathNew)
    os.remove(filePathOld)
    success = str("Successfully added " + file + " to your cydia repo!\n")
    printLetterByLetter(success)
if not "Packages.bz2" in os.listdir(os.getcwd()):
    if not os.listdir(os.getcwd() + "\\adddebs"):
        os.system(os.getcwd() + "\\bzip2.exe " + os.getcwd() + "\\Packages")
        if "Packages.bz2" in os.listdir(os.getcwd()):
            printLetterByLetter("Successfully compressed \"Packages\" to \"Packages.bz2\".")
        else:
            printLetterByLetter("Failed to compress \"Packages\" to \"Packages.bz2\".")
else:
    printLetterByLetter("Failed to compress \"Packages\" to \"Packages.bz2\".")

    

    



'''
#This is the base for the stuff that will be written to the "Packages" file
Package: com.dan.SpringThing
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
