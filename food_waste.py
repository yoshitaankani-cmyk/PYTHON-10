
n = int(input("Enter number of days: "))

prepared_list = []
served_list = []
waste_list = []

for i in range(n):
    print("\nDay", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid quantities")
        continue

    waste = prepared - served

    prepared_list.append(prepared)
    served_list.append(served)
    waste_list.append(waste)

print("\n----- FOOD WASTE REPORT -----")

total_prepared = 0
total_served = 0
total_waste = 0

for i in range(len(waste_list)):

    percentage = (waste_list[i] / prepared_list[i]) * 100

    print("\nDay", i + 1)
    print("Prepared:", prepared_list[i])
    print("Served:", served_list[i])
    print("Wasted:", waste_list[i])
    print("Waste percentage:", round(percentage, 2), "%")

    if percentage > 20:
        print("Warning: High food wastage")
    else:
        print("Food wastage is within limit")

    total_prepared = total_prepared + prepared_list[i]
    total_served = total_served + served_list[i]
    total_waste = total_waste + waste_list[i]

print("\n----- FINAL SUMMARY -----")
print("Total meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total meals wasted:", total_waste)

if total_prepared > 0:
    overall = (total_waste / total_prepared) * 100
    print("Overall waste percentage:", round(overall, 2), "%")
