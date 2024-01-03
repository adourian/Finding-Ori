# This takes a text, an int k (length of kmer), and an int d (max number of mismatches allowed)
# It returns the list of the most frequent kmers with up to d mismatches. 

from ApproximatePatternCount import ApproximatePatternCount
from HammingDist import HammingDistance
from Neighbors import dNeighborhood
from MaxMap import MaxMap

def FreqWordsWithMM(text, k, d):
    """ Finds the most frequent words of length k with up to d mismatches
        text: str, text/genome to be analyzed
        k: int, length of kmers
        d: int, max number of mismatches for it to be considered a match
        Remember that strings that don't appear could be the most frequent if d mismatches are allowed"""
    # First idea: brute force, check all combinations of length k of nucleotides. This is inefficient, as it will check 
    #             combinations that aren't there even with d mismatches. 
    # Better version: We screen through the text. For each that appears, we also add to the count of their d-neighbors (that are different by max d).
    #                 This will ensure that the kmers that don't appear (with d changes) aren't computed. We use a dict structure again to be more efficient and keep track of counts. 
    #                 We will create a function in another file to compute the d-neighborhood of a string.
    
    n=len(text)
    patterns=[]
    freqMap={}
    
    for i in range(n-k+1): # Iterate over whole text
        # Get the current kmer
        pattern = text[i:i+k]
        # Create d-neighborhood
        neighborhood=dNeighborhood(pattern=pattern, d=d)
        neighborhood=list(neighborhood)
        # Iterate over kmers in d-neighborhood
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor]=1
            else:
                freqMap[neighbor]+=1
    # Get the most frequent kmers (with up to 2 mismatches)
    max_freq=MaxMap(freqMap)
    for key in max_freq:
        patterns.append(key)
    return patterns
    
if __name__ == '__main__':
    with open('dataset_30278_9.txt', 'r') as f:
        lines=f.readlines()
    
    text=lines[0].strip()
    line2=lines[1]
    k, d = line2.split(' ')

    print(FreqWordsWithMM(text, int(k), int(d)))
    
         