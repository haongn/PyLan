# metaclass là class tạo ra class. 

class Foo: 
    pass 

x = Foo()
print(type(x))    # type của x là Foo
print(type(Foo))  # type của Foo là type 

# tổng quát: type của tất cả các class đều là type 
# type của các built-in class cũng là type 

for t in int, float, dict, list, tuple: 
    print(type(t))

# cuối cùng, type của type cũng là type: 
print(type(type))


# type là một metaclass, và tất cả các classes trong Python đều là instance của type metaclass.

print(type(3))
print(type(['foo', 'bar', 'baz']))
t = (1, 2, 3, 4, 5)
print(type(t))
print(type(Foo()))    # chú ý: Foo() là khai báo một instance rồi




