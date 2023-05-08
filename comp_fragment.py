def remove_lowercase(infile,outfile):
    output=open(outfile,"w")
    for line in open(infile):
        if not line[0] in "abcdefghijklmnopqrstuvwxyz":
            output.write(line)
    output.close()
infile=open("F:\\File\\poem.txt", 'r')
outfile=open("F:\\File\\setu.txt", 'w')
remove_lowercase(infile,outfile)