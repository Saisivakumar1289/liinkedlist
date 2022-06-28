class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedkist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            s=""
            while n is not None:
                s+=str(n.data)+"---->" if n.ref else str(n.data)
                n=n.ref
            print(s) 

    def add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
    def reverse(self):
        print()
        prev=None
        n=self.head
        while n is not None:
            temp=n.ref
            n.ref=prev
            prev=n
            n=temp
        self.head=prev  

    def get_length(self):
        count=0
        n=self.head
        while n:
            count+=1
            n=n.ref
        print(count)   
            

#testing
if __name__=='__main__':
    obj=linkedkist()
    l=[int(x) for x in input().split()] #dynamically we can take input by using this
    for i in l:
        obj.add_begin(i)
    print("original order")    
    obj.traversal()  
    obj.reverse()  
    print("reverse order")    
    obj.traversal()
    obj.get_length()
                                         

