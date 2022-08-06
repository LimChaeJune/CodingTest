function climbingLeaderboard(ranked, player) {
    
    let result = [];
    let copy_board = [...new Set(ranked)];
    
    for (const play of player){
        if (play >= copy_board[0]){
            result.push(1);
        }
        else if(play <= copy_board[copy_board.length - 1]){
            result.push(copy_board.length + 1);
        }
        else{
            result.push(rankBinarySearch(play, copy_board));
        }

    }

    return result;
    
    function rankBinarySearch(score, arrays){
        let start = 0;
        let end = arrays.length - 1;
        
        while(true){
            let mid = Math.floor((start+end) / 2);
            
            if (arrays[mid] === score){
                return mid + 1;
            }
            else if (arrays[mid] > score && arrays[mid +1] < score){
                return mid + 2;
            }
            else if (arrays[mid] < score && arrays[mid -1 > score]){
                return mid - 1;
            }
            
            if (score < arrays[mid]){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }   
}

function climbingLeaderboard2(scores, alice) {
    let result = [];
    let uniqueScores = [...new Set(scores)];
  for (const score of alice) {
      if (score >= uniqueScores[0]) {
        result.push(1);
      } else if (score < uniqueScores[uniqueScores.length - 1]) {
        result.push(uniqueScores.length + 1);
      } else {
        result.push(rankBinarySearch(score, uniqueScores));
      }
    }
    return result;
  }

}
  function rankBinarySearch(score, uniqueScores) {
    let start = 0;
    let end = uniqueScores.length - 1;
    while (true) {
        let mid = Math.floor((start + end) / 2);
    // base cases
        if (uniqueScores[mid] === score) {
            return mid + 1;
        } 
        else if (uniqueScores[mid] > score && uniqueScores[mid + 1] < score) {
            return mid + 2;
        } 
        else if (uniqueScores[mid] < score && uniqueScores[mid - 1 > score]) {
            return mid - 1;
        }
    // recursion
        if (score < uniqueScores[mid]) {
            start = mid + 1;
        } 
        else {
            end = mid - 1;
        }
    }
  }

console.log(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5 ,25 ,50 ,120]));