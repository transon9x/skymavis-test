import random
from collections import defaultdict

class NATInstance:
    def __init__(self, id, az):
        self.id = id
        self.az = az
        self.subnets = []
        self.total_weight = 0

    def add_subnet(self, subnet):
        self.subnets.append(subnet)
        self.total_weight += subnet.weight

    def __repr__(self):
        return f"Instance ({self.id} - {self.az}): {self.subnets}"

class Subnet:
    def __init__(self, id, az, weight):
        self.id = id
        self.az = az
        self.weight = weight

    def __repr__(self):
        return f"subnet ({self.id} - {self.az}, weight={self.weight})"

def allocate_subnets(nat_instances, subnets):
    az_to_nat = defaultdict(list)
    for nat in nat_instances:
        az_to_nat[nat.az].append(nat)
    
    unallocated_subnets = []
    for subnet in subnets:
        az_nats = az_to_nat[subnet.az]
        if az_nats:
            az_nats.sort(key=lambda nat: nat.total_weight)
            az_nats[0].add_subnet(subnet)
        else:
            unallocated_subnets.append(subnet)
    
    for subnet in unallocated_subnets:
        all_nats = [nat for nats in az_to_nat.values() for nat in nats]
        all_nats.sort(key=lambda nat: nat.total_weight)
        all_nats[0].add_subnet(subnet)

    return nat_instances

nat_instances = [
    NATInstance(1, "us-west1-a"),
    NATInstance(2, "us-west1-b"),
    NATInstance(3, "us-west1-b")
]

subnets = [
    Subnet(1, "us-west1-a", 10),
    Subnet(2, "us-west1-b", 20),
    Subnet(3, "us-west1-b", 30),
    Subnet(4, "us-west1-c", 40)
]

allocated_instances = allocate_subnets(nat_instances, subnets)

for instance in allocated_instances:
    print(instance)
