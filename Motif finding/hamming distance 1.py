dna_str_1 = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
dna_str_2 = "TGAGCGATTAAGCGTGACAGCCCCAGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

def h_d_loop (str_1, str_2):
	h_distance = 0
	for position in range(len(str_1)):
		if str_1[position] != str_2[position]:
			h_distance += 1
	return h_distance

print ("loop haming distance: " )
print (h_d_loop(dna_str_1 , dna_str_2))



