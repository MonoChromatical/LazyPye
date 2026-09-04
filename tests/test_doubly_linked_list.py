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


def test_prepend_adds_values_to_the_beginning():
    linked = DoublyLinkedList()

    linked.prepend(30)
    linked.prepend(20)
    linked.prepend(10)

    assert len(linked) == 3
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (10, 20, 30)


def test_append_accepts_different_value_types():
    linked = make_list(None, "text", {"value": 1})

    assert linked.display_node(0) is None
    assert linked.display_node(1) == "text"
    assert linked.display_node(2) == {"value": 1}


def test_append_and_prepend_preserve_empty_state():
    linked = DoublyLinkedList()

    assert linked.is_empty is True

    linked.append(10)
    assert linked.is_empty is False

    linked.delete_head()
    assert linked.is_empty is True

    linked.prepend(20)
    assert linked.is_empty is False

    linked.delete_tail()
    assert linked.is_empty is True


@pytest.mark.parametrize(
    ("position", "data", "expected"),
    [
        (1, 20, (10, 20, 30)),
        (2, 30, (10, 20, 30, 40)),
    ],
)

