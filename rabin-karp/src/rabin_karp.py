def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    outputstr = ""
    for i in range(M - 1):
        h = (h * 256) % q
    for i in range(M):
        p = (256 * p + ord(pat[i])) % q
        t = (256 * t + ord(txt[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            if j == M:
                outputstr += str(i) + " "

        if i < N - M:
            t = (256 * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t = t + q
    return outputstr


def main():
    pat = input()
    txt = input()

    q = 101
    print(search(pat, txt, q))


main()
