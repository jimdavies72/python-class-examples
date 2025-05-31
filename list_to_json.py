import json

class ListToJSON:
  def __init__(self, list, schema):
    self.__list = list
    self.__schema = schema
    self.__json_object = json.dumps(self.array_to_dictionary(), indent=2)
  
  @property
  def json_object(self):
    return self.__json_object
    
  def array_to_dictionary(self):
    dict_list = []
    
    for rec in self.__list:
      rec_dict = {}
      for i in range(len(rec)):
          rec_dict[self.__schema[i]] = rec[i]
      
      dict_list.append(rec_dict)  
    
    return dict_list
  
  def write_to_file(self, filename):
    with open(filename, 'w') as f:
      f.write(self.__json_object)
  