import urllib3

email = 'tweetable@python.com'
resp = urllib3.PoolManager().urlopen('GET', 'https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(email),
                                     headers={'user-agent': 'Pwnage-Checker-For-Django'})
print('Breached' if resp.data else 'Secure')
