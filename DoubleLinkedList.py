class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def getValue(self):
        return self.value
    
    def getNext_Node(self):
        return self.next_node
    
    def getPrevious_Node(self):
        return self.previous_node
    
    def setValue(self, value):
        self.value = value
   
    def setNext_Node(self, next_node):
        self.next_node = next_node
    
    def setPrevious_Node(self, previous_node):
        self.previous_node = previous_node

class DoublyLinkedList:
    def __init__(self, value):
        self.current_node = Node(value)
        self.initial_node = self.current_node

    def add_nlink(self, value):
        new_node = Node(value)
        self.current_node.setNext_Node(new_node)
        new_node.setPrevious_Node(self.current_node)
        self.current_node = new_node

    def printdl(self):
        output = "[ "
        currentNode = self.initial_node 
        while currentNode:
            output += str(currentNode.getValue())+", "
            currentNode = currentNode.getNext_Node()
        output += "]"
        print(output)

obj1 = DoublyLinkedList(4)
obj1.add_nlink(5)
obj1.add_nlink(7)
obj1.printdl()
