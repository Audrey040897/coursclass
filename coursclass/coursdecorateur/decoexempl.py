# def verify (func):
#     def new(a,b):
#         if a == b or a > b:
#             return func(a,b)
#         else:
#             return func(b,a)
#     return new 

# @verify 
# def soustractionpositif(a,b):
#     return a - b

# a = 8
# b = 4

# print(soustractionpositif(a,b))
# # exercice1
# def decorateur(func):
#     def new(*args,**kw):
#         c = func(*args,**kw)
#         if isinstance(c,str) or isinstance(c,int):
#             raise Exception(f"Le retour de la fonction {func.__name__} est de type {type(c)}")
#         else:
#             return c
#     return new 
# @decorateur   
# def soustractionpositif(a,b):
#     return a - b 

# a = 3
# b = 5
# print(soustractionpositif(a,b))

nbr = {}
def newdecorateur(p = 2):
    def decorateur(func):
        def neww(*agrs,**kw):
            n = func.__name__
            v = nbr.get(n,0)
            nbr[n] = v + 1
            if p ==nbr[n]
                raise Exception("")
            else:
                return func(*args,**kw)
        return new 
    return decorateur

@newdecorateur
def soustractionpositif(a,b):
    return a - b 

a = 5
b = 8
print(soustractionpositif(a,b))