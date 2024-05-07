import graphviz
import os
#%%
# os.chdir('C:/Users/madou/OneDrive - UCLA IT Services/3)_SOC-Honors/graphs/union-power-graph/final-draft')
# os.getcwd()
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

graph = graphviz.Digraph(
                     # name='splines', 
                     engine='neato',
                     # graph_attr={'splines': 'true'},
                     # node_attr={'shape': 'point'}
                     )
#%%
def graphsize(n1, n2, newwidth):
  factor = n2 / n1
  newnums = ''.join([str(newwidth), ',', str(newwidth * factor), '!'])
  return newnums

rescaled = graphsize(n1 = 564, n2 = 406, newwidth = 50)
rescaled
graph.attr(splines='ortho', size=rescaled)

# ######################################################################
# Red edges
# ######################################################################

graph = graphviz.Digraph(
                     # name='splines', 
                     engine='neato',
                     # graph_attr={'splines': 'true'},
                     # node_attr={'shape': 'point'}
                     )
graph.attr(splines='ortho', size=rescaled)

# Add nodes
graph.node('skilled_q', 'Is highly skilled\nlabor necessary?', pos='0,0!', shape='oval')
graph.node('union', 'Union Hiring Hall:\nIncreased Labor Costs', pos='3.5,-1.5!', shape='note')
graph.node('non_union', 'Non-Union Labor:\nLower Labor Costs', pos='-0,-3!', shape='note')
graph.node('large_workforce_q', 'Is a large workforce\nneeded?', pos='-0,-1.5!', shape='oval')

# Add edges with "Yes" labels and set the color attribute to red for "Yes" edges
graph.edge('skilled_q', 'union', label='Yes*', color='red')
graph.edge('large_workforce_q', 'union', label='Yes*', color='red')
graph.edge('skilled_q', 'large_workforce_q', label='No')
graph.edge('large_workforce_q', 'non_union', label='No')

graph.attr(label='\n*Red “Yes” responses indicate points of leverage favorable to the union.', labelloc='b', fontsize='12')

#%%
# Render as PDF
graph.render('union_power_red', format='pdf')



# from graphviz import Digraph
# #####################################################
# What does Digraph do differently??
# #####################################################



