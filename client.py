import data_clean as dc
import classes as cl
import copy
clean_data,results_data=dc.get_data()
print(dc.verify_data(clean_data))
working_data=copy.deepcopy(clean_data)
Tree=cl.GStree(working_data)
Tree.search('hello world')
