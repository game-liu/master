# 广度优先

# 图
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):  # s为起始点
    queue = []
    queue.append(s)  # 把根节点放进队列
    seen = set()  # 将根节点加入到集合中，记录已经访问过哪些节点
    seen.add(s)
    while len(queue):  # 当队列还有数据时
        vertex = queue.pop(0)  # 从队列中拿出一个节点
        nodes = graph[vertex]  # 找到该节点的所有节点
        for w in nodes:
            if w not in seen:  # 如果w还没遍历过
                queue.append(w)
                seen.add(w)
        print(vertex)


if __name__ == '__main__':
    BFS(graph, "A")
