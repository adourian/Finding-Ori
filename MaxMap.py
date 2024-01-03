# This file contains a function that takes a dictionary of kmers with their frequency count,
# and returns the most frequent kmers

def MaxMap(result):
    max_frequency = max(result.values())
    most_frequent_kmers = [kmer for kmer, freq in result.items() if freq == max_frequency]
    return most_frequent_kmers

