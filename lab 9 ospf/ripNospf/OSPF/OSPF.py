import heapq

class Router:
    def __init__(self, router_id, ip_address):
        self.router_id = router_id
        self.ip_address = ip_address
        self.adjacent_routers = {}

    def add_adjacent_router(self, router, cost):
        self.adjacent_routers[router] = cost

    def send_hello(self):
        print(f"Sending Hello from router {self.router_id} with IP address {self.ip_address}")

    def send_lsa(self, lsa):
        print(f"Sending LSA from router {self.router_id} with IP address {self.ip_address}:")
        for l in lsa:
            print(f"  Router ID: {l.router_id}")
            print(f"  Sequence Number: {l.sequence_number}")
            print(f"  Link State ID (Originating Router's IP): {self.ip_address}")

    def send_lsr(self, requested_router_id):
        print(f"Sending LSR from router {self.router_id} with IP address {self.ip_address} to request LSA of router {requested_router_id}")

    def send_lsu(self, lsas):
        print(f"Sending LSU from router {self.router_id} with IP address {self.ip_address} with the following LSAs:")
        for l in lsas:
            print(f"  Router ID: {l.router_id}")
            print(f"  Sequence Number: {l.sequence_number}")
            print(f"  Link State ID (Originating Router's IP): {self.ip_address}")

    def dijkstra_shortest_path(self, routers):
        visited = {self.router_id: 0}
        hq = [(0, self.router_id)]
    
        while hq:
            current_distance, current_router_id = heapq.heappop(hq)
            current_router = routers[current_router_id]
    
            for adjacent_router_id, cost in current_router.adjacent_routers.items():
                new_distance = current_distance + cost
    
                if adjacent_router_id not in visited or new_distance < visited[adjacent_router_id]:
                    visited[adjacent_router_id] = new_distance
                    heapq.heappush(hq, (new_distance, adjacent_router_id))

        return visited


class LSA:
    sequence_number = 0

    def __init__(self, router_id, link_state_id):
        LSA.sequence_number += 1
        self.router_id = router_id
        self.sequence_number = LSA.sequence_number
        self.link_state_id = link_state_id
        
        
        
        
def print_topology(routers):
    print("Network Topology Adjacency List:")
    for router_id, router in routers.items():
        print(f"Router {router_id} ({router.ip_address}):")
        for adjacent_router_id, cost in router.adjacent_routers.items():
            print(f"  - connects to {adjacent_router_id} with cost {cost}")
        print()  # for better readability
        
        
        
        

if __name__ == '__main__':
    num_routers = int(input("Enter the number of routers: "))
    routers = {}

    for i in range(num_routers):
        router_id = input(f"Enter Router {i + 1} ID: ")
        ip_address = input(f"Enter IP address for {router_id}: ")
        routers[router_id] = Router(router_id, ip_address)

    for router in routers.values():
        num_neighbors = int(input(f"Enter the number of neighbors for {router.router_id}: "))
        for j in range(num_neighbors):
            neighbor, cost = input(f"Enter neighbor router ID and cost for {router.router_id} (space-separated): ").split()
            router.add_adjacent_router(neighbor, int(cost))

    for router in routers.values():
        router.send_hello()

    # Example LSA and LSU
    lsas_to_send = [LSA(router.router_id, router.ip_address) for router in routers.values()]
    for router in routers.values():
        router.send_lsa(lsas_to_send)  # Sending the list of LSAs for demonstration
        router.send_lsu(lsas_to_send)

    # Example LSR
    for router in routers.values():
        requested_router_id = input(f"Enter the router ID to request LSA from {router.router_id}: ")
        router.send_lsr(requested_router_id)
	
    # Example Dijkstra's algorithm

    for router in routers.values():
        shortest_paths = router.dijkstra_shortest_path(routers)
        print(f"Shortest paths from {router.router_id}: {shortest_paths}")

   # After all routers and their adjacencies have been added
    print_topology(routers)

