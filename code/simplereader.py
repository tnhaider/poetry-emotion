import sys

def readPoems(fn):
  poems = []
  poem = []
  stanza = []
  prev_line = None
  for line in open(fn):
    line = line.strip()
    if line=="": 
      if prev_line=="":
        if poem!=[]: 
          poems.append(poem)
          poem=[]
      else:
        if stanza!=[]: poem.append(stanza)
        stanza = []
    else:
      stanza.append(line.split("\t"))
    prev_line = line 
  if poem!=[]: poems.append(poem)
  return poems

def printpoem(poem,flag=""):
  for s in poem:
    for line in s:
      print(flag,line)
    print()

if __name__ == "__main__":

  poems = readPoems(sys.argv[1])
  doPrint=False
  #print(len(poems))
  distStanza = {}
  distPoem = {}
  stats0 = {}
  stats1 = {}
  fourline=0
  for poem in poems:
    n = len(poem)
    distPoem[n] = distPoem.get(n,0)+1
    if n==7 and doPrint: printpoem(poem)
    for stanza in poem:
      m = len(stanza)
      if m==2 and doPrint: printpoem(poem,flag=">>>")
      distStanza[m] = distStanza.get(m,0)+1
      if m==4: 
        printpoem([stanza],">>")
        fourline+=1
        emo1,emo2 = set(),set()
        for verse in stanza: 
          a0,a1 = verse[1],verse[2]
          for e in a0.split(" --- "): emo1.add(e)
          for e in a1.split(" --- "): emo2.add(e)
        e1 = len(emo1)
        e2 = len(emo2)
        stats0[e1] = stats0.get(e1,0)+1
        stats1[e2] = stats1.get(e2,0)+1 

  print(fourline)
  for e in sorted(stats0):
    print(e,stats0[e]/(sum(stats0.values())),stats1[e]/(sum(stats1.values())))

  print("=== Poems with n stanzas")
  for n in sorted(distPoem):
    print("n={}".format(n),distPoem[n])
  print("=== Stanzas with m lines")
  for m in sorted(distStanza):
    print("m={}".format(m),distStanza[m]) 

