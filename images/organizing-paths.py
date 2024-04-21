import os
import graphviz
#%%
os.chdir('C:/Users/madou/OneDrive - UCLA IT Services/3)_SOC-Honors/graphs/organizing paths graph/final-draft')
os.getcwd()
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

rescaled = graphsize(n1 = 695,n2 = 657,newwidth = 50)
rescaled
graph.attr(splines='ortho', size=rescaled)
# graph.attr(rankdir='LR') # Turn the graph 90 degrees
#%%                   
# Add nodes
graph.node('1', label='All other labor unions (industrial and\ncraft unions)', shape='box')
graph.node('2', label='Workers organize at the shop floor/\nat the workplace', shape='box')
graph.node('3', label='Election or\n“card check” necessary\n(majority status)', shape='box')
graph.node('4', label='Workers and union negotiate\ntheir first contract;\n work stoppages (strikes) and the\nstate (NLRB) used as instruments\nto compel negotiations', shape='box')
graph.node('5', label='Standard\nCBA (contract) established\nper Section 9(a)', shape='box')

#Prehire Agreements
graph.node('BT1', label='Building and construction\ntrade unions (craft unions)', shape='box', pos='7!,4!')
graph.node('BT2', label='Attract employers based\non employer need for\nhigh skill level and training;\n (“pool of skilled labor”)', shape='box')
graph.node('BT3', label='Election or card check not necessary;\nmajority status not required;\nno workers have been hired yet', shape='box')
graph.node('BT4', label='Employer association voluntarily signs\na pre-hire CBA (contract) established\nper Section 8(f)', shape='box')
graph.node('BT5', label='Workers are dispatched\nfrom the union hiring hall;\nworkers are covered by the\npre-existing CBA', shape='box')


#Node positions
graph.node('1', pos='1,7!')
graph.node('2', pos='1,5.5!')
graph.node('3', pos='1,4!')
graph.node('4', pos='1,2.5!')
graph.node('5', pos='1,1!')

# BT Node positions
graph.node('BT1', pos='5,7!')
graph.node('BT2', pos='5,5.5!')
graph.node('BT3', pos='5,4!')
graph.node('BT4', pos='5,2.5!')
graph.node('BT5', pos='5,1!')

# Add edges
graph.edge('1', '2')    
graph.edge('2', '3')
graph.edge('3', '4')
graph.edge('4', '5')

#Building Trades edges
graph.edge('BT1', '2') 
graph.edge('BT1', 'BT2')
graph.edge('BT2', 'BT3') 
graph.edge('BT3', 'BT4')
graph.edge('BT4', 'BT5')

# Render as SVG
graph.render('organizing-paths', format='svg') #, view=True)
# Render as PNG
graph.render('organizing-paths', format='png')
# Render as PDF
graph.render('organizing-paths', format='pdf')


# Testing

# n = graphviz.Digraph(name='splines', engine='neato',
                     # graph_attr={'splines': 'true'},
                     # node_attr={'shape': 'point'})
# n.node('a', pos='0,0!', color='blue')
# n.node('b', pos='100,0!', color='green')
# n.node('c', pos='50,509!', color='red')
# n.edge('a', 'b', pos='0,0 30,66 70,60 100,0')
# n.render(neato_no_op=2, directory='doctest-output').replace('\\', '/')
# 'doctest-output/splines.gv.pdf'

