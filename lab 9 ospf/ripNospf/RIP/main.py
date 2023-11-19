class Router:
    def __init__(self,name):
        self.name = name
        self.rt = {}

    def update_rt(self, des,dist,next_hop):
        self.rt[des] = (dist,next_hop)

    def display_rt(self):
        print(f"Routing Table for router: {self.name}")
        print("Destination\t Next Hop\t Distance")
        for dest,(dist,nh) in self.rt.items():
            print(f"{dest}\t\t{nh}\t\t{dist}")

net_topt = {
    "a" : ["K3", "K1"],
    "b" : ["K1","K3","K4","K2"],
    "c" : ["K2","K4","K6"],
    "d" : ["K3", "K5", "K6", "K7"],
    "e" : ["K2", "K4", "K7"]
}

neighbours = {
    "a" : ["b"],
    "b" : ["a","c","e"],
    "c" : ["b","d"],
    "d" : ["c","e"],
    "e" : ["b","d"]
}


all_networks = ["K1","K2","K3","K4","K5","K6","K7"]

routers = {}    

for r_name in net_topt:
    routers[r_name] = Router(r_name)

for r_name in routers:
    r = routers[r_name]
    for net in all_networks:
        if net in net_topt[r_name]:
            r.update_rt(net, 0, None)
        else:
            r.update_rt(net, 16, None)

print("Initial Routing Tables:")
for router_name in routers:
    routers[router_name].display_rt()

for _ in range(10):
    for r_name in routers:
        r = routers[r_name]
        for net in all_networks:
            if net not in net_topt[r_name]:
                mdist = 16
                next_hop = None
                for n in neighbours[r_name]:
                    n_router = routers[n]
                    if net in n_router.rt:
                        distance = 1 + n_router.rt[net][0]
                        if distance < mdist:
                            mdist = distance
                            next_hop = n
                r.update_rt(net,mdist,next_hop)

print("\nUpdated Routing Tables:")
for r_name in routers:
    routers[r_name].display_rt()    
