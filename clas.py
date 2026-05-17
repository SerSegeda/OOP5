class Airplane:
    def __init__(self, model: str, capacity: int, payload: float, flight_range: float, fuel_consumption: float):
        if not isinstance(model, str):
            raise TypeError("Назва моделі має бути рядком.")
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Місткість має бути невід'ємним цілим числом.")
        if not isinstance(payload, (int, float)) or payload < 0:
            raise ValueError("Вантажопідйомність має бути невід'ємним числом.")
        if not isinstance(flight_range, (int, float)) or flight_range < 0:
            raise ValueError("Дальність польоту має бути невід'ємним числом.")
        if not isinstance(fuel_consumption, (int, float)) or fuel_consumption < 0:
            raise ValueError("Споживання пального має бути невід'ємним числом.")

        self.model = model
        self.capacity = capacity
        self.payload = float(payload)
        self.flight_range = float(flight_range)
        self.fuel_consumption = float(fuel_consumption)

    def __repr__(self):
        return (f"{self.__class__.__name__}(model='{self.model}', capacity={self.capacity}, "
                f"payload={self.payload}, range={self.flight_range}, fuel={self.fuel_consumption})")


class PassengerPlane(Airplane):
    def __init__(self, model: str, capacity: int, payload: float, flight_range: float, fuel_consumption: float,
                 has_wifi: bool):
        super().__init__(model, capacity, payload, flight_range, fuel_consumption)
        if not isinstance(has_wifi, bool):
            raise TypeError("Параметр has_wifi має бути логічного типу.")
        self.has_wifi = has_wifi


class CargoPlane(Airplane):
    def __init__(self, model: str, capacity: int, payload: float, flight_range: float, fuel_consumption: float,
                 cargo_doors: int):
        super().__init__(model, capacity, payload, flight_range, fuel_consumption)
        if not isinstance(cargo_doors, int) or cargo_doors <= 0:
            raise ValueError("Кількість вантажних дверей має бути додатнім цілим числом.")
        self.cargo_doors = cargo_doors


class MilitaryPlane(Airplane):
    def __init__(self, model: str, capacity: int, payload: float, flight_range: float, fuel_consumption: float,
                 weapon_type: str):
        super().__init__(model, capacity, payload, flight_range, fuel_consumption)
        if not isinstance(weapon_type, str):
            raise TypeError("Тип озброєння має бути рядком.")
        self.weapon_type = weapon_type


class Airline:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Назва авіакомпанії має бути рядком.")
        self.name = name
        self.fleet = []

    def add_plane(self, plane: Airplane):
        if not isinstance(plane, Airplane):
            raise TypeError("Додати можна лише об'єкти типу Airplane або його нащадків.")
        self.fleet.append(plane)

    def get_total_capacity(self) -> int:
        return sum(plane.capacity for plane in self.fleet)

    def get_total_payload(self) -> float:
        return sum(plane.payload for plane in self.fleet)

    def sort_by_flight_range(self):
        self.fleet.sort(key=lambda plane: -plane.flight_range)

    def find_by_fuel_consumption(self, min_fuel: float, max_fuel: float) -> list:
        if not (isinstance(min_fuel, (int, float)) and isinstance(max_fuel, (int, float))):
            raise TypeError("Межі діапазону мають бути числами.")
        return [plane for plane in self.fleet if min_fuel <= plane.fuel_consumption <= max_fuel]


