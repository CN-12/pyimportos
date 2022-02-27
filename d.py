import os

for path, direct, files in os.walk("C:/Users/고객님/Desktop/"):
    print(path)
    print(direct)
    print(files)