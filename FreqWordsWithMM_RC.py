# This is like Frequent words with MM, but also looking into the RC. 
# Approach: we simply compute the RC, count it in both and take the sum. 

from Neighbors import dNeighborhood
from MaxMap import MaxMap
from ReverseComplement import ReverseComplement

def FreqWordsWithMMRC(text, k, d):
    rev_text=ReverseComplement(text)

    n=len(text)
    patterns=[]
    freqMap={}
    
    for i in range(n-k+1): # Iterate over whole text
        # Get the current kmer
        pattern = text[i:i+k]
        patternRC = rev_text[i:i+k]
        # Create d-neighborhood
        neighborhood=dNeighborhood(pattern=pattern, d=d)
        neighborhood=list(neighborhood)
        neighborhoodRC=dNeighborhood(pattern=patternRC, d=d)
        neighborhoodRC=list(neighborhoodRC)
        # Iterate over kmers in d-neighborhood
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor]=1
            else:
                freqMap[neighbor]+=1
        for j in range(len(neighborhoodRC)):
            neighbor = neighborhoodRC[j]
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
    with open('dataset_30278_10.txt', 'r') as f:
        lines=f.readlines()
    
    text=lines[0].strip()
    line2=lines[1].strip()
    k, d = line2.split(' ')

    print(FreqWordsWithMMRC(text, int(k), int(d)))
