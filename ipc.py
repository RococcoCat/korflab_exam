from aa_comp import aa_comp

def ipc(comp):
	least = float('inf')
	least_a = ''
	most = 0
	most_a = ''
	for key, value in comp.items():
		if value < least:	
			least = value
			least_a = key
		if value > most:
			most = value
			most_a = key
	output = {'least': least_a, 'most':most_a}
	return output

seq = str(input("Pleast input sequence: "))
seq = seq.strip("'")
comp = aa_comp(seq)
x = ipc(comp)
print(x)