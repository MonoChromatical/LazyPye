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
def test_insert_middle_inserts_before_position(position, data, expected):
    starting_values = (10, 30) if position == 1 else (10, 20, 40)
    linked = make_list(*starting_values)

    linked.insert_middle(position, data)

    assert len(linked) == len(expected)
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == expected


@pytest.mark.parametrize("values", [(), (10,)])
@pytest.mark.parametrize("position", [-1, 0, 1])
def test_insert_middle_rejects_lists_without_a_middle(values, position):
    linked = make_list(*values)

    with pytest.raises(IndexError):
        linked.insert_middle(position, 99)


@pytest.mark.parametrize("position", [0, 3, 4, -1])
def test_insert_middle_rejects_boundaries_and_invalid_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(IndexError):
        linked.insert_middle(position, 99)


@pytest.mark.parametrize("position", [1.5, "1", None, True])
def test_insert_middle_rejects_non_integer_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(TypeError):
        linked.insert_middle(position, 99)


@pytest.mark.parametrize(
    ("position", "expected"),
    [(0, "first"), (1, "middle"), (2, "last")],
)
def test_display_node_returns_data(position, expected):
    linked = make_list("first", "middle", "last")

    assert linked.display_node(position) == expected


@pytest.mark.parametrize("position", [-1, 3, 100])
def test_display_node_rejects_out_of_range_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(IndexError):
        linked.display_node(position)


@pytest.mark.parametrize("position", [1.5, "1", None, True])
def test_display_node_rejects_non_integer_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(TypeError):
        linked.display_node(position)


def test_display_forward(capsys):
    linked = make_list(10, 20, 30)

    assert displayed_values(linked, capsys) == "10\n20\n30\n"


def test_display_backward(capsys):
    linked = make_list(10, 20, 30)

    assert displayed_values(linked, capsys, forward=False) == "30\n20\n10\n"


def test_delete_head_returns_data_and_preserves_integrity(capsys):
    linked = make_list(10, 20, 30)

    assert linked.delete_head() == 10
    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "20\n30\n"
    assert displayed_values(linked, capsys, forward=False) == "30\n20\n"


def test_delete_head_clears_single_node_list(capsys):
    linked = make_list(10)

    assert linked.delete_head() == 10
    assert len(linked) == 0
    assert linked.is_empty is True
    assert displayed_values(linked, capsys) == "Doubly linked list is empty\n"


def test_delete_head_rejects_empty_list():
    with pytest.raises(IndexError, match="empty linked list"):
        DoublyLinkedList().delete_head()


def test_delete_tail_returns_data_and_preserves_integrity(capsys):
    linked = make_list(10, 20, 30)

    assert linked.delete_tail() == 30
    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "10\n20\n"
    assert displayed_values(linked, capsys, forward=False) == "20\n10\n"


def test_delete_tail_clears_single_node_list(capsys):
    linked = make_list(10)

    assert linked.delete_tail() == 10
    assert len(linked) == 0
    assert linked.is_empty is True
    assert displayed_values(linked, capsys) == "Doubly linked list is empty\n"


def test_delete_tail_rejects_empty_list():
    with pytest.raises(IndexError, match="empty linked list"):
        DoublyLinkedList().delete_tail()


def test_removes_head():
    linked = make_list(10, 20, 30)

    assert linked.remove(10) == 10
    assert len(linked) == 2
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (20, 30)


def test_removes_tail():
    linked = make_list(10, 20, 30)

    assert linked.remove(30) == 30
    assert len(linked) == 2
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (10, 20)


def test_removes_middle():
    linked = make_list(10, 20, 30)

    assert linked.remove(20) == 20
    assert len(linked) == 2
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (10, 30)


def test_remove_removes_first_matching_value():
    linked = make_list(10, 20, 10, 30)

    assert linked.remove(10) == 10
    assert len(linked) == 3
    assert tuple(
        linked.display_node(index)
        for index in range(len(linked))
    ) == (20, 10, 30)


def test_remove_returns_none_when_value_not_found():
    linked = make_list(10, 20, 30)

    assert linked.remove(99) is None
    assert len(linked) == 3


def test_tail_remains_valid_after_delete_and_append(capsys):
    linked = make_list(10, 20)

    linked.delete_tail()
    linked.append(30)

    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "10\n30\n"
    assert displayed_values(linked, capsys, forward=False) == "30\n10\n"


def test_head_remains_valid_after_delete_and_prepend(capsys):
    linked = make_list(20, 30)

    linked.delete_head()
    linked.prepend(10)

    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "10\n30\n"
    assert displayed_values(linked, capsys, forward=False) == "30\n10\n"


def test_combined_operations_preserve_order_and_size(capsys):
    linked = make_list(10, 40)

    linked.insert_middle(1, 20)
    linked.insert_middle(2, 30)
    linked.remove(20)
    linked.delete_head()
    linked.append(50)

    assert len(linked) == 3
    assert displayed_values(linked, capsys) == "30\n40\n50\n"
    assert displayed_values(linked, capsys, forward=False) == "50\n40\n30\n"

