import csv
import itertools
from itertools import chain
import random
import numpy as np


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
    '''
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:3d}'.format(val), end='')
            print('\n')
    '''


def find_deg(graph, vertex):
    count = 0
    for i in range(34):
        if graph[vertex-1][i] == 1:
            count = count + 1

    return count


def is_cluster(s_i, s_j, groups):
    indices = {}
    for i, group in enumerate(groups):
        for num in group:
            indices.setdefault(num, set()).add(i)

    if indices.get(s_i, set()) & indices.get(s_j, set()) == {0}:
        return 1
    else:
        return 0

# modularity: objective function


def compute_Q(m, graph, groups):  # m is the total numbers of edges
    total = 0
    for i in range(8):
        for j in range(8):
            delta = is_cluster(i, j, groups)
            total = total + \
                (graph[i][j]-(find_deg(graph, i)*find_deg(graph, j)/(2*m)))*delta
    Q = 1/(2*m)*total
    return abs(Q)


def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


def pop_input(n):
    max_len = 17  # the number of members in a community must be less than 50% of the total number of nodes
    return 0


def roul_wheel(pop, ps, mps, sur_pts):
    A = []
    matepool = []
    return 0


def genetic_alg(graph):

    return 0


if __name__ == "__main__":
    g = Graph(35)

    with open('karate.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)

        for row in rows:
            # print(int(row[0]), int(row[1]))
            g.add_edge(int(row[0]), int(row[1]))

    # g.print_matrix()

    m = 78  # the network's total edges

    graph1 = np.delete(g.adjMatrix, 0, 0)
    graph = np.delete(graph1, 0, 1)

    # print(find_deg(graph, 3))
    graph_pop = pop_input(graph)
    # print(graph_pop)
    # print(graph_pop[1])

    s1 = [1, 2, 3, 4, 8, 9, 13, 15, 14, 16, 18, 19, 20,
          21, 22, 24, 23, 27, 28, 30, 33, 32, 29, 34, 31]
    s2 = [1, 5, 7, 6, 11, 17]
    s3 = [32, 25, 26]

    groups = [s1, s2, s3]

    print(compute_Q(m, graph, groups))

    a1 = []
    a2 = []*3
    for i in range(34):
        for j in range(i, 35):
            if g.adjMatrix[i][j] == 1:
                a1.append(i)
                a1.append(j)
                a2.append(a1)
                a1 = []

    # print(a2)

    #print(Union(s2[0], s2[1]))
    a = len(a2)
    count = 0
    # print(a)

    for i in a2:
        for j in a2:
            uni = Union(i, j)
            uni.sort()
            if uni not in a2 and len(uni) <= 17:
                a2.append(uni)
                count = count + 1
                print(count)
    print(count+a)
