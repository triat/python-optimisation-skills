"""
Example 3: Memory Optimization with __slots__
Demonstrates 30% memory reduction when creating many class instances.
"""

import sys
from typing import List


# ❌ BEFORE: Regular class without __slots__
class PointRegular:
    """Regular point class - uses __dict__ for attributes"""

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_origin(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


# ✅ AFTER: Optimized class with __slots__
class PointOptimized:
    """Optimized point class - uses __slots__ to reduce memory by ~30%"""
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_origin(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


# Real-world example: Sensor data processing
# ❌ BEFORE: High memory usage
class SensorReadingRegular:
    """Sensor reading without __slots__ - high memory when storing thousands"""

    def __init__(self, timestamp: float, temperature: float, humidity: float,
                 pressure: float, sensor_id: str):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.sensor_id = sensor_id

    def is_valid(self):
        return (0 <= self.temperature <= 100 and
                0 <= self.humidity <= 100 and
                0 <= self.pressure <= 2000)


# ✅ AFTER: Memory-optimized with __slots__
class SensorReadingOptimized:
    """Sensor reading with __slots__ - 30% less memory for large datasets"""
    __slots__ = ['timestamp', 'temperature', 'humidity', 'pressure', 'sensor_id']

    def __init__(self, timestamp: float, temperature: float, humidity: float,
                 pressure: float, sensor_id: str):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.sensor_id = sensor_id

    def is_valid(self):
        return (0 <= self.temperature <= 100 and
                0 <= self.humidity <= 100 and
                0 <= self.pressure <= 2000)


# Memory comparison
def get_size_of_instances(cls, count: int) -> int:
    """Calculate total memory used by multiple instances"""
    instances = [cls(1.0, 2.0, 3.0, 4.0, f"sensor_{i}")
                 if hasattr(cls, '__slots__') or cls.__name__.endswith('Regular')
                 else cls(1.0, 2.0, 3.0)
                 for i in range(count)]

    total_size = sum(sys.getsizeof(inst.__dict__) if hasattr(inst, '__dict__')
                     else sys.getsizeof(inst) for inst in instances)
    return total_size


if __name__ == "__main__":
    # Test with Point classes
    num_points = 10000

    # Create instances
    regular_points = [PointRegular(i, i+1, i+2) for i in range(num_points)]
    optimized_points = [PointOptimized(i, i+1, i+2) for i in range(num_points)]

    # Calculate memory usage
    regular_size = sum(sys.getsizeof(p.__dict__) for p in regular_points)
    optimized_size = sum(sys.getsizeof(p) for p in optimized_points)

    print(f"Creating {num_points:,} Point instances:\n")
    print(f"Regular class memory:   {regular_size:,} bytes")
    print(f"Optimized class memory: {optimized_size:,} bytes")
    print(f"Memory saved: {regular_size - optimized_size:,} bytes "
          f"({(1 - optimized_size/regular_size)*100:.1f}%)\n")

    # Test with SensorReading classes
    num_readings = 10000
    regular_readings = [
        SensorReadingRegular(i, 25.0 + i*0.01, 60.0, 1013.0, f"sensor_{i%100}")
        for i in range(num_readings)
    ]
    optimized_readings = [
        SensorReadingOptimized(i, 25.0 + i*0.01, 60.0, 1013.0, f"sensor_{i%100}")
        for i in range(num_readings)
    ]

    regular_sensor_size = sum(sys.getsizeof(r.__dict__) for r in regular_readings)
    optimized_sensor_size = sum(sys.getsizeof(r) for r in optimized_readings)

    print(f"Creating {num_readings:,} SensorReading instances:\n")
    print(f"Regular class memory:   {regular_sensor_size:,} bytes")
    print(f"Optimized class memory: {optimized_sensor_size:,} bytes")
    print(f"Memory saved: {regular_sensor_size - optimized_sensor_size:,} bytes "
          f"({(1 - optimized_sensor_size/regular_sensor_size)*100:.1f}%)")

    print("\n" + "="*60)
    print("WHEN TO USE __slots__:")
    print("✅ Creating hundreds/thousands of instances")
    print("✅ Fixed set of attributes known in advance")
    print("✅ Memory efficiency is important")
    print("❌ Need dynamic attribute assignment")
    print("❌ Only creating a few instances")
    print("="*60)
