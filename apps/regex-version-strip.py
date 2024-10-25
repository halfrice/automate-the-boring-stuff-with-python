import re

# The first problem that comes to mind is this: We need to be able to take a
# user supplied variable and implement it into our code. Can this be done with
# raw strings? If you research about it, you'll find something we haven't seen
# before: We can use f strings in place of rawstrings.


def regexStrip(text, remove='\s'):
    rex = re.compile(f'^({remove})*|({remove})*$')
    res = rex.sub('', text)

    return res


test1 = regexStrip('  Strip whitespace.  ')
test2 = regexStrip('000~!@#$%^&*()_+000000', '0')
test3 = regexStrip(regexStrip('xXx420NoScopeEZMoneySniper420xXx', 'xXx'), '420')
print(test1)
print(test2)
print(test3)
