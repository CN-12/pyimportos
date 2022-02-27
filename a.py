import os

현위치 = os.getcwd()
print(현위치)
os.chdir("C:/")
바뀐위치 = os.getcwd()
print(바뀐위치)
os.mkdir("C:/Users/고객님/Desktop/vaction/py/um")
print(os.listdir("C:/Users/고객님/Desktop/vaction/py/")) #리스트 형식으로 출력
os.makedirs("C:/Users/고객님/Desktop/vaction/py/um/jun/sik")
print(os.listdir("C:/Users/고객님/Desktop/vaction/py/um/jun/sik"))
os.remove("C:/Users/고객님/Desktop/vaction/py/um/jun/sik/test.txt")