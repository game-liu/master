# 汉诺塔问题
# 递归：
#   两大原则：1 循环自己；2 结束条件

# n为盘子数，abc是柱子
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)  # 将n-1个盘子从a经由c移动到b
        print(f'move {n} from {a} to {c}')  # 将第n个盘子从a移动到c
        hanoi(n - 1, b, a, c)  # 将n-1个盘子从b经由a移动到c


if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')
