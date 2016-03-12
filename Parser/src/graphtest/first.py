'''
Created on 11 mrt. 2016

@author: jeroenbruijning
'''
from igraph import *

# g = Graph()
# 
# g.add_vertices(3)
# g.add_edges([(0,1), (1,2)])
# g.add_edges([(2,0)])
# g.add_vertices(3)
# g.add_edges([(2,3),(3,4),(4,5),(5,3)])
# print(g)

g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
print(g)
print(g.vs[0].attributes())

layout = g.layout('kk')

color_dict = {"m": "blue", "f": "pink"}
# plot(g, layout = layout, vertex_color = [color_dict[gender] for gender in g.vs["gender"]])
visual_style = {}
visual_style["vertex_size"] = 20
visual_style["vertex_label_dist"] = 2
visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
visual_style["vertex_label"] = g.vs["name"]
visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
visual_style["layout"] = layout
# visual_style["bbox"] = (600, 600)
visual_style["margin"] = 40
visual_style["vertex_shape"] = 'hidden'
plot(g, **visual_style)

# import igraph.drawing.shapes as shapes
# from pprint import pprint
# pprint(shapes.__dict__)

g = Graph.Tree(63,2)
plot(g, )
