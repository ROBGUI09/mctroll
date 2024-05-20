import subprocess
import glob

ipa = glob.glob('*.ipa')[0]

cmd = ['docker','run','-e',f'filename={str(ipa)}','-v','/tmp/ipas/:/home/work/files','ipax:latest']

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

with open("res.txt","wb") as f:
    f.write(out)
