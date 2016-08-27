def is_concatenation(dictionary, key):
    # base case: checks for empty string
    if not key:
        return True
    # recursive branch
    idx = 1
    while idx <= len(key):
        if key[0:idx] in dictionary and is_concatenation(dictionary, key[idx:]):
            return True
        idx += 1
    return False

test_dict = ["world", "hello", "super"]
print(test_dict)
print('helloworld', is_concatenation(test_dict, 'helloworld'))
print('supersuper', is_concatenation(test_dict, 'supersuper'))
print('superman', is_concatenation(test_dict, 'superman'))
print('hellosuperhello', is_concatenation(test_dict, 'hellosuperhello'))
