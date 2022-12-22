# compute amino acid composition

def aa_comp(seq):
	# get count of all amino acids
	count = {}
	for i in seq:
		if i not in count:
			count[i] = 1
		else:
			count[i] += 1
	total = sum(count.values())
	per = {}
	for key in sorted(count.keys()):
		per[key] = count[key]/total
	return per

if __name__ == '__main__':
	seq = str(input("Please enter a sequence: "))
	seq = str(seq.strip("'"))
	x = aa_comp(seq)
	print(x)