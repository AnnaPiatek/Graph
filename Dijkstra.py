import graphviz as gv
from graphvizual import *

class Edge:
    def __init__(self,node_0,node_1,weight):
        self.node_0 = node_0
        self.node_1 = node_1
        self.weight= weight

class Graph_0:
    def __init__(self):
        self.list_edges =[]

    def add_edge(self,start,end,weight):
        self.list_edges.append(Edge(start,end,weight))
        self.buble_sort()
        return self

    def list_nodes(self):
        list=[]
        for i in self.list_edges:
            if i.node_0 not in list:
                list.append(i.node_0)
            if i.node_1 not in list:
                list.append(i.node_1)
        return list

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

    def making_friends(self,node):
        list=[]
        for i in self.list_edges:
            if i.node_0==node:
                list.append(i)
        return list

    def print_list_edges(self):
        list_e=[]
        for i in self.list_edges:
            list_e.append([i.node_0,i.node_1,i.weight])
        print(list_e)

    def sort_friends(self,friends):
        length = len(friends) - 1
        sorted = False
        while not sorted:
            sorted = True
            for element in range(0,length):
                # if friends[element][1] > friends[element + 1][1]:
                if friends[element].weight > friends[element + 1].weight:
                    sorted = False
                    hold = friends[element + 1]
                    friends[element + 1] = friends[element]
                    friends[element] = hold
        return friends

    def creating_antecendents(self):
        antecendents = {}
        for i in self.list_nodes():
            antecendents[str(i)]=0
        return(antecendents)

    def nodes_values(self):
        nodes_values = {}
        for i in self.list_nodes():
            nodes_values[str(i)] = 100
        return (nodes_values)

    def dijkstra_alg(self,node_start,node_end):
        nodes_values=self.nodes_values()
        antecendents=self.creating_antecendents()
        nodes_values[node_start]=0
        list_visited_nodes=[str(node_start)]
        list_visited_edges=[]
        friends=[]
        roar=1
        while roar!=20:
            for k in list_visited_nodes:
                if roar==20:
                    break
                friends_i=self.making_friends(k)
                for i in friends_i:
                    if i.weight+nodes_values[str(i.node_0)]<nodes_values[str(i.node_1)]:
                        nodes_values[i.node_1]=nodes_values[i.node_0]+i.weight
                        antecendents[i.node_1]=i.node_0

                for i in friends_i:
                    if i not in friends:
                        friends.append(i)
                        self.sort_friends(friends)
                for k in friends:
                    if k not in list_visited_edges and k.node_1 not in list_visited_nodes and k.node_0 !=node_end:
                        list_visited_edges.append(k)
                        if k.node_0 not in list_visited_nodes:
                            list_visited_nodes.append(k.node_0)
                            if k.node_0==node_end:
                                roar=20
                                break
                        if k.node_1 not in list_visited_nodes:
                            list_visited_nodes.append(k.node_1)
                            if k.node_1==node_end:
                                roar=20
                                break

        node=node_end
        path_d=[]
        while antecendents[node] != 0:
            # path_d.append(antecendents[node])
            node_ant=antecendents[node]
            # node=antecendents[node]
        # path_visible=[]
            for i in list_visited_edges:
                if i.node_0==node_ant and i.node_1==node:
                    # path_d.append([i.node_0,i.node_1,i.weight])
                    path_d.insert(0,[i.node_0,i.node_1,i.weight])
                    break
            node=node_ant
        # for i in list_visited_edges:
        #     path_visible.append([i.node_0,i.node_1,i.weight])
        # path_visible.append(nodes_values[node_end])


        return path_d

    def drawing(self,path):
        Drawing = gv.Digraph(format='png')
        list_e = [['B', 'C', 1], ['C', 'E', 1], ['E', 'A', 2], ['A', 'B', 3], ['D', 'E', 3], ['A', 'D', 3], ['C', 'D', 5], ['B', 'D', 6]]
        for item in list_e:
            node_00 = str(item[0])
            node_11 = str(item[1])
            wei = str(item[2])
            Drawing.edge(node_00, node_11, wei, color='black')
        Drawing = apply_styles(Drawing, styles)
        start = Drawing.render(filename=str(10))
        Drawing.render(view=True)
        list = []
        Drawing = Graph(format='png')
        for i in range(1, len(path) + 1):
            print(path)
            Drawing = gv.Digraph(format='png')
            list.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in list_e:
                node_00 = str(item[0])
                node_11 = str(item[1])
                wei = str(item[2])
                if [node_00, node_11, wei] in list:
                    Drawing.edge(node_00, node_11, wei, color='red')
                elif [node_11, node_00, wei] in list:
                    Drawing.edge(node_00, node_11, wei, color='red')
                else:
                    Drawing.edge(node_00, node_11, wei, color='black')

            Drawing = apply_styles(Drawing, styles)
            i = Drawing.render(filename=str(i))
            Drawing.render(view=True)

if __name__ == "__main__":
    d=Graph_0()
    d.add_edge('A', 'B', 3)
    d.add_edge('B', 'C', 1)
    d.add_edge('B', 'D', 6)
    d.add_edge('C', 'E', 1)
    d.add_edge('C', 'D', 5)
    d.add_edge('D', 'E', 3)
    d.add_edge('E', 'A', 2)
    d.add_edge('A', 'D', 3)
    # print(d.dijkstra_alg('C','B'))
    path=d.dijkstra_alg('C','B')
    d.drawing(path)
    # print(d.list_nodes())
