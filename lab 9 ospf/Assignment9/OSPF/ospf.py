# import heapq

# class Router:
#     sequence_number = 0

#     def __init__(self, router_id, ip_address):
#         self.router_id = router_id
#         self.ip_address = ip_address
#         self.adjacent_routers = {}

#     def add_adjacent_router(self, router, cost):
#         self.adjacent_routers[router] = cost

#     def send_hello(self):
#         print("Sending Hello from router {} with IP address {}".format(self.router_id, self.ip_address))

#     def send_lsa(self, lsa):
#         print("Sending LSA from router {} with IP address {}:".format(self.router_id, self.ip_address))
#         for l in lsa:
#             print("  Router ID: {}".format(l.router_id))
#             print("  Sequence Number: {}".format(l.sequence_number))
#             print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

#     def send_lsr(self, requested_router_id):
#         print("Sending LSR from router {} with IP address {} to request LSA of router {}".format(self.router_id,
#                                                                                                   self.ip_address,
#                                                                                                   requested_router_id))

#     def send_lsu(self, lsas):
#         print("Sending LSU from router {} with IP address {} with the following LSAs:".format(self.router_id,
#                                                                                                self.ip_address))
#         for l in lsas:
#             print("  Router ID: {}".format(l.router_id))
#             print("  Sequence Number: {}".format(l.sequence_number))
#             print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

#     def request_all_lsas(self):
#         for requested_router_id in self.adjacent_routers.keys():
#             self.send_lsr(requested_router_id)

#     def dijkstra_shortest_path(self):
#         visited = {self.router_id: 0}
#         hq = [(0, self.router_id)]
#         while hq:
#             current_distance, current_router = heapq.heappop(hq)
#             for adjacent_router, cost in self.adjacent_routers.items():
#                 new_distance = current_distance + cost
#                 if adjacent_router not in visited or new_distance < visited[adjacent_router]:
#                     visited[adjacent_router] = new_distance
#                     heapq.heappush(hq, (new_distance, adjacent_router))
#                 for further_router, further_cost in routers[adjacent_router].adjacent_routers.items():
#                     if further_router not in visited or new_distance + further_cost < visited[further_router]:
#                         visited[further_router] = new_distance + further_cost
#                         heapq.heappush(hq, (new_distance + further_cost, further_router))
#         return visited

# class LSA:
#     sequence_number = 0

#     def __init__(self, router_id, link_state_id):
#         LSA.sequence_number += 1
#         self.router_id = router_id
#         self.sequence_number = LSA.sequence_number
#         self.link_state_id = link_state_id

# if __name__ == '__main__':
#     filename = input("Enter the input file name: ")
#     routers = {}

#     with open(filename, 'r') as file:
#         num_routers = int(file.readline().strip())
#         for i in range(num_routers):
#             router_id = file.readline().strip()
#             ip_address = file.readline().strip()
#             routers[router_id] = Router(router_id, ip_address)

#         for router in routers.values():
#             num_neighbors = int(file.readline().strip())
#             for j in range(num_neighbors):
#                 neighbor, cost = file.readline().strip().split()
#                 router.add_adjacent_router(neighbor, int(cost))

#     for router in routers.values():
#         router.send_hello()

#     lsas_to_send = [LSA(router.router_id, router.ip_address) for router in routers.values()]
#     for router in routers.values():
#         router.send_lsa(lsas_to_send)
#         router.send_lsu(lsas_to_send)

#     for router in routers.values():
#         router.request_all_lsas()

#     for router in routers.values():
#         shortest_paths = router.dijkstra_shortest_path()
#         print("Shortest paths from {}: {}".format(router.router_id, shortest_paths))


import heapq

class Router:
    sequence_number = 0

    def __init__(self, router_id, ip_address):
        self.router_id = router_id
        self.ip_address = ip_address
        self.adjacent_routers = {}

    def add_adjacent_router(self, router, cost):
        self.adjacent_routers[router] = cost

    def send_hello(self):
        print("Sending Hello from router {} with IP address {}".format(self.router_id, self.ip_address))

    def send_lsa(self, lsa):
        print("Sending LSA from router {} with IP address {}:".format(self.router_id, self.ip_address))
        for l in lsa:
            print("  Router ID: {}".format(l.router_id))
            print("  Sequence Number: {}".format(l.sequence_number))
            print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

    def send_lsr(self, requested_router_id):
        print("Sending LSR from router {} with IP address {} to request LSA of router {}".format(self.router_id,
                                                                                                  self.ip_address,
                                                                                                  requested_router_id))

    def send_lsu(self, lsas):
        print("Sending LSU from router {} with IP address {} with the following LSAs:".format(self.router_id,
                                                                                               self.ip_address))
        for l in lsas:
            print("  Router ID: {}".format(l.router_id))
            print("  Sequence Number: {}".format(l.sequence_number))
            print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

    def request_all_lsas(self):
        for requested_router_id in self.adjacent_routers.keys():
            self.send_lsr(requested_router_id)

    def dijkstra_shortest_path(self):
        visited = {self.router_id: 0}
        hq = [(0, self.router_id)]
        while hq:
            current_distance, current_router = heapq.heappop(hq)
            for adjacent_router, cost in self.adjacent_routers.items():
                new_distance = current_distance + cost
                if adjacent_router not in visited or new_distance < visited[adjacent_router]:
                    visited[adjacent_router] = new_distance
                    heapq.heappush(hq, (new_distance, adjacent_router))
                for further_router, further_cost in routers[adjacent_router].adjacent_routers.items():
                    if further_router not in visited or new_distance + further_cost < visited[further_router]:
                        visited[further_router] = new_distance + further_cost
                        heapq.heappush(hq, (new_distance + further_cost, further_router))
        return visited

class LSA:
    sequence_number = 0

    def __init__(self, router_id, link_state_id):
        LSA.sequence_number += 1
        self.router_id = router_id
        self.sequence_number = LSA.sequence_number
        self.link_state_id = link_state_id

if __name__ == '__main__':
    filename = input("Enter the input file name: ")
    routers = {}

    try:
        with open(filename, 'r') as file:
            num_routers = int(file.readline().strip())
            for i in range(num_routers):
                router_id = file.readline().strip()
                ip_address = file.readline().strip()
                routers[router_id] = Router(router_id, ip_address)

            for router in routers.values():
                num_neighbors = int(file.readline().strip())
                for j in range(num_neighbors):
                    neighbor, cost = file.readline().strip().split()
                    router.add_adjacent_router(neighbor, int(cost))

    except Exception as e:
        print("Error reading the input file:", e)
        exit(1)

    for router in routers.values():
        router.send_hello()

    lsas_to_send = [LSA(router.router_id, router.ip_address) for router in routers.values()]
    for router in routers.values():
        router.send_lsa(lsas_to_send)
        router.send_lsu(lsas_to_send)

    for router in routers.values():
        router.request_all_lsas()

    for router in routers.values():
        shortest_paths = router.dijkstra_shortest_path()
        print("Shortest paths from {}: {}".format(router.router_id, shortest_paths))
