# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:11:23 2019

@author: mario
"""

class TrieNode:
    def __init__(self,word,label):
        self.word=word
        self.edges={}
        self.label=label
        
    def AddEdge(self,edge_label,node_label,word): #edges=dict 
        if edge_label not in self.edges:
            self.edges[edge_label]=TrieNode(word,node_label) #???
            
class Trie:
    def __init__(self):
        self.root=TrieNode('',1)
        self.label_count=2
            
    def AddWord(self,word):
        current_node=self.root
        for i in range(len(word)):
            if word[i] in current_node.edges:
                current_node=current_node.edges[word[i]]
            else:
                if i==len(word)-1:
                    current_node.AddEdge(word[i],self.label_count,word)
                else:
                    current_node.AddEdge(word[i],self.label_count,'')
                self.label_count+=1
                current_node=current_node.edges[word[i]]

def PreOrderTraversal(root):
    for edge in root.edges:
        child=root.edges[edge]
        print(root.label,child.label,edge)
    for edge in root.edges:
        PreOrderTraversal(root.edges[edge])
        
def PostOrderTraversal(root):
    for edge in root.edges:
        PostOrderTraversal(root.edges[edge])
    print(root.edges.keys())




trie=Trie()
trie.AddWord('ATAGA')
trie.AddWord('ATC')
trie.AddWord('GAT')

PreOrderTraversal(trie.root)
print('=========')
PostOrderTraversal(trie.root)