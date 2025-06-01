from abc import ABC, abstractmethod

# abstract export class
class Export(ABC):
  @abstractmethod
  def export(self):
    pass