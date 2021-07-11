def countingValleys(steps, path):
    # Write your code here
    moves = 0
    moves_made = []
    valleys = 0
   
    for step in path:
        if step == 'U':
            moves = moves + 1
        if step == 'D':
            moves = moves -1
        moves_made.append(moves)
    
    i = 0
    # last = len(moves_made)-1
    
    while i < steps:
        if moves_made[i] < 0:
            for j in range(i,steps):
                 if moves_made[j] == 0:
                     valleys = valleys + 1
                     i = j
                     break 
        i = i + 1        
    return valleys        
        