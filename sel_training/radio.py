# Strings, Lists -- Done

# Dictionary

d1 = {
    'one': 'Ankit',
    'two': 'bhargav',
    'three': 'Chandu',
    'four': 'Dharma',
    'one': 'Farah'
}
print(d1)

# The sequence will not be maintained constantly. No index concept

# d1.pop('two')
# print("After pop", d1)

v = d1.get('three')
print(v)
#
# print(d1['three'])
#
# data = d1.items()
# print(data)

k = d1.keys()
print("Keys are", k)
v = d1.values()
print("Values are", v)

# d1.popitem()
# print("After PopItem", d1)
#
# d1.update({'five': 'Hannu', 'six': "India"})
# print("Aftre Update", d1)
#
# d1['seven'] = "John"
# print(d1)


# d1.clear()
# print(d1)
l1 = [1,2,3,4]
v = "check"

d2 = d1.fromkeys(l1, v)
print(d2)

d3 = d1.copy()
print(d3)


d4 = d1
print("D4 is", d4)