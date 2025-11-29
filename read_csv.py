import csv

from generate_values import GenerateValues

sensors = []

with open('config.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        sensor = GenerateValues(
            row["Name"],
            float(row["MaxValue"]),
            float(row["MinValue"]),
            float(row["Interval"]),
            row["Location"]
        )
        sensors.append(sensor)

print(f"Loaded {(sensor.generate())} sensors from configuration.")
while True:
    for sensor in sensors:
        print(sensor.generate())