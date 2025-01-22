function solution(participant, completion) {
    
   let hash = new Map()
   
   for(let c of completion){
       hash.set(c, (hash.get(c) || 0) + 1)
   }

   for(let p of participant){
       if(!hash.get(p)) return p
       hash.set(p, hash.get(p)-1)
   } 
   
}