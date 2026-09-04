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
    def is_empty(self):
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

    # TODO: Update to new DLL format OR Test to see if it still works
    def delete(self, key):
        """Delete the first player with the specified key."""
        current = self.__head

        while current is not None:
            if current.key == key:
                if current == self.__head:
                    self.delete_head()
                    return

                if current == self.__tail:
                    self.delete_tail()
                    return

                current.prev.next = current.next
                current.next.prev= current.prev
                return

    # TODO: Update to new DLL format OR Test to see if it still works
    def display(self, forward=True):
        """Displays all players in the list.
    Args:
        forward:
            - If True, display from head to tail.
            - If False, display from tail to head.
        """
        if self.is_empty:
            print("Player list is empty")
            return

        if forward:
            current = self.__head

            while current is not None:
                print(current)
                current = current.next
        else:
            current = self.__tail

            while current is not None:
                print(current)
                current = current.prev

    # TODO: Update to new DLL format OR Test to see if it still works
    def search(self, key):
        temp = self.__head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
