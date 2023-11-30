#*args

# def student(*names):
#     print("my name is", names[1])
# student('A',"B","c")

# def add(*nums):
#     sum=0
#     for i in nums:
#       sum+=i
#     print(sum)
# add(1,2,3,4)

#**kwargs
# def calcu(**kwargs):
#     total=1
#     for n in kwargs.values():
#       total*=n
#     print(total)
# calcu(num1=2,num2=3, num3=4)

#*args and **kwargs
# def calcu(*args, **kwargs):
#     total=0
#     for n in kwargs.values():
#         total+=n
#     for i in args:
#         total*=i
#     print(total)

# calcu(1,2,3,4,5,num1=2,num2=3)


#break and continue
# 123/45
# i=0
# while i<6:
#     i+=1
#     if i==4:
#         break
#     print(i)

#1245
# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#     print(i)


#return and print
# def add(a,b):
#     c=a+b
#     print(c)
# add(2,3)


# def add(a,b):
#     c=a+b
#     return c
# print(add(2,3))

# x=lambda a,b,c,d:(a+b)*c-d

# print(x(2,3,4,5))

# t=lambda a,b:a*b

# print(t(4,5))

t=lambda a:10+a
print(t(2))
































