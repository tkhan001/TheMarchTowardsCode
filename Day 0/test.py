# Problem: 
# Find the position of a given number in a list of numbers arranged in decreasing order.
# Should minimize the number of times elements from the list are accessed

# Input: List in decreasing order; given number (query)
# Output: int representing the index of the element (position)

def find_elem(list, query):
    pass


if __name__ == "__main__":
    # Sample Test
    list = [12, 8, 5, 4, 3, 1]
    query = 3
    output = 4

    result = find_elem(list, query)

    # Represent test cases as entries in a dictonary
    test = {
        'input': {
            'list': [12, 8, 5, 4, 3, 1],
            'query': 3
        },
        'output': 4
    }

    # Test like this:
    # ** takes the keys from dict and uses the values stored as params for function
    print(find_elem(**test['input']) == test['output'])

