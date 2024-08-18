arr = list(map(int, input().split(" ")))
ascArr = sorted(arr[:])
desArr = sorted(arr[:], reverse=True)

if arr == ascArr:
    print("ascending")
elif arr == desArr:
    print("descending")
else:
    print("mixed")
