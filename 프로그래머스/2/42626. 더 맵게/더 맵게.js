class Heap {
    constructor(){
        this.heap = [] // 선언 및 초기화
    }
    
    swap(i,j){
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]] // 구조분해할당
    }
    
    getParentIndex(i){
        return Math.floor((i-1)/2) // 루트의 부모는 존재하지 않으므로 음수 return
    }
    getLeftChildIndex(i){
        return 2*i + 1
    }
    getRightChildIndex(i){
        return 2*i + 2
    }
    
    heappush(v){
        this.heap.push(v) // python의 heapq.heappush와 유사하게
        this.bubbleUp()
    }
    
    bubbleUp(){ // 부모와 비교하며 위치를 상향 조정하는 함수
        let index = this.heap.length-1
        let parent_index = this.getParentIndex(index)
        
        while(index > 0 && this.heap[index] < this.heap[parent_index]){ // 부모가 더 크다면 교환
            this.swap(index, parent_index)
            index = parent_index
            parent_index = this.getParentIndex(index)
        }
    }
    
    heappop(){
      if(this.heap.length === 0) return null
      if(this.heap.length === 1) return this.heap.pop()
        
      let min = this.heap[0]
      this.heap[0] = this.heap.pop()
      this.bubbleDown(0)

      return min
      
    }
    
    bubbleDown(index){ // 자식과 비교하며 위치를 하향 조정하는 함수
        let left = this.getLeftChildIndex(index)
        let right = this.getRightChildIndex(index)
        
        let min_index = index // 현재 인덱스를 가장 작은 인덱스 값으로 초기화하고 시작
        
        if(left < this.heap.length && this.heap[left] < this.heap[min_index]) min_index = left
        if(right < this.heap.length && this.heap[right] < this.heap[min_index]) min_index = right
        
        if(min_index !== index){
            this.swap(min_index, index)
            this.bubbleDown(min_index)
        }
    }
    
}

function solution(scoville, K) {
    let count = 0
    
    let heap = new Heap()
    
    scoville.forEach((item) => heap.heappush(item))
    
    while(heap.heap[0] < K){
        if (heap.heap.length < 2) return -1; 
        
        let a = heap.heappop()
        let b = heap.heappop()
        let dish = a + b*2
        
        heap.heappush(dish)
        count++
    }
    
    return count
}




