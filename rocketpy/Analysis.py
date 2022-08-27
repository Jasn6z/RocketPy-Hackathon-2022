from .Flight import Flight
from .Function import Function
from .Rocket import Rocket

class Analysis:
    def __init__(self, flight: Flight):
        self.flight = flight
        self.rocket = self.flight.Rocket
        self.motor = self.rocket.Motor
        self.env = self.flight.Environment
        
    def apogee_by_mass(self, flight: Flight):
        """
        Returns a RocketPy Function that, for a given Flight configuration,
        estimates the apogee as a function of the dry mass of the rocket.

            Parameters:
                flight (Flight):    Flight object to provide mass-apogee analysis

            Returns:
                RocketPy Function that provides predicted apogee as a function of dry mass
        """
        # Create version of flight that has ambigious mass
        def apogee(mass):
            variable_rocket = Rocket(
                motor = self.motor,
                radius = self.rocket.radius,
                mass = mass,
                inertiaI = self.rocket.inertiaI,
                inertiaZ = self.rocket.inertiaZ,
                distanceRocketNozzle = self.rocket.distanceRocketNozzle,
                distanceRocketPropellant = self.rocket.distanceRocketPropellant,
                powerOffDrag = 'idk', # FIX !!!!!!!!!!
                powerOnDrag = 'idk' # FIX !!!!!!!!!!
            )

            test_flight = Flight(
                rocket=variable_rocket,
                environment=self.env,
                inclination=flight.inclination,
                heading=flight.heading,
                terminateOnApogee=True,
            )

            return test_flight.apogee
        
        return Function(apogee, inputs="Mass (kg)", outputs="Estimated Apogee (m)")
        
    