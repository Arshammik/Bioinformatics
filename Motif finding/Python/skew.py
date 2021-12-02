def min_skew(dna_seq):"TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

    skew_dic = {0:0}
    
    import numpy as np
    for i, nuc in enumerate(dna_seq):
        
        if nuc == 'C': skew_dic.update({i+1: list(skew_dic.values())[-1] - 1})
        if nuc == 'G': skew_dic.update({i+1: list(skew_dic.values())[-1] + 1})
        if nuc == 'A': skew_dic.update({i+1: list(skew_dic.values())[-1] + 0})
        if nuc == 'T': skew_dic.update({i+1: list(skew_dic.values())[-1] + 0})
        
    # Find item with min value in Dictionary
    min_val = min(skew_dic.items(), key = lambda x: x[1])
    
    # Find all items with the min value
    min_vals = [key for key,value in skew_dic.items() if value == min_val[1]]
    
    return min_vals
