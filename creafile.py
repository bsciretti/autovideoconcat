import sys,os
nome = sys.argv[1]
numero=int(sys.argv[2])
base = ""
i = 1
while i <= numero:
	base=base+"file "+nome+str(i)+".mkv"+"\n"
	i = i+1
print(base)
f = open("files.txt", "w")
f.write(base.rstrip())
f.close()
query ="ffmpeg -f concat -safe 0 -i files.txt -c copy {}.mkv".format(nome)
os.system(query)
