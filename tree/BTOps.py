# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 08:45:25 2018

@author: I309535
"""

from BinaryTree import BinaryTree,BinaryTreeNode

def findFullNodeCount(root):
    if root == None:
        return 0
    
    lc = findFullNodeCount(root.left)
    rc = findFullNodeCount(root.right)
    
    current_status = 1 if root.left!=None and root.right!=None else 0
    return lc+rc+current_status

# @return balanced status, height
def checkBalanceAndHeight(root):
    if root == None:
        return (True,0)
    
    l_balance,lh = checkBalanceAndHeight(root.left)
    r_balance,rh = checkBalanceAndHeight(root.right)
        
    is_balanced = l_balance and r_balance and abs(lh-rh)<=1
    return (is_balanced,1+max(lh,rh))
        
def get_branch(root,search_el):
    branch = list()
    search_status= get_branch_aux(root,search_el,branch,0)
    print 'final branch recieved:',branch
    return search_status,branch

def get_branch_aux(root,search_el,branch,level):
    if root==None:
        return False
    
    branch.append(root.val)
    
    if root.val==search_el:
        #print 'found:',branch
        return True
    
    ls = get_branch_aux(root.left,search_el,branch,level+1)
    rs = get_branch_aux(root.right,search_el,branch,level+1)
    
    # Check if search_el is found in left or right sub-tree
    if ls or rs:
        return True
    
    # If not present in subtree rooted with root, remove
    # root from path and return False
    ### ********* IMP : remove, otherwise previous branch elements will retain
    branch.pop()
    return False
    
    
    
def lca(root,node1,node2):
    path1 = get_branch(root,node1.val)[1]
    path2 = get_branch(root,node2.val)[1]
    
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
        
    return path1[i-1]

def get_branch_sums(root):
    res = []
    get_branch_sums_aux(root,list([0]),res)
    return res
    
def get_branch_sums_aux(root,branch_sum,sum_list):
    if root == None:
        #print 'branch:',branch,' sum:',sum(branch)
        return
    
    branch_sum[0] += root.val
    if root.left==None and root.right==None:
        ## IMP : because with each return from root==null (from left or right child, causes duplicates)
        sum_list.append(branch_sum[0])
        return
    
    get_branch_sums_aux(root.left,list(branch_sum),sum_list)
    get_branch_sums_aux(root.right,list(branch_sum),sum_list)
    
def has_path_sum(root,target_sum):
    
    return hasPathSumHelper(root,0, target_sum)


def hasPathSumHelper(root,partial_path_sum, target_sum):    
    if root==None:
        return
    
    partial_path_sum += root.val
    if root.left==None and root.right==None:
        return partial_path_sum==target_sum
    
    return hasPathSumHelper(root.left,partial_path_sum, target_sum) or hasPathSumHelper(root.right,partial_path_sum, target_sum)
        
def get_diameter(root):
    diameter = list([0])
    get_diameter_aux(root,diameter)
    return diameter[0]

def get_diameter_aux(root,diameter):
    if root == None:
        return 0
    
    lh = get_diameter_aux(root.left,diameter)
    rh = get_diameter_aux(root.right,diameter)
    if diameter[0] < 1+lh+rh:
        diameter[0] = 1+lh+rh
        
    return 1+max(lh,rh)

####
def exterior_binary_tree(root):
    res = list()
    res.append(root.val)
    left_bt_exterior(root.left,res,True)
    print res
    right_extr = right_bt_exterior(root.right,res,True)
    print right_extr
    return res

def left_bt_exterior(subtree,res,is_boundary):
    if subtree == None:
        return
    
    ## preorder traversal
    ## silly mistake: use of return statement
    if is_boundary or (subtree.left==None and subtree.right==None):
        res.append(subtree.val)
    
    left_bt_exterior(subtree.left,res,is_boundary)  
    is_boundary = is_boundary and subtree.left==None
    left_bt_exterior(subtree.right,res,is_boundary)
    
def right_bt_exterior(subtree,res,is_boundary):
    result = list()
    
    if subtree == None:
        return result
    
    ## post order traversal: traverse children first
    result.extend(right_bt_exterior(subtree.left,res,is_boundary and subtree.right==None))
    result.extend(right_bt_exterior(subtree.right,res,is_boundary))
    
    if is_boundary or (subtree.left==None and subtree.right==None):
        #res.append(subtree.val)
        result.append(subtree.val)
    
    return result
    
## top down, left to right columns
def find_columns(root):
    dist_nodes = dict()
    find_columns_helper(root,dist_nodes,0)
    dists = dist_nodes.keys()
    dists.sort()
    print '\n\nTree Columns'
    for dist in dists:
        print dist_nodes[dist]
        
def find_columns_helper(root,dist_nodes,cur_dist):
    if root == None:
        return 
    
    ## preorder traversal
    if cur_dist in dist_nodes:
        dist_nodes[cur_dist].append(root.val)
    else:
        dist_nodes[cur_dist] = [root.val]
        
    find_columns_helper(root.left, dist_nodes, cur_dist-1)
    find_columns_helper(root.right, dist_nodes, cur_dist+1)
    
    
root = BinaryTreeNode(6)
node1 = BinaryTreeNode(3)
node2 = BinaryTreeNode(5)
node3 = BinaryTreeNode(9)

node2.right = node3
node1.left = node2
root.left = node1

node4 = BinaryTreeNode(2)
node5 = BinaryTreeNode(7)
node6 = BinaryTreeNode(4)

node4.left = node5
node4.right = node6
root.right = node4

bt = BinaryTree(root)
print root.level_order()
"""
print 'height of the tree:', root.height()
print 'full nodes count :',findFullNodeCount(root)
print 'search :'
print get_branch(root,3)
print 'tree diameter:',get_diameter(root)
print 'branches sums:',get_branch_sums(root)
print 'has path sum:',has_path_sum(root,21)

lca_res = lca(root,node6,node3)
print 'lca between %d and %d is %s'% (node6.val,node3.val,lca_res)
"""
#print exterior_binary_tree(root)

find_columns(root)
    


