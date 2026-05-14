# Interactive Personal Data Collector

## Description
This Python program collects personal information from the user using `input()` and displays:
- Name
- Age
- Height
- Favourite Number
- Data types of the entered values
- Memory addresses using `id()`
- Approximate birth year

The program also prints a welcome and goodbye message.

---

## Python Code

```python
print("Welcome To The Interactive Personal Data Collecter!",end="\n\n")
name=input("Please Enter Your Name:")
age=int(input("Please Enter Your Age:"))
height=float(input("Please Enter Your Height In Meters:"))
num=int(input("Please Enter Your Favourite Number:"))
print("\n")
print("Thank You! Here Is The information We Have Collected",end="\n\n")
print("Name:",name,"(Type:",type(name),", " "Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),", " "Memory Address:",id(name),")")
print("Height:",height,"(Type:",type(height),", " "Memory Address:",id(height),")")
print("Favourite Number:",num,"(Type:",type(num),", " "Memory Address:",id(num),")",end="\n\n")
print("Your Birth Year Is Approximately:",2026-age,end="\n\n")
print("Thank You For Using The Personal Data Collector. Goodbye!")
```

---

## Sample Output

```text
Welcome To The Interactive Personal Data Collecter!

Please Enter Your Name: Tejas
Please Enter Your Age: 17
Please Enter Your Height In Meters: 1.75
Please Enter Your Favourite Number: 7


Thank You! Here Is The information We Have Collected

Name: Tejas (Type: <class 'str'> , Memory Address: 12345678 )
Age: 17 (Type: <class 'int'> , Memory Address: 12345678 )
Height: 1.75 (Type: <class 'float'> , Memory Address: 87654321 )
Favourite Number: 7 (Type: <class 'int'> , Memory Address: 11223344 )

Your Birth Year Is Approximately: 2009

Thank You For Using The Personal Data Collector. Goodbye!
```

---

## Concepts Used
- `print()`
- `input()`
- Type casting (`int`, `float`)
- Variables
- `type()` function
- `id()` function
- Basic arithmetic

