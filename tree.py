# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:19:07 2019

@author: rrt
"""

class node:
    def __init__(self,node=None):
        self.node=node
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.node)

def midTree(root):
    if(root.left):
        midTree(root.left)
    print(root.node)
    if(root.right):
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
    
    
    

root=node(46) 
node1=node(25) 
node2=node(78) 
node3=node(62)
node4=node(12)
node5=node(37)
node6=node(70)
node7=node(29) 

#root.left=node1
#root.right=node2
#node1.left=node4
#node1.right=node5
#node5.left=node7
#node2.left=node3
#node3.right=node6    

#insert(None,root)
insert(root,node1)
insert(root,node2)
insert(root,node3)
insert(root,node4)
insert(root,node5)
insert(root,node6)
insert(root,node7)



midTree(root)
#preTree(root)
#postTree(root)
#level(root)
