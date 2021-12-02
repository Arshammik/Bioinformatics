def debruijn_graph(ftext, fout):

    ksize = 0
    text = ""
    with open(ftext, "r") as f:
        for i, line in enumerate(f):
            if i==0:
                ksize = int(line.split("\n")[0])
            if i==1:
                text = line.split("\n")[0]
    
    dict_debruijn = {}
    for i in range(0, len(text)):
        if i <= len(text) - ksize:
            string = text[i : i+ksize]
            head, tail = string[0:ksize-1], string[1:]
            if head not in dict_debruijn:
                dict_debruijn[head] = []
            dict_debruijn[head].append(tail)

    with open(fout, "w") as g:
        for key in dict_debruijn:
            if len(dict_debruijn[key]) > 0:
                g.write(key + " -> ")
                for i, elem in enumerate(dict_debruijn[key]):
                    if i < len(dict_debruijn[key]) - 1:
                        g.write(elem + ",")
                    else:
                        g.write(elem + "\n")
if __name__ == "__main__":

    debruijn_graph("inputs/debruijn.txt", "outputs/debruijn.txt")                        