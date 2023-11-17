'''
Assignment 2: Huffman Coding
Date: 29/7/2023
'''
import heapq 

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
  
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"Code for {node.symbol} -> {newVal}")

def encode(chars,freq,nodes):
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
        heapq.heappush(nodes, newNode)
    return chars,freq,nodes

if __name__=='__main__':
    chars=[]
    freq=[]
    nodes=[]
    n=int(input("Enter number of characters for Huffman encoding: "))
    for i in range(n):
        a=input("Enter character: ")
        b=int(input("Enter frequency of "+str(a)+" : "))
        chars.append(a)
        freq.append(b)
    chars,freq,nodes=encode(chars,freq,nodes)
    printNodes(nodes[0])

'''
Output:
Enter number of characters for Huffman encoding: 6
Enter character: a
Enter frequency of a : 5
Enter character: b
Enter frequency of b : 9
Enter character: c
Enter frequency of c : 12
Enter character: d
Enter frequency of d : 13
Enter character: e
Enter frequency of e : 16
Enter character: f
Enter frequency of f : 45
Code for f -> 0
Code for c -> 100
Code for d -> 101
Code for a -> 1100
Code for b -> 1101
Code for e -> 111


Enter number of characters for Huffman encoding: 7
Enter character: a
Enter frequency of a : 1
Enter character: b
Enter frequency of b : 2
Enter character: c
Enter frequency of c : 3
Enter character: d
Enter frequency of d : 4
Enter character: e
Enter frequency of e : 5
Enter character: f
Enter frequency of f : 6
Enter character: g
Enter frequency of g : 7
Code for f -> 00
Code for c -> 010
Code for a -> 0110
Code for b -> 0111
Code for g -> 10
Code for d -> 110
Code for e -> 111
'''
  
  
  