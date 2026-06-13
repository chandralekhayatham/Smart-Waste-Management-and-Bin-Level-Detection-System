from src.sensor import get_distance
from src.sensor import get_fill_percentage

from src.alert import get_status
from src.dashboard import save_data

print("=" * 50)
print(" SMART WASTE MANAGEMENT SYSTEM ")
print("=" * 50)

distance = get_distance()

fill_percentage = get_fill_percentage(distance)

status = get_status(fill_percentage)

save_data(distance, fill_percentage, status)

print("\nDistance:", distance, "cm")
print("Fill Percentage:", fill_percentage, "%")
print("Status:", status)

if status == "FULL":
    print("\n🚨 ALERT: Waste Bin is Full!")

elif status == "HALF FULL":
    print("\n🟡 WARNING: Waste Bin is Half Full")

else:
    print("\n🟢 Bin is Empty")
    print("\nData Logged Successfully")
print("Thank You for Using Smart Waste Management System")