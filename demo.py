# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import json
import time
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
	print('[on_connect] client_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
	print('[on_recv]\n client_id: {0}\n message_type: {1}\n message:{2}\n'.format(client_id,
																			message_type, json.dumps(message_data)))


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
	print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

	@wechat.RECV_CALLBACK(in_class=True)
	def on_message(self, client_id, message_type, message_data):
		# 判断登录成功后，就向文件助手发条消息
		if message_type == MessageType.MT_USER_LOGIN:
			time.sleep(2)
			# wechat_manager.get_friends(client_id)
			

if __name__ == "__main__":
	bot = LoginTipBot()

	# 添加回调实例对象
	wechat_manager.add_callback_handler(bot)
	wechat_manager.manager_wechat(smart=True)

	# 阻塞主线程
	while True:
		time.sleep(0.5)
	'''
	 TODO:
		结合内容画图
		个人数据分析统计
		
	
	'''