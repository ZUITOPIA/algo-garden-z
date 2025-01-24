function solution(nums) {
    let set_nums = new Set(nums)
    
    let select_cnt = nums.length / 2

    return Math.min(set_nums.size, select_cnt);
}