import re

p = re.compile('\"unitPeriodBill":\')
print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
