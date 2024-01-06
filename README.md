```
python3 hello_wordle.py --help
usage: hello_wordle.py [-h] [-d DICTIONARY] [-w WORDLENGTH] [-n NUMBEROFWORDGROUPS] [-ac ALLOWEDCHARACTERS] [-od OUTPUTDIRECTORY]

A small python script that generates tuples of start words for wordle.
Words of specified length are selected from dictionary file.
Only words with disjoint letters are selected.
Startwords may include anagrams.

options:
  -h, --help            show this help message and exit
  -d DICTIONARY, --dictionary DICTIONARY
                        File name of input dictionary. Default is a swedish dictionary: dictionaries/ss100-UTF-8.txt
  -w WORDLENGTH, --wordLength WORDLENGTH
                        Words with this number of characters will be selected from dictionary. Default is 5.
  -n NUMBEROFWORDGROUPS, --numberOfWordGroups NUMBEROFWORDGROUPS
                        Number of word groups. Default is 2. 4 or above requieres patience or a strong computer.
  -ac ALLOWEDCHARACTERS, --allowedCharacters ALLOWEDCHARACTERS
                        If specified, only words consisting of the specified characters are allowed. Default is 'abcdefghijklmnopqrstuvxyzåäö'
  -od OUTPUTDIRECTORY, --outputDirectory OUTPUTDIRECTORY
                        If specified, output files will be created in this directory. Default is '.'
```