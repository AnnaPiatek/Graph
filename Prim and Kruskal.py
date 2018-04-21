from graphvizual import *
import graphviz as gv
class Drawing:
    def drawing(self,path):
        Drawing = Graph(format='png')
        list_e=[['E','D',1],['B','C',2],['D','B',3],['C','D',3],['B','E',4],['A','B',5]]
        for item in list_e:
            # print(list_e)
            # node_00 = str(item.node_0.id)
            node_00 = str(item[0])
            node_11 = str(item[1])
            wei = str(item[2])
            Drawing.edge(node_00, node_11, wei, color='black')
        Drawing = apply_styles(Drawing, styles)
        start = Drawing.render(filename=str(10))
        Drawing.render(view=True)
        list=[]
        Drawing = Graph(format='png')
        for i in range(1,len(path)+1):
            Drawing = Graph(format='png')
            list.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in list_e:
                node_00=str(item[0])
                node_11=str(item[1])
                wei=str(item[2])
                if [node_00,node_11,wei] in list:
                    Drawing.edge(node_00, node_11, wei, color='red')
                elif [node_11,node_00,wei] in list:
                    Drawing.edge(node_00,node_11,wei, color='red')
                else:
                    Drawing.edge(node_00,node_11,wei, color='black')

            Drawing = apply_styles(Drawing, styles)
            i=Drawing.render(filename=str(i))
            Drawing.render(view=True)

if __name__ == "__main__":
    g = Graph_0()
    d = Drawing()
    g.add_edge('A', 'B', 5)
    g.add_edge('B', 'E', 4)
    g.add_edge('E', 'D', 1)
    g.add_edge('D', 'B', 3)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'D', 3)
    g.add_edge('C', 'A', 6)
    '''Prim'''
    # print(g.path_building('D'))
    # print(d.drawing(g.path_building('D')[0]))
    '''Kruskal'''
    print(g.branches_building())
    print(d.drawing(g.branches_building()))
    # print(g.print_list_edges())


