import os

print(os.path.split("C:/Users/고객님/Desktop/vaction/py/um/jun/sik/test.txt"))
print(os.path.splitext("C:/Users/고객님/Desktop/vaction/py/um/jun/sik/test.txt"))
path = "C:/Users/고객님/Desktop/vaction/py/um/jun/sik"
filename = "test.txt"
print(os.path.join(path, filename))
