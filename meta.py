import glob,os

ipa = glob.glob('*.ipa')[0]

cmd = ['pyipa',"-o","meta.json",ipa]

os.system(cmd)
