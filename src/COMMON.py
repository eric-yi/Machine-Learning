#!/usr/bin/python
# -*- coding: utf-8 -*-

SPECIAL = "%"
GENERAL = "?"

Sky = ("Sunny", "Cloudy", "Rainy")
AirTemp = ("Warm", "Cold")
Humidity = ("Normal", "High")
Wind = ("Strong", "Weak")
Water = ("Warm", "Cool")
Forecast = ("Same", "Change")

Parameters = (Sky, AirTemp, Humidity, Wind, Water, Forecase)

Sport = (
    {"Yes" : (Sky[0], AirTemp[0], Humidity[0], Wind[0], Water[0], Forecast[0])},
    {"Yes" : (Sky[0], AirTemp[0], Humidity[1], Wind[0], Water[0], Forecast[0])},
    {"No" : (Sky[2], AirTemp[1], Humidity[1], Wind[0], Water[0], Forecast[1])},
    {"Yes" : (Sky[0], AirTemp[0], Humidity[1], Wind[0], Water[1], Forecast[1])}
)

h = (SPECIAL, SPECIAL, SPECIAL, SPECIAL, SPECIAL, SPECIAL)

def ALL_VERSION_SPACE():
  version_space = []
  for sk in Sky:
    for ai in AirTemp:
      for hu in Humidity:
        for wi in Wind:
          for wa in Water:
            for fo in Forecast:
              version_space.append([sk, ai, hu, wi, wa, fo])
  return version_space

def line_print(lines):
  for line in lines:
    print(line)

def entropy(param_index):
    parameter = Parameters[param_index]
    n = 0
    while n < len(paramter):
        for _sport in Sport:
            _v = 0
            _key = 'No'
            if _sport.hasKey('Yes'):
                _key = 'Yes'
                _v = 1
            _sport[_key][param_index)


        n = n + 1


if __name__ == '__main__':
  for version_space in ALL_VERSION_SPACE():
    print version_space

