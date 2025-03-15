def pairs(elements):
    dict = {} 
    
    for i in range(len(elements)):
        dict[elements[i]] = elements[i+1:]

    # pairs list 
    pairs = []

    for pair_1 in dict:
        temp_pairs = dict[pair_1]

        for pair_2 in temp_pairs:
            pairs.append([pair_1, pair_2])

    return pairs 

if __name__ == "__main__":
    print(pairs(["a", "b", "c"])) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["b", "c"]
# ]