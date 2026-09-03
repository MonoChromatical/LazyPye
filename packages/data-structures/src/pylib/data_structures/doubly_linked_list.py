from dataclasses import dataclass
from typing import Generic, TypeVar

__all__ = ["DoublyLinkedList"]

T = TypeVar("T")

@dataclass(slots=True)
class _Node(Generic[T]):
    """Store the internal state for doubly linked-list node."""

    data: T
    next: "_Node[T] | None" = None
    prev: "_Node[T] | None" = None


class DoublyLinkedList(Generic[T]):
    """Stores values in nodes connected bidirectional.

    Nodes and list pointers are private implementation details. Public methods
    accept zero-based positions and return stored data rather than exposing
    mutable node objects.
    """
    def __init__(self):
        """Create an empty doubly linked list."""

        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self.__size

    @property
    def is_empty(self):
        return self.__head is None

    def append(self, data: T) -> None:
        """Append data to the end of the list.

    def add_data(self, data):
        Args:
            data: Value to store in the new next node.
        """

        new_node = _Node(data)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            return
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node

    def add_data_first(self, data):
        new_node = _Node(data)

        if self.is_empty():
            self._head = new_node
            return

        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def delete(self, key):
        temp = self._head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self._head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print(f"Deleted data node with the value {key}")
                return

            temp = temp.next

        print(f"Data Node with key {key} not found")

    def search(self, key):
        temp = self._head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display_forward(self):
        elements = []
        temp = self._head

        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

    def display_backward(self):
        elements = []
        temp = self._tail

        while temp:
            elements.append(temp.data)
            temp = temp.prev

        return elements
