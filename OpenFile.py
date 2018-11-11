import os
import git
'''
#fileName = listbox_1.get(ACTIVE)
os.system("C:\\Users\\hamid\\OneDrive\\Desktop\\DannyBoi21.github.io\\bzip2.exe " + "C:\\Users\\hamid\\OneDrive\\Desktop\\DannyBoi21.github.io\\Packages")

if not os.listdir(os.getcwd() + "\\adddebs"):
    print("Directory is empty")
else:    
    print("Directory is not empty") 
'''
repo = git.Repo(os.getcwd())
repo.git.add()
repo.git.commit()
repo.git.push('origin', master)
