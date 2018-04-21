#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Edge:
    def __init__(self,node_0,node_1,weight):
        self.node_0 = Node(node_0)
        self.node_1 = Node(node_1)
        self.node_0.friend.append(node_1)
        self.weight= weight

class Node:
    def __init__(self,node):
        self.id=node
        self.color=node
        self.friend=[]

class Graph_0:
    def __init__(self):
        self.list_edges =[]

    def list_nodes(self,list_edges):
        list=[]
        for i in range(0,len(list_edges)):
            if list_edges[i].node_0.id not in list:
                list.append(list_edges[i].node_0.id)
            if list_edges[i].node_1.id not in list:
                list.append(list_edges[i].node_1.id)
        return list

    def making_friends(self,node):
        list=[]
        for i in range(0,len(self.list_edges)):
            if self.list_edges[i].node_0.id==node:
                # list.append([,self.list_edges[i].node_1.id,self.list_edges[i].weight])
                list.append([self.list_edges[i].node_0.id, self.list_edges[i].node_1.id, self.list_edges[i].weight])
            elif self.list_edges[i].node_1.id==node:
                # list.append([self.list_edges[i].node_0.id,self.list_edges[i].weight])
                list.append([self.list_edges[i].node_1.id,self.list_edges[i].node_0.id,self.list_edges[i].weight])
        return list


    def delete_edge(self,list_edges,start,end,weight):
        for i in range (0,len(list_edges)):
            if list_edges[i].node_0.id==start and list_edges[i].node_1.id==end and list_edges[i].weight==weight:
                list_edges.remove(list_edges[i])
                break
            elif list_edges[i].node_1.id==start and list_edges[i].node_0.id==end and list_edges[i].weight==weight:
                 list_edges.remove(list_edges[i])
                 break
        return list_edges

    def delete_node(self,list_edges,n):
        list_nodes = g.list_nodes(list_edges)
        leng=len(list_edges)
        try:
            for i in range (0,leng+1):
                if list_edges[i].node_0.id==n:
                    list_edges.remove(list_edges[i])


                elif list_edges[i].node_1.id==n:
                    list_edges.remove(list_edges[i])
        except IndexError:
            pass
        return list_edges

    def add_edge(self,start,end,weight):
        # self.nodes(start, end)
        n = Edge(start,end,weight)
        self.list_edges.append(n)
        self.buble_sort()
        return self

    def buble_sort(self):
        length = len(self.list_edges) - 1
        sorted = False
        while not sorted:
            sorted = True
            for element in range(0, length):
                if self.list_edges[element].weight > self.list_edges[element + 1].weight:
                    sorted = False
                    hold = self.list_edges[element + 1]
                    self.list_edges[element + 1] = self.list_edges[element]
                    self.list_edges[element] = hold
        return self

    def print_list_edges(self):
        list_e =[]
        for i in range(len(self.list_edges)):
            l=self.list_edges
            list_e.append([l[i].node_0.id,l[i].node_1.id,l[i].weight])
        print(list_e)

    def branches_building(self):
        forest=[]
        list=self.list_edges
        node_0=list[0]
        brancher=[]
        for item in self.list_nodes(self.list_edges):
            forest.append(set(item))
        while list:

            for edge in list:

                for tree in forest:
                    if (set(edge.node_0.id)).issubset(tree):
                        index_0=forest.index(tree)
                    if (set(edge.node_1.id)).issubset(tree):
                        index_1=forest.index(tree)

                if index_1!=index_0:
                    forest[index_0].update(forest[index_1])
                    forest.remove(forest[index_1])
                    brancher.append([edge.node_0.id,edge.node_1.id,edge.weight])
            edger = edge
            list.remove(edger)
            return brancher


    def sort_friends(self,friends):
        length = len(friends) - 1
        sorted = False
        while not sorted:
            sorted = True
            for element in range(0, length):
                # if friends[element][1] > friends[element + 1][1]:
                if friends[element][2] > friends[element + 1][2]:
                    sorted = False
                    hold = friends[element + 1]
                    friends[element + 1] = friends[element]
                    friends[element] = hold
        return friends

    def path_building(self,node_s):
        friends = []
        list = [node_s]
        path = []
        w = 0
        while len(list) != len(self.list_nodes(self.list_edges)):
            if list == [node_s]:
                node_0 = node_s
            else:
                node_0 = path[len(path) - 1][1]
            for item in self.sort_friends(self.making_friends(node_0)):
                if item not in friends and [item[1], item[0], item[2]] not in friends:
                    friends.append(item)
                    friends = self.sort_friends(friends)
            for i in range(0, len(friends) - 1):
                if friends[i][1] not in list:
                    path.append([friends[i][0], friends[i][1], friends[i][2]])
                    list.append(friends[i][1])
                    break
        for item in path:
            w = w + item[2]
        return path, w

# if __name__ == "__main__":
#     g = Graph_0()
#     g.add_edge('A','B',5)
#     g.add_edge('B','E',4)
#     g.add_edge('E','D',1)
#     g.add_edge('D','B',3)
#     g.add_edge('B','C',2)
#     g.add_edge('C','D',3)
#     g.add_edge('C','A',6)
