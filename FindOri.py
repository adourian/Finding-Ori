# This finds the Ori position

from Skew_i import FindSkew

def FindOri(genome):
    skew=FindSkew(genome)
    min_skew=min(skew)
    min_indices = [index for index, value in enumerate(skew) if value == min_skew]
    return min_indices

if __name__ == "__main__":
    with open("dataset_30277_10.txt", 'r') as f:
        lines=f.read()

    ori_loc=FindOri(lines)
    print(ori_loc)