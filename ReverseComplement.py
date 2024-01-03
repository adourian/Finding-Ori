# This file contains a function that takes a DNA string and returns its reverse complement.

def ReverseComplement(text):
    # Get length of text
    n=len(text)
    # Initialize empty string for the reverse complement
    reverse=''
    for i in range(n):
        if text[i]=='A':
            reverse='T'+reverse
        elif text[i]=='T':
            reverse='A'+reverse
        elif text[i]=='G':
            reverse='C'+reverse
        elif text[i]=='C':
            reverse='G'+reverse
    return reverse

if __name__ == "__main__":
    # Read the content of the file
    with open('dataset_30273_2.txt', 'r') as file:
        lines = file.readlines()
    
    # Extract text and pattern from the lines
    text = lines[0]
    text='CCAGATC'
    
    print(ReverseComplement(text=text))

