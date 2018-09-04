import requests
from config import pause, token

class University:
	def __init__(self, vk_university_id):
		self.id = vk_university_id


class User:
	def __init__(self, vk_user_id):
		data = get_user(vk_user_id)
		self.first_name = data['first_name']
		self.last_name = data['last_name']

		if 'bdate' in data and len(data['bdate'].split('.')) == 3:
			self.age = 2018 - int(data['bdate'][-4:])
			self.age_was_guessed = False
		else:
			self.age = guess_user_age(data['id'])
			self.age_was_guessed = True			

		if 'occupation' in data:
			if data['occupation']['type'] == 'university':		
				self.university = University(data['occupation']['id'])
			else:
				self.university = None
		else:
			# try to guess
			self.university = guess_user_university(data['id'])

	def __str__(self):
		return "{first_name} {last_name}, age = {age}, student of {university}".format(
			first_name=self.first_name,
			last_name=self.last_name,
			age=self.age,
			university=self.university)
			


@pause
def fetch_friends(vk_user_id):
	url = 'https://api.vk.com/method/friends.get?user_id={vk_user_id}&access_token={token}&v=5.84'.format(vk_user_id=vk_user_id, token=token)
	r = requests.get(url)
	return [str(vk_id) for vk_id in r.json()['response']['items']]


@pause
def get_user(vk_user_id):
	url = 'https://api.vk.com/method/users.get?user_id={vk_user_id}&fields=bdate,education,occupation&access_token={token}&v=5.84'.format(vk_user_id=vk_user_id, token=token)
	r = requests.get(url)
	return r.json()['response'][0]


@pause
def guess_user_age(vk_user_id):
	return None


@pause
def guess_user_university(vk_user_id):
	pass


if __name__ == '__main__':
	friends_id = fetch_friends('91224186')
	for friend_id in friends_id:
		person = User(friend_id)
		print(person)
