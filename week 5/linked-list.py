class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    
    def add_item(self,item):
        new_node=Node(item)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end="->")
            temp=temp.next
        print("NULL")

    def add_at_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, target_item, new_item):
        temp = self.head
        while temp is not None:
            if temp.item == target_item:
                new_node = Node(new_item)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Item not found")

lost_and_found=linklist()
lost_and_found.add_item("Wallet")
lost_and_found.add_item("ID Card")
lost_and_found.add_item("Notebook")

lost_and_found.display()

lost_and_found.add_at_beginning("Pouch")
lost_and_found.add_after("ID Card","Found Umbrella")

lost_and_found.display()