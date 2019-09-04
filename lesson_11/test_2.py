'''Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и *3.'''

def count_trajectories(N):
    K = [0, 1, 2] + [0]*N
    for i in range(3, N+1):
        if i%3==0:
            K[i] = K[i-1] + K[i-2] + K[i//3]
        else:
            K[i] = K[i-1] + K[i-2]
    return K[N]

print(count_trajectories(10))