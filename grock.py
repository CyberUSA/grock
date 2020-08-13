import vk_api
from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id
import time
## vkhost.github.io
vk_session = vk_api.VkApi(token = "YOU TOKEN")
vk_session._auth_token() 

vk = vk_session.get_api()
g = input("Domen group for spam: ")
msgnum = 0
def spam(group):
	msg = input("Message spam: ")
	users = vk.groups.getMembers(group_id=group)["items"]
	print("SPAM START\n")
	for user in users:
		try:
			info = vk.users.get(user_ids=user, offset=4720, fields="can_write_private_message, online")
			if info[0]["can_write_private_message"] == 1:
				if info[0]["online"] == 1:
					try:
						vk.messages.send(user_id=user, message=msg, random_id=get_random_id())
						print(info[0]["first_name"], info[0]["last_name"], "Получил ваше сообщение")
						msgnum += 1
					except:
						pass
				else:
					pass
			else:
				pass
		except:
			print("Ошибка | 1")



spam(g)
print("\nВсего оправлено:", msgnum)
