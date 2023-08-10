# def chain_sum(n: int):
#     result = n
#     def wrapper(n2=None):
#         nonlocal result
#         if n2 is None:
#             return result
#         result += n2
#         return wrapper
#     return wrapper


# def chain_sum(n: int):
#     def wrapper(n2=None):
#         if n2 is None:
#             return wrapper.result
#         wrapper.result += n2
#         return wrapper
#     wrapper.result = n
#     return wrapper


# def chain_sum(n: int):
#     def wrapper(n2=None):
#         def inner():
#             wrapper.result += n2
#             return wrapper
#         logic = {
#             type(None): lambda: wrapper.result,
#             int: inner}
#         return logic[type(n2)]()
#     wrapper.result = n
#     return wrapper


# print(chain_sum(1)())
# print(chain_sum(2)(4)())
# print(chain_sum(3)(100)(10)())


# class chain_sum:
#     def __init__(self, number) -> None:
#         self.number = number
    
#     def __call__(self, value=0):
#         return chain_sum(self.number + value)
    
#     def __str__(self) -> str:
#         return str(self.number)
    

class chain_sum(int):    
    def __call__(self, addition=0):
        return chain_sum(self + addition)


print(chain_sum(1))
print(chain_sum(2)(4))
print(chain_sum(3)(100)(10))
