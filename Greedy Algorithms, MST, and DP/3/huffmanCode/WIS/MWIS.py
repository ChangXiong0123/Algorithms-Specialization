# Maximum Weighted Independent set
# dynamic programming

def read_file(file):
    f = open(file, 'r').readlines()
    weights = [int(x) for x in f[1:]]
    nums = int(f[0])
    weights.insert(0, 0)
    return weights, nums


def wis_dp(weights, nums):
    # run the dynamic programming algorithm
    # find the optimal value
    A = [0]*(nums+1)
    wis = []
    A[0] = 0
    A[1] = weights[1]
    for i in range(2, nums+1):
        A[i] = max(A[i-1], A[i-2]+weights[i])

    # run the reconstruction procedure
    # find the optimal solution by tracing back
    i = nums
    while i >= 1:
        if A[i-1] > A[i-2] + weights[i]:
            i -= 1
        else:
            wis.append(i)
            i -= 2
    return A, wis


if __name__ == "__main__":
    weights, nums = read_file(
        'Greedy Algorithms, MST, and DP/3/huffmanCode/WIS/mwis.txt')

    A, wis = wis_dp(weights, nums)
    vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    print([int(v in wis) for v in vertices])
