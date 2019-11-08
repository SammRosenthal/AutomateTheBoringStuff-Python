def hourglassSum(arr):
    answer = 0
    current = 0
    dirty = False

    for i in range(4):
        for j in range(4):
            current = getSum(arr, i, j)
            if current > answer or not dirty:
                dirty = True
                answer = current
                current = 0
    return answer

def getSum(arr, i, j):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

