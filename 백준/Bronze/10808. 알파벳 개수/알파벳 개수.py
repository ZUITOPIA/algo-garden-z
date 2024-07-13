arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

alpha = input().split()

result = 0

for i in range(len(arr)):
    for a in alpha:
        result = a.count(arr[i])
    print(result, end=" ")