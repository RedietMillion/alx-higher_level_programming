#!/usr/bin/python3
class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves value of data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves value of `next_node`"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines implementation of a singly linked list"""

    def __init__(self):
        """Initializes instance data"""
        self.__head = None

    def __str__(self):
        """Prints the entire list in stdout"""
        head = self.__head
        values = []
        while head is not None:
            values.append("{}".format(head.data))
            head = head.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        head = self.__head
        if head is None or (head is not None and head.data >= value):
            new_node = Node(value, head)
            self.__head = new_node
            return
        while head is not None:
            next_node = head.next_node
            if next_node is None or next_node.data >= value:
                new_node = Node(value, next_node)
                head.next_node = new_node
                break
            head = next_node
