def levelOrder(self,root):
    res = []
    res.append(root)

    while(len(res) > 0):
        node = res.pop(0)
        print(node.data,end=" ")

        if node.left:
            res.append(node.left)
        if node.right:
            res.append(node.right)   

    return      
       
