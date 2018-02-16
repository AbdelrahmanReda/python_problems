while True :
    x= int(input())
    
    intailaizer=1
    
    
    for q in range (len(str(x))+2):    
        
        comprator=None
        stage_one=(x-(intailaizer)**2)/(2*intailaizer)
        stage_three=stage_two-((stage_one)**2/(2*stage_two))
        print(stage_three)
        intailaizer=stage_three
        




