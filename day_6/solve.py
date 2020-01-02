"""
Solving Day 6, 2019 Advent of Code Challenge
---

"""

import sys
import os
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution


class Planet:
    def __init__(self, name):
        self.name = name
        self.in_orbit_of = None
        self.does_orbit = False

    def set_orbit_of(self, planet):
        self.in_orbit_of = planet
        self.does_orbit = True

    def count_indirect_orbits(self):
        if not self.in_orbit_of:
            return 0
        if self.in_orbit_of.does_orbit:
            return 1 + self.in_orbit_of.count_indirect_orbits()
        else:
            return 1

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Planet {self.name} -> orbits [{self.in_orbit_of}]"


if __name__ == "__main__":
    day = 6
    year = 2019
    input_text = get_input_text(day, year)
    orbits = input_text.strip("\n").split("\n")
    planet_pairs = [orbit.split(")") for orbit in orbits]
    all_planets = dict()
    for (planet_name, in_orbit_name) in planet_pairs:
        planet = Planet(planet_name)
        if planet.name in all_planets:
            planet = all_planets.get(planet.name)
        orbit_planet = Planet(in_orbit_name)
        if orbit_planet.name in all_planets:
            orbit_planet = all_planets.get(orbit_planet.name)
        orbit_planet.set_orbit_of(planet)
        all_planets[planet.name] = planet
        all_planets[orbit_planet.name] = orbit_planet

    for name in all_planets:
        planet = all_planets[name]
    orbit_sum = sum([planet.count_indirect_orbits()
                     for planet in all_planets.values()])
    ## Part 1 ##
    print(f"Solution Day {day} (Part 1):")
    print("The number of direct and indirect orbits is", orbit_sum)

    write_solution(day, year, str(orbit_sum))

    ## Part 2 ##
    #  print(f"Solution Day {day} (Part 2):")

    #  write_solution(day, year,
