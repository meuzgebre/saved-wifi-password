import subprocess
import os

def get_wifi_pass():
	data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
	wifi_name = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]
	pass_file = open('wifi_pass.txt', 'w+')

	# Print In Console
	print('-' * 72)
	print('|{:<33}|| {:<35}|'.format('WIFI Name', 'WIFI Password'))
	print('-' * 72)

	# Write In File
	pass_file.write('-' * 72)
	pass_file.write('\n|{:<33}|| {:<35}|\n'.format('WIFI Name', 'WIFI Password'))
	pass_file.write('-' * 72)

	for wifi in wifi_name:
		res = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split('\n')
		res = [line.split(':')[1][1:-1] for line in res if 'Key Content' in line]

		try:
			# print(f'|\t {wifi} \t\t \t\t {res[0]} \t\t|')
			print('|{:<33}|| {:<35}|'.format(wifi, res[0]))

			# Write Password To File
			pass_file.write('\n|{:<33}|| {:<35}|'.format(wifi, res[0]))
		except IndexError:
			pass

	print('-' * 72)
	pass_file.write('\n')
	pass_file.write('-' * 72)
	pass_file.close()


if __name__ == '__main__':
	get_wifi_pass()