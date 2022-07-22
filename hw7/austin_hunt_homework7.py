class PythonPlugin(PluginBase):
  def main(self):
    self.namespace = None
    self.nodes = self.core.load_own_sub_tree(self.active_node)
    self.node_paths = self.get_paths_to_nodes()
    self.graph = {}
    # every possible station pair should be included, each direction, so do nested
    for src_node in self.nodes:
      for dest_node in self.nodes:
        if self.is_station(src_node) and self.is_station(dest_node):
          src_name = self.core.get_attribute(src_node, 'name')
          dest_name = self.core.get_attribute(dest_node, 'name')
          self.graph['{0}->{1}'.format(src_name, dest_name)] = self.breadth_first_search(src_node, dest_node)
    self.pretty_print_graph()
    output = self.parse_graph_to_text_descriptions(writefile=True)
    self.logger.info(output)

  def get_all_switches_stations_adjacent_to_station(self, station_path):
    """ Return list of all stations adjacent to station """
    adjacent = {}
    for track in self.nodes:
      if self.is_track(track):
        src_path = self.get_track_end(track, 'src')
        if src_path == station_path:
          src = self.core.load_by_path(self.active_node, self.convert_path_to_relative(src_path))
          dest_path = self.get_track_end(track, 'dst')
          dest = self.core.load_by_path(self.active_node, self.convert_path_to_relative(dest_path))
          if self.is_station(dest) or self.is_switch(dest):
            adjacent[dest_path] = self.core.get_attribute(track, 'length')
    return adjacent

  def parse_graph_to_text_descriptions(self, writefile=False):
    """ for each path, include a description of the route like:
    A path from StationA to StationB is 150 miles. On the path you will travel through StationC, StationD, and StationE.

    Description of path excludes the src and destination.
    Do not mention pairs that have no paths (path_length of -1).
    Store template for description for easier population of descriptions.
    Save result into a text file named after the name of the RN network (like mynetwork.txt).
    """
    text_file = self.core.get_attribute(self.active_node, 'name').replace(' ','').lower() + '.txt'
    jinja = self.modules['jinja2']
    template = jinja.Template(self.core.get_attribute(self.active_node, 'outputTemplate'))
    output = template.render(graph=self.graph)
    if writefile:
      file_hash = self.add_file(text_file, output)
    return output
  def write_routes_list_to_file(self, routes_list, filename):
    """ given a list of english-formatted routes, write them to a text file """
    with open(filename, 'w') as f:
      f.writelines(routes_list)

  def breadth_first_search(self, src_station, target_station):
    queue = []
    src_station_path = self.core.get_path(src_station)
    src_station_name = self.core.get_attribute(src_station, 'name')
    target_station_path = self.core.get_path(target_station)
    visited = {p: -1 for p in self.node_paths}
    traversal_length_so_far = 0
    path_so_far = [src_station_name]
    queue.append((src_station_path, traversal_length_so_far, path_so_far))
    visited[src_station_path] = traversal_length_so_far
    while queue:
      current_station_path, traversal_length_so_far, path_so_far = queue.pop(0)
      adjacent  = self.get_all_switches_stations_adjacent_to_station(current_station_path)
      adjacent_station_paths = adjacent.keys()
      for adjacent_station_path in adjacent_station_paths:
        distance_to_adjacent_path = adjacent[adjacent_station_path]
        if visited[adjacent_station_path] == -1:
          total_distance = distance_to_adjacent_path + traversal_length_so_far
          total_path = path_so_far + [self.get_node_name_from_path(adjacent_station_path)]
          queue.append((adjacent_station_path, total_distance, total_path))
          visited[adjacent_station_path] = {
            'path_length': distance_to_adjacent_path + traversal_length_so_far,
            'path': total_path
          }
    return visited[target_station_path]

  def get_node_name_from_path(self, node_path):
    """ given a node path, return its name """
    node = self.core.load_by_path(self.active_node, self.convert_path_to_relative(node_path))
    return self.core.get_attribute(node, 'name')

  def pretty_print_graph(self):
    """ Pretty print the graph (as json)"""
    import json
    out = json.dumps(self.graph, sort_keys=True, indent=4)
    self.logger.info(out)
    with open('austin_hunt_homework6_output.json','w') as f:
      json.dump(self.graph, f)

  def convert_path_to_relative(self, node_path):
    """ return relative path of node based on current active_node
    by removing the active node path from beginning of node's path """
    return node_path.replace(self.active_node['nodePath'], '')

  def is_station(self, node):
    """ return true if node is a station; false otherwise """
    return self.core.is_instance_of(node, self.META['Station'])

  def is_switch(self, node):
    """ return true if node is a station; false otherwise """
    return self.core.is_instance_of(node, self.META['Switch'])

  def is_track(self, node):
    """ return true if node is a track, false otherwise """
    return self.core.is_instance_of(node, self.META['Track'])

  def get_paths_to_nodes(self):
    """ return a dictionary containing all node
    paths as keys and the respective nodes as their values """
    return {
            self.core.get_path(node): node \
                for node in self.nodes
                }

  def get_track_end(self, track, end='src'):
    """ Get the source (end='src') or destination (end='dest')
    station of a track node. the src or the dst is the Port. Want the
    corresponding station which is the parent of that port, i.e.
    get port, then get path to port, then get parent of that path. """
    pointer_path = self.core.get_pointer_path(track, end)
    if pointer_path:
      node = self.node_paths[pointer_path]
      parent = self.core.get_parent(node)
      parent_path = self.core.get_path(parent)
      return parent_path
    else:
      return None