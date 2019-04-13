# Example 1: valid credit card number
# 4539 1488 0343 6467
# The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling
# 4_3_ 1_8_ 0_4_ 6_6_
# If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:
# 8569 2478 0383 3437
# Then sum all of the digits:
# 8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
# If the sum is evenly divisible by 10, then the number is valid. This number is valid!


class Luhn(object):
    def __init__(self, card_num):
        self.card_num = [int(num) for num in card_num if num.isdigit()]

    def is_valid(self):
        if len(self.card_num) == 1:
            return False

        nums = []
        index = 0
        for num in self.card_num:
            num = self.__calculate_luhn_number(index, num)
            nums.append(num)
            index += 1

        return sum(nums) % 10 == 0

    def __calculate_luhn_number(self, index, num):
        if index % 2 == 0:
            num *= 2
        if num > 9:
            num -= 9
        return num
