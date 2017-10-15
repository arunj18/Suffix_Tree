import data_clean as dc
import classes as cl
import copy
clean_data,results_data=dc.get_data()
print(dc.verify_data(clean_data))
working_data=copy.deepcopy(clean_data)
#for x in working_data:
	#x[0]=x[0].replace(' ','$')
	#x[1]=x[1].replace(' ','$')
#print(working_data)
#print(working_data[0])
#print(clean_data[0])
#print(results_data[0])

#print(working_data[0][1])
Tree=cl.GStree(working_data)
#Tree.first_occur("fox")
Tree.rel("wolf lamb")
#Tree.check_word("wolf")
#Tree.check_word("wolf")
