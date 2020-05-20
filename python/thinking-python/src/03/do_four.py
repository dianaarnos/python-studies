def do_twice(function, value):
    function(value)
    function(value)

def print_spam():
    print('spam')

def print_twice(value):
    print(value)
    print(value)

def do_four(function, value):
    do_twice(function, value)
    do_twice(function, value)

do_four(print_twice, 'spam')