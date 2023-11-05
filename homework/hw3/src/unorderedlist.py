"""
unorderedlist.py
Jon Shallow
20231102
"""

from node import Node


class UnorderedList:
    """
    Class representation of an UnorderedList
    """

    def __init__(self):
        """
        Constructor
        """
        self.head = None

    def prepend(self, item):
        """
        Create node that has item and make it the first element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        """
        Count the number of elements in the unordered list.
        :return: integer
        """
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def is_empty(self):
        """
        Check whether the unordered list has no nodes.
        :return: True if the unordered list object doesn't have any eleemnt.
        """
        return self.head is None

    def search(self, item):
        """
        Search for item in the unordered list.
        :param item: integer
        :return: True if item found. False otherwise.
        """
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        return False

    def __str__(self):
        """
        Create string representation of the unordered list object. The string
        shows the data items, separated by ','. If the list is empty, the
        string is empty string.
        :return: string
        """
        ul_str = ""
        curr_node = self.head
        while curr_node:
            if curr_node.get_next() is None:
                ul_str = ul_str + str(curr_node.get_data())
            else:
                ul_str = ul_str + str(curr_node.get_data()) + ", "
            curr_node = curr_node.get_next()
        return ul_str

    def append(self, item):
        """
        Create node that has item and make it the last element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        curr_node = self.head
        if curr_node is None:
            new_node.set_next(None)
            self.head = new_node
        else:
            while curr_node:
                if curr_node.get_next() is None:
                    new_node.set_next(None)
                    curr_node.set_next(new_node)
                    break
                curr_node = curr_node.get_next()

    def pop(self):
        """
        Remove first node/element in unordered list and return its data property
        :return: integer
        """
        if self.head is None:
            return None
        else:
            value = self.head.get_data()
            self.head = self.head.get_next()
            return value

    def remove(self, item):
        # If the item is removed successfully, return the item.
        # Otherwise, return the `self._head`.
        # Replace these comments with a well-formed docstring.
        pass
