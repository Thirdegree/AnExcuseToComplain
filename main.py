import praw, re

r = praw.Reddit("AnExcuseToComplain by /u/thirdegre")

def _login():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)
	return USERNAME

Trying = True
while Trying:
	try:
		USERNAME = _login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

def main():
	pattern = r"^\/r\/SummerReddit( )*$"
	stream = praw.helpers.comment_stream(r, "all")
	for comment in stream:
		match = re.match(pattern, comment.body)
		if match:
			comment.reply("/r/AnExcuseToComplain")
			r.submit("AnExcuseToComplain","/u/%s's Attempt at Easy Karma"%comment.author.name, url=comment.permalink)

while True:
	try:
		main()
	except Exception as e:
		print e
		if e == KeyboardInterrupt:
			raise e