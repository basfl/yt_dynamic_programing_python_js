from tree import print_tree
from tree import NewNode
import pytest


@pytest.fixture
def make_node():
    root = NewNode(2)
    root.left = NewNode(1)
    root.right = NewNode(4)
    root.right.left = NewNode(3)
    root.right.right = NewNode(5)
    return root


def test_compare(make_node):
    #assert supply_data[0] == "NYC", "should pass"
    result = []
    expect = [1, 2, 3, 4, 5]
    result.append(print_tree(make_node))
    print(make_node)
    for index,ele in  enumerate(expect):
        assert ele ==result[index] , "should pass"
    #assert result == expect, "should pass"
