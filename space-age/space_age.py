import datetime

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.seconds_in_earth_year = 31557600
        self.orb_periods_of_planets_in_earth_years = \
            {"mercury": 0.2408467,
             "venus": 0.61519726,
             "mars": 1.8808158,
             "jupiter": 11.862615,
             "saturn": 29.447498,
             "uranus": 84.016846,
             "neptune": 164.79132
             }

    def on_planet(self, planet_name):
        planet_name = planet_name.lower().strip()
        result = None
        if planet_name != 'earth':
            planet_orb_period_in_earth_years = \
                self.orb_periods_of_planets_in_earth_years[planet_name] * self.seconds_in_earth_year
            result = self.seconds/planet_orb_period_in_earth_years
        else:
            result = self.seconds/self.seconds_in_earth_year
        return round(result, 2)
