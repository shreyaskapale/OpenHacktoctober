import matplotlib.pyplot as plt
from textblob import TextBlob
name={}       # how many times person made new text(new line)
word={}       # different  words count for different persons
countword={}  # count of total words for persons
explodeit={}
date={}       # for date
datecheck={}
temp={}
tot=0
pos=0
neg=0;

f=open('inpu.txt','r')     # opens a txt file which contains chat
#print(f.read())
for line in f:
 print(line)
 line=line.strip()
 if line:
    
    fir =line.split("- ")
    if len(fir)>1:
      fir1=fir[1].split(': ')
      dateit=fir[0].split(',')
      if dateit[0] not in datecheck:
        datecheck[dateit[0]]=dateit[0]
        date[dateit[0]]={}
      if fir1[0] not in name:
         name[fir1[0]]=1
         word[fir1[0]]={}
         explodeit[fir1[0]]=0.02
         countword[fir1[0]]=0
      
         
      else:
        name[fir1[0]]+=1

      fir2=fir1[1].split(' ')
      for wording in fir2:
        if wording in word[fir1[0]]:
            word[fir1[0]][wording]+=1
        else:
            word[fir1[0]][wording]=1;
        testimonial = TextBlob(wording)
        tot+=testimonial.sentiment.polarity
        if testimonial.sentiment.polarity>0:
           pos+=testimonial.sentiment.polarity
        else:
          neg+=testimonial.sentiment.polarity
        countword[fir1[0]]+=1
        date[dateit[0]][fir1[0]]=countword[fir1[0]]

#print(fir1)
print(word)
print(countword)
print("total sentiment is ")
print(tot)
print("total positve sentiment is ")
print(pos)
print("total negative sentiment is ")
print(neg)


print(name)
s= 'Person 1'
c=0;
print(date)                 # to make date wise words
for gate ,v in date.items():
  print(gate)
  for s,t in v.items():
    if s in temp:
      v[s]=v[s]-temp[s]
      #print("hee")
      #print(v)
  temp=v
  print(temp)

  print(date)

  if tot>0:
    print("chat is positive through out of about ")
    print(tot)
  else:
    print("chat is negative of about")
    print(tot) 

f.close()

labels = list(name.keys())
sizes = list(name.values())
explode = list(explodeit.values())

fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode= explode ,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  
plt.title('number of new lines')

labels = list(countword.keys())
sizes = list(countword.values())
explode = list(explodeit.values())

fig2, ax2 = plt.subplots()
ax2.pie(sizes,explode= explode ,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax2.axis('equal')  
plt.title('number of total words')


neg=abs(neg)
labels = ['positive chat','negative chat']
sizes = [pos,neg]
explode = [0.02,0.02]

fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode= explode ,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  
plt.title('sentiment about chat')


plt.show()

 


  