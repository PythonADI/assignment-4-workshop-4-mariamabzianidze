# task 1
print("\ntask N1\n")

names = ["George", "Adam", "Jacob", "Mark"]
for name in names:
    print(name)

# task 2
print("\ntask N2\n")

for friend in names:
    print(f"Hello, {friend}! Hope you're having a great day!")

# task 3
print("\ntask N3\n")

transportation = ["Tesla", "BMW", "Ford Mustang", "Mercedes"]
for transport in transportation:
    print(f"I would like to own a {transport}.")

# task 4
print("\ntask N4\n")

guest_list = ["Emma", "Olivia", "Charlotte"]
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you join for dinner.")

# task 5
print("\ntask N5\n")

change = "Olivia"
print(f"Unfortunately, {change} can't make it to the dinner.")

guest_list[1] = "Sophia"
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")
    
# task 6
print("\ntask N6\n")

print("Great news! I found a bigger dinner table, so I'm inviting more guests.")
guest_list.insert(0, "Evelyn")
guest_list.insert(2, "Luna") 
guest_list.append("Ava")
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

# task 7
print("\ntask N7\n")

print("Unfortunately, my new dinner table won't arrive in time, and I can invite only two people for dinner.\n")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")
print("\nGreat news for the remaining guests!\n")

for guest in guest_list:
    print(f"Dear {guest}, you're still invited to dinner!")

del guest_list[:]
print("\nFinal guest list:", guest_list)

# task 8
print("\ntask N8\n")

places = ["Tokyo", "Paris", "New York", "Rome", "Swiss Alps"]
print("Original list:")
print(places)

print("\nList in alphabetical order:")
print(sorted(places))

print("\nOriginal list after sorted:")
print(places)

print("\nList in reverse alphabetical order:")
print(sorted(places, reverse=True))

# task 9
print("\ntask N9\n")

guest_list = ["Evelyn", "Emma"]

for guest in guest_list:
    print(f"Dear {guest}, you're still invited to dinner!")

print(f"\nI am inviting {len(guest_list)} people to dinner.")

# task 10
print("\ntask N10\n")

languages = ["Chinese", "English", "Spanish", "French", "Korean"]

print("Original list:")
print(languages)


print("\nFirst language:", languages[0])
print("Last language:", languages[-1])

languages[2] = "German"
print("\nList after modifying an element:")
print(languages)

languages.append("Turkish")
print("\nList after appending an element:")
print(languages)


languages.insert(2, "Japanese")
print("\nList after inserting an element at index 2:")
print(languages)

del languages[3]
print("\nList after deleting the element at index 3:")
print(languages)

popped_language = languages.pop()
print(f"\nPopped language: {popped_language}")
print("List after popping the last element:")
print(languages)

languages.remove("Korean")
print("\nList after removing 'Korean':")
print(languages)

print("\nSorted list temporary:")
print(sorted(languages))


print("\nOriginal list after sorted:")
print(languages)


languages.sort()
print("\nList after sort in alphabetical order:")
print(languages)

languages.sort(reverse=True)
print("\nList after sort in reverse alphabetical order:")
print(languages)

languages.reverse()
print("\nList after reverse:")
print(languages)

print(f"\nThe list contains {len(languages)} languages.")

# task 11
print("\ntask N11\n")

languages = ["Chinese", "English", "Spanish", "French", "Korean"]
print("\nAttempting to access an out-of-range index:")

index_to_access = 10
if index_to_access < len(languages):
    print(languages[index_to_access])
else:
    print(f"Error: Index {index_to_access} is out of range. The list has only {len(languages)} elements.")
