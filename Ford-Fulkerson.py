import graphviz as gv
from graphvizual import *

class Edge:
    def __init__(self,node_0,node_1,capacity):
        self.node_0 = node_0
        self.node_1 = node_1
        self.capacity = capacity
        self.flow=0

class Graph_0:
    def __init__(self):
        self.list_edges = []
        self.max_flow=0

    def add_edge(self,start,end,capacity):
        self.list_edges.append(Edge(start,end,capacity))
        return self

    def list_nodes(self):
        list=[]
        for i in self.list_edges:
            if i.node_0 not in list:
                list.append(i.node_0)
            if i.node_1 not in list:
                list.append(i.node_1)
        return list
    def making_friends(self,node):
        list=[]
        for i in self.list_edges:
            if i.node_0==node:
                list.append(i)
        return list
    def print_list_edges(self):
        list_e=[]
        for i in self.list_edges:
            list_e.append([i.node_0,i.node_1,i.flow,i.capacity])
        return(list_e)
    def creating_antecendents(self):
        antecendents = {}
        for i in self.list_nodes():
            antecendents[str(i)]=0
        return(antecendents)

    def find_path(self,node_start,node_end):
        antecendents = self.creating_antecendents()
        list_visited_nodes = [str(node_start)]
        list_visited_edges = []
        friends = []
        roar = 1
        while roar != 20:
            for k in list_visited_nodes:
                if roar == 20:
                    break
                friends_i = self.making_friends(k)
                for i in friends_i:
                        if i.capacity!=i.flow:
                            antecendents[i.node_1] = i.node_0

                for i in friends_i:
                    if i not in friends:
                        friends.append(i)
                for k in friends:
                    if k not in list_visited_edges and k.node_1 not in list_visited_nodes and k.node_0 != node_end and k.capacity!=k.flow:
                        list_visited_edges.append(k)
                        if k.node_0 not in list_visited_nodes:
                            list_visited_nodes.append(k.node_0)
                            if k.node_0 == node_end:
                                roar = 20
                                break
                        if k.node_1 not in list_visited_nodes:
                            list_visited_nodes.append(k.node_1)
                            if k.node_1 == node_end:
                                roar = 20
                                break

        node = node_end
        path_d = []
        node_ant = antecendents[node]
        end=0
        while node_ant != 0:

            for i in self.list_edges:
                if i.node_1==node and i.node_0==node_ant:
                    path_d.insert(0,i)
                    node=i.node_0
                    node_ant=antecendents[node]
        max_flow=0
        minimum=path_d[0]
        for i in path_d:
            if (i.capacity-i.flow)<(minimum.capacity-minimum.flow):
                minimum=i
        minn=minimum.capacity-minimum.flow
        max_flow=max_flow+minn
        # Graph_0().max_flow=max_flow+Graph_0().max_flow

        # print(max_flow)# print(min)
        final_path=[]
        for i in path_d:
            i.flow=i.flow+minn
            # print([i.node_0,i.node_1,i.flow,i.capacity])
            final_path.append([i.node_0,i.node_1,i.flow,i.capacity])
            # print(list_visited_nodes)
        list_visited_nodes=[]
        list_visited_edges=[]
        antecendents=self.creating_antecendents()
        end=0
        path_d=[]
        # prin(max_flow)
        # maxx=Graph_0Graph_0().max_flow().max_flow
        # Graph_0().max_flow=maxx+ max_flow
        # print(Graph_0().max_flow)
        # print(Graph_0.max_flow)

        return [final_path,max_flow]


    def list_nodes(self):
        list_nodes=[]
        visited_nodes=[]
        for i in self.list_edges:
            if i.node_0 not in visited_nodes:
                list_nodes.append(i.node_0)
                visited_nodes.append(i.node_0)
            elif i.node_1 not in visited_nodes:
                list_nodes.append(i.node_1)
                visited_nodes.append(i.node_1)
        return list_nodes


    # def drawing(self,path):
    #     Drawing = gv.Digraph(format='png')
    #     list_e = self.print_list_edges()
    #     for item in list_e:
    #         node_00 = str(item[0])
    #         node_11 = str(item[1])
    #         flow = 0
    #         capacity=str(item[3])
    #         obj='%s/%s'%(flow,capacity)
    #         Drawing.edge(node_00, node_11,obj, color='black')
    #     Drawing = apply_styles(Drawing, styles)
    #     start = Drawing.render(filename=str(0))
    #     Drawing.render(view=True)
    #     list = []
    #     Drawing = Graph(format='png`')
    #     for k in range(0,3):
    #         Drawing = gv.Digraph(format='png')
    #         for i in range(0,len(path[k][0]):
    #             list.append([str(path[k][i][0]), str(path[k][i][1]), str(path[k][i][2]),str(path[k][i][3])])
    #         for item in list_e:
    #             node_00 = str(item[0])
    #             node_11 = str(item[1])
    #             flow = str(item[2])
    #             capacity=str(item[3])
    #             obj = '%s/%s' % (flow, capacity)
    #             if [node_00, node_11, flow,capacity] in list:
    #                 Drawing.edge(node_00, node_11, obj, color='red')
    #             elif [node_11, node_00, flow,capacity] in list:
    #                 Drawing.edge(node_00, node_11, obj, color='red')
    #             else:
    #                 Drawing.edge(node_00, node_11, obj, color='black')
    #         Drawing = apply_styles(Drawing, styles)
    #         i = Drawing.render(filename=str(i))
    #         Drawing.render(view=True)
    #     return maximax






if __name__ == "__main__":
    # d = Graph_0()
    # d.add_edge('Start', 'A', 9)
    # d.add_edge('Start', 'B', 9)
    # d.add_edge('A', 'B', 10)
    # d.add_edge('A', 'C', 8)
    # d.add_edge('B', 'C', 1)
    # d.add_edge('B', 'D', 3)
    # d.add_edge('D', 'C', 8)
    # d.add_edge('C', 'Sink', 10)
    # d.add_edge('D', 'Sink', 7)
    d = Graph_0()
    d.add_edge('Start', 'B', 5)
    d.add_edge('Start', 'C', 4)
    d.add_edge('C', 'B', 6)
    d.add_edge('B', 'E', 4)
    d.add_edge('C', 'E', 4)
    d.add_edge('E', 'Sink', 7)
    d.add_edge('C', 'Sink', 4)
    # max_flow = 0
    # styles['graph']['label'] = 'minimum = %s maximum flow = %s' % (min,
    # d.drawing(d.find_path('Start','Sink'))
    to_draw=[]
    sum=0
    max_flow=[]
    for i in range (0,3):
        to_draw.append((d.find_path('Start','Sink')))
        sum=sum+to_draw[i][1]
        max_flow.append(sum)

    Drawing = gv.Digraph(format='png')
    for i in range(0,len(d.print_list_edges())):
        Drawing.edge(str(d.print_list_edges()[i][0]),str(d.print_list_edges()[i][1]), '0/%s'%(str(d.print_list_edges()[i][3])), color='black')
    Drawing = apply_styles(Drawing, styles)
    # Drawing.render(view=True,filename=str(0))
    new_path=[[]]
    a=0
    for i in to_draw:
        for k in i[0]:
            new_path[a].append([k[0],k[1]])
        new_path.append([])
        a=a+1

    # print(d.print_list_edges())
    edges_path=[]
    for i in d.print_list_edges():
        edges_path.append([i[0],i[1]])

    def find_edge(edge,number_of_path):

        for i in to_draw[number_of_path][0]:
            if edge[0] == i[0] and edge[1] == i[1]:
                new_edge = i
                return (new_edge)


    def find_in_list(edge):
        for i in d.print_list_edges():
            if edge[0] == i[0] and edge[1] == i[1]:
                return i


    # print(find_in_list(['D', 'C'])
    # print(d.print_list_edges())

    number_of_path=-1
    number_of_edge=-1
    lol=1

    for found_path in new_path[0:3]:
        number_of_path=number_of_path+1
        number_of_edge=-1
        list=[]
        for found_edge in found_path:
            # number_of_edge = number_of_edge + 1
            # print(found_edge,number_of_edge)
            list.append(found_edge)

        lol=0
        # print(to_draw)
        for found_edge in found_path:

            number_of_edge = number_of_edge + 1
            minimum=to_draw[number_of_path][1]

            Drawing = gv.Digraph(format='png')
            Drawing = apply_styles(Drawing, styles)
            styles['graph']['label'] =str('minimum %s,max flow %s'%(minimum,max_flow[number_of_path]))
            # print(styles['graph']['label'])
            for edge in edges_path:
                # flow = to_draw[number_of_path][0][number_of_edge][2]
                # capacity = to_draw[number_of_path][0][number_of_edge][3]
                # wei = str('%s/%s' % (flow, capacity))

                if edge in list:
                    new_edge=find_edge(edge,number_of_path)
                    wei=str('%s/%s'%(str(new_edge[2]),str(new_edge[3])))
                    Drawing.edge(new_edge[0], new_edge[1],wei, color='red')

                else:
                    if number_of_path==0:
                        new_edge=find_in_list(edge)
                        # print(new_edge)
                        wei=str('0/%s'%(new_edge[3]))
                        # print(wei)
                        Drawing.edge(edge[0], edge[1], wei, color='black')
                    if number_of_path==1:
                        if find_edge(edge,number_of_path-1)!=None:
                            new_edge=find_edge(edge,number_of_path-1)
                            wei=str('%s/%s'%(new_edge[2],new_edge[3]))
                            Drawing.edge(edge[0], edge[1], wei, color='black')
                        else:
                            new_edge = find_in_list(edge)
                            wei = str('%s/%s'%(new_edge[2],new_edge[3]))
                            Drawing.edge(edge[0], edge[1], wei, color='black')
                    if number_of_path==2:
                        if find_edge(edge,number_of_path-1)!=None:
                            new_edge=find_edge(edge,number_of_path-1)
                            wei=str('%s/%s'%(new_edge[2],new_edge[3]))
                            Drawing.edge(edge[0], edge[1], wei, color='black')
                        elif find_edge(edge,number_of_path-2)!=None:
                            new_edge=find_edge(edge,number_of_path-2)
                            wei=str('%s/%s'%(new_edge[2],new_edge[3]))
                            Drawing.edge(edge[0], edge[1], wei, color='black')
                        else:
                            new_edge = find_in_list(edge)
                            wei = str('%s/%s'%(new_edge[2],new_edge[3]))
                            Drawing.edge(edge[0], edge[1], wei, color='black')

        Drawing.render(view=True,filename=str(lol))
        lol=lol+1
            # print(styles['graph']['label']=)
    print(to_draw)

