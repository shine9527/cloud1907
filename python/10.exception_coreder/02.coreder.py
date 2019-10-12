def mycorder(function_name):
    def wrapper():
        print('running start.....')
        function_name()
        print('running stop......')
    return wrapper


@mycorder
def get():
    print('hello world')


get()
