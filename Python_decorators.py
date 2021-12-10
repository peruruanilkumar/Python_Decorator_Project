def log_message(func):
    def inner(*ar, **kw):
        result = func(*ar, **kw)
        print(result)
        return result
    return inner

@log_message
def a_function_that_returns_a_string():
    yield "a string"
    #return "a string"

@log_message
def a_function_that_returns_a_strings_with_a_newline(s):
    yield "{}\n".format(s)
    #return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    yield string
    #return string

a = a_function_that_returns_a_string()
a1=str(next(a))
print(a1)

ss=str(input("enter a string to return withnew line :"))
b2=a_function_that_returns_a_strings_with_a_newline(ss)
b1=str(next(b2))
print(b1,"\n")


string1=str(input("enter a another string :"))
ans=a_function_that_returns_another_string(string1)
ans1=(next(ans))
print(ans1)

f=open("decorator_logs.txt","w")

f.write("{}\n".format(a1))
print("\n")
f.write("{}\n".format(b1))
f.write(ans1)
f.close()