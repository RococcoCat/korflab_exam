
import fasta_lib

filename = 'test.fasta'
for header, seq in fasta_lib.fasta_generator(filename):
	print(header)
	print(seq)



				
			
				
		