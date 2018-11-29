
class _node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
class binary_search_tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        """
        description:
            This method inserts data into the Binary Search Tree.
        input:
            Data to be stored.
        output:
            N/A
        """
        if not self.root:
            self.root = _node(data)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        """
        description:
            A recursive function to start from the root of the tree,
            and compare its data with the data to be added recursively,
            to decide the place it will be inserted into the tree.
            
            This function isn't called by the user, it is called 
            internally by the insert() function.
        input:
            Data to be added, and the root at first then the rest of the nodes.
        output:
            N/A
        """
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = _node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = _node(data)
                
            
    def remove_node(self, data, node):
        """
        description:
            A recursive function that decides which case of deletion we are in:
            (1) If it is a leaf node it removes it and the parent points to None.
            (2) If it is a node with single child it removes it and make the parent
                points to the child of the deleted node.
            (3) If it is a root node it finds the predecessor and swaps with it,
                then continues as one of the first two cases.
                
            This function isn't called by the user, it is called 
            internally by the remove() function.
        input:
            Data to be removed, and the root to start from there.
        output:
            The node that will be replaced by the removed node.
        """
        if not node:
            return node
        
        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print('Removing a leaf node ...')
                del node
                return None
            
            if not node.left_child:
                print('Removing a node with single right child ...')
                temp_node = node.right_child
                del node
                return temp_node
            
            if not node.right_child:
                print('Removing a node with single left child ...')
                temp_node = node.left_child
                del node
                return temp_node
            
            print('Removing a node with two children ...')
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)
            
        return node
            
    def get_predecessor(self, node):
        """
        description:
            A recursive function that finds the predecessor of the root node.
            The predecessor is the biggest value in the left of the root.
            
            This function isn't called by the user, it is called 
            internally by the remove_node() function.
        input:
            The root that needs to be swapped.
        output:
            The node with the biggest value on its left.
        """
        if node.right_child:
            return self.get_predecessor(node.right_child)
        
        return node
        
    def remove(self, data):
        """
        description:
            This method removes a given data from the tree.
        input:
            Data to be removed.
        output:
            N/A
        """
        if self.root:
            self.root = self.remove_node(data, self.root)
    
    def get_min_value(self):
        """
        description:
            This method gets the minimum value in the tree.
        input:
            N/A
        output:
            The output of the get_min() function.
        """
        if self.root:
            return self.get_min(self.root)
        
    def get_min(self, node):
        """
        description:
            A recursive function that starts from the root,
            then goes to the left most item and returns its value.
            
            This function isn't called by the user, it is called 
            internally by the get_min_value() function.
        input:
            The root of the tree.
        output:
            Minimum value in the tree.
        """
        if node.left_child:
            return self.get_min(node.left_child)
        
        return node.data
    
    def get_max_value(self):
        """
        description:
            This method gets the maximum value in the tree.
        input:
            N/A
        output:
            The output of the get_max() function.
        """
        if self.root:
            return self.get_max(self.root)
        
    def get_max(self, node):
        """
        description:
            A recursive function that starts from the root,
            then goes to the right most item and returns its value.
            
            This function isn't called by the user, it is called 
            internally by the get_max_value() function.
        input:
            The root of the tree.
        output:
            Maximum value in the tree.
        """
        if node.right_child:
            return self.get_max(node.right_child)
        
        return node.data
    
    def traverse(self):
        """
        description:
            This method traverses and prints all the items in the tree.
        input:
            N/A
        output:
            N/A
        """
        if self.root:
            self.in_order(self.root)
            
    def in_order(self, node):
        """
        description:
            A recursive function that starts from the root,
            then traverses the tree in an in_order traverse,
            and prints the items.
            
            This function isn't called by the user, it is called 
            internally by the traverse() function.
        input:
            The root of the tree.
        output:
            N/A
        """
        if node.left_child:
            self.in_order(node.left_child)
            
        print(node.data)
        
        if node.right_child:
            self.in_order(node.right_child)