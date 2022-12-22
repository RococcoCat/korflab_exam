# input: seq and window size
# output: table with position and avg hydropathy
# more positive the value: the more hydrophobic the amino acids

import pandas as pd

def hydropathy(seq, win):
	kd = {'A': 1.8, 'C': 2.5, 'D': -3.5, 'E': -3.5,'F':2.8,
		'G': -0.4, 'H':-3.2,'I': 4.5, 'K': -3.9,'L': 3.8,
 		'M': 1.9, 'N': -3.5, 'P': -1.6, 'Q': -3.5,'R': -4.5,
 		'S': -0.8, 'T': -0.7, 'V': 4.2, 'W':-0.9, 'Y': -1.3}
	
	avg = []
	temp = 0
	for i in range(len(seq)-win):	
		window = seq[i:i+win]
		for j in window:
			temp += kd[j]
		avg.append(temp)
		temp = 0
	d = {'position':list(seq)[0:(len(seq)-win)], 'average hydropathy': avg}
	df = pd.DataFrame(data=d)
	return df
	

seq, win = input("Please enter sequence (capitalized) and window size as an int: ").split()
seq = str(seq)
seq.strip("'")
win = int(win)
h = hydropathy(seq, win)
print(h)



#Jack Kyte, Russell F. Doolittle, A simple method for displaying the hydropathic character of a protein, Journal of Molecular Biology, Volume 157, Issue 1, 1982,