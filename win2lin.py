import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python3 win2lin.py file", file=sys.stderr)
		exit(1)

	with open(sys.argv[1], 'rb') as fd:
		data = fd.read()

	data = data.replace(b'\x0d\x0a', b'\x0a')

	with open(sys.argv[1], 'wb') as fd:
		fd.write(data)

