# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

new_val = [2*item if item % 2 == 0 else item for item in values]
print(new_val)

# write the list comprehension equivalent to the `for` loop

