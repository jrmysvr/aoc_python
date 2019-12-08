from day_4.solve import (parse_range,
                         take_while,
                         is_six_digits,
                         is_within_range,
                         has_a_doubled_digit,
                         has_no_decreasing_digits,
                         is_valid_password)


class ParseRangeTests:

    def test_range_values_are_ints(self):
        text = "0-0"
        output = parse_range(text)
        assert isinstance(output[0], int)
        assert isinstance(output[1], int)

    def test_for_0_0(self):
        text = "0-0"
        assert parse_range(text) == (0, 0)

    def test_for_1000_9999(self):
        text = "1000-9999"
        assert parse_range(text) == (1000, 9999)


class TakeWhileTests:

    def test_case_0(self):
        nums = [1, 1, 2, 2, 3, 3, 3]
        assert take_while(nums, nums[0]) == ([1, 1], [2, 2, 3, 3, 3])
        assert take_while(nums, 2) == ([], nums)

    def test_case_1(self):
        nums = [1, 1, 1]
        assert take_while(nums, nums[0]) == ([1, 1, 1], [])


class PredicateTests:

    def test_is_six_digits_truthy(self):
        nums = [111111, 999999]
        for num in nums:
            assert is_six_digits(num)

    def test_is_six_digits_falsy(self):
        nums = [1, 1111111]
        for num in nums:
            assert not is_six_digits(num)

    def test_is_within_range_truthy(self):
        low = 100
        high = 102
        for i in range(low, high + 1):
            assert is_within_range(i, low, high)

    def test_is_within_range_falsy(self):
        low = 100
        high = 102
        diff = high - low
        for i in range(low, high + 1):
            val_high = i + diff + 1
            val_low = i - diff - 1
            assert not is_within_range(val_high, low, high)
            assert not is_within_range(val_low, low, high)

    def test_has_a_doubled_digit_truthy(self):
        nums = [11, 22, 133, 144, 1055, 1661, 7700, 108801]
        for num in nums:
            assert has_a_doubled_digit(num)

        nums = [11222, 11122, 33344555]
        for num in nums:
            assert has_a_doubled_digit(num)

    def test_has_a_doubled_digit_falsy(self):
        nums = [1, 2, 13, 45, 501, 12345, 98707]
        for num in nums:
            assert not has_a_doubled_digit(num)

        nums = [111, 1222, 33331]
        for num in nums:
            assert not has_a_doubled_digit(num)

    def test_has_no_decreasing_digits_truthy(self):
        nums = [11, 123, 345, 445566, 678888999]
        for num in nums:
            assert has_no_decreasing_digits(num)

    def test_has_no_decreasing_digits_falsy(self):
        nums = [10, 132, 453, 4345566, 6788889899]
        for num in nums:
            assert not has_no_decreasing_digits(num)


class CheckPasswordTests:

    def test_case_0(self):
        test_password = 112233
        assert is_valid_password(test_password, 0, test_password + 1)

    def test_case_4(self):
        test_password = 111122
        assert is_valid_password(test_password, 0, test_password + 1)

    def test_case_1(self):
        test_password = 223450
        assert not is_valid_password(test_password, 0, test_password + 1)

    def test_case_2(self):
        test_password = 123789
        assert not is_valid_password(test_password, 0, test_password + 1)

    def test_case_3(self):
        test_password = 123444
        assert not is_valid_password(test_password, 0, test_password + 1)
