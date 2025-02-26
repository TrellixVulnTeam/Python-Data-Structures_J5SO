class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def search(root,key): 
      
    if root is None or root.val == key: 
        return root 
  
    if root.val < key: 
        return search(root.right,key) 
    
    return search(root.left,key)  

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

if __name__ == "__main__":
    
    r = Node(50) 
    insert(r,Node(30)) 
    insert(r,Node(20)) 
    insert(r,Node(40)) 
    insert(r,Node(70)) 
    insert(r,Node(60)) 
    insert(r,Node(80)) 
    
    # Print inoder traversal of the BST 
    inorder(r) 
    key = search(r,98)
    if key:
        print("Found")
    else:
        print("Not found")