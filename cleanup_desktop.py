from distutils.core import setup
import py2exe
import os
import shutil

#Defining the path where magic happens
desktop_path = os.path.expanduser("~\Desktop")

#Define the path from where to where the files should be moved
folder_path = os.path.join(desktop_path,"organizer")

#Create the folder undefined if it doenst already exists
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

#looping through every element in desktop_path
for filename in os.listdir(desktop_path):
    #only taking elements wit the specific endings
    if filename.endswith((".pdf",".txt", ".docx", ".png", ".jpg", ".docx", ".odt", ".ods")):
        print(f"Moving file: {filename}")
        file_path = os.path.join(desktop_path, filename)
        destination_path = os.path.join(folder_path, filename)
        shutil.move(file_path, destination_path)


setup(console=['desktop_organizer.py'])





