class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return True
        temp = self.root
        while 1:
            if temp == None:
                temp = newNode
            if temp.value == value:
                return "Invalid"
            if temp.value < value:
                if temp.right == None:
                    temp.right = newNode
                    return True
                temp = temp.right
                continue
            if temp.value > value:
                if temp.left == None:
                    temp.left = newNode
                    return True
                temp = temp.left
                continue

    def insertRecursive(self,value):
        temp=self.root
        def inserting(node,value):
            if node==None:
                return Node(value)
            if value<node.value:
                node.left=inserting(node.left,value)
            else:
                node.right=inserting(node.right,value)
            return node
        return inserting(temp,value)



    def inOrderTraverse(self,temp='start'):
        if temp=='start':
            temp=self.root
            print("Inorder Traverse\n")
        if temp==None:
            return True
        self.inOrderTraverse(temp.left)
        print(temp.value,end="-->")
        self.inOrderTraverse(temp.right)

    def preorderTraverse(self):
        def preorder(node):
            if node==None:
                return True
            print(node.value,end="-->")
            preorder(node.left)
            preorder(node.right)

        if self.root is None:
            return None
        preorder(self.root)



    def postOrderTraverse(self,temp='start'):
        if temp=='start':
            temp=self.root
            print("Post Order Traverse\n")
        if temp==None:
            return True
        self.postOrderTraverse(temp.left)
        self.postOrderTraverse(temp.right)
        print(temp.value,end="-->")

    def minimum(node):
        while node.left!=None:
            node=node.left
        return node

    def delete(self,value):
        if self.root is None:
            return None
        def deleting(node,value):
            if node==None:
                return None
            if node.value>value:
                node.left=deleting(node.left,value)
            elif node.value<value:
                node.right=deleting(node.right,value)
            else:
                if node.left==None and node.right==None:
                    node.value=None
                    return None
                if node.left==None:
                    return node.right
                elif node.right==None:
                    return node.left
                else:
                    rightMin=binaryTree.minimum(node.right).value
                    node.right=deleting(node.right,rightMin)
                    node.value=rightMin
            return node
        self.root=deleting(self.root,value)


def main():
    binary = binaryTree()
    while 1:
        n = int(input("\n1.Insert into Binary-Search-Tree.\t2.Remove From Binary-Search-Tree"
                      "\n3.PreOrder-Traverse.\t4.Inorder-Traverse.\t5.PostOrder-Traverse\n"
                      "6.Multiple Insert\t7.Exit\n"))
        if n == 1:
            binary.insert(int(input("Enter Value to be insert :-")))
        if n == 2:
            value=int(input("Enter value:-"))
            binary.delete(value)
        if n==3:
            binary.preorderTraverse()
        if n==4:
            binary.inOrderTraverse()
        if n==5:
            binary.postOrderTraverse()
        if n==6:
            values=list(map(int,input().split()))
            for value in values:
                binary.insert(value)

        if n==7:
            print("'''Opertions Done'''")
            break


if __name__ == '__main__':
    main()
