def tim_phan_tu_xuat_hien_nhieu(nums):

    n = len(nums)
    

    if n == 0:
        return []

    threshold = n // 3

    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    result = []
    for num, count in frequency_map.items():
        if count > threshold:
            result.append(num)

    return result
#test
nums1 = [3, 2, 3]

print(f"Mảng: {nums1}")
print(f"Các phần tử xuất hiện nhiều hơn n/3 lần: {tim_phan_tu_xuat_hien_nhieu(nums1)}")


print("-" * 20)

nums2 = [1, 1, 1, 3, 3, 2, 2, 2]

print(f"Mảng: {nums2}")
print(f"Các phần tử xuất hiện nhiều hơn n/3 lần: {tim_phan_tu_xuat_hien_nhieu(nums2)}")
