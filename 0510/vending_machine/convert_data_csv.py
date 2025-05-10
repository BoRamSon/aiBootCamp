
class ConvertData:
  def __init__(self):
    self.get_datas = []
    self.data_dict_list = []

  def start(self):
    self.get_csv()
    self.make_dict_list()
    return self.data_dict_list

  def get_csv(self):
    with open('vanding_machine_stock.csv', 'r') as f:
      lines = f.readlines()
      self.get_datas = lines
      return lines
    
  def make_dict_list(self):
    for i in self.get_datas:
      data_dict = {}
      seperator = i.split(',')
      data_dict['num'] = seperator[0]
      data_dict['menu'] = seperator[1]
      data_dict['price'] = seperator[2]
      data_dict['stock'] = seperator[3].strip()
      self.data_dict_list.append(data_dict)
    self.data_dict_list.pop(0)

if __name__ == '__main__':
  c = ConvertData()
  c.start()
