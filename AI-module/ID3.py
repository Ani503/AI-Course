import math
from collections import Counter

def entropy(labels):
    n = len(labels)
    return sum(-c/n * math.log2(c/n) for c in Counter(labels).values())

def id3(data, labels, attrs):
    # Stop conditions
    if len(set(labels)) == 1: return labels[0]  # All same class
    if not attrs: return Counter(labels).most_common(1)[0][0]  # No attributes left
    
    # Pick best attribute to split
    best = max(attrs, key=lambda a: calc_gain(data, labels, a))
    
    # Build tree recursively
    tree = {best: {}}
    for val in set(row[best] for row in data):
        subset = [i for i,row in enumerate(data) if row[best] == val]
        tree[best][val] = id3([data[i] for i in subset], [labels[i] for i in subset], 
                               [a for a in attrs if a != best])
    return tree

def calc_gain(data, labels, attr):
    total_entropy = entropy(labels)
    values = set(row[attr] for row in data)
    
    weighted_entropy = 0
    for val in values:
        subset = [labels[i] for i,row in enumerate(data) if row[attr] == val]
        weighted_entropy += len(subset)/len(labels) * entropy(subset)
    
    return total_entropy - weighted_entropy

# Test it
data = [['S','H','H','F'], ['S','H','H','T'], ['O','H','H','F'], ['R','M','H','F'],
        ['R','C','N','F'], ['R','C','N','T'], ['O','C','N','T'], ['S','M','H','F'],
        ['S','C','N','F'], ['R','M','N','F'], ['S','M','N','T'], ['O','M','H','T'],
        ['O','H','N','F'], ['R','M','H','T']]
labels = ['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']

tree = id3(data, labels, [0,1,2,3])
print(tree)