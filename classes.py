import os
class GStree(object):
	class Node(object):
		def __init__(self,title=-1,word=-1):
			self.out = {}
			self.title=title
			self.word=word
		def get_all(self):
			occur=[]
			def get_all_inner(s):
				for x in s.out.keys():
					if(x=='$'):
						if(type(s.out['$'])==list):
							for y in s.out['$']:
								occur.append((y.title,y.word))
						else:
							occur.append((s.out['$'].title,s.out['$'].word))
					elif('$' in x):
						occur.append((s.out[x].title,s.out[x].word))
					else:
						get_all_inner(s.out[x])
			get_all_inner(self)
			return occur
	def __init__(self,working_data):
		self.root = self.Node()
		self.working_data=working_data
		self.word_count=0
		print("Tree initialized!")
		for x in range(len(working_data)):
			self.working_data[x][1]=self.working_data[x][1].lower()
			self.working_data[x][1]=self.working_data[x][1].split(' ')
		print("Building Tree...")
		for x in range(len(working_data)):
			for y in range(len(working_data[x][1])-1):
				self.add_word(working_data[x][1][y],x,y)
		print("Tree built.")
		print("Tree status: ",self.tree_status()," words")
	def search(self,word):
		word=word.split(' ')
		if(type(word)==list):
			print("Erroneous Usage. More than one word detected. Use .rel() instead")
			return
		occur=self.check_word(word)
		if(occur):
			for x in occur:
				print("Found in Title: ",self.working_data[x[0]][0])
				if(x[1]-5<0):
					f_i=0
				else:
					f_i=x[1]
				if(x[1]+5>len(self.working_data[x[0]][1])-1):
					e_i=len(self.working_data[x[0]][1])-1
				else:
					e_i=x[1]+5
				print("Phrase: ",end=' ')
				for y in range(f_i,e_i+1):
					print(self.working_data[x[0]][1][y],end=' ')
				print('\n')
		else:
			print("No occurences found")
	def rel(self,sentence):
		sentence=sentence.split(' ')
		flag=False
		if(len(sentence)==1):
			self.search(sentence[0])
		else:
			title_wise={}
			for x in range(len(self.working_data)):
				title_wise[x]={}
				for y in sentence:
					title_wise[x][y]=[]
			for x in sentence:
				occur=self.check_word(x)
				for y in occur:
					title_wise[y[0]][x].append(y[1])
			deletions=[]			
			for x in title_wise.keys():
				flag=True
				for y in sentence:
					title_wise[x][y].sort()
					if(title_wise[x][y]):
						flag=False
				if(flag):
					deletions.append(x)
			for x in deletions:
				del title_wise[x]
			scores=self.get_scores(title_wise,sentence)
			order=list(scores.keys())
			order.sort(reverse=True)
			for x in order:
				if(type(scores[x])==list):
					for y in scores[x]:
						flag=True
						print("Title: ",self.working_data[y[0]][0])
						for z in range(y[2],y[1]+1):
							print(self.working_data[y[0]][1][z], end=" ")
						print("\n---------------------------------------------------------")
				else:
					y=scores[x]
					flag=True
					print("Title: ",self.working_data[y[0]][0])
					for z in range(y[2],y[1]+1):
						print(self.working_data[y[0]][1][z], end= " ")
					print("\n-------------------------------------------------------------")
			if(flag==False):
				print("No occurences found")
	def get_scores(self,title_wise,sentence):
		scores={}
		for x in title_wise.keys():
			score=0
			max_i=-1
			min_i=9999999999
			for z in sentence:
				score+=len(title_wise[x][z])
			for z in range(1,len(sentence)):
				if(title_wise[x][sentence[z-1]] and title_wise[x][sentence[z]]):
					if(min(title_wise[x][sentence[z-1]]) < min(title_wise[x][sentence[z]])):
						score+=len(self.working_data[x][1])-(min(title_wise[x][sentence[z]])-min(title_wise[x][sentence[z-1]]))
					if(max(title_wise[x][sentence[z-1]]) < max(title_wise[x][sentence[z]])):
						score+=len(self.working_data[x][1])-(max(title_wise[x][sentence[z]])-max(title_wise[x][sentence[z-1]]))
			for z in range(len(sentence)):
				if(title_wise[x][sentence[z]]):
					if(max(title_wise[x][sentence[z]]) > max_i):
						max_i=max(title_wise[x][sentence[z]])
					if(min(title_wise[x][sentence[z]]) < min_i):
						min_i=min(title_wise[x][sentence[z]])
			if(score not in scores.keys()):
				scores[score]=(x,max_i,min_i)
			elif(type( scores[score])==list):
				scores[score].append((x,max_i,min_i))
			else:
				scores[score]=[scores[score],(x,max_i,min_i)]
		return scores
	def add_word(self,word,title_no=-1,word_no=-1):
		if(title_no==-1 or word_no==-1):
			print("Erroneous Usage.")
			return
		for i in range(len(word)):		
			s=self.root
			while(True):
				check_list=[]
				if(s.out.keys()):
					for x in s.out.keys():
						check_list=[]
						check_list.append(x)						
						check_list.append(word[i:])
						check_prefix=os.path.commonprefix(check_list)
						if(check_prefix!=''):
							break
				else:					
					check_prefix=''
				change=len(check_prefix)
				if(change==0):
					n=self.Node(title_no,word_no)
					if(word[i:]=='' and '$' in s.out.keys()):
						if(type(s.out['$'])==list):
							s.out['$'].append(n)
						else:
							s.out['$']=[s.out['$'],n]
					else:					
						s.out[word[i:]+'$']=n
					break
				elif(change>0 and check_prefix not in s.out.keys()):
					for x in list(s.out.keys()):
						if(x.startswith(check_prefix)):
							y=x
							break
					temp=s.out[y]
					s.out.pop(y)
					s.out[check_prefix]=self.Node()
					s=s.out[check_prefix]
					if(word[i+change:]=='' and y[change:]=='$'):
						s.out['$']=[temp,self.Node(title_no,word_no)]
							
					else:
						s.out[y[change:]]=temp
						s.out[word[i+change:]+'$']=self.Node(title_no,word_no)
					break
				else:
					i+=change
					s=s.out[check_prefix]
		self.word_count+=1
	def tree_status(self):
		return self.word_count
	def check_word(self,word):
		s=self.root
		occur=[]
		i=0
		while(True):
			check_list=[]
			if(s.out.keys()):
				for x in s.out.keys():
					check_list=[]
					check_list.append(x)						
					check_list.append(word[i:])
					check_prefix=os.path.commonprefix(check_list)
					if(check_prefix!=''):
						break
			else:					
				check_prefix=''
			change=len(check_prefix)
			if(word[i:]!='' and check_prefix==''):
				break
			elif(word[i:]=='' and s.out.keys()):
				occur=s.out[y].get_all()
				break
			elif(word[i+change:]=='' and s.out.keys()):				
				for x in list(s.out.keys()):
						if(x.startswith(check_prefix)):
							y=x
							break
				if('$' in y):
					occur.append((s.out[y].title,s.out[y].word))
				else:
					occur=s.out[y].get_all()
				break
			else:	
				s=s.out[check_prefix]
				i+=change
		return occur
	def diff_check(self,word,x):
		flag=True
		substrings = [word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1)]
		substrings.pop(len(word)-1)
		substrings.sort(key=len,reverse=True)		
		index={}
		for s in substrings:
			if(len(s) not in index.keys()):
				index[len(s)]=[]
				index[len(s)].append(s)
			else:
				index[len(s)].append(s)
		i=len(word)-1
		while(i>0):
			results=[]
			for z in index[i]:
				occur=self.check_word(z)
				for y in occur:
					if(y[0]==x):
						results.append(y[1])
			if(results):
				results.sort()				
				return results
			i=i-1
		return []
	def first_occur(self,word):
		occur=self.check_word(word)
		title_wise=[]
		if(occur):
			for x in range(len(self.working_data)):
				title=[]			
				for y in occur:
					if(y[0]==x):
						title.append(y[1])
				title_wise.append(title)
		result=[]
		for x in range(len(title_wise)):
			if(title_wise[x]):
				title_wise[x].sort()
			else:
				title_wise[x]=self.diff_check(word,x)
		for x in range(len(title_wise)):
			print("Title : ",self.working_data[x][0])
			if(title_wise[x]):
				print("Word :",self.working_data[x][1][title_wise[x][0]])
			else:
				print("No occurences")
