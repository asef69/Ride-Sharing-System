from abc import ABC,abstractmethod
from ride import RideMatching,RideRequest,RideSharing
class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount):
        super().__init__(name, email, nid)       
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location

    def display_profile(self):
        print(f"Rider Details!!\n{self.name} and email {self.email}")

    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print("Amount less than 0")

    def update_location(self,current_location):
        self.current_location=current_location

    # Instead of importing at the top:
# from ride import RideMatching, RideRequest, RideSharing, Ride

    def request_ride(self, ride_sharing, destination, vehicle_type):
        from ride import RideRequest, RideMatching  # Import here
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
    
    # ...



    def show_current_ride(self):
        print("Ride details")
        print(f"Start Location:{self.current_ride.start_location}")
        print(f"End Location:{self.current_ride.end_location}") 
        print(f"Vehicle Type:{self.current_ride.vehicle.vehicle_type}")
        print(f"Driver Name:{self.current_ride.driver.name}")
        print(f"Estimated Fare:{self.current_ride.estimated_fare}")
        print(f"Start Time:{self.current_ride.start_time}")
        print(f"End Time:{self.current_ride.end_time}")


class Driver(User):
    def __init__(self, name, email, nid,current_location):
        super().__init__(name, email, nid)              
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f"Driver Name:{self.name}")

    def accept_ride(self,ride):
        ride.rider=self
        self.start_ride()
        ride.set_driver(self)
    def reach_destination(self):
        if self.current_ride:
            self.current_ride.end_ride()  # No argument needed  # Correct: Only the ride calls its own method  # Call end_ride on the ride object


        

