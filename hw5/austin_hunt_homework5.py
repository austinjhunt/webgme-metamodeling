class PythonPlugin(PluginBase):
  def main(self):
    self.namespace = None
    self.nodes = self.core.load_own_sub_tree(self.active_node)
    self.node_paths = self.get_paths_to_nodes()
    self.graph = {}
    for node in self.nodes:
      node_path = node['nodePath']
      node_dict = {
        'is_meta_node': self.core.is_meta_node(node),
        'name': self.core.get_attribute(node, 'name'),
        'GUID': self.core.get_guid(node),
        'meta': self.get_meta_type(node) if node_path != '' else None,
        'attributes': self.get_attributes(node)
      }
      self.graph[node_path] = node_dict
    self.pretty_print_graph()

  def pretty_print_graph(self):
    """ Pretty print the graph (as json)"""
    import json
    out = json.dumps(self.graph, sort_keys=True, indent=4)
    self.logger.info(out)
    with open('austin_hunt_homework5_output.json', 'w') as f:
      json.dump(self.graph, f)

  def get_attributes(self, node):
    """ Get the attribute names using built in method of core;
    then get value of each attribute by its name for current node;
    store each attribute name as key and attribute value as value
    in the returned dictionary; do not include the python code itself """
    attributes = self.core.get_attribute_names(node)
    return {
     a : self.core.get_attribute(node, a) for a in attributes if a not in ['pythonCode', 'scriptCode']
    }

  def get_meta_type(self, node):
    """ if node is a meta node, then the name of the meta type is itself;
    otherwise, get the meta type of the node, then get path
    to meta type node, then get node by its path, then get its name and return it """
    if self.core.is_meta_node(node):
      meta_node_name = self.core.get_attribute(node, 'name')
    else:
      meta = self.core.get_meta_type(node)
      meta_node_path = meta['nodePath']
      meta_node = self.core.load_by_path(self.active_node, meta_node_path)
      meta_node_name = self.core.get_attribute(meta_node, 'name')
    return meta_node_name

  def get_paths_to_nodes(self):
    """ return a dictionary containing all node
    paths as keys and the respective nodes as their values """
    return {
            self.core.get_path(node): node \
                for node in self.nodes
                }