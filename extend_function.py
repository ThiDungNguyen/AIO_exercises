def extend_function(x, y):
    "for question 7"
    # Su dung extend de noi y vao x
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

if __name__ == "__main__":
    assert extend_function(list_num1, extend_function(
        list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]

    print(extend_function(list_num1, extend_function(list_num2, list_num3)))