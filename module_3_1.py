calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    string_info = (len(string), string.upper(), string.lower())
    count_calls()
    return string_info

def is_contains(string, list_to_search):
    global calls
    is_contains = (string.lower() in (item.lower() for item in list_to_search))
    count_calls()
    return is_contains

print(string_info('Water'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)