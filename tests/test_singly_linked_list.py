import lazypye.data_structures.singly_linked_list as linked_list_module
import pytest
from lazypye.data_structures import SinglyLinkedList


def make_list(*values):
    linked = SinglyLinkedList()
    for value in values:
        linked.add_data(value)
    return linked


def displayed_values(linked, capsys):
    linked.display_linkedlist()
    return capsys.readouterr().out


def test_singly_linked_list_is_the_only_public_class():
    assert linked_list_module.__all__ == ["SinglyLinkedList"]
    assert not hasattr(linked_list_module, "Node")
    assert not hasattr(linked_list_module, "SLinkedList")
    assert not hasattr(SinglyLinkedList(), "head")


def test_new_list_is_empty(capsys):
    linked = SinglyLinkedList()

    assert len(linked) == 0
    assert displayed_values(linked, capsys) == "None\n"


def test_add_data_appends_values(capsys):
    linked = make_list(10, 20, 30)

    assert len(linked) == 3
    assert displayed_values(linked, capsys) == "10 → 20 → 30 → None\n"


def test_add_data_accepts_different_value_types():
    linked = make_list(None, "text", {"value": 1})

    assert linked.display_node(0) is None
    assert linked.display_node(1) == "text"
    assert linked.display_node(2) == {"value": 1}


@pytest.mark.parametrize(
    ("position", "data", "expected"),
    [
        (1, 20, (10, 20, 30)),
        (2, 30, (10, 20, 30, 40)),
    ],
)
def test_add_middle_inserts_before_position(position, data, expected):
    starting_values = (10, 30) if position == 1 else (10, 20, 40)
    linked = make_list(*starting_values)

    linked.add_middle(position, data)

    assert len(linked) == len(expected)
    assert tuple(linked.display_node(index) for index in range(len(linked))) == expected


@pytest.mark.parametrize("values", [(), (10,)])
@pytest.mark.parametrize("position", [-1, 0, 1])
def test_add_middle_rejects_lists_without_a_middle(values, position):
    linked = make_list(*values)

    with pytest.raises(IndexError):
        linked.add_middle(position, 99)


@pytest.mark.parametrize("position", [0, 3, 4, -1])
def test_add_middle_rejects_boundaries_and_invalid_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(IndexError):
        linked.add_middle(position, 99)


@pytest.mark.parametrize("position", [1.5, "1", None, True])
def test_add_middle_rejects_non_integer_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(TypeError):
        linked.add_middle(position, 99)


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


def test_delete_first_returns_data_and_preserves_integrity(capsys):
    linked = make_list(10, 20, 30)

    assert linked.delete_first() == 10
    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "20 → 30 → None\n"


def test_delete_first_clears_single_node_list(capsys):
    linked = make_list(10)

    assert linked.delete_first() == 10
    assert len(linked) == 0
    assert displayed_values(linked, capsys) == "None\n"


def test_delete_first_rejects_empty_list():
    with pytest.raises(IndexError, match="empty linked list"):
        SinglyLinkedList().delete_first()


def test_remove_middle_returns_data_and_preserves_integrity(capsys):
    linked = make_list(10, 20, 30, 40)

    assert linked.remove_middle(2) == 30
    assert len(linked) == 3
    assert displayed_values(linked, capsys) == "10 → 20 → 40 → None\n"


@pytest.mark.parametrize("position", [-1, 0, 2, 3])
def test_remove_middle_rejects_boundaries_and_invalid_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(IndexError):
        linked.remove_middle(position)


@pytest.mark.parametrize("values", [(), (10,), (10, 20)])
def test_remove_middle_rejects_lists_without_a_middle(values):
    linked = make_list(*values)

    with pytest.raises(IndexError):
        linked.remove_middle(1)


@pytest.mark.parametrize("position", [1.5, "1", None, True])
def test_remove_middle_rejects_non_integer_positions(position):
    linked = make_list(10, 20, 30)

    with pytest.raises(TypeError):
        linked.remove_middle(position)


def test_delete_last_returns_data_and_preserves_integrity(capsys):
    linked = make_list(10, 20, 30)

    assert linked.delete_last() == 30
    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "10 → 20 → None\n"


def test_delete_last_clears_single_node_list(capsys):
    linked = make_list(10)

    assert linked.delete_last() == 10
    assert len(linked) == 0
    assert displayed_values(linked, capsys) == "None\n"


def test_delete_last_rejects_empty_list():
    with pytest.raises(IndexError, match="empty linked list"):
        SinglyLinkedList().delete_last()


def test_tail_remains_valid_after_delete_and_append(capsys):
    linked = make_list(10, 20)

    linked.delete_last()
    linked.add_data(30)

    assert len(linked) == 2
    assert displayed_values(linked, capsys) == "10 → 30 → None\n"


def test_combined_operations_preserve_order_and_size(capsys):
    linked = make_list(10, 40)
    linked.add_middle(1, 20)
    linked.add_middle(2, 30)
    linked.remove_middle(1)
    linked.delete_first()
    linked.add_data(50)

    assert len(linked) == 3
    assert displayed_values(linked, capsys) == "30 → 40 → 50 → None\n"
