#
# starter file for hw1pr3, cs35 spring 2017...
# 

import csv
from collections import *

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")


def CSV_to_dictionary(csv_filename):
    """ returns a dictionary (defaultdict) of
        unweighted first-letter counts from 
        the file wds.csv
    """
    LoR = readcsv( csv_filename )  # List of rows
    #print("LoR is", LoR)
    counts = {}
    for Row in LoR:
        word = Row[0]     # the o.g word
        num  = Row[1]   # the changed word
        counts[word] = num   # add one to that letter's counts
    # done with for loop
    return counts

#
# annotate_text_starter
#
#   Shows off how to style portions of an input text
#   This does not actually use the annotations dictionary (but you will...)
#
def annotate_text_starter( text, annotations ):
    """ this is a letter-by-letter (instead of word-by-word)
        text-annotater. It makes the 'z' characters in the input text bright red.
        It also changes the '\n' characters to "<br>"

        It does not use the annotations dictionary (but you'll want to!)
        It is not general (but you'll build a general template engine!)

        try with 
          + text = "Bees that buzz -\nand kids that blow dandelion fuzz..."
    """
    new_html_string = ''
    for c in text:    # letter-by-letter!
        if c == 'z':
            # we use Python's cool "text-formatting" ability...
            new_c = '<span style="color:{0};">{1}</span>'.format("red", c)
        elif c == '\n':  # handle new lines...
            new_c = "<br>"
        else:
            new_c = c

        # add the new character, new_c
        new_html_string += new_c 

    # finished!
    return new_html_string


def annotate_text(text, dictionary):
    """
    takes in a string and dictionary
    and outputs it in html form with the modernized form,
    looking at the dictionary
    """
    
    words = ''
    new_html_string = ''
    
    for i in range(len(text)):
        if text[i] not in ' !?.:;,-_()[]{}|' and i != len(text)-1:     
            words += text[i]
        
        else:
            if i == len(text)-1 and text[i] not in '!?.:;,-_()[]{}|':
                words+= text[i]

            if words in dictionary.keys():
                temp = dictionary[words]
                if text[i] in "!?.:;,'-_()[]{}|":
                    new_html_string += '<span style="color:rgb(0, 0, 150);" title=' + words + '>' + temp + '</span>' + text[i] + ' '
                else:
                    new_html_string += '<span style="color:rgb(0, 0, 150);" title=' + words + '>' + temp + '</span>' + ' '
                words = ''
            
            else:
                if text[i] in "!?.:;,'-_()[]{}|":
                    new_html_string += words + text[i] + ' '
                else:
                    new_html_string += words + ' '
                words= ''

    return new_html_string[:-1]





# Larger example for testing...


#
# Here are the text and dictionary of substitutions used in hamlet_substitution.html
#
# Note that we don't give away the template engine here (there'd be nothing left!) 
#
# Inspired by
# http://nfs.sparknotes.com/hamlet/page_50.html
#

HAMLET_A1S4 = """
'The king doth wake tonight and takes his rouse,
Keeps wassail and the swaggering upspring reels,
And, as he drains his draughts of Rhenish down,
The kettle-drum and trumpet thus bray out
The triumph of his pledge.'
"""

#
# this would be read in from a csv file and constructed
#
# Again, we don't give that function (it's the hw!)
HAMLET_SUBS = { "doth":"does", "rouse":"partying", 
                "wassail":"drinks",
                "reels":"dances", "Rhenish":"wine", 
                "bray":"blare", "pledge":"participation"}



#
# You can see the output in  hamlet_substitution.html
#