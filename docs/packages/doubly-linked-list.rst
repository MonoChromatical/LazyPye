Doubly linked list
==================

Package information
-------------------

.. code-block:: text

   Distribution:         lazypye-data-structures
   Repository directory: packages/data-structures
   Module:               lazypye.data_structures.doubly_linked_list
   Public import:         lazypye.data_structures.DoublyLinkedList

Installation
------------

Install only the data-structures distribution directly from the repository:

.. code-block:: console

   py -m pip install "git+https://github.com/MonoChromatical/LazyPye.git#subdirectory=packages/data-structures"

For the reusable installation blueprint and the distinction between distribution
names and import paths, see :doc:`../getting-started`.

Import
------

.. code-block:: python

   from lazypye.data_structures import DoublyLinkedList

Description
-----------

A doubly linked list stores values in nodes connected in both directions.
This implementation supports appending and prepending data, inserting values at middle positions,
retrieving data by position, removing values, removing either end, reporting its length, checking
whether it is empty, and displaying values in either direction.

Private node design
-------------------

`DoublyLinkedList` is the only public class. The private `_Node` type, head and tail links,
and node connections are implementation details. Each node stores links to both the next and previous nodes.
Public methods accept and return data rather than exposing mutable node objects, preventing callers from accidentally
corrupting the list connections.

Positions
---------

Positions are zero-based. The first value is at position `0`. `insert_middle()` accepts positions from `1` through
`len(linked) - 1` and inserts before the value currently at that position.
It rejects position `0` and the append position `len(linked)`. Use `prepend()`
to insert at the beginning and `append()` to insert at the end.

Complete example
----------------

.. code-block:: python

    from lazypye.data_structures import DoublyLinkedList

        linked = DoublyLinkedList[int]()
        linked.append(10)
        linked.append(30)
        linked.add_middle(1, 20)
        print(linked.display_node(1))
        linked.display()
        linked.display(forward=False)

.. code-block:: text

   20
   10 → 20 → 30 → None
   30 → 20 → 10 → None # backwards

Public interface
----------------

`DoublyLinkedList()`
~~~~~~~~~~~~~~~~~~~~~~

Creates an empty doubly linked list. An optional type argument can describe its data:

.. code-block:: python

   names = DoublyLinkedList[str]()

`len(linked)`
~~~~~~~~~~~~~~~

Returns the number of stored values.

.. code-block:: python

   linked = DoublyLinkedList[int]()
   linked.append(10)
   print(len(linked))

.. code-block:: text

   1

`is_empty`
~~~~~~~~~~~~

Returns `True` when the list contains no values and `False` otherwise.

.. code-block:: python

    linked = DoublyLinkedList[int]()
    print(linked.is_empty)

.. code-block:: text

    True

`append(data)`
~~~~~~~~~~~~~~~~~~

Appends `data` to the end of the list and returns `None`.

.. code-block:: python

   linked.append(20)
   linked.append(30)

`prepend(data)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prepends `data` to the beginning of the list and returns `None`.

:param position: Integer from `1` through `len(linked) - 1`.
:param data: Value to insert.
:returns: `None`.

.. code-block:: python

   linked = DoublyLinkedList[int]()
   linked.prepend(10)

`insert_middle(position, data)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inserts `data` before the existing value at a middle `position`.

:param position: Integer from `1` through `len(linked) - 1`.
:param data: Value to insert.
:returns: `None`.
:raises TypeError: If `position` is not an integer.
:raises IndexError: If it is zero, an append position, or outside the list.

.. code-block:: python

   linked = DoublyLinkedList[int]()
   linked.append(10)
   linked.append(30)
   linked.insert_middle(1, 20)

`display_node(position)`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the data at `position`, never the private node.

:param position: Zero-based position to retrieve.
:returns: The stored data.
:raises TypeError: If `position` is not an integer.
:raises IndexError: If it is outside the list.

.. code-block:: python

   print(linked.display_node(1))

.. code-block:: text

   20

`display(forward=True)`
~~~~~~~~~~~~~~~~~~~~~~~~

Prints every value in the list.

By default, values are displayed from the head to the tail.
Passing `forward=False` displays values from the tail to the head.

An empty list prints `Doubly linked list is empty`.

:param forward: If `True`, display from head to tail. If `False`, display from tail to head.
:returns: `None`.

.. code-block:: python

   linked.display()
   linked.display(forward=False)

.. code-block:: text

   10
   20
   30
   30
   20
   10

`delete_head()`
~~~~~~~~~~~~~~~~~~

Removes and returns the first value.

:returns: The removed data.
:raises IndexError: If the list is empty.

.. code-block:: python

   first = linked.delete_head()
   print(first)

.. code-block:: text

   10

`remove(data)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Searches for the first matching value, removes it, and returns the removed data.
If the value is not found, `None` is returned.

:param data: Value to search for and remove.
:returns: The removed data, or `None` if the value was not found.

.. code-block:: python

   linked = DoublyLinkedList[int]()
   linked.append(10)
   linked.append(20)
   linked.append(30)
   removed = linked.remove(20)
   print(removed)

.. code-block:: text

   20

`delete_tail()`
~~~~~~~~~~~~~~~~~

Removes and returns the final value.

:returns: The removed data.
:raises IndexError: If the list is empty.

.. code-block:: python

   last = linked.delete_tail()
   print(last)

.. code-block:: text

   30

Edge cases
----------

* Retrieving any position from an empty list raises `IndexError`.
* Removing an end value from an empty list raises `IndexError`.
* Middle insertion requires at least two existing values.
* `insert_middle()` rejects position `0` and position `len(linked)`.
* Negative and out-of-range positions raise `IndexError`.
* Non-integer positions, including booleans, raise `TypeError`.
* `remove()` removes only the first matching value.
* `remove()` returns `None` when the requested value is not present.
* `display()` prints a message when the list is empty.
* `display(forward=False)` traverses the list backwards using the previous node links.

API reference
-------------

See :doc:`../api/doubly-linked-list` for generated signatures and docstrings.
