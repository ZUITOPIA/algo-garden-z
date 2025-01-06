def solution(ingredient):
    arr = []
    count = 0
    i = 0
    
    while i < len(ingredient):
        arr.append(ingredient[i])
        i += 1
        
        if len(arr) >= 4 and arr[-4:] == [1,2,3,1]:
            count += 1
            
            for _ in range(4):
                arr.pop()
        
    return count