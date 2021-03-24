# Алгоритм поиска в ширину скорость выполнения O(V+E) V- количество вершин,E - количество ребер
from collections import deque

# создание графа
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[0] == "a"


def search(name):
    """
    Алгоритм поиска в ширину скорость выполнения O(V+E) V- количество вершин,E - количество ребер
    :param name: имя в графе
    :return: нужное значение
    """
    search_queue = deque()  # создание новой очереди
    search_queue += graph["you"]  # все соседи добавляются в очередь поиска
    searched = [] # для отслеживания укже проверенных людей
    while search_queue:  # пока очередь не пуста
        person = search_queue.popleft()  # из очереди извлекается первый человек
        if not person in searched:
            if person_is_seller(person):  # проверяем является ли он продовцом манго
                print(person + "is a mango seller!")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("you"))