from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
	print("Let's drive!")
	taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
	current_taxi = None
	bill = 0.0
	command = ''
	while command.lower() != 'q':
		print(MENU)
		command = input(">>> ").lower()[0]
		if command == 'd':
			if current_taxi is None:
				print("Please select a taxi first.")
			else:
				distance = input("Distance: ")
				while not distance.isdigit():
					distance = input("Please enter a valid distance: ")
				print("Distance driven:", current_taxi.drive(int(distance)))
				print(f"Your {current_taxi.name} trip cost you:", current_taxi.get_fare())
				bill += current_taxi.get_fare()
				print("Bill to date:", bill)
		elif command == 'c':
			print("Taxis available:\n"+list_taxis(taxis))
			done = False
			while not done:
				index = input("Choose taxi: ")
				if index.isdigit():
					if int(index) > 0 and int(index) <= len(taxis):
						done = True
			current_taxi = taxis[int(index)-1]
			print(str(current_taxi))
			current_taxi.start_fare()
	print(f"Total trip cost: {bill:.2f}"+'\nTaxis are now:\n'+list_taxis(taxis))

def list_taxis(taxis):
	output = ''; count = 0
	for taxi in taxis:
		count += 1
		output = f"{output}{count}: {str(taxi)}\n"
	return output.rstrip('\n')

main()
