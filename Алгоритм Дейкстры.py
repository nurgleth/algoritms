# создание  Графа
# для реализации этого примера понадобиться три хеш-таблицы

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6  # хеш таблийца в таблитце с соседями узла и их стоймостями
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# хеш таблица для хранения стоймости всх узлов
infinity = float("inf")  # бесконечность
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# хеш таблица для родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []  # массив для отслеживания всех уже обработаных узлов графа


def find_lowest_cost_node(costs):
    """
    находит узел с наименьшей стоймостью среди необработанных
    :param costs:
    :return:
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # перебрать все узлы (а и б)
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если этот узел с наименьшей стоймостью из уже выведеных
            # и он еще не был обработан
            lowest_cost = cost  # он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # найти узел с наименьшей соимостью среди необработанных

while node is not None:  # если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost  # обновить стоимость для этого узла
            parents[n] = node  # этот узел становитсся новым родителем для соседа
    processed.append(node)  # узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # найти следующий узел для обработаки и повторить цикл
