from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Awesome Taxi",20,2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(fare)
    assert fare > 48.77 and fare < 48.79
main()
