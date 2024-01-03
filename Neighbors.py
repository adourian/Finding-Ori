# This file contains a function that generates the d-neighborhood of a string. 

from HammingDist import HammingDistance

def dNeighborhood(pattern, d):
    k=len(pattern)
    nucleotides=['A', 'T', 'C', 'G']
    if d == 0:
        return pattern
    elif k==1:
        return ['A', 'C', 'T', 'G']
    # Initialize empty set
    neighborhood=set()
    # generate suffixes
    suffixPattern=pattern[1:]
    suffixNeighbors=dNeighborhood(suffixPattern, d)
    for string in suffixNeighbors:
        if HammingDistance(string, suffixPattern) < int(d):
            for nucleotide in nucleotides:
                neighborhood.add(str(nucleotide)+str(string))
        else:
            neighborhood.add(str(pattern[0])+str(string))
    return neighborhood

if __name__ =='__main__':
    with open('datasets/dataset_30282_4.txt', 'r') as f:
        lines=f.readlines()
    text=lines[0].strip()
    d=lines[1].strip()
    text='TGCAT'
    d=2
    d_neighbors=dNeighborhood(text, d)
    print(len(d_neighbors))
    # just getting correct submission format
    print(' '.join(d_neighbors))