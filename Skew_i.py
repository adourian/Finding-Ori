# This file contains a function that determines the skew_i values for a given sequence

def FindSkew(genome):
    """ Finds the skew_i values of a sequence
        genome: str, contains the sequence we want to analyze"""
    
    # Get the length:
    n=len(genome)
    # Initialize skew
    skew=[0]
    # Iterate through the genome:
    for i in range(n):
        if genome[i] == 'C':
            skew.append(skew[i]-1)
        elif genome[i] == 'G':
            skew.append(skew[i]+1)
        else:
            skew.append(skew[i])
    return skew

if __name__ == "__main__":
    input='GATACACTTCCCGAGTAGGTACTG'
    skew=FindSkew(input)
    
    # Just getting string output format for submission
    output=''
    for i in range(len(skew)):
        output+=str(skew[i])+' '
    print(output)