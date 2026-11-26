from textnode import *

def main():
    tn = TextNode("hi", TextType.PLAIN)
    tn1 = TextNode("hi", TextType.BOLD, "https://www.boot.dev")

    print(tn.__eq__(tn1))
    print(tn.__repr__())
    print(tn1.__repr__())

main()