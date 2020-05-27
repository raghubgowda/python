def find_max(numbers: list):
    max_num = 0
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num
