class Node:
    def __init__(self, tank):
        self.tank = tank
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_tank(self, tank):
        new_node = Node(tank)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self, count):
        temp = self.head
        for i in range(count):
            print(temp.tank, end=" -> ")
            temp = temp.next
        print("(repeats)")


# Main
tanks = CircularLinkedList()
tanks.add_tank("Tank 1")
tanks.add_tank("Tank 2")
tanks.add_tank("Tank 3")

tanks.display(6)
