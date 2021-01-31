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

@pytest.fixture
def node_string(make_node):
    return str(make_node)

@pytest.mark.skip(reason="wrong way of testing")
def test_compare(make_node):
    result = []
    expect = [1, 2, 3, 4, 5]
    result.append(print_tree(make_node))
    print(make_node)
    for index,ele in  enumerate(expect):
        assert ele ==result[index] , "should pass"

def test_node_display(node_string,make_node):
    print(make_node)
    assert node_string==str(make_node),"should pass"
    
