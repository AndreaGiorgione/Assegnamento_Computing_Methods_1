"""First assignment for the CMEPDA course, 2022/23.
"""

import argparse
from pstats import Stats #For all the stuff done by command line
import string #For the function string.ascii
import numpy #For array of letters count
import time #For elapsed time
from matplotlib import pyplot

#Global variables
t0 = time.time()#The beginning of the time
N = 26 #Numbers of letters

#Function that counts frequencies of letters
def parsefile(text, start, finish, histo, stats, helping):
    '''
    '''
    #Give help if nedded
    if helping == True:
        print("""
        Use --start to indicate the starting line of the file analysis (first line counted)
        Use --end to indicate the ending line of the file analysis (first line not counted)
        Use --histo to plot an histogram
        Use --stats to print some basic stats of the file
        Use --helping to get help
        """)
        return

    #Create a alpha-numeric dictionary for letters search
    alphabet = string.ascii_lowercase
    numbers = range(N)

    dict1 = dict(zip(alphabet, numbers))

    #With DICT  decide whether a word is upper or lower
    DICT = dict1

    #Get rid of useless part in the text with an else if. In case of no necessity of cuts, programme run on the entire file
    #i = text.find('*** START ***'.lower())
    #j = text.find('*** END***'.lower())
    if start != '':
        i = text.find(start.lower()) #Useful with 'CHAPTER 1' or 'PART 1'
    else:
        i = 0
    if finish != '':
        j = text.find(finish.lower()) #Useful with 'THE END' or 'The End'
    else:
        j = len(text)
    text = text[i:j]

    #Letters detection, histogram bins construction and features counting
    bins = numpy.zeros(len(alphabet))

    n = 0 #Index for values in the dictionary
    lett = 0 #Counter of letters met
    char = 0 #Counter of total characters
    words = 0 #Number of word
    p = 0 #Control parameter

    lines = 0 #Lines counter
    for x in text:
        char = char + 1
        if x in DICT:
            lett = lett + 1
            n = DICT.get(x)
            bins[n] = bins[n] + 1 
        if x == ' ' or x =='\n':
            if p == 0:
                words = words + 1
                p = 1
        elif x != ' ':
            p = 0
        if x=='\n':
            lines = lines + 1

    #In the end, count the bins
    bins = bins / lett * 100

    #Print some informations
    if stats:
        print(f'Number of letters: {lett}')
        print(f'Number of characters: {char}')
        print(f'Number of words: {words}')
        print(f'Number of lines: {lines}\n')

    #In case there's no need to print the istogram
    if not histo:
        #Count the time in case of no istogram
        end = time.time()
        print(f'Total elapsed time: {end - t0}')
        return

    #A funny way to print the results of the exercise
    print(f'Percentage content of the bins:')
    for i in range(N):
        car = alphabet[i]
        print(car, "{0:6.2f}".format(bins[i])+"%",  '*'*int(5*bins[i]))

    #Histogram
    fig, ax = pyplot.subplots(1, 1)
    ax.hist(range(N), len(alphabet), weights = bins)

    ax.set_title("Histogram of letters appearances")
    ax.set_xlabel('Letters')
    ax.set_ylabel('Percentage')

    #Set label on top of every bin centered on every bin
    rects = ax.patches
    labels = alphabet
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom')


    #Count the time in case of Istogram
    end = time.time()
    print(f'Total elapsed time: {end - t0}')

    pyplot.show()


def process(file_path, start, finish, histo, stats, helping):
    """
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as text:
        text = text.read().lower()
    parsefile(text, start, finish, histo, stats, helping)
    print('Done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='Path to the input file')
    parser.add_argument('--start', type=str, default='', help='Start of the document')
    parser.add_argument('--end', type=str, default='',  help='End of the document')
    parser.add_argument('--histo', action='store_true', help='Show a letter histogram')
    parser.add_argument('--stats', action='store_true', help='Show general stats of the book')
    parser.add_argument('--helping', action='store_true', help='Give an help to user')
    args = parser.parse_args()
    process(args.infile, args.start, args.end, args.histo, args.stats, args.helping)