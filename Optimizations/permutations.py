numbers = [0, 1, 2, 3, 4, 5]

def permutations(elements: []) -> [[]]:
    # Base case
    if len(elements) == 0:
        return [[]]
    head = elements[0]
    tail = elements[1:]
    allPermutations = []
    for i in range(len(elements)):
        perms = permutations(elements[:i] + elements[i+1:])
        for p in perms:
            allPermutations.append([elements[i], *p])
    return allPermutations

     

print(permutations([1, 2, 3]))