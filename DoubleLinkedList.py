class DoublyLinkedList:
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

