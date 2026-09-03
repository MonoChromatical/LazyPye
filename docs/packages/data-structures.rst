Singly linked list
==================

Package information
-------------------

.. code-block:: text

   Distribution:         lazypye-data-structures
   Repository directory: packages/data-structures
   Module:               lazypye.data_structures.singly_linked_list
   Public import:         lazypye.data_structures.SinglyLinkedList

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

   from lazypye.data_structures import SinglyLinkedList

Description
-----------

A singly linked list stores values in nodes connected in one direction. This
implementation supports appending data, inserting and removing middle values,
retrieving data by position, removing either end, reporting its length, and
displaying all stored values.

Private node design
-------------------

`SinglyLinkedList` is the only public class. The private `_Node` type, head
and tail links, and node connections are implementation details. Public methods
accept and return data, preventing callers from accidentally corrupting links.

Positions
---------

Positions are zero-based. The first value is at position `0`.

`add_middle()` accepts positions from `1` through `len(linked) - 1` and
inserts before the value currently at that position. It rejects position `0`
and the append position `len(linked)`.

`remove_middle()` accepts positions from `1` through `len(linked) - 2`.
Use `delete_first()` or `delete_last()` for boundary removal.

Complete example
----------------

.. code-block:: python

   from lazypye.data_structures import SinglyLinkedList

   linked = SinglyLinkedList[int]()
   linked.add_data(10)
   linked.add_data(30)
   linked.add_middle(1, 20)

   print(linked.display_node(1))
   linked.display_linkedlist()

.. code-block:: text

   20
   10 → 20 → 30 → None

Public interface
----------------

`SinglyLinkedList()`
~~~~~~~~~~~~~~~~~~~~~~

Creates an empty linked list. An optional type argument can describe its data:

.. code-block:: python

   names = SinglyLinkedList[str]()

`len(linked)`
~~~~~~~~~~~~~~~

Returns the number of stored values.

.. code-block:: python

   linked = SinglyLinkedList[int]()
   linked.add_data(10)
   print(len(linked))

.. code-block:: text

   1

`add_data(data)`
~~~~~~~~~~~~~~~~~~

Appends `data` to the end of the list and returns `None`.

.. code-block:: python

   linked.add_data(20)
   linked.add_data(30)

`add_middle(position, data)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inserts `data` before the existing value at a middle `position`.

:param position: Integer from `1` through `len(linked) - 1`.
:param data: Value to insert.
:returns: `None`.
:raises TypeError: If `position` is not an integer.
:raises IndexError: If it is zero, an append position, or outside the list.

.. code-block:: python

   linked = SinglyLinkedList[int]()
   linked.add_data(10)
   linked.add_data(30)
   linked.add_middle(1, 20)

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

`display_linkedlist()`
~~~~~~~~~~~~~~~~~~~~~~~~

Prints every value in order followed by `None`. An empty list prints `None`.

:returns: `None`.

.. code-block:: python

   linked.display_linkedlist()

.. code-block:: text

   10 → 20 → 30 → None

`delete_first()`
~~~~~~~~~~~~~~~~~~

Removes and returns the first value.

:returns: The removed data.
:raises IndexError: If the list is empty.

.. code-block:: python

   first = linked.delete_first()
   print(first)

.. code-block:: text

   10

`remove_middle(position)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Removes and returns data at a non-boundary `position`.

:param position: Integer from `1` through `len(linked) - 2`.
:returns: The removed data.
:raises TypeError: If `position` is not an integer.
:raises IndexError: If it is a boundary, outside the list, or no middle exists.

.. code-block:: python

   linked = SinglyLinkedList[int]()
   linked.add_data(10)
   linked.add_data(20)
   linked.add_data(30)
   removed = linked.remove_middle(1)
   print(removed)

.. code-block:: text

   20

`delete_last()`
~~~~~~~~~~~~~~~~~

Removes and returns the final value.

:returns: The removed data.
:raises IndexError: If the list is empty.

.. code-block:: python

   last = linked.delete_last()
   print(last)

.. code-block:: text

   30

Edge cases
----------

* Retrieving any position from an empty list raises `IndexError`.
* Removing an end value from an empty list raises `IndexError`.
* Middle insertion requires at least two existing values.
* Middle removal requires at least three existing values.
* Negative and out-of-range positions raise `IndexError`.
* Non-integer positions, including booleans, raise `TypeError`.

API reference
-------------

See :doc:`../api/data-structures` for generated signatures and docstrings.
