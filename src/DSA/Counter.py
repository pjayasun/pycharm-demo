from collections import Counter

list1 = ["mark", "mark", "Pranesh", "mark", "gunner", "Pranesh", "ajay", "ajay", "ajay", "ajay"]

counter = Counter(list1)


print(counter)
print(counter.keys())
print(counter.values())

counter.popitem()

print(counter)

# Sorting by frequency
sorted_by_frequency = counter.most_common(2)
print(sorted_by_frequency)


sorted_by_item = sorted(counter.items())
print(sorted_by_item)

print(counter.get("Pranesh"))