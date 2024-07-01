import csv

with open('data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for i in range(1, 101):
    key = f"key{i}"
    value = f"value{i}"
    writer.writerow([key, value])

print("CSV file generated: data.csv")