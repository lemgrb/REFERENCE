
def main():
    foo(username = 'lem', password = 'Passw0rd')

def foo(**args):
    if len(args):
        for i in args:
            print(f'{i}={args[i]}')
    else:
        print('Empty args')


if __name__ == "__main__" : main()
