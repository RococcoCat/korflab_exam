import numpy as np
import pandas as pd
import argparse

# find overlaps in gff file

# accept input from user
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="enter .fasta file", type=str)
args = parser.parse_args()


def overlap(filename):
    # read file into pandas dataframe
    gff = pd.read_csv(
        filename, 
        sep="\t", 
        header=None,
        comment="#", 
        names=("seqname", "source", "feature", "start",
               "end", "score", "strand", "frame", "attribute"),
    )

    # extract start and end positions
    start = gff['start']
    end = gff['end']

    overlaps = []
    # check if there are overlaps
    for start_pos, end_pos in zip(start, end):
        past_start = np.array(start_pos > gff['start'], dtype=bool)
        before_end = np.array(end_pos < gff['end'], dtype=bool)
        overlap = gff[past_start & before_end]
        overlap = tuple(overlap['feature'])
        if len(overlap) > 0 and overlap not in overlaps:
            # create tuple of the features that are overlapping and append to overlaps
            overlaps.append(overlap)
    
    return overlaps
    
def main():
    print(overlap(args.filename))
    

if __name__ == '__main__':
    main()
            