import subprocess
import glob

ipa = glob.glob('*.ipa')[0]

proc = subprocess.Popen('docker','run','--rm','-e',f'filename={str(ipa)}','-v','/tmp/ipas/:/home/work/files','ipax:latest'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

with open("res.txt","w") as f:
    f.write(out)
