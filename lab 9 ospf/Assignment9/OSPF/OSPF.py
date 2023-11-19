import heapq

class Router:
    def __init__(self, router_id, ip_address):
        self.router_id = router_id
        self.ip_address = ip_address
        self.adjacent_routers = {}

    def add_adjacent_router(self, router, cost):
        self.adjacent_routers[router] = cost

    def send_hello(self):
        print("Sending Hello from router {} with IP address {}".format(self.router_id,self.ip_address))

    def send_lsa(self, lsa):
        print("Sending LSA from router {} with IP address {}:".format(self.router_id,self.ip_address))
        for l in lsa:
            print("  Router ID: {}".format(l.router_id))
            print("  Sequence Number: {}".format(l.sequence_number))
            print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

    def send_lsr(self, requested_router_id):
        print("Sending LSR from router {} with IP address {} to request LSA of router {}".format(self.router_id,self.ip_address,requested_router_id))

    def send_lsu(self, lsas):
        print("Sending LSU from router {} with IP address {} with the following LSAs:".format(self.router_id,self.ip_address))
        for l in lsas:
            print("  Router ID: {}".format(l.router_id))
            print("  Sequence Number: {}".format(l.sequence_number))
            print("  Link State ID (Originating Router's IP): {}".format(self.ip_address))

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
    num_routers = int(input("Enter the number of routers: "))
    routers = {}

    for i in range(num_routers):
        router_id = input("Enter Router {} ID: ".format(i + 1))
        ip_address = input("Enter IP address for {}: ".format(router_id))
        routers[router_id] = Router(router_id, ip_address)

    for router in routers.values():
        num_neighbors = int(input("Enter the number of neighbors for {}: ".format(router.router_id)))
        for j in range(num_neighbors):
            neighbor, cost = input("Enter neighbor router ID and cost for {} (space-separated): ".format(router.router_id)).split()
            router.add_adjacent_router(neighbor, int(cost))

    for router in routers.values():
        router.send_hello()

    
    lsas_to_send = [LSA(router.router_id, router.ip_address) for router in routers.values()]
    for router in routers.values():
        router.send_lsa(lsas_to_send)
        router.send_lsu(lsas_to_send)

    
    for router in routers.values():
        requested_router_id = input("Enter the router ID to request LSA from {}: ".format(router.router_id))
        router.send_lsr(requested_router_id)

    
    for router in routers.values():
        shortest_paths = router.dijkstra_shortest_path()
        print("Shortest paths from {}: {}".format(router.router_id,shortest_paths))

