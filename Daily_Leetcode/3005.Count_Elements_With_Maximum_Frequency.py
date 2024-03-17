from collections import Counter


def maxFrequencyElements(nums):
    # Đếm tần số xuất hiện của mỗi phần tử
    freq_counter = Counter(nums)
    # Tìm giá trị tần số xuất hiện lớn nhất
    max_frequency = max(freq_counter.values())
    # Dùng list comprehension để lấy các phần tử có
    # tần số xuất hiện = max_frequency
    max_freq_elements = [
        num for num, freq in freq_counter.items() if freq == max_frequency
    ]
    # Tính số các phần tử với max_frequency
    total_frequency = max_frequency * len(max_freq_elements)

    return total_frequency


print(maxFrequencyElements([1, 2, 2, 3, 1, 4]))
