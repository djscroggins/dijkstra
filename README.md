Implementation of Dijkstra's Algorithm

#### RUN:

\> python dijkstra.py

#### NOTE:

If default system interpreter is Python2, program will throw error.
Python3 should be specified if not system default.

Input files are hard-coded into .py file. Program will execute automatically
only if source files are located in same directory.

#### HEAP IMPLEMENTATION:

The algorithm makes use of Python's default heapq, a minimum priority queue.
For altering heap content, Python's documentation suggests initializing an empty
priority queue and implementing a series of functions based on heappop() and
heappush(), using a dictionary and place-holding variable to track an item that
is being altered.

The documentation can be viewed here:
https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes

My implementation is based on this structure, using the sets module to track
vertices that have been removed and pushing vertices to the heap when first
encountered in the adjacency list. The asymptotic running time is identical
to the in-class algorithm, as heappop() and heappush() both have time complexity
of O(lg n).


#### EXPECTED OUTPUT:

dijkstra(Case1.txt) --> [None, 'A', 'J', 'G', 'F', 'E', 'D', 'H', 'C', 'B']  Length = 142

dijkstra(Case1.txt) --> [None, 'A', 'G', 'E', 'L', 'B']  Length = 45

dijkstra(Case1.txt) --> [None, 'A', 'D', 'H', 'K', 'G', 'Q', 'B']  Length = 214