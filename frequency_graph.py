# consts
RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

class FrequencyGraph:
  def __init__(self, source_data):
    assert type(source_data) == list, 'Source data is not a list'
    assert len(source_data) > 0, 'Source data is an empty list'
    self.__data = self.clear_bad_data(source_data)
    self.__data = self.negatives_to_positives(self.__data)
    self.__frequency_data = self.__create_frequency_dict()
  
  @property
  def frequency_data(self):
    return self.__frequency_data
  
  @staticmethod
  def clear_bad_data(source_data):
    assert type(source_data) == list, 'Source data is not a list'
    assert len(source_data) > 0, 'Source data is an empty list'
    
    clean_data = []
    
    for item in source_data:
      if type(item) == int:
        clean_data.append(item)
    
    return clean_data
  
  @staticmethod
  def negatives_to_positives(source_data):
    assert type(source_data) == list, 'Source data is not a list'
    assert len(source_data) > 0, 'Source data is an empty list'
    
    for item in source_data:
      if item < 0:
        source_data[source_data.index(item)] *= -1
    
    return source_data
  
  def __create_frequency_dict(self):
    frequency_dict = {}
    
    for item in self.__data:
      if item in frequency_dict:
        frequency_dict[item] += 1
      else:
        frequency_dict[item] = 1
    return frequency_dict
  
  def print_graph(self):
    graph=""
    for x in self.__frequency_data:
      graph += f"{x}: { "X" * self.__frequency_data[x]}\n"
  
    print()
    print(f"{RED}Frequency Data:")
    print(f"______________{NC}")
    print(f"{GREEN}{graph}{NC}")
