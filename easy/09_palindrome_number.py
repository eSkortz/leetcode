def solution(x: int) -> bool:
    x = str(x)
    counter = 0
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            counter = 1
            break
    if counter == 0:
        return True
    return False