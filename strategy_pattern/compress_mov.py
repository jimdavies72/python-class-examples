from strategy_pattern import Compress

# concrete compression class - MOV
class CompressMOV(Compress):
  def compress(self):
    print("Compressing file in MOV format")