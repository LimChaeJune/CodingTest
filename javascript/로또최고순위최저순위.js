function solution(lottos, win_nums) {
    let min_result = 7;
    let max_result = 7;
    
    lottos_slide = lottos.slice();
    winnums_slide = win_nums.slice();
            
    
    for (element of lottos_slide){
      if (element === 0){
          continue;
      }  
      else{
          for (win_num of winnums_slide){
            if (win_num === element){
               min_result -= 1;              
            }
          }         
      }
    }
    
    
    // max
    for (element of lottos_slide){
      if (element === 0){
          max_result -= 1;
      }  
      else{
          for (win_num of winnums_slide){
            if (win_num === element){
               max_result -= 1;
            }
          }         
      }
    }
    
    min_result = min_result === 7 ? 6 : min_result
    max_result = max_result === 7 ? 6 : max_result
    
    var answer = [max_result, min_result];
    
    
    return answer;
}