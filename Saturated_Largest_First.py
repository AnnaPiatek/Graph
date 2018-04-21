class Edge:
    def __init__(self,node_0,node_1):
        self.node_0 = Node(node_0)
        self.node_1 = Node(node_1)


class Node:
    def __init__(self,node):
        self.id=node
        self.color=0
        self.degree=0
        self.saturation=0
        self.visited=0
class Graph_0:
    def __init__(self):
        self.list_edges =[]
    def add_edge(self,start,end):
        n = Edge(start,end)
        self.list_edges.append(n)
        return self
    def list_nodes(self):
        list_id=[]
        list=[]
        for i in self.list_edges:
            if i.node_0.id not in list_id:
                list.append(i.node_0)
                list_id.append(i.node_0.id)
            if i.node_1.id not in list_id:
                list.append(i.node_1)
                list_id.append(i.node_1.id)
        return list
    def print_list_edges(self):
        list_e =[]
        for i in range(len(self.list_edges)):
            l=self.list_edges
            list_e.append([l[i].node_0.id,'color',l[i].node_0.color,'degr',l[i].node_0.degree,l[i].node_1.id,'color',l[i].node_1.color],'degr',l[i].node_0.degree])
        print(list_e)
    def print_list_nodes(self):
        list=[]
        for i in self.list_nodes():
            if [i.id,i.color,i.degree] not in list:
                list.append([i.id,'color',i.color,'degr',i.degree,'sat',i.saturation])
        print(list)

    def degree_adding(self):
        for node_obj in self.list_nodes():
            degree = 0
            saturation = 0
            list = []
            for edge in self.list_edges:
                if edge.node_0.id == node_obj.id and edge.node_1 not in list:
                    list.append(edge.node_1)
                    degree = degree + 1
                elif edge.node_1.id == node_obj.id and edge.node_0 not in list:
                    list.append(edge.node_0)
                    degree = degree + 1
            for node in self.list_nodes():
                if node.id == node_obj.id:
                    node.degree = str(degree)
                    break
        return self.print_list_edges()
    def saturation_adding(self):

        for node in self.list_nodes():
            list = []
            saturation=0
            for i in self.list_edges:
                if i.node_0.id==node and i.node_1 not in list:
                    list.append(i.node_1)
                    if i.node_1.color!=0:
                        saturation=saturation+1
                elif i.node_1.id==node and i.node_0 not in list:
                    list.append(i.node_0)
                    if i.node_0.color != 0:
                        saturation = saturation + 1
            node.saturation = saturation

        return self
    def maximum_sat(self):
        self.saturation_adding()
        list=self.bubblesort_degree()
        for i in list:
            if i.visited==0:
                maximum=i
                break
        for i in list:
            if i.saturation>maximum.saturation and i.visited==0:
                maximum=i
        maximum.visited=1
        return maximum

    # def making_friends(self,node):
    #     list=[]
    #     for i in self.list_edges:
    #         if i.node_0.id==node and i.node_1 not in list:
    #             list.append(i.node_1)
    #         elif i.node_1.id==node and i.node_0 not in list:
    #             list.append(i.node_0)
    #     return list

    def swap(self,A,x,y):
        tmp=A[x]
        A[x]=A[y]
        A[y]=tmp
    def bubblesort_degree( self ):
        self.degree_adding()
        list=[]
        '''list_given ~~ self.list_nodes'''
        for i in self.list_nodes():
            list.append(i)
        for i in range( len( list ) ):
            for k in range( len(list ) - 1, i, -1 ):
                if ( list[k].degree > list[k - 1].degree ):
                    self.swap( list, k, k - 1 )
        return list
    # def bubblesort_sat(self,list_given):
    #     self.saturation_adding()
    #     sorted_list=self.bubblesort_degree()
    #     list=[]
    #     for i in sorted_list:
    #         list.append(i)
    #     for i in range(len(list)):
    #         for k in range(len(list) - 1, i, -1):
    #             if (list[k].saturation > list[k - 1].saturation):
    #                 self.swap(list, k, k - 1)
    #     for i in list:
    #         print(i.id,i.degree,i.color)
    #     return list

    def SLF(self):
        list=self.bubblesort_degree()

        for i in list:
            self.saturation_adding()
            node=self.maximum_sat()
            list=[]
            for edge in self.list_edges:
                if edge.node_0.id==node.id and edge.node_1 not in list:
                    list.append(edge.node_1)
                elif edge.node_1.id==node and edge.node_0 not in list:
                    list.append(edge.node_0)
            for k in list:
                if node.color==k.color:
                    node.color=node.color+1
        # self.print_list_nodes()
        return self






if __name__ == "__main__":
    g = Graph_0()
    g.add_edge('A','B')
    g.add_edge('A','E')
    g.add_edge('E','B')
    g.add_edge('E','D')
    g.add_edge('D','C')
    g.add_edge('B','C')
    g.add_edge('B','F')
    g.add_edge('D','F')
    # g.saturation_adding(g.bubblesort_degree())
    g.SLF()
    # g.degree_adding()
    # g.print_list_nodes()    # g.print_list_edges()
    # g.print_list_nodes()
    # g.making_friends('B')
    # print(g.degree_adding())
    # g.maximum_sat()
    # g.saturation_adding()

    # g.print_list_edges()