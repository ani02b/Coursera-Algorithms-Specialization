import heapq
from collections import namedtuple

Node = namedtuple('Node', ('weight','index'))

def read_file(name):
    """Given the path/name of the text file, return the heap with nodes.
    """
    
    tree = []
    
    file = open(name, 'r')
    data = file.readlines()
    
    for index, line in enumerate(data[1:]):
        item = line.split()
        tree.append(Node(int(item[0]), str(index)))
    
    heapq.heapify(tree)
    return tree
        
def combine(a,b):
    """Combine two nodes into a single one.
    """
    return Node(a.weight+b.weight, '+'.join([a.index, b.index]))


def huffman(tree):
    """Given the initial tree, return the length of each node. 
    """
    code_len = [0]*len(tree)
    while(len(tree)>1):
        # Pop two min items
        a = heapq.heappop(tree)
        b = heapq.heappop(tree)
        
        # Reinsert the combined item
        new_node = combine(a,b)
        heapq.heappush(tree, new_node)
        #heapq.heappush(tree,combine(a,b))
        
        # add 1 to the code length for a,b
        com = [int(item) for item in new_node.index.split('+')]
        for i in com:
            code_len[i] += 1
        
    return code_len

def main():
    tree = read_file('C:\\Users\\KIIT\\Programs\\3rd Year\\CC3\\huffman.txt')
    codes = huffman(tree)
    print("Max=", max(codes), "Min=", min(codes))

if __name__ == '__main__':
    main()