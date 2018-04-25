# num = int(input(u"输入一个整数："))
# if num > 42:
#     print(u"这个数大于42")
# else:
#     print(u"这个数不大于42")

import random
import sys
print(sys.argv)
num = int(random.random()*100)
print(u"随机数已产生，猜猜我是几^-^")
for i in range(6):
    n = int(input(u"输入一个100以内整数："))
    if n == num:
        print(u"真厉害，你猜对了！！！")
        break
    elif n < num:
        print(u"你输的数太小了！！！")
    else:
        print(u"你输的太大了！！！")
print(u"随机数是"+str(num))
