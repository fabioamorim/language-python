from io import StringIO

message = "Hello guys"

file = StringIO(message)

print(file)
# <_io.StringIO object at 0x0000021EA00408B0>

print(file.read())
# Hello guys

file.seek(0)

print(file.read())
# Hello guys