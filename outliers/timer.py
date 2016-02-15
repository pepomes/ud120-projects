import datetime

diff = 2

t0 = time.localtime()
t1 = t0 + diff
while time.localtime() < t1:
    print t1 - time.localtime()
print "\a"
