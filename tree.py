# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:19:07 2019

@author: rrt
"""

class Node:
    def __init__(self,node=None):
        self.node=node
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.node)

def midTree(root):
    if(root):
        midTree(root.left)
        print(root.node)    
        midTree(root.right)

def preTree(root):
    if root:
        print(root.node)
        preTree(root.left)
        preTree(root.right)
        
def postTree(root):
    if root:
        postTree(root.left)
        postTree(root.right)
        print(root.node)
        
def level(root):
    seq=[]
    seq.append(root)
    while(seq):
        cur=seq.pop(0)
        print(cur)
        if cur.left:
            seq.append(cur.left)
        if cur.right:
            seq.append(cur.right)

def insert(root,node):
    if(not root ):
        root=node
    else:
        if(root.node<node.node):
            if(not root.right):
                root.right=node
            else:
                insert(root.right,node)
        else:
            if(not root.left):
                root.left=node
            else:
                insert(root.left,node)
    
def test():
    nodes=[46,25,78,62,12,37,70,29]
    root=Node(nodes[0])
    for i in range(1,len(nodes)):
        nodei=Node(nodes[i])
        insert(root,nodei)
    midTree(root)
    
test()        
        
    

