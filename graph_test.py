import unittest
from graph import Graph, dsf, bsf, get_first_node
from payload import dsf_graph, dsf_expected, bsf_graph, bsf_expected


class TestGraphMethods(unittest.TestCase):

    def test_get_first_node(self):
        expected = '1'
        graph: Graph = {f'{expected}': [], '2': []}
        actual = get_first_node(graph)
        self.assertEqual(actual, expected)

    def test_bsf(self):
        actual = bsf(bsf_graph, get_first_node(dsf_graph))
        self.assertEqual(actual, bsf_expected)

    def test_dsf(self):
        actual = dsf(dsf_graph, get_first_node(dsf_graph))
        self.assertEqual(actual, dsf_expected)


if __name__ == '__main__':
    unittest.main()
