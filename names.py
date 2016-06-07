def partone(students):
    for i in range (0, len(students)):
        for j in students[i].itervalues():
            print j,
        print ""
  
def parttwo(names):
    count=1
    
    for key,val in names.items():
        print key
        for i in range (0, len(val)):
            print count,"-",
            count+=1
            lettercount=0
            for j in val[i].itervalues():
            	
                print j,
                for l in range (0,len(j)):
                	lettercount+=1
        
            
            print "-",lettercount,
            print ""



students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
partone(students)
parttwo(users)
