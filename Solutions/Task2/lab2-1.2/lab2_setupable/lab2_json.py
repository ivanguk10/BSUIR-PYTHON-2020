class JSON:

    # <editor-fold desc="Serialisation">

    __typeDict__ = {
        'bool': lambda x, offset: '{},\n'.format(str(x).lower()),
        'str': lambda x, offset: '\"{}\",\n'.format(x),
        'int': lambda x, offset: '{},\n'.format(x),
        'dict': lambda x, offset: '{},\n'.format(JSON._dict_(x, offset + 3)),
        'list': lambda x, offset: '{},\n'.format(JSON._list_(x, offset + 3)),
        'object': lambda x, offset: '{},\n'.format(JSON._obj_(x, offset + 3, False))
    }

    def _dict_(d: dict, offset: int):
        added_string = '{\n'
        for key in d.keys():
            if not ((type(d[key])).__name__ in JSON.__typeDict__.keys()):
                added_string += '{}\"{}\": {}'.format(offset * ' ', key, JSON.__typeDict__['object'](d[key], offset))
            else:
                added_string += '{}\"{}\": {}'.format(offset * ' ', key,
                                              JSON.__typeDict__[(type(d[key])).__name__](d[key], offset))
        added_string = added_string[:-2] + '\n'
        added_string += '{}'.format(' ' * (offset - 3)) + '}'
        return added_string

    def _list_(l: list, offset: int):
        added_string = '[\n'
        for i in l:
            if not ((type(i)).__name__ in JSON.__typeDict__.keys()):
                added_string += '{}{}'.format(offset * ' ', JSON.__typeDict__['object'](i, offset))
            else:
                added_string += '{}{}'.format(offset * ' ',
                                              JSON.__typeDict__[(type(i)).__name__](i, offset))
        if len(added_string) > 4:
            added_string = added_string[:-2] + '\n'
        added_string +='{}]'.format(' ' * (offset-3))
        return added_string

    def _obj_(obj, offset: int, is_Start: bool):
        json_string = ''
        if is_Start:
            json_string = '{}'.format((offset - 3) * ' ')
        json_string += '{\n'
        for i in [attr for attr in dir(obj) if not attr.startswith('_')]:
            if not ((type(obj.__getattribute__(i))).__name__ in JSON.__typeDict__.keys()):
                json_string += '{}\"{}\": {}'.format(offset * ' ', i,
                                                     (JSON.__typeDict__['object'])(obj.__getattribute__(i), offset))
            else:
                json_string += '{}\"{}\": {}'.format(offset * ' ', i,
                                                     JSON.__typeDict__[(type(obj.__getattribute__(i))).__name__](
                                                         obj.__getattribute__(i), offset))
        if len(json_string) > 4:
            json_string = json_string[:-2] + '\n'
        return json_string + '{}'.format((offset-3) * ' ') + '}'

    def serialize(obj: object):
        if type(obj) is tuple:
            return JSON._list_(list(obj), 3)
        elif type(obj) is list:
            return JSON._list_(obj, 3)
        elif type(obj) is dict:
            return JSON._dict_(obj, 3)
        else:
            return JSON._obj_(obj, 3, True)

    # </editor-fold>

    # <editor-fold desc="Deserialisation">

    def _from_list_(l: list, offset: int, position: int):
        result_list = []
        last_position = position
        for line in l[position:]:
            if last_position != position:
                last_position += 1
                continue
            elif line.startswith((offset+1) * ' '):
                if line[offset+3] == '{':
                    obj_result = JSON._from_obj_(l, offset + 3, position + 1)
                    result_list.append(obj_result[0])
                    position = obj_result[1] + 1
                    last_position += 1
                    continue
                elif line[offset+3] == '[':
                    list_result = JSON._from_list_(l, offset + 3, position + 1)
                    result_list.append(list_result[0])
                    position = list_result[1] + 1
                    last_position += 1
                    continue
                elif line[offset+3] == '\"':
                    result_list.append(line[offset+4:(line.find('\"', offset + 4))])
                elif line[offset+3] != 'f' and line[offset+3] != 't':
                    if line[len(line)-1] == ',':
                        result_list.append(int(line[offset + 3:-1]))
                    else:
                        result_list.append(int(line[offset + 3:]))
                else:
                    result_list.append(False if line[offset+3] == 'f' else True)
                position += 1
                last_position += 1
            else:
                return result_list, position

    def _from_obj_(obj: list, offset: int, position: int):
        result_dict = dict()
        last_position = position
        for line in obj[position:]:
            if last_position != position:
                last_position += 1
                continue
            elif line.startswith((offset + 1) * ' '):
                key = line[offset+4:(line.find('\"', offset + 4))]
                start_pos = line.find(':') + 2
                value = True
                if line[start_pos] == '{':
                    obj_result = JSON._from_obj_(obj, offset + 3, position + 1)
                    result_dict[key] = obj_result[0]
                    position = obj_result[1] + 1
                    last_position += 1
                    continue
                elif line[start_pos] == '[':
                    list_result= JSON._from_list_(obj, offset + 3, position + 1)
                    result_dict[key] = list_result[0]
                    position = list_result[1] + 1
                    last_position += 1
                    continue
                elif line[start_pos] == '\"':
                    result_dict[key] = line[start_pos + 1:(line.find('\"', start_pos + 1))]
                elif line[start_pos] != 'f' and line[start_pos] != 't':
                    result_dict[key] = int(line[start_pos:len(line)-1])
                else:
                    result_dict[key] = False if line[start_pos] == 'f' else True
                position += 1
                last_position += 1
            else:
                return result_dict, position

    def deserialize(json_str: str):
        json_list = json_str.split('\n')
        if json_list[0] == '{':
            json_dict = JSON._from_obj_(json_list[1:], 0, 0)
            return json_dict[0]
        elif json_list[0] == '[':
            json_list = JSON._from_list_(json_list[1:], 0, 0)
            return json_list[0]
        else:
            raise Exception('Bad JSON - string')

    # </editor-fold>
