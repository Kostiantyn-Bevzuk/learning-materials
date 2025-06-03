class DataProcessor:

  data_storage = []

  def __init__(self, data=[]):
        self.data = data
        self.result = None

  async def add_data(self, new_data):
        for item in new_data:
            self.data.append(item)
        self.data.sort()

  async def process_data(self):
        total = 0
        for i in range(len(self.data)):
            total = total + self.data[i]
        if len(self.data) > 0:
            self.result = total / len(self.data)
        else:
            self.result = 0
        DataProcessor.data_storage.append(self.result)
        return self.result

  async def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self.data))
        file.close()

  async def load_from_file(self, filename):
        file = open(filename, 'r')
        content = file.read()
        self.data = eval(content)
        file.close()

