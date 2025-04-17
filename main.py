from ride import RideMatching,Ride,RideRequest,RideSharing
from users import Rider,Driver
from vehicle import Car,Bike

hello=RideSharing("Hello")
rahim=Rider("Rahim","rahim@gmail.com",1234,"Mohakhali",1200)
hello.add_rider(rahim)
kolim=Driver("Kolim","kolim@gmail.com",1256,"Tejgaon")
hello.add_driver(kolim)
rahim.request_ride(hello,"Dhanmondi","car")
kolim.reach_destination()
rahim.show_current_ride()
