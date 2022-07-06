def factorial(n): 
    """Return factorial of n."""
    return 1 if n < 2 else n * factorial(n - 1)


result = dir(factorial)
print(result)

# listing attributes of functions that dont exist in plain instances: 
class C: pass
obj = C()
def func(): pass 
result = sorted(set(dir(func)) - set(dir(obj)))
print(result)

# nhu vay la dir của hàm nhiều hơn dir của một instance cụ thể (ở đây là instance obj của class C)
result = factorial.__annotations__
print(result)







