def find_lcsubstr(s1, s2):
    # 生成矩阵，方便之后计算，比字符串长度多一列
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    max_len = 0  # 记录最长相同子串，最长匹配长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1  # 相同就加1，否则默认为0
                if max_len < m[i + 1][j + 1]:
                    max_len = m[i + 1][j + 1]  # 最长匹配长度
                    p = i + 1  # 最长匹配在s1中对应的最后一位
    return s1[p - max_len: p], max_len  # 返回最长匹配字符串和最长匹配

    # m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    # mmax = 0  # 最长匹配的长度
    # p = 0  # 最长匹配对应在s1中的最后一位
    # for i in range(len(s1)):
    #     for j in range(len(s2)):
    #         if s1[i] == s2[j]:
    #             m[i + 1][j + 1] = m[i][j] + 1
    #             if m[i + 1][j + 1] > mmax:
    #                 mmax = m[i + 1][j + 1]
    #                 p = i + 1
    # return s1[p - mmax:p], mmax  # 返回最长子串及其长度


"""
[
[0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 1], 
[0, 0, 2, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0], 
[0, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 3, 0]
]
"""

print(find_lcsubstr('abcdfg', 'abdfga'))
