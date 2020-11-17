import csv
import itertools
from itertools import chain


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:3d}'.format(val), end='')
            print('\n')


def compute_Q(m, graph):
    Q = 1/(2*m)
    return 0


def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


def pop_input(graph):
    s1 = []
    s2 = []
    for i in range(35):
        for j in range(i, 35):
            if graph[i][j] == 1:
                s1.append(i)
                s1.append(j)
                s2.append(s1)
                s1 = []

    print(s2)

    #print(Union(s2[0], s2[1]))

    for i in s2:
        for j in s2:
            uni = Union(i, j)
            uni.sort()
            if uni not in s2:
                s2.append(uni)

    print(s2)

    print('length:', len(s2))


def genetic_alg(graph):
    return 0


if __name__ == "__main__":
    g = Graph(35)

    with open('karate.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)

        for row in rows:
            #print(int(row[0]), int(row[1]))
            g.add_edge(int(row[0]), int(row[1]))

    # g.print_matrix()

    m = 78  # the network's total edges

    graph = g.adjMatrix
    pop_input(graph)
