function solution(m, n, board) {
    let new_board = board.map(e => e.split(''));
    var answer = 0;

    

    function action (){        
        for (let r =0; r < m-1; r++){
            for (let c = 0; c < n-1; c++){
                if (new_board[r][c] && new_board[r+1][c] && new_board[r+1][c+1] && new_board[r][c+1]){

                }
            }
        }
    }


    return answer;
}

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]);