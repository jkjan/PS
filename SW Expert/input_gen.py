from random import randint


def get_input_case():
    D = randint(3, 13)
    W = randint(1, 20)
    K = randint(1, D)

    film = [[0 for _ in range(W)] for _ in range(D)]
    input_text = open("2112_input.txt", "wt")
    input_text.write("%d %d %d\n" % (D, W, K))

    for i in range(D):
        for j in range(W):
            film[i][j] = randint(0, 1)
            input_text.write("%d " % film[i][j])
        input_text.write("\n")

    input_text.close()

    return D, W, K, film