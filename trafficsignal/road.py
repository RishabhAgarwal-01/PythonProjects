#observers
class Road:
    def __init__(self, road_id, road_name):
        self.id = road_id
        self.road_name = road_name
        self.traffic_light = None
    
    #change the traffic light of the road i.e.
    def set_traffic_light(self, traffic_light):
        self.traffic_light = traffic_light
    
    def get_traffic_light(self):
        return self.traffic_light
    
    def get_id(self):
        return self.id