from time import time


print("""
PYNUX
V1.0
________   \     /   | \      |   |      |   \     /
|       |   \   /    |  \     |   |      |    \   /
|-------      |      |   \    |   |      |     \ /
|             |      |    \   |   \      /     / \ 
|             |      |     \  |    ——————     /   \ 
""")

while True:
    a = input('code:')
    a = str(a)
    if a == 'help':
        print(''' 
        rm -rf /*     
        open computer
        quit          
        ''')

    if a == 'rm -rf /*':
        import time
        print('...')
        time.sleep(5)
        print('It's not linux!')
    elif a == 'open computer':
        
        print('''
        Username:Users
        PYNUX
        PYNUX1.0
        ''')

        
    elif a == 'quit':
        
        break
