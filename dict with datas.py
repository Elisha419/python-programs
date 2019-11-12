#create a dict,add dates like,roll_no,marks,along with gender,now I want to print all the names
#and marks whose gender is male,how would you do that?for female all females name and marks no
#discrimination pls :D

Dict={'roll no':[1,2,3,4],'marks':[50.0,60.0,70.0,80.0],'name':["Ram","Hari","Sita","Gita"],'gender':["male","male","female","female"]}

for i in range(len(Dict['roll no'])):
    if Dict['gender'][i]=='male':
       print(Dict['marks'][i])
       print(Dict['name'][i])
       print(Dict['gender'][i])

















