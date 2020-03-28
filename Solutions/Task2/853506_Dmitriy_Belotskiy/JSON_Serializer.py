import json


class Node:
    basic_types = [int, float, list, dict, set, tuple, str]
    iterable_types = [list, dict, set, tuple]
    noniterable_types = [int, float, str]

    def __init__(self, name, obj, parent):
        self.name = name
        if self.name:
            self.name = '\"' + self.name + '\"'
        self.value = obj
        if type(obj) is str:
            self.value = "\"" + self.value + "\""
        self.children = []
        self.parent = parent

    def add_child(self, other):
        self.children.append(other)

    def __str__(self):
        if type(self.value) in self.noniterable_types:
            if self.name:
                return "".join([self.name + ": ", str(self.value)])
            return str(self.value)
        sign_tokens = '{}'
        if type(self.value) is list:
            sign_tokens = '[]'
        result_string = self.name + ": " + sign_tokens[0]
        for ch in self.children:
            s_ch = str(ch)
            result_string += s_ch + ', '
        result_string = result_string[:-2] + sign_tokens[1]

        return result_string


class JSON_Serializer:
    basic_types = [int, float, list, dict, set, tuple, str]
    iterable_types = [list, dict, set, tuple]
    noniterable_types = [int, float, str]

    def __init__(self,obj):
        self.root = Node("", obj, None)
        self.build_tree(self.root)

    def build_tree(self, obj):
        if type(obj.value) in self.noniterable_types:
            return
        if type(obj.value) in self.iterable_types:
            if isinstance(obj.value, dict):
                for key, value in obj.value.items():
                    new_node = Node(key, value, obj)
                    obj.add_child(new_node)
                    self.build_tree(new_node)
            else:
                for value in obj.value:
                    new_node = Node(None, value, obj)
                    obj.add_child(new_node)
                    self.build_tree(new_node)
            return
        cls_attr = [[key, value] for key, value in type(obj.value).__dict__.items() if
                    self.is_basic(value) and not key.startswith("__")]
        obj_attr = [[key, value] for key, value in obj.value.__dict__.items()]
        obj_attr.extend(cls_attr)
        for attr in obj_attr:
            new_node = Node(attr[0], attr[1], obj)
            obj.add_child(new_node)
            self.build_tree(new_node)

    def is_basic(self, obj):
        obj_type = type(obj)
        if obj_type in self.basic_types:
            return True
        return False

    def __str__(self):
        string = str(self.root)
        if string.startswith(':'):
            return string[2:]
        else:
            return string


class InnerClass:
    def __init__(self):
        self.string1 = "first str"
        self.string2 = "second string"
        self.string3 = "third string"


class TestClass:
    def __init__(self):
        self.spisok = [10, 20, 30, 40]
        self.first = 228
        self.second = 322
        self.inner = InnerClass()


'''
if __name__ == '__main__':
    x = TestClass()
    y = [100, 2, "spam"]
    z = 100
    print(JSON_Serializer(x))
    print(JSON_Serializer(y))
    print(JSON_Serializer(z))
'''

