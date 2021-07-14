def jumpingOnClouds(c):
    p = 0
    jump = 0
    
    while p < n - 1:
        if p + 2 < n and c[p+2] == 0:
            jump += 1
            p += 2
        elif p + 1 < n and c[p + 1] == 0:
            jump += 1
            p+=1
    return jump
            