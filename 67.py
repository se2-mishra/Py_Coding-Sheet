obj=open("F:\\File\New.txt","w")
obj.write("A poem by Paramhansa Yogananda")
obj.write("Better than Heaven or Arcadia")
obj.write("I love thee, O my India!")
obj.write("And thy love I shall give")
obj.write("To every brother nation that lives")
obj.close()
obj1=open("F:\\File\New.txt","r")
s1=obj1.read(48)
print(s1)
obj1.close()