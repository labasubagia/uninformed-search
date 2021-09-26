from graph import dsf, bsf, get_first_node
from payload import dsf_graph, bsf_graph


bsf_result = bsf(bsf_graph, get_first_node(bsf_graph))
dsf_result = dsf(dsf_graph, get_first_node(dsf_graph))

separator = " -> "
print(f'BSF = {separator.join(bsf_result)}')
print(f'DSF = {separator.join(dsf_result)}')
