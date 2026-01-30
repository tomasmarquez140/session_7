print(dir("x"))
print(help("x".capitalize))
s ="bob ATE piZZA"
print(s.capitalize())

print(s.count("A"))
s = "banana and another ana + ana again"
print(s.count("ana"))
s = "banana"
print(s.find("ana"))
print(s.find("ana", 2))

print(s.replace("ana", "BOB"))
s = "I, like to go out!"
print(s.split(" "))

punct = ",.!:"
for c in punct:
    s = s.replace(c, "")
print(s.split())