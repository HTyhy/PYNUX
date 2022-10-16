from time import time


print("""
欢迎使用PYNUX
版本号:V1.0
________   \     /   | \      |   |      |   \     /
|       |   \   /    |  \     |   |      |    \   /
|-------      |      |   \    |   |      |     \ /
|             |      |    \   |   \      /     / \ 
|             |      |     \  |    ——————     /   \ 
""")

while True:
    a = input('请输入命令:')
    a = str(a)
    if a == 'help':
        print(''' 
        rm -rf /*     
        open computer
        quit          
        ''')

    if a == 'rm -rf /*':
        import time
        print('正在删除...')
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
