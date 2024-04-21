import os
import graphviz
#%%
os.chdir('C:/Users/madou/OneDrive - UCLA IT Services/3)_SOC-Honors/graphs/organizing paths graph/final-draft')
os.getcwd()
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin\\'
graph = graphviz.Digraph(engine='neato')
#%%
def graphsize(n1, n2, newwidth):
  factor = n2 / n1
  newnums = ''.join([str(newwidth), ',', str(newwidth * factor), '!'])
  return newnums

rescaled = graphsize(8.92, 5.35, 50)
rescaled
graph.attr(splines='ortho', size=rescaled)
#%%
# Add nodes
graph.node('worker', label='Construction\nWorker', pos='5.5,0!', shape='note')
graph.node('worker_register', label='Registers on\nUnion\nOut-of-work List', pos='5.5,3!', shape='oval')
graph.node('union_hirehall', label='Union Hiring Hall', pos='3,3!', shape='note')
graph.node('employer', label='Employer', pos='0,0!', shape='note')
graph.node('employer_request', label='Employer\nRequests\nWorker', pos='3,1.5!', shape='oval')
graph.node('employer_layoff', label='Employer\nLays-off\nWorker', pos='3,0!', shape='oval')
graph.node('union_dispatch', label='Union Dispatches\nWorker (same pay\nand benefits as\nprevious employer)', pos='0,3!', shape='oval')
#%%
# Add edges
graph.edge('worker_register', 'union_hirehall')#, label='No')
graph.edge('employer', 'employer_request')#, label='Yes')
graph.edge('employer_request', 'union_hirehall')#, label='No')
graph.edge('union_hirehall', 'union_dispatch')
graph.edge('union_dispatch', 'employer')
graph.edge('employer', 'employer_layoff')
graph.edge('employer_layoff', 'worker')
graph.edge('worker', 'worker_register')
#%%
# Render as SVG
graph.render('hiring-hall-dispatch', format='svg')
# Render as PNG
graph.render('hiring-hall-dispatch', format='png')
# Render as PDF
graph.render('hiring-hall-dispatch', format='pdf', view=True)
#%%
# check working directory
os.getcwd()
# change working directory (if necessary)
# os.chdir('/path/to/your/directory')


# ################################### #

# Digraph() arguments/settings
# name='splines', 
# graph_attr={'splines': 'true'},
# node_attr={'shape': 'point'}

# Saving these in case I decide to use them later
# graph.attr(rankdir='LR')
# graph.attr(nodesep='2.5')  # Increase horizontal spacing between nodes
# graph.attr(ranksep='2.5')  # Increase vertical spacing between nodes


# ######################################################################
# Trying something else from ChatGPT to make labels not on top of edges
# ######################################################################

# from graphviz import Digraph
# #####################################################
# What does Digraph do differently??
# #####################################################
