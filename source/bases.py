#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number

    str_num = str_num[::-1]
    result = 0
    for i in range(0,len(str_num)):
        cur_num = str_num[i]
        cur_num = int(cur_num)
        result +=  cur_num*(base**i)
        # print cur_num
    print result

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number


def main():
    decode('101',2)
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # if len(args) == 3:
    #     str_num = args[0]
    #     base1 = int(args[1])
    #     base2 = int(args[2])
    #     result = convert(str_num, base1, base2)
    #     print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    # else:
    #     print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
