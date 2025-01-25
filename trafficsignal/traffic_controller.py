import threading
import time
from signal import Signal
from road import Road
from traffic_light import TrafficLight


class TrafficController:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._roads = {}  # Instance variable for storing roads
                cls._instance._road_lock = threading.Lock()  # Lock for thread-safe access to roads
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def add_road(self, road: Road):
        with self._road_lock:
            self._roads[road.id] = road

    def remove_road(self, road_id: str):
        with self._road_lock:
            return self._roads.pop(road_id, None)

    def start_traffic_control(self, max_cycles=3):
        threads = []
        for road in self._roads.values():
            traffic_light = road.get_traffic_light()
            t = threading.Thread(target=self._control_traffic_light, args=(traffic_light, max_cycles))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

    def _control_traffic_light(self, traffic_light: TrafficLight, max_cycles):
        cycles = 0
        while cycles < max_cycles:
            try:
                # Simulate red signal
                print(f"Traffic light {traffic_light.id} turned RED")
                time.sleep(traffic_light.red_duration / 1000)  # Convert to seconds
                traffic_light.change_signal(Signal.GREEN)

                # Simulate green signal
                print(f"Traffic light {traffic_light.id} turned GREEN")
                time.sleep(traffic_light.green_duration / 1000)
                traffic_light.change_signal(Signal.YELLOW)

                # Simulate yellow signal
                print(f"Traffic light {traffic_light.id} turned YELLOW")
                time.sleep(traffic_light.yellow_duration / 1000)
                traffic_light.change_signal(Signal.RED)

                cycles += 1  # Increment cycle count
            except Exception as e:
                print(f"Error in Traffic Light Control {traffic_light.id}: {e}")

    def handle_emergency(self, road_id: str):
        with self._road_lock:
            road = self._roads.get(road_id)
            if road:
                traffic_light = road.get_traffic_light()
                traffic_light.change_signal(Signal.GREEN)
                print(f"Emergency handled on road {road_id}: Green signal activated.")
                return True
        return False
