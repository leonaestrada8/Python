class DeliveryRoute:
    def __init__(self, start, destination, distance, time):
        self.start = start
        self.destination = destination
        self.distance = distance
        self.time = time

class RoutingSystem:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def calculate_efficient_route(self, start, destination, criteria):
        efficient_route = None

        for route in self.routes:
            if route.start == start and route.destination == destination:
                if efficient_route is None:
                    efficient_route = route
                    continue
                if criteria == "distance" and route.distance < efficient_route.distance:
                    efficient_route = route
                elif criteria == "time" and route.time < efficient_route.time:
                    efficient_route = route

        return efficient_route

system = RoutingSystem()
system.add_route(DeliveryRoute("A", "B", 100, 60))
system.add_route(DeliveryRoute("A", "B", 120, 50))
system.add_route(DeliveryRoute("A", "C", 150, 80))

efficient_route_by_distance = system.calculate_efficient_route("A", "B", "distance")
print(f"Efficient route by distance: {efficient_route_by_distance.distance} km")

efficient_route_by_time = system.calculate_efficient_route("A", "B", "time")
print(f"Efficient route by time: {efficient_route_by_time.time} minutes")

