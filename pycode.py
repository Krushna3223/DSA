
print("\n1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")

print("\n\n2. Sum of squares of numbers from 1 to 10:")
total = sum(i*i for i in range(1, 11))
print("Sum =", total)

print("\n3. Squares of numbers from 1 to 100:")
for i in range(1, 101):
    print(f"{i}^2 = {i*i}")

print("\n4. Multiplication table:")
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("\n5. Even numbers:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\n6. Odd numbers:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")

print("\n\n7. Factorial of a number:")
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"Factorial of {num} = {fact}")

print("\n8. Count numbers divisible by 7 from 1–100:")
count = sum(1 for i in range(1, 101) if i % 7 == 0)
print("Count =", count)

print("\n9. Reverse a number:")
num = 12345
rev = int(str(num)[::-1])
print("Reverse:", rev)

print("\n10. Armstrong number check:")
num = 153
s = sum(int(d)**3 for d in str(num))
print(num, "is Armstrong" if s == num else "Not Armstrong")



print("\n\n11. Positive/Negative check:")
n = -4
print("Positive" if n > 0 else "Negative")

print("\n12. Largest of two numbers:")
a, b = 20, 40
print("Largest =", max(a, b))

print("\n13. Largest of three numbers:")
a, b, c = 40, 20, 60
print("Largest =", max(a, b, c))

print("\n14. Even/Odd check:")
n = 7
print("Even" if n % 2 == 0 else "Odd")

print("\n15. Shopping discount:")
bill = 1200
discount = bill * 0.10 if bill >= 1000 else 0
print("Payable =", bill - discount)

print("\n16. Income tax calculator:")
income = 450000
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30
print("Tax =", tax)



print("\n\n18. Area of a triangle:")
b, h = 10, 5
print("Area =", 0.5 * b * h)

print("\n19. Area of circle:")
r = 5
print("Area =", 3.14159 * r * r)

print("\n20. Area of rectangle:")
l, w = 5, 3
print("Area =", l * w)

print("\n21. Convert cm to meter:")
cm = 250
print("Meters =", cm / 100)

print("\n22. Celsius to Fahrenheit:")
c = 37
print("F =", (c * 9/5) + 32)



print("\n\n23. Even check (function):")
def is_even(n):
    return n % 2 == 0
print(is_even(10))

print("\n24. String length:")
def length(s):
    return len(s)
print(length("Hello"))

print("\n25. Palindrome check:")
def is_pal(s):
    return s == s[::-1]
print(is_pal("madam"))

print("\n26. Sum of list:")
def list_sum(lst):
    return sum(lst)
print(list_sum([1,2,3,4,5]))

print("\n27. Largest number in list:")
def largest(lst):
    return max(lst)
print(largest([5,1,9,2]))

print("\n28. Factorial (recursive):")
def fact(n):
    return 1 if n<=1 else n * fact(n-1)
print(fact(6))



lst = [10,20,30,40,50]
print("\n\n29. List:", lst)
print("30. After append:", lst + [60])
print("31. After insert:", lst[:2] + [15] + lst[2:])
print("32. Reverse:", lst[::-1])
print("33. Second largest:", sorted(lst)[-2])
print("34. Remove duplicates:", list(set([1,2,3,2,1])))



print("\n\n35. Smallest number divisible by 3 & 7:")
num = 1
while True:
    if num % 3 == 0 and num % 7 == 0:
        print(num)
        break
    num += 1




print("\n\n36. File operations executed (writing, reading, appending).")

with open("file1.txt", "w") as f:
    f.write("Hello World")

with open("file1.txt", "a") as f:
    f.write("\nPython Practical File")

with open("file1.txt") as f:
    print("\nFile Content:\n", f.read())



print("\n\n37. Class and object demonstration:")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s1 = Student("Krushna", 95)
s1.display()



print("\n\n38. Tuple & Set operations:")

t = (1,2,3)
s = {1,2,3,4}
print("Tuple:", t)
print("Set:", s)
print("Union:", s.union({5,6}))
print("Intersection:", s.intersection({2,3,10}))



print("\n\n39. Dictionary Operations:")

d = {"name":"Krushna","age":19}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
d["city"] = "Pune"
print("Updated:", d)




print("\n\n40. String Programs:")

s = "Hello World"
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Vowel Count:", sum(1 for i in s.lower() if i in "aeiou"))
print("Reversed:", s[::-1])
print("No Spaces:", s.replace(" ",""))



