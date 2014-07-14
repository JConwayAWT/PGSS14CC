# This is a non-Euclidean way of generating cities and calculating minimum distances.
# It identifies the index of the nearest city from each given city, but doesn't create paths or remove cities visited.
# needs more work to become an actual solution algorithm

import random

def main():
  number_of_cities = 10
  distances_from_cities = []
  for k in range(number_of_cities): # assigning random distances
    current_distances = []
    for j in range(number_of_cities):
      random_distance = random.randint(1, 100)
      current_distances.append(random_distance)
    distances_from_cities.append(current_distances)

  for x in range(number_of_cities): # setting up the distances matrix
    for y in range(number_of_cities):
      if x == y:
        distances_from_cities[x][y] = 0
      else:
        distances_from_cities[x][y] = distances_from_cities[y][x]

  city_used_in_path = [False]*number_of_cities
  city_used_in_path[0] = True
  index_of_min_distance = []

  for k in range(number_of_cities): # identify minimum distance for each city
    current_distances = distances_from_cities[k]
    minimum_distance_from_current_city = min([distance for distance in current_distances if distance > 0])
    index_to_remove = current_distances.index(minimum_distance_from_current_city)
    for j in range(number_of_cities): # remove minimum distance index
      distances_from_cities[j].pop(index_to_remove)
    index_of_min_distance.append(index_to_remove)
    print minimum_distance_from_current_city

  print index_of_min_distance
  print distances_from_cities



if __name__ == '__main__':
    main()