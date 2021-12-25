from collections import defaultdict


def defdict():
    return []


def reverse_complement(seq):
   
    dct = {"A": "T", "T": "A", "C": "G", "G": "C"}
    mer = ""
    for char in seq:
        mer = dct[char] + mer
    return mer


def shared_kmers(k, sta, stb):
    

    b_dct = defaultdict(defdict)
    for i, _ in enumerate(stb[: -k + 1]):
        b_dct[stb[i : i + k]].append(i)

    matches = []
    for i, _ in enumerate(sta[: -k + 1]):
        match = sta[i : i + k]
        rev_match = reverse_complement(match)

        for compare in (match, rev_match):
            if compare in b_dct.keys():
                for v in b_dct[compare]:
                    matches.append((i, v))

    return matches


if __name__ == "__main__":

    k = 3
    sta = "TGGCCTGCACGGTAG"
    stb = "GGACCTACAAATGGC"

    out = shared_kmers(k, sta, stb)
    print(out)
    print(len(set(out)))
