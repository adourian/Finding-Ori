# This file is an update on the MostFrequentWords file to handle mismatches.
# It counts the number of times a kmer is present in a text with up to d mismatches.

from HammingDist import HammingDistance
from ApproximateMatching import ApproximateMatching

def ApproximatePatternCount(text, kmer, d):
    """text: str, genome to be analyzed
       kmer; str, kmer
       d: int, max number of mismatches to still be considered a match"""
    count=len(ApproximateMatching(kmer=kmer, text=text, d=d))
    return count

if __name__ == '__main__':
    # Read file:
    with open('datasets/dataset_30278_6.txt', 'r') as f:
        lines=f.readlines()
    # Get parameters
    text=lines[1].strip()
    kmer=lines[0].strip()
    d=lines[2].strip()
    text='CATGCCATTCGCATTGTCCCAGTGA'
    kmer='CCC'
    d=2
    # Get matches
    d_matches=ApproximatePatternCount(text, kmer, d)
    
    print(d_matches)
