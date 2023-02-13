# python3
import requests

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code her
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1         
            opening_brackets_stack.pop()
    if len(opening_brackets_stack) == 0:
        return None                               
    return opening_brackets_stack[-1].position

def main():
    text = input()
    url = 'https://github.com/DA-testa/steks-un-iekavas-Algerts-Kligulis/blob/main/test/1'
    if text.startswith('I'):
        text = input()
    else:
        text = requests.get(url).text        
    mismatch = find_mismatch(text)
    if mismatch is None:
        print("Success")   
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
