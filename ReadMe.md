This is my program to automatically upload tweaks and stuff to a github cydia repo!

I'm pretty sure that it can run without python as a dependency but idk.

It requires a specific layout of folders & files.

GITHUB PAGES REPO

-adddebs
	-Add .deb files to upload here

-debs
	-Added .deb files go here

-js,images,assets,css, ect. all other webpage attributes

-unpack bzip2 here if u dont already have it(not in a folder, all bzip2 
files go directly into the root og the github pages repo folder)

-CyUploader.exe

-index.html

-Packages(no file extention)

-Release(no file extention)

-And obviously CyUploader.exe and git.bat

I assume you have already setup a repo if you are going to use this, so the only new thing should be the "adddebs" folder where .deb files to be added will go.

Now just run CyUploader :)

I will complete the comments sometime later :P

NOTES:

You don't need to type the quotation marks yourself when it asks for a commit message. 

I took care of that for you all :)

The test files need to be in the root for them to work.