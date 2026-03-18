

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if (unit == "packets"):
		print(seed_type.capitalize(), "seeds:", quantity, unit, "packets")
	elif (unit == "grams"):
		print(seed_type.capitalize(), "seeds:", quantity, unit, "grams")
	elif (unit == "area"):
		print(seed_type.capitalize(), "seeds:", quantity, unit, "area")

ft_seed_inventory("tomato", 15, "packets")