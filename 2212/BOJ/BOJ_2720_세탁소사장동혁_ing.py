T = int(input())

for _ in range(T):
    C = int(input())
    QDNP = [0, 0, 0, 0]
    # Q = 25, D = 10, N = 5, P = 1
    QDNP[0] = C // 25
    C -= QDNP[0] * 25
    QDNP[1] = C // 10
    C -= QDNP[1] * 10
    QDNP[2] = C // 5
    C -= QDNP[2] * 5
    QDNP[3] = C

    print(*QDNP)