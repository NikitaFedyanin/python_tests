from datetime import datetime
"""
Дан массив прямых связей между дронами - кто с кем дружит. Каждая такая связь представлена,
 как строка с двумя именами разделеными дефисом. Для примера: "dr101-mr99" означает
 что dr101 и mr99 дружат между собой. Кроме этого даны два имени. Попробуйте определить,
 связаны ли они через других дронов, вне зависимости от глубины этих связей
"""
start_time = datetime.now()


def check_connection(network, first, second):

    friends = [i.split('-') for i in network]
    connections = [[] for i in network]
    all_drones = set([j for i in network for j in i.split('-')])
    usefull_drones = []
    connect = False

    for i in range(len(connections)):
        for count in friends:
            for dron in friends:
                if dron[0] in connections[i] and dron[1] not in connections[i]:
                    connections[i].append(dron[1])
                    usefull_drones.append(dron[1])
                    continue
                if dron[1] in connections[i] and dron[0] not in connections[i]:
                    connections[i].append(dron[0])
                    usefull_drones.append(dron[0])
                    continue
                if connections[i] == [] and dron[0] not in usefull_drones and dron[1] not in usefull_drones:
                    connections[i].append(dron[0])
                    connections[i].append(dron[1])
                    usefull_drones.append(dron[0])
                    usefull_drones.append(dron[1])
            if set(usefull_drones) == all_drones:
                break


    connections = [i for i in connections if i != []]
    for connection in connections:
        if first in connection and second in connection:
            connect = True
    return connect

check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super", "dr101-src", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "mr99-out00", "dr101-out00", "src-out01", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout"),
        "scout2", "scout3")
print("--- %s seconds ---" % str((datetime.now() - start_time)))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
