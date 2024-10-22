spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 'bananas']
spam3 = ['apples']
spam4 = []


def comma(arr):
    s = ''

    if len(arr) == 0:
        return s
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        s += arr[0] + ' and ' + arr[1]
    else:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                s += 'and ' + arr[i]
            else:
                s += arr[i] + ', '

    return s


print(comma(spam))
print(comma(spam2))
print(comma(spam3))
print(comma(spam4))
