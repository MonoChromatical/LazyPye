import lazypye.data_structures.doubly_linked_list as linked_list_module
import pytest

from lazypye.data_structures import DoublyLinkedList


def make_list(*values):
    linked = DoublyLinkedList()
    for value in values:
        linked.append(value)
    return linked


def displayed_values(linked, capsys, forward=True):
    linked.display(forward)
    return capsys.readouterr().out

def test_doubly_linked_list_is_the_only_public_class():
    assert linked_list_module.__all__ == ["DoublyLinkedList"]
    assert not hasattr(linked_list_module, "Node")
    assert not hasattr(linked_list_module, "DLinkedList")
    assert not hasattr(DoublyLinkedList(), "head")
    assert not hasattr(DoublyLinkedList(), "tail")


def test_new_list_is_empty(capsys):
    linked = DoublyLinkedList()

    assert len(linked) == 0
    assert linked.is_empty is True
    assert displayed_values(linked, capsys) == "Doubly linked list is empty\n"


def test_append_adds_values_to_the_end():
    linked = make_list(10, 20, 30)

    assert len(linked) == 3
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (10, 20, 30)


