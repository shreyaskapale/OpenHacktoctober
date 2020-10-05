

travelling_km=float(input("Enter distance travelled in km:"))
vehicle_fuel_avg=float(input("Enter Fuel Average in km/liter:"))
diesel_cost=float(input("Enter cost of diesel in INR:"))
fuel_consumption=travelling_km/ vehicle_fuel_avg;
cost_per_day = diesel_cost * fuel_consumption;
print("Total fuel consumed:",fuel_consumption)
print("The cost of driving per day to office.:",cost_per_day)
