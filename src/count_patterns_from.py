neighbours = {
  'A': ['B', 'D', 'E', 'F', 'H'],
  'B': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
  'C': ['B', 'D', 'E', 'F', 'H'],
  'D': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
  'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
  'F': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
  'G': ['D', 'B', 'E', 'F', 'H'],
  'H': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
  'I': ['B', 'D', 'E', 'F', 'H']
}

long_paths = [
  # Horizontal long paths
  ['A', 'B', 'C'],
  ['D', 'E', 'F'],
  ['G', 'H', 'I'],
  # Vertical long paths
  ['A', 'D', 'G'],
  ['B', 'E', 'H'],
  ['C', 'F', 'I'],
  # Diagonal long paths
  ['A', 'E', 'I'],
  ['C', 'E', 'G']
]

second_list_element_is_neighbour_if_first_is_visited = {}
for point in neighbours:
  second_list_element_is_neighbour_if_first_is_visited[point] = []
for long_path in long_paths:
  second_list_element_is_neighbour_if_first_is_visited[long_path[0]].append(long_path[1:3])
  second_list_element_is_neighbour_if_first_is_visited[long_path[2]].append(long_path[0:2][::-1])


def recursive_function(path, length):

  current_point = path[-1]
  neighbours_to_visit = []

  for neighbour in neighbours[current_point]:
    if neighbour not in path:
      neighbours_to_visit += neighbour

  for long_path_points in second_list_element_is_neighbour_if_first_is_visited[current_point]:
    point_that_must_be_visited = long_path_points[0]
    neighbour = long_path_points[1]
    if point_that_must_be_visited in path and neighbour not in path and neighbour not in neighbours_to_visit:
      neighbours_to_visit += neighbour

  if len(path) == length - 1:
    return len(neighbours_to_visit)

  num_patterns = 0
  for neighbour in neighbours_to_visit:
    num_patterns += recursive_function(path + [neighbour], length)
  return num_patterns


def count_patterns_from(first_point, length):
  if length < 1:
    return 0
  elif length == 1:
    return 1
  elif length > 9:
    raise Exception
  return recursive_function([first_point], length)


if __name__ == "__main__":
  # n_patterns = 0
  # for i in range(4, 10):
  #   for j in neighbours:
  #     n_patterns += count_patterns_from(j, i)
  # print(n_patterns)
  print(count_patterns_from('H', 9))
