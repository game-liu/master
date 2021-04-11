# 广度优先搜索

def search(name):
    graph = {}
    graph['you'] = ["apple", "banana", "waterflow"]
    graph["apple"] = []
    graph["banana"] = []
    graph["waterflow"] = ["yours"]

    from collections import deque
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:

        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    if 'y' in name:
        return 1
    else:
        return 0


print(search("you"))
