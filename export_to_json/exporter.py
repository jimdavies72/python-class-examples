from export_to_json import Export

import json

# export class allowing for different export types such as list to json or csv to json, text to json....
class Exporter:
  def __init__(self, export_type: Export):
    self.__export_type = export_type
  
  @property
  def export_type(self):
    return self.__export_type
  
  @export_type.setter # setter decorator allows for update of attribute
  def export_type(self, value):
    self.__export_type = value
   
  @property
  def json_object(self):
    return self.__json_object
   
  def export(self):
    self.__json_object = json.dumps(self.__export_type.export(), indent=2)
  
  def write_to_file(self, filename):
    with open(filename, 'w') as f:
      f.write(self.__json_object)