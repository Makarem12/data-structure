import pytest
from Linkedlist import LinkedList
from Node import Node

@pytest.fixture
def empty_linked_list():
    
    return LinkedList()


@pytest.fixture
def sample_linked_list():
    
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    return ll

def test_empty_linked_list_initialization(empty_linked_list):
   
    assert len(empty_linked_list) == 0

def test_empty_linked_list_length(empty_linked_list):
 
    assert len(empty_linked_list) == 0

def test_get_item_from_sample_linked_list(sample_linked_list):
    assert sample_linked_list[1] == 2

def test_get_item_from_empty_linked_list(empty_linked_list):
    with pytest.raises(IndexError):
        empty_linked_list[0]

def test_empty_linked_list_to_string(empty_linked_list):
    assert str(empty_linked_list) == "LinkedList: Empty"

def test_sample_linked_list_to_string(sample_linked_list):
    assert str(sample_linked_list) == "LinkedList: 1 -> 2 -> 3"
