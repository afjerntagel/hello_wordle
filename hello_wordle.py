import re
import gc
import sys
import os.path
from os.path import exists          
import argparse
from datetime import datetime
import itertools

def canonicalise_word(word):
    return ''.join(sorted(word))
    
def areNotDisjoint(anagramList):
    s = "".join(anagramList)
    if (len(s)) != len(set(s)):
        return True
    else:
        return False


def get_anagram_dict(file_name, number_of_characters, allowedCharacters=None):
    anagram_dict=dict()

    if (allowedCharacters == None):
        allowedCharacters = re.compile("^[abcdefghijklmnopqrstuvwxyzåäö]+$")
    else:
        allowedCharacters = re.compile(f"^[{allowedCharacters}]+$")

    dont_allow_repetitions        = re.compile(r'^(?!.*(.)(\1)).*$')

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            for l in f.readlines():
                l=l.strip().lower()
                if (len(l) == number_of_characters) and ( allowedCharacters.match(l) ):
                    canonicalised_word = canonicalise_word(l)

                    if(dont_allow_repetitions.match(canonicalised_word)):
                        if( canonicalised_word in anagram_dict):
                            anagram_dict[canonicalised_word].append(l)
                        else:
                            anagram_dict[ canonicalised_word] = [l]
    except FileNotFoundError:
        raise FileNotFoundError("File '{file_name}' not found.")
        
    return anagram_dict

def main():
    # Create an ArgumentParser instance.
    parser = argparse.ArgumentParser(description='A small python script that generates tuples of start words for wordle.\
    \
    Startwords may include anagrams. Words of specified length are selected from dictionary file. Only words with disjoint letters are selected.')

    # Add an argument for the file name
    parser.add_argument('-d', '--dictionary', help='File name of input dictionary. Default is a swedish dictionary: dictionaries/ss100-UTF-8.txt', default='dictionaries/ss100-UTF-8.txt')

    # Add an argument for the number of characters
    parser.add_argument('-w', '--wordLength', type=int, help='Words with this number of characters will be selected from dictionary. Default is 5.', default=5)

    # Add number of desired word groups
    parser.add_argument('-n', '--numberOfWordGroups', type=int, help='Number of word groups. Default is 2. 4 or above requieres patience or a strong computer.', default=2)
   
    # Add charset
    parser.add_argument('-ac', '--allowedCharacters', help='If specified, only words consisting of the specified characters are allowed. Default is \'abcdefghijklmnopqrstuvxyzåäö\'', default=".")

    # Add name of output directory
    parser.add_argument('-od', '--outputDirectory', help='If specified, output files will be created in this directory. Default is \'.\'', default=".")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Test if result file can be created
    if (not os.access(args.outputDirectory, os.W_OK)):
        raise(BaseException, "Output directory not writeable:", args.outputDirectory)

    anagram_dict= get_anagram_dict(args.dictionary, args.wordLength, args.allowedCharacters)

    print ("Number of words in anagram_dict: ", len(anagram_dict))

    anagramKeyList = list (anagram_dict.keys())

    anagramKeyTuples = itertools.filterfalse(areNotDisjoint, itertools.combinations(anagramKeyList , args.numberOfWordGroups))
 
    formatted_datetime = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    basename = os.path.basename(args.dictionary)

    fileName = f"{args.outputDirectory}/{formatted_datetime}-{basename}"

    try:
        with open(fileName, 'w', encoding='utf-8') as outputFile:

            for anagramKeyTuple in anagramKeyTuples:
                results =[] 
                for anagram in anagramKeyTuple:
                    results.append(anagram_dict[anagram])
                outputFile.write(str (results) + '\n')
                outputFile.flush() 

    except BaseException as e:
        raise(e)

if __name__ == '__main__':
    main()
