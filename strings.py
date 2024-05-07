s = "Abc"
print(s[0:2])

# strings are immutable
# s[0] = "pp" // this wont work
# print(s)
print(id(s))
s += "def"
print(s)
print(id(s))

# addition vs concatenation

print(int("123") + int("10"))

print(str(123) + str(456))

#combine list of strings

strs = ["ab", "cdd", "dd"]
print("".join(strs))