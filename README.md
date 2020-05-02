# Full Text Search Index Tool - Python capstone project (based on inverted index)
This is a capstone project in python to develop entire full text index search tool to be capable of indexing several files based on inverted index and enable a quick textual search capability in all files' contents.

---

## Existing search capabilities:
  - Create indexes (in-memory) for given files
  - Search for a word or a phrase in a file
  - Search in multiple files
  - Display search results- files that contain the word and frequency of occurrence in each file
  - Search results are sorted with most frequent occurrence on the top
  - Search case-insensitive
  - Search irrespective of the punctuations

## Planned future enhancements:
  - Read files on physical disk and index them --> then search
  - Provide a path of files and search within all the files on that path
  - Develop UI to: give path of text files, enter phrase to search for, search results, open file from results
  - Store the files as well as indexes in DB
  - Check if the file is modified or new and only then index it
  - Run periodic update of indexes

## Example:
**Search results for a word "pune":**
![Example1](https://drive.google.com/uc?id=1LbsZEqt8mRDkpddZDlpOzePSLvtPesFO)