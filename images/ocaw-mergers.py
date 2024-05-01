import os
import graphviz
#%%
def graphsize(old_length, old_width, newwidth):
  factor = old_width / old_length
  newnums = ''.join([str(newwidth), ',', str(newwidth * factor), '!'])
  return newnums

rescaled = graphsize(8.92, 5.35, 50)
rescaled
#%%
# os.chdir('C:/Users/madou/OneDrive - UCLA IT Services/3)_SOC-Honors/graphs/organizing paths graph/final-draft')
# os.getcwd()
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin\\'
#%%


graph = graphviz.Digraph(engine='neato')
graph.attr(splines='ortho', size=rescaled)
# Add nodes
graph.node('UMWA', label='United Mine Workers of America\n(UMWA)', pos='4,5.5!', shape='rectangle')
graph.node('OWIU', label='Oil Field, Gas Well\nand Refinery Workers\n(OWIU)', pos='2.5,4!', shape='rectangle') # shape='note')
graph.node('UGCCWA', label='Gas, Coke, and\nChemical Workers\n(UGCCWA)', pos='4.55,4!', shape='rectangle')
graph.node('OCAW', label='Oil Chemical and Atomic Workers\n(OCAW)', pos='3.25,2.5!', shape='rectangle')
graph.node('UPIU', label='United Paperworkers\'\nInternational Union\n(UPIU)', pos='0,2.5!', shape='rectangle')
graph.node('PACE', label='Paper, Allied-Industrial,\nChemical and Energy Workers\n(PACE)', pos='1,1!', shape='rectangle')
graph.node('USW', label='United Steelworkers\n(USW)', pos='1,-0.5!', shape='rectangle')

# Add labels
graph.node('merger', label='Merger', pos='3.5,3.25!', shape='plaintext', fontsize='20')
graph.node('split', label='Split', pos='3.5,4.75!', shape='plaintext', fontsize='20')
graph.node('pace_merger', label='Merger', pos='1.25,1.75!', shape='plaintext', fontsize='20')
# graph.node('usw_merger', label='Merger  ', pos='2,0.15!', shape='plaintext', fontsize='20')
#%%
# Add edges
graph.edge('UMWA', 'UGCCWA')
graph.edge('UGCCWA', 'OCAW')
graph.edge('OWIU', 'OCAW')
graph.edge('UPIU', 'PACE')
graph.edge('OCAW', 'PACE')
graph.edge('PACE', 'USW', label='Merger ', fontsize='20', lp='3,2.5')
#%%
# Render as PNG
graph.render('ocaw', format='pdf')
