import sys
import binascii

def patch_binary(file, off, data):
	with open(file, 'rb') as fd:
		content = fd.read()

	# extend the file if size is not enough
	content = content.ljust(off, b'\x00')

	# replace the data at off
	content = content[:off] + data + content[off+len(data):]

	with open(file, 'wb') as fd:
		fd.write(content)

def parse_off(off_s):
	return int(off_s[2:], 16) if off_s[:2] == '0x' else int(off_s)

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage: python3 binpatch.py file offset hex", file=sys.stderr)
		exit(1)

	patch_binary( \
		sys.argv[1], parse_off(sys.argv[2]), binascii.unhexlify(sys.argv[3]))