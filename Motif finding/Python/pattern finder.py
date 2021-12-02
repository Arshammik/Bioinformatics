text = "ACTGAGATGCGACCTTCACGGCCTCACCGTTCGGTATGTACCGCGGAGATTCTCGCGAAGCGCTAGGGTATCTGGTCAGCCCACGCGATGCTTATAAACACTCCATTCTTACTCGTCACATGCGGTCTCGCAGGTATCATGCGAGATGTC"
k = 5


def FrequencyMap(text, k):
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq


print(FrequencyMap(text, k))


def FrequentKmers(text, k):
    kmers = []
    freq = FrequencyMap(text, k)
    m = max(freq.values())
    for most_frequent_kmer in freq:
        if freq[most_frequent_kmer] == m:
            kmers.append(most_frequent_kmer)

    return kmers


print("most frequent k-mer is")
print(FrequentKmers(text, k))

