from imp import reload
import time
while True:
    from testPkg import test
    reload(test)
    print(test.aVar)
    time.sleep(10)
