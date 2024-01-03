# This file contains a function that takes a kmer, a text, and an int d, and returns the 
# positions in the text where there are matches (with hamming distance<=d)

from HammingDist import HammingDistance

def ApproximateMatching(kmer, text, d):
    """ Takes kmer (str), text (str), d (int) 
        Returns indexes of where kmer matches text with
        up to d mismatches"""
    d_matches=[] # initialize empty list of indexes for matches
    k=len(kmer)
    for i in range(len(text)-k+1):
        Hdist=HammingDistance(kmer, text[i:i+k])
        if Hdist <= int(d):
            d_matches.append(i)
    return d_matches

if __name__ == '__main__':
    # Read file
    with open("dataset_30278_4.txt", 'r') as f:
        lines=f.readlines()
    # Get parameters
    kmer=lines[0].strip()
    text=lines[1].strip()
    d=lines[2].strip()
    
    # Get matches
    d_matches=ApproximateMatching(kmer, text, d)
    # Convert to space-separated string for submission
    output=''
    for i in range(len(d_matches)):
        output+=str(d_matches[i])+' '
    print(output)