a = 89
def func():
    global a
    a = 90
    print(a)

func()

print(a)
