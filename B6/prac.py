
try:
    # input
    N = int(input())
    if N <= 0:
        raise ValueError("N must be a positive integer")
    arr = input().split(" ")
    if len(arr) != N:
        raise ValueError("The number of elements does not match N")
    # yeu cau danh sach so int
    arr = [int(x) for x in arr]
    target = int(input())

    # thuc thi thuat toan
    arr.sort()
    result = binary_search_loop(arr, target)
    print(result)
except Exception as e:
    print("Error:", e)
finally:
    print("End")