arr = ["alice", "bob", "martin"]
arr.sort(reverse=True)
print(arr)

# custom sort
arr.sort(key=lambda x: len(x))
print(arr)