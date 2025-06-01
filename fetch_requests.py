import requests

class FetchRequests:
  def __init__(self, url):
    if url[-1] != '/':
      url += '/'
    self.__url = url
    
  def get_data(self, endpoint):
    
    if endpoint[0] == '/':
      endpoint = endpoint[1:]
      
    response = requests.get(self.__url + endpoint)

    if response.status_code == 200:
      return response.json()
    else:
      return f"'{'{response.status_code}: {response.reason}'}'"
    
  