# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import json
import datetime
import time
from wechat import WeChatManager, MessageType
import os
from tools.message import Message
import jieba

wechat_manager = WeChatManager(libs_path='../../libs')


# wlc
def get_common_words():
    global word_times

    def add_word(*l):
        for word in l[0]:
            if len(word) <= 1:
                continue
            if word in word_times:
                word_times[word] += 1
            else:
                word_times[word] = 1

    def add_macros():  # 似乎没啥用，因为不加的话分词也会这么分
        with open("data/macros", "r") as ft:
            for macro in ft:
                jieba.add_word(macro)

    with open("data/jilu.txt", "r") as ft:
        for line in ft:
            msg = Message(line)
            # print(repr(msg.msg).strip("'"))   #按理说用str(msg.msg)就行，但是有些输入法自带的表情是Unicode编码的，会报错。
            add_macros()
            add_word(jieba.lcut(msg.msg))


# wlc
def get_remark(wxid):
    for friend in friends:
        if isinstance(friend, str):
            print(friend)
        if friend['wxid'] == wxid:  # 逐个遍历，来确定是哪个friend
            try:
                return friend['remark']
            except:
                return friend['nickname']

    return wxid


# wlc
def get_chatroom_remark(wxid):
    for chatroom in chatrooms:
        if type(chatroom) == type("hh"):
            print(chatroom)
        if chatroom['wxid'] == wxid:  # 逐个遍历，来确定是哪个chatroom
            try:
                return chatroom['nickname']
            except:
                print("WTFWTF??")
                return wxid

    return wxid


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect]\nclient_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):  # 和LoginTipBot.on_message()效果差不多
    # message_data是dict类型
    '''
		发送/收到了新消息后，会触发该函数
		在这里添加我的功能！！
	'''

    global friends
    if message_type == MessageType.MT_USER_LOGIN:
        friends += [message_data]  # 把自己的信息加入到friends里

    elif message_type == MessageType.MT_RECV_TEXT_MSG:
        '''
		[on_recv]
		client_id: 1
		message_type: 11046
		message:{
			"at_user_list": [], 
			"from_wxid": "wxid_crcb154yyvk341", 
			"is_pc": 0, 
			"msg": "hhh", 
			"msgid": "3498112850856170001", 
			"room_wxid": "", 
			"timestamp": 1612790173, 
			"to_wxid": "wxid_zxr2684nhhad22", 
			"wx_type": 1}
		 '''

        if showInConsole:
            print("[TEXT]---")
            print("from", get_remark(message_data['from_wxid']))
            if (message_data['room_wxid'] != ''):
                print("to chatroom:", get_chatroom_remark(message_data['to_wxid']))
            else:
                print("to:", get_remark(message_data['to_wxid']))
            print("内容为：", message_data['msg'])
            print("----")

    # wlc
    # 智障的自动回复
    # if  message_data['to_wxid'] != message_data['from_wxid']: #不是自己和自己聊天
    #	 gen_msg = message_data['msg']+'是啥意思'
    # to_wxid = message_data['from_wxid']
    # wechat_manager.send_text(client_id, to_wxid, gen_msg)

    elif message_type == MessageType.MT_RECV_REVOKE_MSG:
        get_recalled_msg(message_data)
    with open("data/log.txt", "a") as f:
        # print("writing")

        # wlc
        # 这块的格式啥的不要改了 by wlc
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write('[on_recv](%s)\t\tclient_id: %s\t\tmessage_type: %s\t\tmessage:%s\n' % (t, client_id,
                                                                                        message_type, json.dumps(
            message_data)))  # 一条内容放在一行，方便处理
    # print("writing finished")


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close]\nclient_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)  # 如果注释掉这个装饰器，那么就不会把信息print到console
    def on_message(self, client_id, message_type, message_data):
        # print(message_type)
        # 判断登录成功后，就向文件助手发条消息
        if message_type == MessageType.MT_USER_LOGIN:
            wechat_manager.send_text(client_id, 'filehelper', '该消息通过wechat_pc_api项目接口发送')


# wlc
def get_friends():
    global friends, file_exist
    # print("exporting friends...")
    friends_file = "data/friends.txt"
    if not file_exist:
        os.system("python tools/get_friends.py > %s" % friends_file)
    with open(friends_file, "r") as f:
        while "message_type: 11030" not in f.readline():
            pass
        raw = f.readline().strip(" message:")
        friends = eval(raw)


# print("Friends exported!!")

# wlc
def get_chatrooms():
    global chatrooms, file_exist
    chatrooms_file = "data/chatrooms.txt"
    if not file_exist:
        os.system("python tools/get_chatrooms.py > %s" % chatrooms_file)
    with open(chatrooms_file, "r") as f:
        while "message_type: 11031" not in f.readline():
            pass
        raw = f.readline().strip(" message:")
        chatrooms = eval(raw)


# wlc
def get_recalled_msg(message_data):
    global showInConsole
    with open("data/log.txt", "r") as f:
        for data in f:
            tt = data.split('\t')[-1]
            msg = eval(tt.strip(' message:'))
            if type(msg) == dict:
                try:
                    if msg['msgid'] in message_data['raw_msg'] and showInConsole:
                        print("[recalled TEXT]---")
                        print("from", get_remark(msg['from_wxid']))
                        if (msg['room_wxid'] != ''):
                            print("to chatroom:", get_chatroom_remark(msg['to_wxid']))
                        else:
                            print("to:", get_remark(msg['to_wxid']))
                        print("内容为：", msg['msg'])
                        print("----")
                        return
                except:
                    pass


if __name__ == "__main__":
    showInConsole = 1  # 表示是否把信息显示在console里
    file_exist = 1  # 表示friends.txt,chatrooms.txt文件是否存在

    word_times = dict()
    # 获取好友、群聊的信息
    friends = dict()
    chatrooms = dict()
    get_friends()
    get_chatrooms()

    f = open("data/log.txt", "w")
    f.close()  # 清空log.txt里的数据

    # 每次运行完程序，log.txt里都会有这次运行过程中微信产生的消息

    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)
    print("ok!")
    get_common_words()
    l_word_times = list(word_times.items())
    l_word_times.sort(key=lambda w: w[1], reverse=1)
    print(l_word_times[0:20])

    # 阻塞主线程
    while True:
        time.sleep(0.5)
    # break
