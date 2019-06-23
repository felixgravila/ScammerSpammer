import requests
import random
import json

# URL
url = ''
# Number of spam calls
spamcalls = 10
# Payload format
def makePayload(user, pwd):
    return {
        "xuser": user,
        "xpass": pwd
    }


def adjustPasswords(pwd):
    while len(pwd) < 8:
        pwd = pwd + str(int(random.uniform(0,100)))
    if pwd[0].isalpha():
        return pwd[0].upper() + pwd[1:];
    return "Password" + pwd

with open('first-names.txt') as f:
    firstnames = list(f)
with open('last-names.txt') as f:
    lastnames = list(f)
with open('1000-most-common-passwords.txt') as f:
    passwords = list(f)
firstnames = list(map((lambda s: s.replace('\n','').lower()), firstnames))
lastnames = list(map((lambda s: s.replace('\n','').lower()), lastnames))
passwords = list(map(adjustPasswords, map((lambda s: s.replace('\n','')), passwords)))

joining=['','.','-','_']
providers=['gmail','yahoo','aol','mail','outlook', 'icloud.com']

def makeRandomMailAddress():
    fst = random.choice(firstnames)
    snd = random.choice(lastnames)
    join = random.choice(joining)
    provider = random.choice(providers)
    m = ""
    if random.uniform(0,1) > 0.75:
        m = m + fst[0] + snd
    else:
        m = m + fst + join + snd

    if random.uniform(0,1) > 0.75:
        if random.uniform(0,1) > 0.5:
            ryear = str(int(random.uniform(1950, 2010)))
        else:
            ryear = str(int(random.uniform(0,99)))
        m = m + ryear

    return m + "@" + provider + ".com"


for i in range(0,spamcalls):
    mail = makeRandomMailAddress()
    pwd = random.choice(passwords)
    data = makePayload(mail,pwd)
    response = requests.post(url, data=data).status_code
    i += 1
    print("%s - %s %s (%s)" % (i, mail, pwd, response))
