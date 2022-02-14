

def longest_palindromic_substring(s):

    N = len(s)

    dp = [[False] * N for _ in range(N)]
    # print(dp)

    for i in range(N):
        dp[i][i] = True
    
    best = f'{s[0]}'
    # print(dp)

    for j in range(1,N):
        print(f"j:{j}")
        for i in range(j-1,-1,-1):
            print(f"i:{i}")
            if s[i] == s[j] and ( i+1 == j or dp[i + 1][j-1]):
                dp[i][j] = True
                if len(best) < j-i + 1:
                    best = s[i:j + 1]

    return best

print(longest_palindromic_substring('ABBA'))

#SOL 2

def longestPalindrome(s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                print('start: %s, end: %s' % (start, end))
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]
    
    
# print(longestPalindrome("ABB"))