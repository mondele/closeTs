#!/usr/bin/env python3
#closeTs.py
#version 0.1

# by John Wood -- for Tech Advance
# This script walks a tS or BTTW project directory and
# writes chunk information into the manifest for all
# files present. It is a "quick and dirty" way to update
# a project. IT DOES NOT VERIFY THE CONTENTS OF THE CHUNKS.
# If a file is present for a chunk, the script will mark it
# closed in the manifest.

# Usage: closeTs <path to folder>

# Import necessary python components

import os	# file system commands
import re	# regular expressions
import sys	# command line arguments
import shutil	# high level file operations
import json # json structures

# Define classes used

arguments=sys.argv[1:]
count_args=len(arguments)
print("closeTs: For quickly closing a BTT Writer or translationStudio project's chunks.\n")
if count_args!=1: #If there is not exactly one argument, fail with a usage remark.
    if count_args == 0:
        print ("closeTs.py script to close tStudio project chunks")
        print("Usage: python3 closeTs.py <path to project folder>")
    elif count_args > 1:
        print ("closeTs.py currently only handles one project at a time")
    sys.exit(1)

targetFolder=sys.argv[1]
if not os.path.isdir(targetFolder):
    print("I don't think that's a folder.\n")
    sys.exit(1)
else:
    if "manifest.json" not in os.listdir(targetFolder):
        print("That folder doesn't look like a translation project.")
        print("There isn't a manifest.json file.\n")
        sys.exit(1)
#if not re.search(r'.u?sfm',targetFolder, flags=re.IGNORECASE):
#    print("Not a USFM file as far as I can tell.")
#    sys.exit(1)
#target_file=re.sub(r'.u?sfm','.html',convert_file,flags=re.IGNORECASE)
#print("Converting "+convert_file+" to "+target_file+"\n")

output=""

os.chdir(targetFolder)
dirList = os.listdir()
#print(os.getcwd())
#print(dirList)

with open(targetFolder+"manifest.json", 'r', encoding='utf-8') as theManifest:
    theJSON=json.load(theManifest)

#print("\n"+json.dumps(theJSON, indent=4)+"\n")
#print(theJSON['finished_chunks'])

myChunks = []

for listing in dirList:
    if(listing!=".git"):
        if(os.path.isdir(listing)):
            #print("It looks like "+listing+" is a directory")
            newDir= targetFolder + listing
            #print("\nGoing to change to "+newDir+"\n")
            # Doing this procedurally
            os.chdir(newDir)
            for filename in os.listdir():
                myChunks.append(listing+"-"+re.sub(r'.txt','',filename))
                #output=output+"\n\t\t\""+listing+"-"+re.sub(r'.txt','',filename+"\"")
            os.chdir("..")
        #else:
            #print(listing + " is probably a file")

#print(output)
theJSON['finished_chunks'].extend(x for x in myChunks if x not in theJSON['finished_chunks'])

#print(u"\n"+json.dumps(theJSON, indent=4)+"\n")

with open(targetFolder+"newManifest.json", 'w', encoding='utf-8') as newManifest:
    temp = json.dump(theJSON,newManifest, ensure_ascii=False, indent="\t")