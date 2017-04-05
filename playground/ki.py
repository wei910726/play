from datetime import date
import re
# now = date.today()
# print(str(now))
s = '0I7OU76EFCWNOHQSVT1H'
p = re.compile(r'^[0-9A-Z].*$')
ls = p.match(s)
if ls:
    print(ls.group())