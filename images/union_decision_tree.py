import matplotlib.pyplot as plt
import networkx as nx

def draw_game_tree():
    plt.figure(figsize=(12, 8), dpi=300)
    G = nx.DiGraph()

    # Add nodes with positions and labels
    positions = {
        'Nature of\nWork': (0, 0),
        'HS': (-4, -2), 'NHS': (4, -2),
        'HS_NC': (-6, -5), 'HS_C': (-2, -5),
        'HS_NC_EmpC': (-7, -8), 'HS_NC_EmpW': (-5, -8),
        'HS_C_EmpC': (-3, -8), 'HS_C_EmpW': (-1, -8),
        'NHS_NC': (2, -5), 'NHS_C': (6, -5),
        'NHS_NC_EmpC': (1, -8), 'NHS_NC_EmpW': (3, -8),
        'NHS_C_EmpC': (5, -8), 'NHS_C_EmpW': (7, -8),
    }
    
    # Labels indicating the decision maker
    labels = {
        'Nature of\nWork': 'Nature of\nWork',
        'HS': 'Union', 'NHS': 'Union',
        'HS_NC': 'Employer', 'HS_C': 'Employer',
        'NHS_NC': 'Employer', 'NHS_C': 'Employer',
        'HS_NC_EmpC': 'More Likely', 'HS_NC_EmpW': 'Less Likely',
        'HS_C_EmpC': 'More Likely', 'HS_C_EmpW': 'Less Likely',
        'NHS_NC_EmpC': 'More Likely', 'NHS_NC_EmpW': 'Less Likely',
        'NHS_C_EmpC': 'Less Likely', 'NHS_C_EmpW': 'More Likely',
    }

    # Add edges along with the labels
    edges = [
        ('Nature of\nWork', 'HS', 'Highly Skilled'),
        ('Nature of\nWork', 'NHS', 'Not Highly Skilled'),
        ('HS', 'HS_NC', 'No Challenge\n(less likely)'),
        ('HS', 'HS_C', 'Challenge\n(more likely)'),
        ('NHS', 'NHS_NC', 'No Challenge\n(more likely)'),
        ('NHS', 'NHS_C', 'Challenge\n(less likely)'),
        ('HS_NC', 'HS_NC_EmpC', 'Continue'),
        ('HS_NC', 'HS_NC_EmpW', 'Walk Away'),
        ('HS_C', 'HS_C_EmpC', 'Continue'),
        ('HS_C', 'HS_C_EmpW', 'Walk Away'),
        ('NHS_NC', 'NHS_NC_EmpC', 'Continue'),
        ('NHS_NC', 'NHS_NC_EmpW', 'Walk Away'),
        ('NHS_C', 'NHS_C_EmpC', 'Continue'),
        ('NHS_C', 'NHS_C_EmpW', 'Walk Away'),
    ]

    # Nodes and edges with attributes
    G.add_nodes_from(positions)
    G.add_edges_from([(u, v, {'label': label}) for u, v, label in edges])

    # Add edge colors
    edge_colors = ['red', 'red', 'black', 'red', 'red', 'black', 'black', 'black', 'red', 'black', 'red', 'black', 'black', 'black']
    edge_styles = ['--' if x == 'red' else '-' for x in edge_colors]
    # Draw edges with specified colors
    nx.draw_networkx_edges(G, pos=positions, edge_color=edge_colors, arrows=True, min_source_margin=20, min_target_margin=20, style=edge_styles)

    # Node sizes and labels
    nx.draw_networkx_nodes(G, pos=positions, node_size=4000, node_color='none', edgecolors='black')
    
    # Node labels
    nx.draw_networkx_labels(G, pos=positions, labels=labels, font_size=9, font_weight='bold')
    
    # Edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels, font_color='black', font_size=8)

    # Display the graph
    # plt.title('Extensive Form Game Tree')
    plt.axis('off')
    # plt.savefig('union_decision_tree.png', dpi=300)
    plt.savefig('union_decision_tree.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
    # plt.show()

draw_game_tree()

edge_colors = ['red', 'red', 'black', 'red', 'red', 'black', 'black', 'black', 'red', 'black', 'red', 'black', 'black', 'black']


