# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    first_num  = int(sys.argv[1])
    second_num = int(sys.argv[-1])
    sign = sys.argv[2]
    if sign == '+':
        return first_num + second_num
    if sign == '-':
        return first_num - second_num
    if sign == '*':
        return first_num * second_num
    if sign == '/':
        return first_num / second_num
    return None


if __name__ == "__main__":
    print(main())
