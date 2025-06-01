from export_to_json import Export

import csv

# concrete list to json class implementing the export abstract class
class ExportCSV(Export):
  
  def __init__(self, filename):
    self.__filename = filename
  
  def export(self):
   with open(self.__filename, 'r') as f: 
      reader = csv.DictReader(f)
      self.__list = list(reader)
      
      return self.__list