"""Unit converter for length, weight and temperature."""

LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
          "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}
WEIGHT = {"mg": 0.000001, "g": 0.001, "kg": 1.0, "lb": 0.45359237, "oz": 0.028349523125}


def convert_factor(value, src, dst, table):
    if src not in table or dst not in table:
        raise ValueError(f"Unknown unit. Choose from: {', '.join(table)}")
    return value * table[src] / table[dst]


def convert_temperature(value, src, dst):
    units = {"c", "f", "k"}
    src, dst = src.lower(), dst.lower()
    if src not in units or dst not in units:
        raise ValueError("Temperature units are c, f, k")
    celsius = {"c": value, "f": (value - 32) * 5 / 9, "k": value - 273.15}[src]
    return {"c": celsius, "f": celsius * 9 / 5 + 32, "k": celsius + 273.15}[dst]


def convert(kind, value, src, dst):
    if kind == "length":
        return convert_factor(value, src, dst, LENGTH)
    if kind == "weight":
        return convert_factor(value, src, dst, WEIGHT)
    if kind == "temperature":
        return convert_temperature(value, src, dst)
    raise ValueError("Type must be length, weight or temperature")


def main():
    print("Unit Converter (type 'q' to quit)")
    while True:
        kind = input("Type (length/weight/temperature): ").strip().lower()
        if kind == "q":
            break
        try:
            value = float(input("Value: "))
            src = input("From unit: ").strip()
            dst = input("To unit: ").strip()
            print(f"{value} {src} = {convert(kind, value, src, dst):.4g} {dst}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
