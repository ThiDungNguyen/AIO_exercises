# question 1.
'''Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1'''


def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list)-k+1):
        sublist = num_list[i:(i+k)]
        print(max(sublist))
        result.append(max(sublist))
    return result


if __name__ == "__main__":
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    print(max_kernel(num_list=[3, 4, 5, 1, -44, 5, 10, 12, 33, 1], k=3))
