import numpy as np


def main():
    nn = int(input("\nEnter Number of Nodes: "))
    graph = np.full((50, 50), -1, dtype=int)

    ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    for i in range(nn):
        for j in range(nn):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] == -1:
                t = int(input(f"\nEnter Distance between {ch[i]} - {ch[j]}: "))
                graph[i][j] = graph[j][i] = t

    via = np.full((50, 50), -1, dtype=int)

    print("\nAfter Initialization")

    for i in range(nn):
        print(f"\n{ch[i]} Table")
        print("Node\tDist\tVia")
        for j in range(nn):
            print(f"{ch[j]}\t{graph[i][j]}\t{via[i][j]}")

    sh = np.full((50, 50, 50), -1, dtype=int)
    for i in range(nn):
        for j in range(nn):
            for k in range(nn):
                if (graph[i][j] > -1) and (graph[j][k] > -1):
                    sh[i][j][k] = graph[j][k] + graph[i][j]
                else:
                    sh[i][j][k] = -1

    for i in range(nn):
        print(f"\n\nFor {ch[i]}")
        for j in range(nn):
            print(f"\nFrom {ch[j]}")
            for k in range(nn):
                print(f"{ch[k]} {sh[i][j][k]}")

    final = np.copy(graph)
    for i in range(nn):
        for j in range(nn):
            via[i][j] = i
            for k in range(nn):
                if (final[i][j] > sh[i][k][j] or final[i][j] == -1) and sh[i][k][j] > -1:
                    final[i][j] = sh[i][k][j]
                    via[i][j] = k

            if final[i][j] == -1:
                for k in range(nn):
                    if final[i][k] != -1 and final[k][j] != -1:
                        if final[i][j] == -1 or final[i][j] > final[i][k] + final[k][j]:
                            if final[i][k] + final[k][j] > -1:
                                final[i][j] = final[i][k] + final[k][j]
                                via[i][j] = k

    print("\nAfter Update:")

    for i in range(nn):
        print(f"\n{ch[i]} Table")
        print("Node\tDist\tVia")
        for j in range(nn):
            via_node = '-' if i == via[i][j] else ch[via[i][j]]
            print(f"{ch[j]}\t{final[i][j]}\t{via_node}")


if __name__ == "__main__":
    main()
