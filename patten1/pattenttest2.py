
import re

s = ''' 01 bottle         
02 bag 
03                  big1
100 able'''


print(re.findall('\s+',s))

print(re.split('\s+\d+\s+'," " + s))
# 使用小括号的 pattern 捕获数据被放到







