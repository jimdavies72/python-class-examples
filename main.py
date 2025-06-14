from frequency_graph import FrequencyGraph
from list_to_json import ListToJSON
from message import Message
from encoder import Encoder
from fetch_requests import FetchRequests

from strategy_pattern import CompressMP4, CompressMOV, CompressWEBM, Video_Storage

from export_to_json import  ExportList, Exporter, ExportCSV

# frequency graph
# source_data = [1, None, 2, 3, "i", 4, 1, 1, None, 2, 3, 4, 4, 4]
# frequency_graph = FrequencyGraph(source_data)
# print(frequency_graph.frequency_data)
# frequency_graph.print_graph()


# list to json
# schema = ["name", "age", "location", "degree"]
# input_list= [
#   ["james", 52, "liverpool"],
#   ["mary", 27, "st. helens"],
#   ["bob", 23, "runcorn"],
#   ["sarah", None, "warrington", "BA 2:1 Art"],
# ]
# list_to_json = ListToJSON(input_list, schema)
# print(list_to_json.json_object)
# list_to_json.write_to_file("output.json")


# Encoder - Encode/Decode secret messages
# readable_message = Message("Hello World 1 2 3")

# my_encoded_message = Encoder(readable_message)
# encoded_hex_message = my_encoded_message.encode_message()
# print(f"|{encoded_hex_message}|")

# #encoded_message = Message('48 65 6c 6c 6f 57 6f 72 6c 64 6f 6e 65 74 77 6f 74 68 72 65 65')
# encoded_message = Message(encoded_hex_message)

# my_readable_message = Encoder(encoded_message)
# print(my_readable_message.decode_message())

# http request example
# request = FetchRequests("https://jsonplaceholder.typicode.com/")
# print(request.get_data("posts/1"))

# strategy design pattern and dependency injecection example using abstract class. 
# video_storage1 = Video_Storage(CompressMOV())
# video_storage1.store("video.mov")
# video_storage2 = Video_Storage(CompressMP4())
# video_storage2.store("test.mp4")
# video_storage3 = Video_Storage(CompressWEBM())
# video_storage3.store("test.webm")


# a re-factor of the class list_to_json (above) to comply with SOLID principles.
# list to json....
schema = ["name", "age", "location", "degree"]
input_list= [
  ["james", 52, "liverpool"],
  ["mary", 27, "st. helens"],
  ["bob", 23, "runcorn"],
  ["sarah", None, "warrington", "BA 2:1 Art"],
]
export_list = Exporter(ExportList(input_list, schema))
export_list.export()
#print(export_list.json_object)
export_list.write_to_file("output.json")

# csv to json...
export_csv = Exporter(ExportCSV("test_users.csv"))
export_csv.export()
#print(export_csv.json_object)
export_csv.write_to_file("test_users.json")



