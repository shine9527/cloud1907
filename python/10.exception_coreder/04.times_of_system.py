import datetime

username = ['tom', 'jerry', 'hale']
password = {'tom': '123456', 'jerry': 'jerry123', 'hale': 'hale123'}


def userLoad(func):
    def load(user, passwd):
        if user in username:
            if password[user] == passwd:
                func(user, passwd)
            else:
                print('password error!')
        else:
            print('Failed')
    return load


@userLoad
def myFunc(user, passwd):
    print('''
    user: {}
    passwd: {}
    load once of: {}'''.format(user, passwd, datetime.datetime.now()))


username = input('username: ')
passwwd = input('password: ')
myFunc(username, passwwd)
