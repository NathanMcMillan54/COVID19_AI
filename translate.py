# this file will translate english to utf and utf to english
# this will be a security thing
import io

# test = "\x74\x65\x73\x74"

# print(test)


# if the thing above this works then this here should
f = io.open("textFiles/test.txt", mode="r", encoding="utf-8")
print(f.read())
