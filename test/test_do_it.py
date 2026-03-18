import pytest
from do_it import *

# =========================================
# Question 1 - merge_with_fallback
# =========================================
def test_merge_with_fallback_basic():
    assert merge_with_fallback(['a','b'], [1,2], [10,20]) == {'a':10,'b':20}

def test_merge_with_fallback_partial():
    assert merge_with_fallback(['a','b','c'], [1,2,3], [10]) == {'a':10,'b':2,'c':3}

def test_merge_with_fallback_empty_override():
    assert merge_with_fallback(['x','y'], [5,6], []) == {'x':5,'y':6}

def test_merge_with_fallback_empty_all():
    assert merge_with_fallback([], [], []) == {}

def test_merge_with_fallback_mismatch():
    assert merge_with_fallback(['a','b','c'], [1,2,3], [10,20]) == {'a':10,'b':20,'c':3}


# =========================================
# Question 2 - group_numbers_by_parity
# =========================================
def test_group_numbers_basic():
    assert group_numbers_by_parity([1,2,3,4]) == {'odd':[1,3],'even':[2,4]}

def test_group_numbers_all_even():
    assert group_numbers_by_parity([2,4,6]) == {'odd':[],'even':[2,4,6]}

def test_group_numbers_all_odd():
    assert group_numbers_by_parity([1,3,5]) == {'odd':[1,3,5],'even':[]}

def test_group_numbers_empty():
    assert group_numbers_by_parity([]) == {'odd':[],'even':[]}

def test_group_numbers_negatives():
    assert group_numbers_by_parity([-1,-2]) == {'odd':[-1],'even':[-2]}


# =========================================
# Question 3 - invert_dict_with_sets
# =========================================
def test_invert_dict_basic():
    assert invert_dict_with_sets({'a':1,'b':2}) == {1:{'a'},2:{'b'}}

def test_invert_dict_duplicates():
    assert invert_dict_with_sets({'a':1,'b':1}) == {1:{'a','b'}}

def test_invert_dict_empty():
    assert invert_dict_with_sets({}) == {}

def test_invert_dict_multiple():
    assert invert_dict_with_sets({'x':10,'y':10,'z':20}) == {10:{'x','y'},20:{'z'}}

def test_invert_dict_strings():
    assert invert_dict_with_sets({'a':'x','b':'x'}) == {'x':{'a','b'}}


# =========================================
# Question 4 - flatten_mixed_list
# =========================================
def test_flatten_mixed_basic():
    assert flatten_mixed_list([1,[2,3],(4,5)]) == [1,2,3,4,5]

def test_flatten_mixed_only_lists():
    assert flatten_mixed_list([[1,2],[3]]) == [1,2,3]

def test_flatten_mixed_empty():
    assert flatten_mixed_list([]) == []

def test_flatten_mixed_single():
    assert flatten_mixed_list([42]) == [42]

def test_flatten_mixed_nested_simple():
    assert flatten_mixed_list([1,(2,),[3]]) == [1,2,3]


# =========================================
# Question 5 - count_unique_elements
# =========================================
def test_count_unique_basic():
    assert count_unique_elements([1,1,2,3]) == 3

def test_count_unique_empty():
    assert count_unique_elements([]) == 0

def test_count_unique_all_unique():
    assert count_unique_elements([1,2,3]) == 3

def test_count_unique_strings():
    assert count_unique_elements(['a','a','b']) == 2

def test_count_unique_mixed():
    assert count_unique_elements([1,'1',1]) == 2


# =========================================
# Question 6 - recursive_factorial
# =========================================
def test_factorial_basic():
    assert recursive_factorial(5) == 120

def test_factorial_zero():
    assert recursive_factorial(0) == 1

def test_factorial_one():
    assert recursive_factorial(1) == 1

def test_factorial_three():
    assert recursive_factorial(3) == 6

def test_factorial_large():
    assert recursive_factorial(6) == 720


# =========================================
# Question 7 - recursive_reverse_list
# =========================================
def test_reverse_basic():
    assert recursive_reverse_list([1,2,3]) == [3,2,1]

def test_reverse_empty():
    assert recursive_reverse_list([]) == []

def test_reverse_single():
    assert recursive_reverse_list([42]) == [42]

def test_reverse_strings():
    assert recursive_reverse_list(['a','b']) == ['b','a']

def test_reverse_duplicates():
    assert recursive_reverse_list([1,1,2]) == [2,1,1]


# =========================================
# Question 8 - tuple_to_frequency_dict
# =========================================
def test_tuple_freq_basic():
    assert tuple_to_frequency_dict((1,2,2)) == {1:1,2:2}

def test_tuple_freq_empty():
    assert tuple_to_frequency_dict(()) == {}

def test_tuple_freq_single():
    assert tuple_to_frequency_dict((5,)) == {5:1}

def test_tuple_freq_strings():
    assert tuple_to_frequency_dict(('a','a','b')) == {'a':2,'b':1}

def test_tuple_freq_mixed():
    assert tuple_to_frequency_dict((1,'1',1)) == {1:2,'1':1}


# =========================================
# Question 9 - set_intersection_all
# =========================================
def test_set_intersection_basic():
    assert set_intersection_all([{1,2,3},{2,3},{2}]) == {2}

def test_set_intersection_empty_list():
    assert set_intersection_all([]) == set()

def test_set_intersection_single():
    assert set_intersection_all([{1,2}]) == {1,2}

def test_set_intersection_no_common():
    assert set_intersection_all([{1},{2}]) == set()

def test_set_intersection_strings():
    assert set_intersection_all([{'a','b'},{'b','c'}]) == {'b'}


# =========================================
# Question 10 - group_words_by_last_letter
# =========================================
def test_group_last_letter_basic():
    assert group_words_by_last_letter(['cat','bat','car']) == {
        't':['cat','bat'],
        'r':['car']
    }

def test_group_last_letter_empty():
    assert group_words_by_last_letter([]) == {}

def test_group_last_letter_single():
    assert group_words_by_last_letter(['hi']) == {'i':['hi']}

def test_group_last_letter_duplicates():
    assert group_words_by_last_letter(['a','ba']) == {
        'a':['a','ba']
    }

def test_group_last_letter_mixed():
    assert group_words_by_last_letter(['dog','dig']) == {
        'g':['dog','dig']
    }


# =========================================
# Question 11 - recursive_flatten
# =========================================
def test_recursive_flatten_basic():
    assert recursive_flatten([1,[2,[3,4]],5]) == [1,2,3,4,5]

def test_recursive_flatten_empty():
    assert recursive_flatten([]) == []

def test_recursive_flatten_single():
    assert recursive_flatten([42]) == [42]

def test_recursive_flatten_deep():
    assert recursive_flatten([[1,[2,[3]]]]) == [1,2,3]

def test_recursive_flatten_mixed():
    assert recursive_flatten([1,[2],3]) == [1,2,3]


# =========================================
# Question 12 - dict_of_squares
# =========================================
def test_dict_squares_basic():
    assert dict_of_squares([1,2,3]) == {1:1,2:4,3:9}

def test_dict_squares_empty():
    assert dict_of_squares([]) == {}

def test_dict_squares_single():
    assert dict_of_squares([5]) == {5:25}

def test_dict_squares_negatives():
    assert dict_of_squares([-1,-2]) == {-1:1,-2:4}

def test_dict_squares_duplicates():
    assert dict_of_squares([2,2]) == {2:4}















































# import pytest
# from do_it import *

# # =========================================
# # Question 1 - merge_with_priority
# # =========================================
# def test_merge_with_priority_basic():
#     assert merge_with_priority(['a','b','c'], [1,2,3], [10,20,30]) == {'a':10,'b':20,'c':30}

# def test_merge_with_priority_partial_override():
#     assert merge_with_priority(['a','b','c'], [1,2,3], [10]) == {'a':10,'b':2,'c':3}

# def test_merge_with_priority_empty_second():
#     assert merge_with_priority(['a','b'], [1,2], []) == {'a':1,'b':2}

# def test_merge_with_priority_empty_keys():
#     assert merge_with_priority([], [], []) == {}

# def test_merge_with_priority_mismatched_lengths():
#     assert merge_with_priority(['x','y','z'], [5,6,7], [50,60]) == {'x':50,'y':60,'z':7}


# # =========================================
# # Question 2 - group_by_first_letter
# # =========================================
# def test_group_by_first_letter_basic():
#     assert group_by_first_letter(['apple','banana','apricot']) == {
#         'a': ['apple','apricot'],
#         'b': ['banana']
#     }

# def test_group_by_first_letter_single():
#     assert group_by_first_letter(['cat']) == {'c': ['cat']}

# def test_group_by_first_letter_empty():
#     assert group_by_first_letter([]) == {}

# def test_group_by_first_letter_mixed_case():
#     assert group_by_first_letter(['Apple','ant']) == {
#         'A': ['Apple'],
#         'a': ['ant']
#     }

# def test_group_by_first_letter_duplicates():
#     assert group_by_first_letter(['hi','hello','hi']) == {
#         'h': ['hi','hello','hi']
#     }


# # =========================================
# # Question 3 - invert_and_group
# # =========================================
# def test_invert_and_group_basic():
#     assert invert_and_group({'a':1,'b':2}) == {1:['a'],2:['b']}

# def test_invert_and_group_duplicates():
#     assert invert_and_group({'a':1,'b':1,'c':2}) == {1:['a','b'],2:['c']}

# def test_invert_and_group_single():
#     assert invert_and_group({'x':10}) == {10:['x']}

# def test_invert_and_group_empty():
#     assert invert_and_group({}) == {}

# def test_invert_and_group_multiple_same():
#     assert invert_and_group({'a':1,'b':1,'c':1}) == {1:['a','b','c']}


# # =========================================
# # Question 4 - filter_dict_by_value
# # =========================================
# def test_filter_dict_by_value_basic():
#     assert filter_dict_by_value({'a':10,'b':5,'c':20}, 10) == {'a':10,'c':20}

# def test_filter_dict_by_value_equal():
#     assert filter_dict_by_value({'a':10,'b':15}, 10) == {'a':10,'b':15}

# def test_filter_dict_by_value_none_pass():
#     assert filter_dict_by_value({'a':1,'b':2}, 5) == {}

# def test_filter_dict_by_value_all_pass():
#     assert filter_dict_by_value({'x':50,'y':60}, 10) == {'x':50,'y':60}

# def test_filter_dict_by_value_empty():
#     assert filter_dict_by_value({}, 10) == {}


# # =========================================
# # Question 5 - zip_to_nested_dict
# # =========================================
# def test_zip_to_nested_dict_basic():
#     assert zip_to_nested_dict(['a','b'], [1,2]) == {
#         'a': {'value':1},
#         'b': {'value':2}
#     }

# def test_zip_to_nested_dict_partial():
#     assert zip_to_nested_dict(['a','b','c'], [1]) == {
#         'a': {'value':1}
#     }

# def test_zip_to_nested_dict_empty():
#     assert zip_to_nested_dict([], []) == {}

# def test_zip_to_nested_dict_single():
#     assert zip_to_nested_dict(['x'], [99]) == {'x': {'value':99}}

# def test_zip_to_nested_dict_extra_values():
#     assert zip_to_nested_dict(['a'], [1,2,3]) == {'a': {'value':1}}


# # =========================================
# # Question 6 - sum_even_numbers
# # =========================================
# def test_sum_even_numbers_basic():
#     assert sum_even_numbers([1,2,3,4]) == 6

# def test_sum_even_numbers_all_odd():
#     assert sum_even_numbers([1,3,5]) == 0

# def test_sum_even_numbers_empty():
#     assert sum_even_numbers([]) == 0

# def test_sum_even_numbers_negatives():
#     assert sum_even_numbers([-2,-4,3]) == -6

# def test_sum_even_numbers_large():
#     assert sum_even_numbers(list(range(100))) == sum([i for i in range(100) if i%2==0])


# # =========================================
# # Question 7 - flatten_list_of_lists
# # =========================================
# def test_flatten_list_basic():
#     assert flatten_list_of_lists([[1,2],[3,4]]) == [1,2,3,4]

# def test_flatten_list_empty_inner():
#     assert flatten_list_of_lists([[1],[],[2,3]]) == [1,2,3]

# def test_flatten_list_empty_outer():
#     assert flatten_list_of_lists([]) == []

# def test_flatten_list_single_element():
#     assert flatten_list_of_lists([[42]]) == [42]

# def test_flatten_list_nested_strings():
#     assert flatten_list_of_lists([['a','b'],['c']]) == ['a','b','c']


# # =========================================
# # Question 8 - unique_chars_in_words
# # =========================================
# def test_unique_chars_basic():
#     assert unique_chars_in_words(['hi','hello']) == set('hielo')

# def test_unique_chars_empty():
#     assert unique_chars_in_words([]) == set()

# def test_unique_chars_single_word():
#     assert unique_chars_in_words(['abc']) == {'a','b','c'}

# def test_unique_chars_repeated_letters():
#     assert unique_chars_in_words(['aa','bb']) == {'a','b'}

# def test_unique_chars_numbers_and_letters():
#     assert unique_chars_in_words(['a1','b2']) == {'a','b','1','2'}


# # =========================================
# # Question 9 - transpose_matrix
# # =========================================
# def test_transpose_matrix_basic():
#     assert transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]]

# def test_transpose_matrix_single_row():
#     assert transpose_matrix([[1,2,3]]) == [[1],[2],[3]]

# def test_transpose_matrix_single_column():
#     assert transpose_matrix([[1],[2],[3]]) == [[1,2,3]]

# def test_transpose_matrix_empty():
#     assert transpose_matrix([]) == []

# def test_transpose_matrix_strings():
#     assert transpose_matrix([['a','b'],['c','d']]) == [['a','c'],['b','d']]


# # =========================================
# # Question 10 - group_by_length
# # =========================================
# def test_group_by_length_basic():
#     assert group_by_length(['a','to','be']) == {1:['a'],2:['to','be']}

# def test_group_by_length_empty():
#     assert group_by_length([]) == {}

# def test_group_by_length_same_length():
#     assert group_by_length(['hi','no']) == {2:['hi','no']}

# def test_group_by_length_mixed():
#     assert group_by_length(['a','abc','ab']) == {1:['a'],2:['ab'],3:['abc']}

# def test_group_by_length_duplicates():
#     assert group_by_length(['a','a','ab','ab']) == {1:['a','a'],2:['ab','ab']}


# # =========================================
# # Question 11 - union_of_sets
# # =========================================
# def test_union_of_sets_basic():
#     assert union_of_sets([{1,2},{2,3}]) == {1,2,3}

# def test_union_of_sets_empty():
#     assert union_of_sets([]) == set()

# def test_union_of_sets_single():
#     assert union_of_sets([{42}]) == {42}

# def test_union_of_sets_duplicates():
#     assert union_of_sets([{1,1,2},{2,3,3}]) == {1,2,3}

# def test_union_of_sets_strings():
#     assert union_of_sets([{'a','b'},{'b','c'}]) == {'a','b','c'}


# # =========================================
# # Question 12 - product_of_tuple_numbers
# # =========================================
# def test_product_of_tuple_numbers_basic():
#     assert product_of_tuple_numbers((1,2,3,4)) == 24

# def test_product_of_tuple_numbers_empty():
#     assert product_of_tuple_numbers(()) == 1

# def test_product_of_tuple_numbers_single():
#     assert product_of_tuple_numbers((5,)) == 5

# def test_product_of_tuple_numbers_negatives():
#     assert product_of_tuple_numbers((-1,2,-3)) == 6

# def test_product_of_tuple_numbers_large():
#     assert product_of_tuple_numbers((1,2,3,4,5)) == 120


# # =========================================
# # Question 13 - flatten_tuple_list
# # =========================================
# def test_flatten_tuple_list_basic():
#     assert flatten_tuple_list([(1,2),(3,4)]) == [1,2,3,4]

# def test_flatten_tuple_list_empty_inner():
#     assert flatten_tuple_list([(1,),(),(2,3)]) == [1,2,3]

# def test_flatten_tuple_list_empty_outer():
#     assert flatten_tuple_list([]) == []

# def test_flatten_tuple_list_single_element():
#     assert flatten_tuple_list([(42,)]) == [42]

# def test_flatten_tuple_list_mixed_types():
#     assert flatten_tuple_list([('a','b'),('c',)]) == ['a','b','c']


# # =========================================
# # Question 14 - recursive_sum
# # =========================================
# def test_recursive_sum_basic():
#     assert recursive_sum([1,2,3,4]) == 10

# def test_recursive_sum_empty():
#     assert recursive_sum([]) == 0

# def test_recursive_sum_single_element():
#     assert recursive_sum([42]) == 42

# def test_recursive_sum_negatives():
#     assert recursive_sum([-1,-2,3]) == 0

# def test_recursive_sum_large():
#     assert recursive_sum(list(range(101))) == sum(range(101))


# # =========================================
# # Question 15 - recursive_max
# # =========================================
# def test_recursive_max_basic():
#     assert recursive_max([1,5,3,4]) == 5

# def test_recursive_max_single():
#     assert recursive_max([42]) == 42

# def test_recursive_max_negatives():
#     assert recursive_max([-1,-5,-3]) == -1

# def test_recursive_max_duplicates():
#     assert recursive_max([2,2,2,2]) == 2

# def test_recursive_max_large():
#     assert recursive_max(list(range(100))) == 99