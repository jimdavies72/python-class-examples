from strategy_pattern import Compress

# concrete compression class - MP4
class CompressMP4(Compress):
  def compress(self):
    print("Compressing file in MP4 format")