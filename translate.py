# this file will translate english to utf and utf to english
# this will be a security thing


test = "\x74\x65\x73\x74"

print(test)


# if the thing above this works then this here should
testFileName = open("textFiles/test.txt").read()

print(testFileName.encode('utf8'))
