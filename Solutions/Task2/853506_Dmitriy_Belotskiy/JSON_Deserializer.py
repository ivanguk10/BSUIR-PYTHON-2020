from json import loads


class Node:
    def __init__(self, name, parent = None):
        self.parent = parent
        self.name = name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.name+":"+self.text
        else:
            return self.name

    def to_dict(self):
        dictionary=dict()
        if not self.children:
            return self.name, self.text
        else:
            for child in self.children:
                child_info = child.to_dict()
                dictionary[child_info[0]]=child_info[1]
        return self.name, dictionary


class Parser:
    def __init__(self,parse_string):
        self.parse_strig = "root:"+parse_string
        self.root=None
        self.current_node=None
        self.current_mode = []
        self.result_dict = {}

    def process(self, remaining_string):
        remaining=self.state.process(remaining_string,self)
        if remaining:
            self.process(remaining)

    def start(self):
        col_ind=self.parse_strig.find(':')
        name=self.parse_strig[:col_ind]
        node=Node(name, None)
        self.current_node = node
        self.root = node
        ChildNode.process(self.parse_strig[col_ind+1:], self)

    def to_dict(self):
        return self.root.to_dict()[1]


class ChildNode:
    @classmethod
    def process(cls,remaining_string,parser):
        stripped=remaining_string.strip()
        if remaining_string.startswith("{"):
            remaining_string=DictProcessor.process(remaining_string[1:],parser)
        elif remaining_string.startswith('['):
            remaining_string=ListProcessor.process(remaining_string[1:],parser)
        else:
            remaining_string=TextNode.process(remaining_string,parser)
        if remaining_string.startswith(','):
            parser.current_node=parser.current_node.parent
            return remaining_string[1:]
        return remaining_string


class TextNode:
    @classmethod
    def process(cls, remaining_string, parser):
        length=len(remaining_string)
        com_ind= remaining_string.find(',')
        sq_ind=remaining_string.find(']')
        crv_ind=remaining_string.find('}')
        if com_ind==-1:
            com_ind=length
        if sq_ind==-1:
            sq_ind=length
        if crv_ind==-1:
            crv_ind=length
        end=min(min(crv_ind,sq_ind),com_ind)
        text = remaining_string[:end]
        parser.current_node.text = text
        return remaining_string[end:]


class DictProcessor:
    @classmethod
    def process(cls,remaining_string,parser):
        while not remaining_string.startswith('}'):
            col_ind=remaining_string.find(':')
            name=remaining_string[:col_ind]
            node=Node(name,parser.current_node)
            parser.current_node.children.append(node)
            parser.current_node=node
            remaining_string=ChildNode.process(remaining_string[col_ind+1:],parser)
        parser.current_node=parser.current_node.parent
        return remaining_string[1:]


class ListProcessor:
    @classmethod
    def process(cls,remaining_string, parser):
        i=0
        while not remaining_string.startswith(']'):
            name = str(i)
            i += 1
            node = Node(name,parser.current_node)
            parser.current_node.children.append(node)
            parser.current_node = node
            remaining_string = ChildNode.process(remaining_string, parser)
        parser.current_node = parser.current_node.parent
        return remaining_string[1:]


class Shtirlits:         # свой среди чужих
    def __init__(self, dictionary):
        self.__data = dictionary

    def __getattr__(self, item):
        item = str(item)
        if item in self.__data.keys():
            if isinstance(self.__data[item], dict):
                return Shtirlits(self.__data[item])
            else:
                return self.__data[item]

    def __str__(self):
        return str(self.__data)

'''
if __name__== '__main__':
    parser = Parser("{dic:{a:3,b:2,c:1},int1:1,int2:3}")
    diction = loads("{\"dic\":{\"a\":3,\"b\":2,\"c\":1},\"int1\":1,\"int2\":3}")
    print(diction)
    parser.start()
    Sh = Shtirlits(parser.to_dict())
    print(Sh.__data['dic']['a'])
    print(Sh.dic.a)
'''
