class Json_to_object(object):
    """Class converts json string to object dict.

    Class contains methods for conversion json string to object dict.

    Attributes:
        _counter(int): symbol index of string
        _str(str): string for conversion
    """

    _counter = 0
    _str = ''

    @staticmethod
    def __to_string(self, dict_object, key, is_key):
        """Conversion data to str()

        Converts data to str() while symbol not equal to '\"'.
        Add note to dictionary if key exist, otherwise add key.

        Arguments:
            dict_object(dict): result dict
            key(str): key in result dict
            is_key(bool): check key existing
        """

        buf_string = ''
        while self._str[self._counter] != '\"':
            buf_string += self._str[self._counter]
            self._counter += 1

        self._counter += 1

        if is_key:
            return buf_string

        else:
            dict_object[key] = buf_string
            return ''

    def __to_list(self):
        """Conversion data to list()

            Converts data to list() while symbol not equal to ']'.

            Return:
                buf_list(list): data list of string
            """

        buf_list = []

        while self._str[self._counter] != ']':

            if self._str[self._counter] == '[':
                buf_list.append(self.__to_list())

            elif self._str[self._counter] == '{':
                buf_list.append(self.from_json(self._str, self._counter))

            elif self._str[self._counter] == ' ' or self._str[self._counter] == ',':
                self._counter += 1
                continue

            elif self._str[self._counter] == 'n':
                self._counter += 4
                buf_list.append(None)

            elif self._str[self._counter] == 't':
                self._counter += 4
                buf_list.append(True)

            elif self._str[self._counter] == 'f':
                self._counter += 5
                buf_list.append(False)

            elif self._str[self._counter] == '\"':
                buf_str = ''
                self._counter += 1
                while self._str[self._counter] != '\"':
                    buf_str += self._str[self._counter]
                    self._counter += 1
                self._counter += 1
                buf_list.append(buf_str)

            else:
                buf_str = ''
                while self._str[self._counter] != ',' and self._str[self._counter] != ']':

                    buf_str += self._str[self._counter]
                    self._counter += 1
                try:
                    buf_list.append(float(buf_str))

                except Exception:
                    raise FromJsonError('Incorrect value')

        self._counter += 1
        return buf_list

    @staticmethod
    def __to_object(self, dict_object):
        """Method converts string to dict.

        Json string converts into dict by symbol.

        Arguments:
            dict_object(dict): result dict.
        """

        key = ''
        is_key = True

        while True:

            symbol = self._str[self._counter]
            if symbol == '\"':
                self._counter += 1
                key = self.__to_string(self, dict_object, key, is_key)

            elif symbol == ' ':
                self._counter += 1
                continue

            elif symbol == ':':
                self._counter += 1
                is_key = False

            elif is_key:
                raise FromJsonError('Incorrect json format')

            elif symbol == '}':
                self._counter += 1
                return

            elif symbol == '{':
                dict_object[key] = self.from_json(self._str, self._counter)

            elif symbol == ',':
                key = ''
                is_key = True
                self._counter += 1

            elif symbol == 'n':
                self._counter += 4
                dict_object[key] = None

            elif symbol == 't':
                self._counter += 4
                dict_object[key] = True

            elif symbol == 'f':
                self._counter += 5
                dict_object[key] = False

            elif symbol == '[':
                self._counter += 1
                dict_object[key] = self.__to_list()

            else:
                buf_str = ''

                while self._str[self._counter] != ',' and self._str[self._counter] != '}':
                    buf_str += self._str[self._counter]
                    self._counter += 1
                try:
                    dict_object[key] = float(buf_str)

                except Exception:
                    raise FromJsonError('Incorrect value')

    def from_json(self, string, counter=0):
        """Method takes string for parsing to dict.

        Arguments:
            string(str): string for parsing
            counter(int): index of string

        Return:
            dict_object(dict): data dict of parsing json string.
        """

        if not string:
            return {}

        dict_object = {}
        self._str = string
        self._counter = counter

        if self._str[self._counter] == '{':
            self._counter += 1
            self.__to_object(self, dict_object)

        else:
            raise FromJsonError('Incorrect json format')

        return dict_object


class FromJsonError(Exception):
    """Class to represent FromJson error

    FromJsonError represents error occurred during operations
    with Json_to_object.

    Attributes:
        message(str): represents error message.
    """

    def __init__(self, message='Error'):

        self.message = message
