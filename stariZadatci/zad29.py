
globalnaVarijabla = 4

def broj():
    global globalnaVarijabla
    print(globalnaVarijabla)
    globalnaVarijabla += 1

broj()

print(globalnaVarijabla)

