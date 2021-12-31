from threading import Thread

def cong(a , b):
    return a + b

thu = Thread(target=cong , args=(2,3 ,))
thu.start()

print(thu.getName())