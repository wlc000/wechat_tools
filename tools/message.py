import re


class Message(object):
    def __init__(self, msgstr):
        self.msgstr = msgstr  # 整行的信息
        try:
            self.msgdict = eval(re.search("message:(?P<msg>.+)$", msgstr).group("msg"))  # 只有msg字典
        except:
            self.msgdict = dict()

    # def __str__(self):
    # 	return self.msgstr

    @property
    def type(self):
        return re.search(r"message_type: (?P<TYPE>\d+)", self.msgstr).group("TYPE")

    @property
    def from_wxid(self):
        try:
            return self.msgdict['from_wxid']
        except:
            return ""

    @property
    def to_wxid(self):
        try:
            return self.msgdict['to_wxid']
        except:
            return ""

    @property
    def msg(self):
        try:
            return self.msgdict['msg']
        except:
            return ""
