import copy

class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.routing_table = {neighbor: {"next_hop": neighbor, "distance": 1} for neighbor in neighbors}
        self.routing_table[self.name] = {"next_hop": self.name, "distance": 0}

    def update_routing_table(self, neighbor, distance_vector):
        for destination, data in distance_vector.items():
            if destination not in self.routing_table or self.routing_table[destination]["distance"] > data["distance"] + self.routing_table[neighbor]["distance"]:
                self.routing_table[destination] = {"next_hop": neighbor, "distance": data["distance"] + self.routing_table[neighbor]["distance"]}

    def send_routing_table(self):
        return self.routing_table

class Network:
    def __init__(self):
        self.routers = {}

    def add_router(self, router):
        self.routers[router.name] = router

    def simulate(self, iterations):
        for _ in range(iterations):
            for router in self.routers.values():
                for neighbor in router.neighbors:
                    distance_vector = router.send_routing_table()
                    self.routers[neighbor].update_routing_table(router.name, distance_vector)

    def print_routing_tables(self):
        for router in self.routers.values():
            print("Routing table for {}:".format(router.name))
            print("| Destination IP | Next Hop Router | Distance |")
            for destination, data in router.routing_table.items():
                print("| {} | {} | {} |".format(destination,data['next_hop'],data['distance']))
            print("\n")

if __name__ == "__main__":
    network = Network()

    num_routers = int(input("Enter the number of routers: "))

    for i in range(num_routers):
        name = input("Enter the name of router {}: ".format(i + 1))
        neighbors = input("Enter the neighbors for router {} separated by spaces: ".format(name)).split()
        network.add_router(Router(name, neighbors))

    iterations = int(input("Enter the number of simulation iterations: "))
    network.simulate(iterations)
    network.print_routing_tables()

