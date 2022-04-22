from collections import Counter

r,c,k = map(int, input().split())
r = r-1
c = c-1
board = []
for i in range(3):
  value = list(map(int, input().split()))
  board.append(value)

answer = 0
# 현재 행길이
curr_x = 3
# 현재 열길이
curr_y = 3

def mySort():
  global curr_y
  global curr_x
  global board
  
  # x의 최대 길이
  maxLenx = 0
  # y의 최대 길이
  maxLeny = 0  
  # R연산 - 행의 개수가 열의 개수와 같거나 작을때
  if curr_x >= curr_y:        
    for i in range(curr_x):
      sort_Value = []
      val_cnt = Counter(board[i])        


      for key in val_cnt:
        sort_Value.append((key, val_cnt[key]))          
      sort_Value.sort(key = lambda x: (x[1],x[0]))

      newvalue = []
      for val1 in sort_Value:
        # 0일때는 무시
        if val1[0] == 0:
          continue
        newvalue.append(val1[0])      
        newvalue.append(val1[1])      

      board[i] = newvalue
      maxLenx = max(maxLenx, len(newvalue))

    if maxLenx > 100:
      maxLenx = 100
    
    # 최대 길이로 현재 길이 변경
    curr_y = maxLenx

    # 최대 길이보다 부족하면 0 채워줌
    for k in range(curr_x):
      for _ in range(len(board[k]), maxLenx):
        board[k].append(0)
    
        
  else:
    # transpos한 데이터
    trans = list(map(list, zip(*board)))
    # 정렬 완료된 리스트를 담을 배열
    sorted_val = []

    for i in range(curr_y):
      sort_Value = []
      val_cnt = Counter(trans[i])
          
      for key in val_cnt:
        sort_Value.append((key, val_cnt[key]))                    
      sort_Value.sort(key = lambda x: (x[1],x[0]))
   
      newvalue = []
      for val1 in sort_Value:
        # 0일때는 무시
        if val1[0] == 0:
          continue
        newvalue.append(val1[0])      
        newvalue.append(val1[1])      

      sorted_val.append(newvalue)
      maxLeny = max(maxLeny, len(newvalue))      

    if maxLeny > 100:
      maxLeny = 100

    # 최대 길이보다 부족하면 0 채워줌
    for k in range(len(sorted_val)):
      for _ in range(len(sorted_val[k]), maxLeny):
        sorted_val[k].append(0)

    # 최대 길이로 현재 길이 변경
    curr_x = maxLeny

    board = list(map(list, zip(*sorted_val)))   
      


while True:
  if answer > 100:
    answer = -1
    break 
    
  if r <= curr_x-1 and c <= curr_y-1:  
    # 해당 값이 일치하면 종료
    if board[r][c] == k:
      break  
    
  mySort()    
  answer += 1

print(answer)