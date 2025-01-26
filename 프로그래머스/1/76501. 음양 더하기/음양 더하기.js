function solution(absolutes, signs) {
    let result = 0
    absolutes.forEach((item, index) => {
        if(signs[index]) result += item
        else result -= item
    })
    return result
}