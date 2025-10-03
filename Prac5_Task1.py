#code for the given question

def lcs(a, b):
    m = len(a)
    n = len(b)


    c = [[{'val': 0, 'dir': ''} for _ in range(n + 1)] for _ in range(m + 1)]


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j]['val'] = c[i - 1][j - 1]['val'] + 1
                c[i][j]['dir'] = 'd'
            else:
                if c[i - 1][j]['val'] >= c[i][j - 1]['val']:
                    c[i][j]['val'] = c[i - 1][j]['val']
                    c[i][j]['dir'] = 'u'
                else:
                    c[i][j]['val'] = c[i][j - 1]['val']
                    c[i][j]['dir'] = 's'


    def construct_lcs(c, a, i, j):
        if i == 0 or j == 0:
            return ""
        if c[i][j]['dir'] == 'd':
            return construct_lcs(c, a, i - 1, j - 1) + a[i - 1]
        elif c[i][j]['dir'] == 'u':
            return construct_lcs(c, a, i - 1, j)
        else:
            return construct_lcs(c, a, i, j - 1)

    lcs_str = construct_lcs(c, a, m, n)


    print("Cost matrix (val):")
    for i in range(m + 1):
        print([c[i][j]['val'] for j in range(n + 1)])

    print("\nDirection matrix (dir):")
    for i in range(m + 1):
        print([c[i][j]['dir'] if c[i][j]['dir'] else '-' for j in range(n + 1)])

    print("\nLength of LCS:", c[m][n]['val'])
    print("LCS:", lcs_str)
    return lcs_str


X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"

lcs(X, Y)
