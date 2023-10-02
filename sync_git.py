import subprocess
import sys
import os

def get_modified_files(repo):
	lines = subprocess.run(["git", "-C", repo, "status", "--porcelain"], \
		stdout=subprocess.PIPE, text=True).stdout.splitlines()
	return [line.split(" ")[-1] for line in lines]

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage: python3 sync_git.py " + \
			"[local repo path] [remote ssh user@address] [remote repo path]", \
			file=sys.stderr)
		exit(1)

	while True:
		modified = get_modified_files(sys.argv[1])
		for f in modified:
			subprocess.run(["scp", "-r", os.path.join(sys.argv[1], f), \
				sys.argv[2] + ':' + os.path.join(sys.argv[3], f)])