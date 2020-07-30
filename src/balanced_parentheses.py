
"""

Given a string which contains parentheses, write a program to validate
whether it has balanced parentheses or not
if it is balanced (well formed), return true, otherwise false

E.g.
(())((())) ( )  - true
( () )((())) (  - false
()    - true
)(    - false

"""

# (5+6) *(7+8) / (4-3)
# validate the input
# parse the input

# need stack data structure
# strategy
# ( -- open parenthesis --> push on the stack
# ) -- pop from the stack
# once the entire string is processes, check if stack is empty or not
# Error conditions --
# Assumption:
#   ()()()
"""
what if input contains:

([](){}()[]) -- well formed

[] -- well formed

([)(){}()[]) -- not well formed
"""

from stack import Stack


def validate_parentheses(str):
    if len(str) == 0:
        return True

    stack = Stack()  # create a stack var

    for c in str:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.is_empty():
                return False
            stack.pop()
        else:
            raise ValueError("Invalid input!")

    # if stack.is_empty():
    #     return True
    # else:
    #     return False

    return stack.is_empty()


def validate_parentheses_for_any_chars(str):
    if len(str) == 0:
        return True

    stack = Stack()  # create a stack var

    for c in str:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.is_empty():
                return False
            stack.pop()

    # if stack.is_empty():
    #     return True
    # else:
    #     return False

    return stack.is_empty()


def validate_parentheses_all(str):
    # set
    open_brackets = {'(', '[', '{'}
    closed_brackets = {')', ']', '}'}

    # dict
    closed_open = {')': '(',
                   ']': '[',
                   '}': '{'
                   }

    if len(str) == 0:
        return True

    stack = Stack()

    for c in str:  # for each character
        if c in open_brackets:
            stack.push(c)
        elif c in closed_brackets:
            if stack.is_empty():
                return False

            popped_bracket = stack.pop()  # save the bracket
            # compare with corresponding bracket from the dictionary
            if popped_bracket != closed_open[c]:
                return False

    return stack.is_empty()


print(validate_parentheses_all("(){}[]"))        # true
print(validate_parentheses_all("(([]){}[])")) # true
print(validate_parentheses_all("(([){}[])")) # false
print(validate_parentheses_all("([])")) # true
print(validate_parentheses_all("[        avbc   ]")) # true


#
# str1 = "(())((()))()"
# print(validate_parentheses(str1))
#
# str1 = "("  # corner case, edge case
# print(validate_parentheses(str1))
#
# str1 = ""  # corner case, edge case
# print(validate_parentheses(str1))
#
# str1 = ")"  # corner case, edge case
# print(validate_parentheses(str1))
#
# str1 = "(())(()))()"
# print(validate_parentheses(str1))
#
# # str1 = "(())((a(d)x))()"
# # print(validate_parentheses(str1))
#
# print(validate_parentheses_for_any_chars("(5+6) *(7+8) / (4-3)"))
# print(validate_parentheses_for_any_chars("(5+6) *(7+8) / (4-3"))
