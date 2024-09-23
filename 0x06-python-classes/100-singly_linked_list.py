#!/usr/bin/python3
"""
Module: 100-singly_linked_list.py
Defines classes Node and SinglyLinkedList for managing a singly linked list.
"""

class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data value to be stored.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node linked to this node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node linked to this node.

        Args:
            value (Node or None): The next node object or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted.

        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Prints the entire list in stdout, one node number by line.

        Returns:
            str: The formatted string representation of the list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
