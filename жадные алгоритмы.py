# O(n^2)
# список штатов

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# список станций окрывающие различные штаты
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}


final_station = set()  # итоговый набор станций
while states_needed:
    best_station = None  # станция обслуживающая больше всего штатов
    states_covered = set()  # содержит все штаты обслуживаемые этой станцией которые еще не выходят в текущее покрытие
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered  # те штаты которые входят в зону покрытия станции больше не нужны
    final_station.add(best_station)
print(final_station)



