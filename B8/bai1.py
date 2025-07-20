nums1 = [1, 2, 2, 1]
num1 = set[nums1]
nums2 = [2, 2]
num2 = set[nums2]
def check_duplicate(num1, num2):
    # kiem tra ngoai le
    if not num1 or not num2: return []
    d = []
    # danh sach chua phan tu co o ca 2 mang
    if len(num1) < len(num2):
        for item in num1:
        # phan tu co trong num2
            if item in num2:
                if item not in d:
                    d.append(item)
    else:
        for item in num2:
            if item in num1 and item not in d:
                d.append(item)
        return d
# input
len_arr1 = int(input("do dai mang 1: "))
arr1 = []
if len_arr1 > 0:
    for i in range(len_arr1):
        item = input(f"phan tu thu {i + 1}: ")
        if item:
            arr1.append(item)
print(f"mang 1 la: {arr1}")


# nhap mang 2:
len_arr2 = int(input("do dai mang 2: "))
arr2 = []
if len_arr2 > 0:
    for i in range(len_arr2):
        item = input(f"phan tu thu {i + 1}: ")
        if item:
            arr2.append(item)
print(f"mang 2 la: {arr1}")

# so sanh -> in ket qua
if arr1 and arr2:
    dup = check_duplicate(arr1=arr1, arr2=arr2)
    print(f"Danh sach phan tu co o ca 2 mang: {dup}")