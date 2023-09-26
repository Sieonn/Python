# def solution(arr, queries):
arr = [0, 1, 2, 3, 4]	
queries = [[0, 1],[1, 2],[2, 3]]

def solution(arr, queries):
    for i, j in queries:
        for k in range(i, j+1):
            arr[k] = arr[k] + 1
    return arr

    




arr = [0, 1, 2, 3, 4]	
queries = [[0, 1],[1, 2],[2, 3]]
