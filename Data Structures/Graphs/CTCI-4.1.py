"""
GRAPHS

a tree is a type of graph but not all graphs are trees
A tree is a connected graph without cycles
a graph is a tree that may contain cycles

A graph is a connection of nodes with edges between them
graphs can be directed or undirected
directed edges are like a one way street and undirected
are like a two way street

a graph can consist of multiple isolate subgraphs
if there is a path between every pair of vertices, its called a connected
graph

a graph can have cycles or not.
An acylcic graph is one without cycles

REPRESENTATION
Adjacency list or Adjancy Matrix

AL is the most common way to represent a graph
each vertex(node) stores list of adjacent vertices it touches
In an undirected graph, edge (a,b) would be stored twice
    once in a's adjacent vertices and once in b's adjacent vertices


class def for graph node would look the same as a tree node

class Graph{
    public Node[] nodes
}
class Node{
    public string name
    public Node[] children
}



"""

"""


Route between nodes
"""