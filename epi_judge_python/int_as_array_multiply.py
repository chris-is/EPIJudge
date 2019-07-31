from test_framework import generic_test


def multiply(num1, num2):

    if(len(num1) > len(num2)):
        tmp = num2
        num2 = num1
        num1 = tmp
    else:
        tmp = num1
        num1 = num2
        num2 = tmp

    bottom_num = num1[::-1]
    bottom_num[-1] = abs(bottom_num[-1])
    upper_num = num2[::-1]
    upper_num[-1] = abs(upper_num[-1])


    result = 0
    shift_by_ten = 1
    for index_i, i in enumerate(bottom_num):
        carry_over = 0
        tmp = 0
        remainder = 0
        for index_j, j in enumerate(upper_num):
            i_times_j = i*j
            sum = i_times_j + carry_over

            if(sum > 9):
                carry_over = sum // 10
                remainder = sum % 10
            else:
                carry_over = 0
                remainder = sum

            if (index_j == len(upper_num) - 1):
                tmp += sum * (10**index_j)
            elif (index_j == 0):
                tmp += remainder
            else:
                tmp += remainder * (10**index_j)

        tmp *= shift_by_ten
        result += tmp
        shift_by_ten *= 10

    if (num1[0] < 0 and num2[0] > 0) or (num1[0] > 0 and num2[0] < 0):
         result = -result

    res = [int(x) for x in str(abs(result))]
    if result < 0:
        res[0] = -res[0]
    print(result)
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       "int_as_array_multiply.tsv",
                                       multiply))