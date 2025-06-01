from strategy_pattern.compress import Compress

class Video_Storage:

  def __init__(self, compress: Compress) -> None:
    self.__compress = compress
    
  
  @property
  def compress(self):
    return self.__compress
  
  @compress.setter # setter decorator allows for update of attribute
  def compress(self, value):
    self.__compress = value
    
  def store(self, filename):
    self.__compress.compress()
    
    print(f"Storing video {filename}")