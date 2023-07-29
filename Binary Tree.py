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

    def inOrderTraverse(self,temp='start'):
        if temp=='start':
            temp=self.root
            print("Inorder Traverse\n")
        if temp==None:
            return True
        self.inOrderTraverse(temp.left)
        print(temp.value,end="-->")
        self.inOrderTraverse(temp.right)

    def preorderTraverse(self,temp='start'):
        if temp=='start':
            temp=self.root
            print("PreOrder Traverse\n")
        if temp==None:
            return True
        print(temp.value,end="-->")
        self.inOrderTraverse(temp.left)
        self.inOrderTraverse(temp.right)

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

    def delete(self,value,temp:Node='start'):
        if temp=='start':
            temp=self.root
        if temp==None:
            return None
        if temp.value<value:
            temp.left=self.delete(temp.left,value)
        elif temp.value>value:
            temp.right=self.delete(temp.right,value)
        else:
            if temp.left==None and temp.right==None:
                temp.value=None
                return None
            if temp.left==None:
                temp=temp.right
            elif temp.right==None:
                temp=temp.left
            else:
                temp.right=self.delete(temp.right,binaryTree.minimum(temp.right))



def main():
    binary = binaryTree()
    while 1:
        n = int(input("\n1.Insert into Binary-Search-Tree.\t2.Remove From Binary-Search-Tree"
                      "\n3.PreOrder-Traverse.\t4.Inorder-Traverse.\t5.PostOrder-Traverse\n"))
        if n == 1:
            binary.insert(int(input("Enter Value to be insert :-")))
        if n == 2:
            binary.delete(int(input("Enter value:-")))
        if n==3:
            binary.preorderTraverse()
        if n==4:
            binary.inOrderTraverse()
        if n==5:
            binary.postOrderTraverse()
        if n==6:
            print("'''Opertions Done'''")
            break



if __name__ == '__main__':
    main()
