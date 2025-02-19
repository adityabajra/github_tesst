yname=(input("enter your name")).lower()
mname=(input("input her name")).lower()
combined_string = yname + mname 
counttrue=combined_string.count("t")
counttrue += combined_string.count("r")
counttrue +=combined_string.count("u")
counttrue +=combined_string.count("e")
countlove =combined_string.count("l") 
countlove +=combined_string.count("o") 
countlove +=combined_string.count("v") 
countlove +=combined_string.count("e") 
lov_score= counttrue*10+countlove
if lov_score <10 or lov_score >90:
    print("yo go together like coke and mentos")
elif lov_score>40 and lov_score<50:
    print(f"{lov_score}you are alright together")
else:
    
    print(f"{lov_score}hehe")    
    print("testing github") 