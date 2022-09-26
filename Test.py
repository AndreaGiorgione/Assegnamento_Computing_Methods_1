"""First assignment for the CMEPDA course, 2022/23.
"""

'''
import argparse


def process(file_path):
    """
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    print(text)
    print('Done.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    process(args.infile)
'''


from dataclasses import dataclass
import string
import numpy #For array of letters count
import time #For elapsed time
from matplotlib import pyplot

input_file = 'The quick brown fox jumps over the lazy dog. This is a sentence\n with every word. '

#Create a alpha-numeric dictionary for letters search
N = 26 #Numbers of letters

alphabet = string.ascii_lowercase
Alphabet = string.ascii_uppercase
numbers = range(N)

dict1 = dict(zip(alphabet, numbers))
dict2 = dict(zip(Alphabet, numbers))

DICT = dict1 | dict2

#Get rid of useless part in the text
i = input_file.find('This is') #Useful with 'CHAPTER 1' or 'PART 1'
j = input_file.find('with every') #Useful with 'THE END' or 'The End'
input_file = input_file[i:]
print(input_file)

#Letters detection, histogram bins construction and features counting
bins = numpy.zeros(len(alphabet))

n = 0 #Index for values in the dictionary
l = 0 #Counter of letters met
c = 0 #Counter of total characters
w = 0 #Number of word
 
p = 0 #Control parameter
    
for x in input_file:
    c = c + 1
    if x in DICT:
        l = l + 1
        n = DICT.get(x)
        bins[n] = bins[n] + 1 #Whitout square braket?
    if x == ' ':
        if p == 0:
            w = w + 1
            p = 1
    elif x != ' ':
        p = 0

lines = 1 #Lines counter

for line in input_file:
    if line == "\n":
        lines = lines + 1

bins = bins / l * 100

print(f'Number of letters: {l}')
print(f'Number of characters: {c}')
print(f'Number of words: {w}')
print(f'Number of lines: {lines}')
print(f'Percentage content of the bins: \n {bins}')
    
#Help message request (just an idea)
args = '--Help' #Input?
if args == '--Help':
    print('Programme do this and that') #Something else?

#Programme duration
start = time.time()
end = time.time()
print(f'Total elapsed time: {end - start}')


#Histogram (to be fixed)
fig, ax = pyplot.subplots(1, 1)
ax.hist(range(N), len(alphabet), weights = bins)

ax.set_title("Histogram of letters appearances")
ax.set_xlabel('Letters')
ax.set_ylabel('Percentage')

rects = ax.patches
labels = Alphabet

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')

pyplot.show()


