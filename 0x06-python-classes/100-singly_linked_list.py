#!/usr/bin/python3
"""This module contains a class `Node`"""


class Node:
    """This class defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiates a Node Instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the value of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of next_node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""
    def __init__(self):
        """Initializes a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts nodes into the singly linked list in a sorted order."""
        new_node = Node(value, None)

        if self.__head is None:
            self.__head = new_node

        else:
            pointer = self.__head
            newhead = self.__head
            sortanset = False

            while sortanset is False:
                if new_node.data < pointer.data:
                    new_node.next_node = pointer
                    if self.__head == pointer:
                        self.__head = new_node
                    else:
                        newhead.next_node = new_node
                    sortanset = True

                if new_node.data >= pointer.data:
                    newhead = pointer
                    if pointer.next_node is None:
                        new_node.next_node = None
                        pointer.next_node = new_node
                        sortanset = True
                    pointer = pointer.next_node

    def __str__(self):
        """Comments"""
        print_head = self.__head
        count = 1

        while print_head is not None:
            if count != 1:
                print()
            print("{}".format(print_head.data), end="")
            print_head = print_head.next_node
            count += 1
        return ""
