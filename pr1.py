# Program to search an element from the array / list

arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == x:
        print(x, "found at index", i)
        found = True
        break

if not found:
    print(x, "not found in the list")





# Program to find the sum of array/list elements

arr = [10, 20, 30, 40, 50]
total = 0

for element in arr:
    total = total + element

print("Sum of elements =", total)
