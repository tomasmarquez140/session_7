text = "Hello World"
print(text)
text = 'Hello World 2' #single vs double
print(text)
print(text[4])
print(len(text))
text = ""
print(len(text))

text = "Bob"
print(text[-1]) # last character in the string
print(text[-3])

# print(text[3]) this is an error
print(text[6//3])

# you can add two strings
s1 = "Hello"
s2 = "Bye"
print(s1 + s2)
print(s1*4)

#string is iterable, you can use for over it
s1 = "Hello my name is Bob"
for c in s1:
    print(c)

s1 = "I like ot give hi fives"
# print this string but replace 'i`with 'y'
# y lyke to gyve hy fyves
for c in s1:
    if c == "i":
        print("y", end= "")
    elif c == "I":
        print("Y", end= "")
    else:
        print(c, end= "")
    print()
