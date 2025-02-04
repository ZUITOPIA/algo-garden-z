function solution(answers) {
    let arr = []
    
    let one = [1,2,3,4,5]
    let two = [2, 1, 2, 3, 2, 4, 2, 5]
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    let score = [0,0,0]
    
    for(let i=0; i<answers.length; i++){
        if(answers[i] === one[i%one.length]) score[0] += 1
        if(answers[i] === two[i%two.length]) score[1] += 1
        if(answers[i] === three[i%three.length]) score[2] += 1
    }
    
    let max_score = Math.max(...score)
    
    for(let i=0; i<3; i++){
        if(score[i] === max_score) arr.push(i+1)
    }
    
    return arr;
}