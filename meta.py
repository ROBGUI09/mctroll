import subprocess
import glob

ipa = glob.glob('*.ipa')[0]

cmd = ['pyipa',"-o","meta.json",ipa]

os.system(cmd)
