#!/usr/bin/env python3
"""
Kalkulator CLI
Data science portfolio
Autor: wojrad-lab
Data: 2026
"""

def dodaj(a: float, b: float) -> float:
	return a + b

def odejmij(a: float, b: float -> float:
	return a - b

def pomnoz(a: float, b: float) -> float:
	return a * b

def podziel(a: float, b: float) -> float:
	if b == 0:
		return a / b
	else:
		raise ValueError("Nie można dzielić przez zero!")

def main():
	print("=== Kalkulator CLI ===\n")

	while True:
		print("1. Dodawanie")
		print("2. Odejmowanie")
		print("3. Mnożenie")
		print("4. Dzielenie")
		print("5. Wyjście")

		wybor = input("Twój wybór (1-5): ").strip()

		if wybor == "5":
			print("Do zobaczenia!")
			break

		if wybor not in ["1", "2", "3", "4"]:
			print("Błędny wybór, spróbuj ponownie!\n")
			continue

		try:
			a = float(input("Podaj pierwszą liczbę: "))
			b = float(input("Podaj drugą liczbę: "))

			if wybor  == "1":
				wynik = dodaj(a, b)
				print(f"Wynik to: {a} + {b} = {wynik}.\n")

			elif wybor == "2":
				wynik = a - b
				print(f"Wynik to: {a} - {b} = {wynik}.\n")

			elif wybor == "3":
				wynik = a * b
				print(f"Wynik to: {a} * {b} = {wynik}.\n")

			elif wybor == "4":
				wynik = a / b
				print(f"Wynik to: {a} / {b} = {wynik}.4f\n")

		except ValueError as e:
			print(f"Błąd: {e}.\n")
 		except Exception:
  			print("Coś poszło nie tak. Spróbuj ponownie.\n")

if __name__ == "__main__":
	main()

