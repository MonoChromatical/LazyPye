from dataclasses import dataclass
from typing import Generic, TypeVar

__all__ = ["SinglyLinkedList"]

T = TypeVar("T")


@dataclass(slots=True)
class _Node(Generic[T]):
    """Store the internal state for one linked-list node."""

    data: T
    next: "_Node[T] | None" = None


class SinglyLinkedList(Generic[T]):
    """Store values in nodes connected in one direction.

    Nodes and list pointers are private implementation details. Public methods
    accept zero-based positions and return stored data rather than exposing
    mutable node objects.
    """

    def __init__(self):
        """Create an empty singly linked list."""

        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0

    def __len__(self) -> int:
        """Return the number of values in the list."""

        return self._size

    def add_data(self, data: T) -> None:
        """Append data to the end of the list.

        Args:
            data: Value to store in the new tail node.
        """

        new_node = _Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def add_middle(self, position: int, data: T) -> None:
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

        previous = self._node_at(position - 1)
        previous.next = _Node(data, previous.next)
        self._size += 1

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

    def display_linkedlist(self) -> None:
        """Print all stored values from first to last."""

        current = self._head

        while current is not None:
            print(current.data, end=" \u2192 ")
            current = current.next

        print("None")

    def delete_first(self) -> T:
        """Remove and return the first value.

        Returns:
            The data previously stored at the beginning of the list.

        Raises:
            IndexError: If the list is empty.
        """

        if self._head is None:
            raise IndexError("delete from empty linked list")

        removed = self._head
        self._head = removed.next
        self._size -= 1

        if self._head is None:
            self._tail = None

        return removed.data

    def remove_middle(self, position: int) -> T:
        """Remove and return data from a middle position.

        Args:
            position: Zero-based position to remove. It must be greater than
                zero and less than the final position.

        Returns:
            The removed data.

        Raises:
            TypeError: If position is not an integer.
            IndexError: If position refers to the first or last node, or lies
                outside the list.
        """

        self._validate_middle_removal_position(position)

        previous = self._node_at(position - 1)
        removed = previous.next
        previous.next = removed.next
        self._size -= 1
        return removed.data

    def delete_last(self) -> T:
        """Remove and return the final value.

        Returns:
            The data previously stored at the end of the list.

        Raises:
            IndexError: If the list is empty.
        """

        if self._head is None:
            raise IndexError("delete from empty linked list")

        if self._head.next is None:
            removed_data = self._head.data
            self._head = None
            self._tail = None
            self._size = 0
            return removed_data

        previous = self._head
        while previous.next is not self._tail:
            previous = previous.next

        removed_data = self._tail.data
        previous.next = None
        self._tail = previous
        self._size -= 1
        return removed_data

    def _node_at(self, position: int) -> _Node[T]:
        """Return the private node at position."""

        self._validate_position(position)

        current = self._head
        for _ in range(position):
            current = current.next

        return current

    def _validate_position(self, position: int) -> None:
        """Validate a position that may address any node."""

        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError("position must be an integer")

        if position < 0 or position >= self._size:
            raise IndexError("linked list position out of range")

    def _validate_middle_insertion_position(self, position: int) -> None:
        """Validate a position strictly after the start and before the end."""

        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError("position must be an integer")

        if position <= 0 or position >= self._size:
            raise IndexError(
                "middle insertion position must be between the first and last nodes"
            )

    def _validate_middle_removal_position(self, position: int) -> None:
        """Validate a position that excludes the first and last nodes."""

        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError("position must be an integer")

        if position <= 0 or position >= self._size - 1:
            raise IndexError(
                "middle removal position must be between the first and last nodes"
            )
