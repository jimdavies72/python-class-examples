from export_to_json import Export

# concrete list to json class implementing the export abstract class
class ExportList(Export):
  
  def __init__(self, list, schema):

    self.__list = list
    self.__schema = schema
    
  def export(self):
    dict_list = []
    
    print("Exporting list...")
    for rec in self.__list:
      rec_dict = {}
      for i in range(len(rec)):
          rec_dict[self.__schema[i]] = rec[i]
      
      dict_list.append(rec_dict)  
    
    return dict_list
    
    
    