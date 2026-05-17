from clas import *
company = Airline("Sky-Tech")

company.add_plane(PassengerPlane("Boeing 737", 189, 20000, 5400, 2500, True))
company.add_plane(CargoPlane("Antonov An-225", 6, 250000, 15400, 18000, 1))
company.add_plane(MilitaryPlane("F-16", 1, 7800, 4200, 1200, "Missiles"))

print(f"Загальна місткість (пасажирів): {company.get_total_capacity()}")
print(f"Загальна вантажопідйомність (кг): {company.get_total_payload()}")

company.sort_by_flight_range()
print("\nЛітаки після сортування за дальністю польоту:")
for p in company.fleet:
    print(f"{p.model} - {p.flight_range} км")

print("\nЛітаки зі споживанням пального від 2000 до 3000 літрів:")
found_planes = company.find_by_fuel_consumption(2000, 3000)
for p in found_planes:
    print(p)