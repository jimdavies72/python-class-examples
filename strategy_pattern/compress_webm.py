from strategy_pattern import Compress

# concrete compression class - WEBM
class CompressWEBM(Compress):
  def compress(self):
    print("Compressing file in WEBM format")