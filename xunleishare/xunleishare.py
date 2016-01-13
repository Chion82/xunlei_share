# coding=utf-8

import requests, argparse

class XunleiShare(object):

	def __init__(self):
		self.get_host()

	def get_host(self):
		request_result = requests.get('https://raw.githubusercontent.com/Chion82/Chion82.github.io/master/server_host')
		self.__host = request_result.text.replace('\n','')

	def get_gdrive_id(self):
		request_json = requests.get(self.__host + '/api/gdriveid').json()
		self.__gdrive_id = request_json['gdriveid']
		return self.__gdrive_id

	def commit_magnet_task(self, magnet_link):
		request_json = requests.post(self.__host + '/api/commit_magnet.do', data={'magnet_link':magnet_link}).json()
		return request_json

	def commit_normal_task(self, download_link):
		request_json = requests.post(self.__host + '/api/commit_normal_task.do', data={'link':download_link}).json()
		return request_json

	def query_task(self, task_id):
		request_json = requests.get(self.__host + '/api/task/' + task_id).json()
		return request_json


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('link', type=str, help='The download link')
	parser.add_argument('-o', '--output', help='The output shell script which contains the Aria2 download commands')
	parser.add_argument('-a', '--async', action='store_true', help='Download in asynchronous mode. If specified, each generated aria2c command is followed by an "&"')
	args = parser.parse_args()

	xunlei = XunleiShare()
	gdrive_id = xunlei.get_gdrive_id()

	if (args.link.find('magnet:?') != -1):
		commit_result_json = xunlei.commit_magnet_task(args.link)
	else:
		commit_result_json = xunlei.commit_normal_task(args.link)

	if (commit_result_json['status'] != 'OK'):
		print('提交任务失败，请重试')
		print('Failed to commit download task. Please retry.')
		if 'error' in commit_result_json:
			if 'msg' in commit_result_json['error']:
				print('ERR_MSG=%s' % commit_result_json['error']['msg'])
		exit()

	task_query_result_json = xunlei.query_task(commit_result_json['task_id'])

	if (task_query_result_json['status'] == 'Task Not Finished'):
		print('任务未完成，进度：' + str(task_query_result_json['progress']))
		print('Download task unfinished. Progress: ' + str(task_query_result_json['progress']))
		exit()

	if (task_query_result_json['status'] != 'OK'):
		print('未知错误')
		print('Unknown error.')
		exit()

	commands = '#!/bin/sh\n'
	for file_info in task_query_result_json['records']:
		commands  = commands + ('aria2c -c -s10 -x10 --header "Cookie: gdriveid=%s;" -o "%s" "%s" %s\n' % (gdrive_id, file_info['title'], file_info['downurl'], '&' if args.async else ''))

	if (args.output):
		output_file = args.output
	else:
		output_file = 'xunlei_output'

	import sys
	f = open(output_file, 'w+')
	if sys.version_info.major == 2:
		f.write(commands.encode('utf8'))
	elif sys.version_info.major == 3:
		f.write(commands)
	f.close()

	import subprocess
	subprocess.call(['chmod', '755', output_file])

	print('Aria2命令已输出至 %s ' % output_file)
	print('Aria2 commands are generated into %s ' % output_file)
