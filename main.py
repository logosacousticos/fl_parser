# def bytes_from_file(filename, chunksize=8192):
#     with open(filename, "rb") as f:
#         while True:
#             chunk = f.read(chunksize)
#             if chunk:
#                 for b in chunk:
#                     yield b
#             else:
#                 break


def bytes_from_file(filename, chunksize=64):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

# example:
text = ''
for b in bytes_from_file('test.flp'):
    text += chr(b)

print(text)