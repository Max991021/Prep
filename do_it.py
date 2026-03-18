def merge_with_fallback(keys, values1, values2):
    new_dict = {}
    for index, element in enumerate(keys):
        if index>= len(values2):
            new_dict.setdefault(element,values1[index])
        else:
            new_dict.setdefault(element,values2[index])
    return new_dict        
print(merge_with_fallback(['a','b','c'], [1,2,3], [10]))
def group_numbers_by_parity(nums):
    
    # new.setdefault('even', [num for num in nums if num %2==0])
    return {'odd':[num for num in nums if num %2!=0 ] }| {'even':[num for num in nums if num %2==0 ] }
print(group_numbers_by_parity([1,2,3,4]))

def invert_dict_with_sets(data):
    return {value:set(key for key,value2 in data.items() if value2==value) for key,value in data.items()}
print(invert_dict_with_sets({'x':10,'y':10,'z':20}))


def flatten_mixed_list(items):
    new = []
    for i in items:
        if isinstance(i,list | tuple):
            new.extend(flatten_mixed_list(i))
        else:
            new.append(i)
    return new
print(flatten_mixed_list([1,[2,3],(4,5)]))
def count_unique_elements(items):
    return sum(1 for item in set(items))
print(count_unique_elements([1,1,2,3]))

def recursive_factorial(n):
    # if n <=1:
    #     return [1]
    
    # rec = recursive_factorial(n-1)
    # current = n*rec[-1]
    # rec.append(current)
    return 1 if n <=1 else n*recursive_factorial(n-1)
print(recursive_factorial(5))
def recursive_reverse_list(lst):
    return [] if not lst else [lst[-1]]+recursive_reverse_list(lst[:-1]) 
print(recursive_reverse_list([1,2,3]))

def tuple_to_frequency_dict(tpl):
    return {element:tpl.count(element) for element in tpl}
print(tuple_to_frequency_dict((1,2,2)))
def set_intersection_all(sets_list):
    return set.intersection(*sets_list)
    
print(set_intersection_all([{1,2,3},{2,3},{2}]))


def group_words_by_last_letter(words):
    pass

def recursive_flatten(data):
    pass

def dict_of_squares(nums):
    pass