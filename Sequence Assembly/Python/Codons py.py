#John Hopkines Genomic Data Science
#Amino Acid Tranlator
#V.0.1.0
#June, 5th, 2022
#1:31 (+3;30 GMT)

'''

DNA = input("Please enter your DNA sequence:\n")


DNA_new = DNA.replace("\n", "")

print("Your DNA sequence:\n", DNA_new)


RNA_map = DNA_new.maketrans("ATGC", "AUGC")

RNA = DNA_new.translate(RNA_map)

print("Your RNA sequence:\n",RNA)


# The codons Dictionary
# AUG is M and a start codon
codons = {
      "AUG":"Methionine","AUA":"Isoleucine","AUC":"Isoleucine","AUU":"Isoleucine",
      "AGA":"Arginine"  ,"AGC":"Serine"    ,"AGG":"Arginine"  ,"AGU":"Serine",
      "ACA":"Threonine","ACC":"Threonine","ACG":"Threonine","ACU":"Threonine",
      "AAA":"Lysine","AAC":"Asparagine","AAG":"Lysine","AAU":"Asparagine",
      "UUA":"Leucine","UUC":"Phenylalanine","UUG":"Leucine","UUU":"Phenylalanine",
      "UGA":"STOP","UGC":"Cysteine","UGG":"Tryptophan","UGU":"Cysteine",
      "UCA":"Serine","UCC":"Serine","UCG":"Serine","UCU":"Serine",
      "UAA":"STOP","UAC":"Tyrosine","UAG":"STOP","UAU":"Tyrosine",
      "GUA":"Valine","GUC":"Valine","GUG":"Valine","GUU":"Valine",
      "GGA":"Glycine","GGC":"Glycine","GGG":"Glycine","GGU":"Glycine",
      "GCA":"Alanine","GCC":"Alanine","GCG":"Alanine","GCU":"Alanine",
      "GAA":"Glutamic acid","GAC":"Aspartic acid","GAG":"Glutamic acid","GAU":"Aspartic acid",
      "CUA":"Leucine","CUC":"Leucine","CUG":"Leucine","CUU":"Leucine",
      "CGA":"Arginine","CGC":"Arginine","CGG":"Arginine","CGU":"Arginine",
      "CCA":"Proline","CCC":"Proline","CCG":"Proline","CCU":"Proline",
      "CAA":"Glutamine","CAC":"Histidine","CAG":"Glutamine","CAU":"Histidine",



}

volume_of = {
    "A":  67.0, "C":  86.0, "D":  91.0,
    "E": 109.0, "F": 135.0, "G":  48.0,
    "H": 118.0, "I": 124.0, "K": 135.0,
    "L": 124.0, "M": 124.0, "N":  96.0,
    "P":  90.0, "Q": 114.0, "R": 148.0,
    "S":  73.0, "T":  93.0, "V": 105.0,
    "W": 163.0, "Y": 141.0,
}


Proteins = {
      "Alanine" : "A",
      "Cysteine": "C",
      "Aspartic acid" : "D",
      "Glutamic acid" : "E",
      "Phenylalanine" : "F",
      "Glycine" : "G",
      "Histidine" : "H",
      "Isoleucine" : "H",
      "Lysine" : "K",
      "Leucine" : "L",
      "Methionine": "M",
      "Asparagine": "N",
      "Proline" : "P",
      "Glutamine": "Q",
      "Arginine" : "R",
      "Serine" : "S",
      "Threonine" : "T",
      "Valine": "V",
      "Tryptophan": "W",
      "Tyrosine" : "Y"
}





###################################################################################
############################   Classic RNA translator   ########################### 
###################################################################################


# The codon
cd1 = []

# The Full name protein
pr1 = []

# The protein annot
pr_sh1 = []

print("\nThis is the Translation of your DNA Sequence Reading Frame(RF) No.1:\n") 
for i in range(0, len(RNA),3):

# RF 1 is starting from 0 however RF 2 and RF 3 having a +1 and +2 starting point Respectively


    A = RNA[i : i+3] # Reading 3 nucleotide but the last ones might be 2 or 1 nucleotide long
    if A in codons.keys(): # Trimming all A's in 3 length nucleotide
        P = codons[A] # Finding the dictionary value
        pr1.append(P)
        cd1.append(A)
        PS = Proteins[P] # Finding the dictionary value
        pr_sh1.append(PS)

print("\nThe Codons of RNA for RF_1 is:\n")   
print(cd1)

print("\nThe Translated sequence of your DNA for RF_1 is:\n")   
print(pr1)

print("\nAnd the protein annotation for that :\n") 
print(pr_sh1)  



cd2 = []
pr2 = []
pr_sh2 = []

print("\nThis is the Translation of your DNA Sequence Reading Frame(RF) No.2:\n") 
for i in range(1, len(RNA),3):

    A = RNA[i : i+3]
    if A in codons.keys():
        P = codons[A]
        pr2.append(P)
        cd2.append(A)
        PS = Proteins[P]
        pr_sh2.append(PS)

print("\nThe Codons of RNA for RF_2 is:\n")   
print(cd2)

print("\nThe Translated sequence of your DNA for RF_2 is:\n")   
print(pr2)

print("\nAnd the protein annotation for that :\n") 
print(pr_sh2)  




cd3 = []
pr3 = []
pr_sh3 = []

print("\nThis is the Translation of your DNA Sequence Reading Frame(RF) No.3:\n") 
for i in range(2, len(RNA),3):

    A = RNA[i : i+3]
    if A in codons.keys():
        P = codons[A]
        pr3.append(P)
        cd3.append(A)
        PS = Proteins[P]
        pr_sh3.append(PS)


print("\nThe Codons of RNA for RF_3 is:\n")   
print(cd3)

print("\nThe Translated sequence of your DNA for RF_3 is:\n")   
print(pr3)

print("\Aand the protein annotation for that :\n") 
print(pr_sh3)  



# Not_Run
############################################################

###################################################################################
########################   Modern approach RNA translator   ####################### 
###################################################################################




#!/user/bin/python


dna = input ("please enter your sequence:\n")



def has_stop_codon(dna):
    stop_codon_found = False
    stop_codons = ["taa", "tag", "tga"]

    for frame in range (0,2):

        for i in range ( frame, len(dna) , 3):
            read = dna[i : i+3].lower()

            if read in stop_codons:
                stop_codon_found = True
            else:
                stop_codon_found = False
    return stop_codon_found

         
        
print(has_stop_codon(dna,0))
print(has_stop_codon(dna,1))
print(has_stop_codon(dna,2))





X = ("ACGT")

def GC (X):
    N_count = X.count("n") + X.count('N')
    GC_Persentage = float(X.count("c") + X.count("C") + X.count("g") + X.count("G")) * 100  / (len(X) - N_count)
    return GC_Persentage

print(GC(X))







seq = "TCGA"

def reverse_string (seq):
    return seq [::-1]

def complement (seq):
    RNA_map = seq.maketrans("ATGC", "TAGC")
    seq = seq.translate(RNA_map)
    return seq
    


def reverse_complement (seq):
    seq = reverse_string(seq)
    seq = complement (seq)
    return seq


print(reverse_complement(seq))




make_complement = {

    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C",
    "a" : "T",
    "t" : "A",
    "c" : "G",
    "g" : "C",
    "n" : "N",
    "N" : "N",
}

'''






