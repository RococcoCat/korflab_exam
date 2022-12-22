import argparse
import numpy as np
from collections import Counter
import math
import os

# Shannon entropy = - Sum(P(xi) * log P(xi))

# accept input from user
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="enter .fasta file", type=str)
parser.add_argument("param", help="enter window, threshold, mask format", nargs='*')
args = parser.parse_args()

def entropy_filter(filename, window=3, threshold=0.3, lower=False):
	# if lower = False: mask will be N
	# if lower = True: mask will be lowercase letter
	# masks regions of low entropy

    with open(filename,'r') as f:
        lines = f.readlines()
        sequences = []
        header = []
        read = ""
        
        # read sequences into a numpy array
        for line in lines:
            if not line.startswith('>'):
                read += line.rstrip('\n')
            if line.startswith('>') or line == lines[-1]:
                if(read != ""):
                    sequences.append(np.array(list(read.strip())))
                    read = ""
                if line.startswith('>'):
                    header.append(line.strip())
        sequences = np.array(sequences)
        
    # iterate through columns and calculate entropy
    counts = {}
    entropy = []
    size = np.shape(sequences)[0]
    for col in sequences.T: 
        counts = Counter(col)
        h = 0
        for value in counts.values():
            prob = value / size
            h -= prob * math.log(prob,10)
        entropy.append(h)
    
    # iterate through entropy list, if a position < threshold, mask it
    for pos in range(len(entropy) - window+1):
        window_entropy = sum(entropy[pos:pos+window])
        if window_entropy < threshold:
            for seq in sequences:
                for i in range(pos, pos+window):
                    if lower == True:
                        seq[i] = seq[i].lower()
                    else:
                        seq[i] = 'N'
        
    # write sequences to a fasta file
    newfile = os.path.splitext(filename)[0] + '_filtered.fasta'
    with open(newfile,'w') as w:
        for i in range(len(header)):
            w.write(header[i]+'\n')
            w.write("".join([str(i) for i in sequences[0]])+'\n')


def main():
    window = int(args.param[0])
    threshold = float(args.param[1])
    lower = bool(args.param[2])
    entropy_filter(args.filename, window, threshold, lower)

if __name__ == '__main__':
    main()
    print("Complete")