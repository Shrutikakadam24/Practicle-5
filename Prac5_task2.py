def longest_repeating_subsequence(s):
    n = len(s)

    c = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                c[i][j] = 1 + c[i - 1][j - 1]
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])


    lrs = ""
    i = n
    j = n
    while i > 0 and j > 0:
        if c[i][j] == c[i - 1][j - 1] + 1 and s[i - 1] == s[j - 1] and i != j:
            lrs = s[i - 1] + lrs
            i -= 1
            j -= 1
        elif c[i][j] == c[i - 1][j]:
            i -= 1
        else:
            j -= 1

    print(" Matrix :")

    print("      ", end="")
    for j_print in range(n + 1):
        if j_print == 0:
            print(f"{0:3}", end=" ")
        else:
            print(f"{s[j_print-1]:3}", end=" ")
    print()

    for i_print in range(n + 1):
        if i_print == 0:
            print(f"{0:3} ", end="")
        else:
            print(f"{s[i_print-1]:3} ", end="")
        for j_print in range(n + 1):
            print(f"{c[i_print][j_print]:3}", end=" ")
        print()

    print("\nLongest Repeating Subsequence:", lrs)
    return c[n][n]

s = "AABEBCDD"
length = longest_repeating_subsequence(s)
print("Length of Longest Repeating Subsequence:", length)
