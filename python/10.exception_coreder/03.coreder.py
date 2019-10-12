# def mycorder(function_name):
#     def wrapper(message):
#         print('start....')
#         function_name(message)
#         print('stop....')
#     return wrapper
#
#
# @mycorder
# def get(info):
#     print(info)


def mycorder(function_name):
    def wrapper(*args, **kwargs):
        print('start....')
        function_name(*args, **kwargs)
        print('stop....')
    return wrapper


@mycorder
def get(info, opera, string):
    print(info, opera, string)

@mycorder
def put(info):
    print(info)

@mycorder
def gpfile(*args, **kwargs):
    print(args, kwargs)


get('hello', 'kitty', 'hao')
put('hao')
gpfile('hello', 'kitty', 'hao', name='tom', age=18, sex='man')
