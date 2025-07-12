st = {1, 2, 3}
print(st)

st.add(4)  # add single items
print(st)

st.update([5, 6])  # add multiple items
print(st)

st.remove(4)  # Error occurs when the elements does not found
print(st)

st.discard(6)  # Does not error occurs even the elements not found
print(st)

print(len(st))
print(10 in st)

# st.clear()
st2 = st.copy()
print(st2)
print(st is st2)  # False → different objects
print(st == st2)  # True  → same values

print("# Set Comprehension")
exor = {(x ^ 1) for x in range(10)}
print(exor)

print("# Frozenset:")
st3 = frozenset({1, 2, 3, 1})
# st3.discard(5) # frozensets are immutable
print(st3)

print("# Set Operations:")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
print("A U B:", a.union(b))
print("A ∩ B:", a.intersection(b))  # Same for a&b
print("A - B:", a.difference(b))  # Same for a-b
print("A ^ B:", a.symmetric_difference(b))  # (A U B) - (A ∩ B)
