import sys
__author__ = "Colin"

print(sys.getdefaultencoding())

s = "hello world."

s_gbk = s.encode("gbk")
s_unicode1 = s_gbk.decode("gbk")

s_utf8 = s.encode("utf-8")
s_unicode2 = s_utf8.decode("utf-8")
print(s)
print(s_gbk)
print(s_unicode1)
print(s_utf8)
print(s_unicode2)
print('-') * 9
gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)
