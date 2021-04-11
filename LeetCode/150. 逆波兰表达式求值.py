"""
2021-03-20 周六
根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

 

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
 

示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

"""
from typing import List


class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))  # int 再不是数字的时候报错
            except:
                num1 = stack.pop()  # 注意弹出的和计算的顺序
                num2 = stack.pop()
                stack.append(self.cal(num2, num1, token))
        return stack[0]

    def cal(self, num1, num2, token):
        if token == '+':
            return num1 + num2
        elif token == '-':
            return num1 - num2
        elif token == '*':
            return num1 * num1
        else:
            return int(num1 / float(num2))  # 特别注意除法


if __name__ == '__main__':
    tokens = ["4", "13", "5", "/", "+"]
    ret = Solution().evalRPN(tokens)
    print(ret)
