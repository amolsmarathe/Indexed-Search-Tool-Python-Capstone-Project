# Indexed Search Tool - Python capstone project (based on inverted index)
This is a capstone project in python to develop entire full text index search tool to be capable of indexing several files based on inverted index and enable a quick textual search capability in all files' contents. <br />
![SearchImage](https://drive.google.com/uc?id=10sWLl8uxAM77RT7YRdLZaiVOs4QxOFOW)
---

## Existing search capabilities:
  - Create indexes (in-memory) for all the docx files present in directories and sub-directories
  - Search for a word or a phrase in a file
  - Search in multiple files
  - Display search results- files that contain the word and frequency of occurrence in each file
  - Search results are sorted with most frequent occurrence on the top
  - Search case-insensitive
  - Search irrespective of the punctuations
  - Read files on physical disk and index them --> then search
  - Provide a path and search within all directories and sub-directories for existing docx files
  - Provide a warning for the files which are currently in Open state may not have latest search results.
  - Real-time display of a list of currently opened files to quickly understand which files are being modified.

## Planned future enhancements:
  - Develop UI to: give path of text files, enter phrase to search for, search results, open file from results
  - Store the files as well as indexes in DB
  - Check if the file is modified or new and only then index it
  - Save indexes in files or in database and run periodic update of indexes

## Example:
**Search results for a phrase "list, github":** <br />
&nbsp;&nbsp;&nbsp;&nbsp;![Example1](https://drive.google.com/uc?id=1x-cCWhyd0-igaUZz2ZTdlMy0MXHI2zmc)
