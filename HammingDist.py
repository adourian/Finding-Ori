# This file contains a function that calculates the Hamming distance between two strings.

def HammingDistance(str1, str2):
    """ Calculates the number of mismatches (excluding deletions) 
        between two strings"""
    # Check if strings of the same length
    if len(str1)!=len(str2):
        print('Hamming Distance function not appropriate for strings of different lengths: it does not process deletions')
        return False
    # Get length of strings:
    n=len(str1)
    # Initalize distance as 0
    dist=0
    # Iterate through strings
    for i in range(n):
        if str1[i]!=str2[i]:
            dist+=1
    return dist

if __name__ == '__main__':
    # Read file
    with open("datasets/dataset_30278_3.txt", 'r') as f:
        lines=f.readlines()
    # Get strings
    str1=lines[0]
    str2=lines[1]
    str1='CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
    str2='CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'
    # Get Hamming distance
    Hdist=HammingDistance(str1, str2)
    print(Hdist)
