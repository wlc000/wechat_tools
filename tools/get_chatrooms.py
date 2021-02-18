# -*- coding: utf-8 -*-
'''
该程序是从demo.py复制过来，稍加改动得到的。
用于得到群聊列表。

'''


from __future__ import unicode_literals

import wechat
import json
import time
import sys
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../../libs')


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
	# print('[on_connect]\nclient_id: {0}'.format(client_id))
	pass

@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):	# 和LoginTipBot.on_message()效果差不多
	print('[on_recv]\n client_id: {0}\n message_type: {1}\n message:{2}\n'.format(client_id,
																			message_type, json.dumps(message_data)))
	pass


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
	# print('[on_close]\nclient_id: {0}'.format(client_id))
	pass


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

	@wechat.RECV_CALLBACK(in_class=True)
	def on_message(self, client_id, message_type, message_data):
		# print(message_type)
		# 判断登录成功后，就向文件助手发条消息
		if message_type == MessageType.MT_USER_LOGIN:
			# wechat_manager.send_text(client_id, 'filehelper', '[Doge][Doge]该消息通过wechat_pc_api项目接口发送~哈哈')
			wechat_manager.get_chatrooms(client_id)

		


if __name__ == "__main__":

	

	bot = LoginTipBot()

	# 添加回调实例对象
	wechat_manager.add_callback_handler(bot)
	wechat_manager.manager_wechat(smart=True)


	time.sleep(2)
	time.sleep(2)
	time.sleep(2)

	