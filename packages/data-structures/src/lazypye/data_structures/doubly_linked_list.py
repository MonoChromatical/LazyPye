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

        self.__head: _Node[T] | None = None
        self.__tail: _Node[T] | None = None
        self.__size = 0

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self.__size

    @property
    def is_empty(self) -> bool:
        return self.__head is None

    def append(self, data: T) -> None:
        """Append data to the end of the list.

        Args:
            data: Value to store in the new next node.
        """

        new_node = _Node(data)

        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

    def prepend(self, data: T) -> None:
        """Prepend data to the beginning of the list.

        Args:
            data: Value to store in the new node.
        """

        new_node = _Node(data)

        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

        self.__size += 1

    def insert_middle(self, position: int, data: T) -> None:
        """Insert data before an existing middle position.

        Args:
            position: Zero-based insertion position. It must be greater than
                zero and less than the current list length.
            data: Value to store in the inserted node.

        Raises:
            TypeError: If position is not an integer.
            IndexError: If position is zero, is an append position, or lies
                outside the list.
        """
        self._validate_middle_insertion_position(position)

        current = self._node_at(position)
        previous = current.prev

        new_node = _Node(data, next=current, prev=previous)

        previous.next = new_node
        current.prev = new_node

        self.__size += 1

    def delete_head(self):
        """Remove and return the first value.

        Returns:
            The data previously stored at the beginning of the list.

        Raises:
            IndexError: If the list is empty.
        """

        if self.is_empty:
            raise IndexError("delete from empty linked list")

        if self.__head == self.__tail:
            removed = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1

            return removed.data

        removed = self.__head
        self.__head = removed.next
        self.__head.prev = None
        self.__size -= 1

        return removed.data

    def delete_tail(self):
        """Remove and return the final value.

        Returns:
            The data previously stored at the end of the list.

        Raises:
            IndexError: If the list is empty.
        """

        if self.is_empty:
            raise IndexError("delete from empty linked list")

        if self.__head == self.__tail:
            removed = self.__tail
            self.__head = None
            self.__tail = None
            self.__size -= 1

            return removed.data

        removed = self.__tail
        self.__tail = removed.prev
        self.__tail.next = None
        self.__size -= 1
        return removed.data

    def remove(self, data: T) -> T | None:
        """Remove and return the first matching value.

        Args:
            data: Value to search for and remove.


        Returns:
            The removed value, or None if the value was not found.

        Raises:
            IndexError: If the list is empty.
        """
        current = self.__head

        while current is not None:
            if current.data == data:
                if current == self.__head:
                    return self.delete_head()

                if current == self.__tail:
                    return self.delete_tail()

                removed = current.data

                current.prev.next = current.next
                current.next.prev = current.prev
                self.__size -= 1
                return removed

            current = current.next
        return None

    def display(self, forward=True):
        """Prints all stored values in the list.
        Args:
            forward:
                - If True, display from head to tail.
                - If False, display from tail to head.
        """
        if self.is_empty:
            print("Doubly linked list is empty")
            return

        if forward:
            current = self.__head

            while current is not None:
                print(current.data)
                current = current.next
        else:
            current = self.__tail

            while current is not None:
                print(current.data)
                current = current.prev

    # TODO: Update to new DLL format OR Test to see if it still works
    def search(self, key):
        temp = self.__head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    def display_node(self, position: int) -> T:
        """Return the data stored at a zero-based position.

        Returning data instead of a node keeps list connections private.

        Args:
            position: Zero-based position to retrieve.

        Returns:
            The data stored at position.

        Raises:
            TypeError: If position is not an integer.
            IndexError: If position lies outside the list.
        """

        return self._node_at(position).data

