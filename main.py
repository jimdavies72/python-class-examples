from frequency_graph import FrequencyGraph
from list_to_json import ListToJSON
from message import Message
from encoder import Encoder

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
readable_message = Message("Hello World 1 2 3")

my_encoded_message = Encoder(readable_message)
encoded_hex_message = my_encoded_message.encode_message()
print(f"|{encoded_hex_message}|")

print('----------------------------------')
print()

#encoded_message = Message('48 65 6c 6c 6f 57 6f 72 6c 64 6f 6e 65 74 77 6f 74 68 72 65 65')

encoded_message = Message(encoded_hex_message)

my_readable_message = Encoder(encoded_message)
print(my_readable_message.decode_message())



