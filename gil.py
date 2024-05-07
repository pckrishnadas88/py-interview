# https://realpython.com/python-gil/
import sys
a = []
b = a
print(sys.getrefcount(a))
