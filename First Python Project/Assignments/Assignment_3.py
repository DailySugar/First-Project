"""
Created on Oct 13, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121

This program uses the Jaccard Similarity measure to determine
which document has the greatest similarity to a specified document.

All of this work is mine, and any methods or ideas borrowed are
referenced above such code.
"""

# import sys
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import tkinter as tk
from pathlib import Path
import ntpath
import glob
import re

# Method found from question #35851281 on stack overflow
path = str(Path.home() / "Downloads")

# Experimental, place python file in the same folder as all the other files
# Name your stop words file "StopWords.txt" and drag-drop the file you
# want to compare onto the python file.
# folder_directory = sys.path[0]
# stop_words = sys.path[0] + "\\" + "StopWords.txt"

# Comment this out if you want to manually type in directories
folder_directory = askdirectory(title="Select the folder of files that you want to compare to:", initialdir=path)
stop_words = filedialog.askopenfilename(title="Select your stop words file:", initialdir=path)

# Uncomment this to manually type in directories
# file_directory = str(Path.home() / "Downloads/test/Documents_2/Journey_Centre_Earth.txt")
# folder_directory = str(Path.home() / "Downloads/test/Documents_2")
# stop_words = str(Path.home() / "Downloads/test/StopWords.txt")

txt_files = glob.glob(folder_directory + "/" + "*.txt")

print("Processing, please wait: ")


def letters_only(string):
    """
    Parameter: String
    Returns: String
    Description: Converts to lower case and removes non-letter components.
    """
    # Replace weird apostrophes with proper ones.
    string = string.replace("’", "'").lower()
    # Thanks to Q#1276764 on stack overflow for info on re.sub.
    # Removes all apostrophes not encased by letters.
    string = re.sub('[^a-z]\'|\'[^a-z]|$\'|\'$', ' ', string, flags=re.UNICODE)
    # Remove all non-letter characters except apostrophes, but keep spaces in between.
    string = re.sub('[^a-z\']', ' ', string, flags=re.UNICODE)
    return string


stop_words = letters_only(open(stop_words, "r", encoding="utf-8").read()).split()


def get_words(file):
    """
    Parameter: String
    Returns: List of strings (Each string is a word in the file)
    Description: Gets and processes all the words in the file.
    """
    words = letters_only(open(file, "r", encoding="utf-8").read())
    # DEPRECATED: Turns out that removing the stop words at the very beginning
    # significantly bottle-necks the program compared to just ignoring them until
    # later. Keeping this for future reference.
    # # Remove stop words
    # for x in stop:
    #     # Thanks to w3schools.com/python/python_regex.asp for a list of Regular Expressions
    #     words = re.sub(r"\b" + x + r"\b", '', words)
    return words.split()


def word_count(words):
    """
    Parameters:
        words: List of strings
    Returns: Dictionary
    Description: Returns the # of appearances of each word
        in words, excluding words which are either in stop_words,
        or words which appear less than 5 times.
    """
    count_dict = {}
    for x in words:
        # Incrementing by 1 per word found
        try:
            count_dict[x] += 1
        except:
            count_dict[x] = 1
    # Removing counts below 5 and stop words
    for x in list(count_dict.keys()):
        if count_dict[x] < 5 or x in stop_words:
            count_dict.pop(x)
    return count_dict


def j_s(count_dict1, count_dict2):
    """
    Parameters:
        count_dict1: Dictionary
        count_dict2: Dictionary
    Returns: Float
    Description: Takes two word counts and runs the
        Jaccard Similarity Measure on them.
    """
    if len(count_dict2) == 0 or len(count_dict1) == 0:
        return 0
    intersection = 0
    for x in count_dict1:
        try:
            if count_dict2[x] > 0:
                intersection += 1
        except:
            continue
    union = len(count_dict1) + len(count_dict2) - intersection
    return intersection / union


def jaccard_similarity(files):
    """
    Parameters:
        files: List of strings
    Returns: List of lists
    Description: Main function. calls all other functions to handle the files inputted,
        and returns a list of each book, with its most similar book, and the similarity
        number.
    """
    recommendations = []
    word_counts = {}
    # Get word counts of all files.
    for file in files:
        word_counts[ntpath.basename(file)] = word_count(get_words(file))
    # Loop through all books to get their recommendations.
    for compare_file in word_counts:
        similarities = {}
        # Similarities of all files relative to compare_file.
        for file in word_counts:
            similarities[file] = j_s(word_counts[compare_file], word_counts[file])
        most_similar = ["", 0]
        # Get most similar file.
        for x in similarities:
            if similarities[x] > most_similar[1] and x != compare_file:
                most_similar = [x, similarities[x]]
        # Add compare_file, with its most_similar to recommendations.
        recommendations.insert(len(recommendations), [compare_file, most_similar[0], most_similar[1]])
    return recommendations


output = jaccard_similarity(txt_files)

# Showing results in tkinter
tk.Label(text="Book", pady=20).grid(row=0, column=0)
tk.Label(text="Recommendation").grid(row=0, column=1)
tk.Label(text="Similarity").grid(row=0, column=2)

n = 1
for j in output:
    tk.Label(text=j[0], width=40, height=2).grid(row=n, column=0)
    tk.Label(text=j[1], width=40, height=2).grid(row=n, column=1)
    tk.Label(text=j[2], width=40, height=2).grid(row=n, column=2)
    n += 1

tk.mainloop()
