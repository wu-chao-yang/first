class Record:
    def __init__(self,data,order,money,province):
        self.data = data
        self.order =order
        self.money  = money
        self.province =province

import my_modu
class Reader:
    def read_data(self)->list[Record]:
        pass

class TextFileResder(Reader):
    def __init__(self,path):
        self.path = path

    def read_data(self)->list[Record]:
        f=open(self.path,'r',encoding='utf')
        for line in f.readlines():
            line.strip()
            print(line)


if __name__ == '__main__':
    reading=TextFileResder("D:/test1.txt")
    reading.read_data()