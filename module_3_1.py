calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    return string in list_to_search

print(string_info('capybara'))
print(string_info('armageddon'))
print(is_contains('urban', ['ban', 'banan', 'urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)