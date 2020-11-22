def addition(num1, num2):
    return num1 + num2


def make_tuple(var1, var2):
    return var1, var2


def make_list(var1, var2):
    return [var1, var2]


def make_dictionary(var1, var2):
    return {"firstVariable": var1, "secondVariable": var2}


int1 = 5
int2 = 10
str1 = "Jan"
str2 = "Man"

print(addition(int1, int2))
print(make_tuple(str1, str2))
print(make_list(str1, str2))
print(make_dictionary(str1, str2))
