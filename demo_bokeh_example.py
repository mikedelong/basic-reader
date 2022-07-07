from bokeh.io import output_file, save
from bokeh.models import Circle, HoverTool, Plot, Range1d
from bokeh.plotting import from_networkx
from networkx import Graph, spring_layout

G = Graph()

for item in [
    (0, {'name': 'home', 'type': 'location', 'size': 17}),
    (1, {'name': 'house', 'type': 'structure', 'size': 10}),
    (2, {'name': 'cat', 'type': 'inhabitant', 'size': 1})]:
    G.add_node(node_for_adding=item[0], **item[1])

for node in range(2):
    G.add_edge(u_of_edge=node, v_of_edge=node + 1)

plot = Plot(width=400, height=400, x_range=Range1d(-2, 2), y_range=Range1d(-2, 2))
plot.add_tools(HoverTool())
graph = from_networkx(G, spring_layout, scale=1, center=(0, 0))
graph.node_renderer.glyph = Circle(size=15, fill_color='red')
plot.renderers.append(graph)

filename = 'networkx_graph.html'
output_file(filename=filename)
save(obj=plot, filename=filename)
