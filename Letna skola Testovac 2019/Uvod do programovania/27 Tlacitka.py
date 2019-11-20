x = int(input())

def akcia10():
  print("ABD", end = '')
  
def akcia20():
  print("ACD", end = '')
  
def akcia40():
  print("A", end = '')
  akcia20()
  print("D",  end = '')

def akcia30():
  print("A" +"C"*5 + "D", end = '')

def akcia50():
  print("A", end ='')
  akcia30()
  print("C", end = '')
  akcia10()
  akcia10()
  akcia10()
  akcia10()
  akcia10()
  print("D", end = '')

def akcia1():
  print("ABD")

def akcia2():
  print("ACD")
  
def akcia3():
  print("A" +"C"*5 + "D")
  
def akcia4():
  print("A", end = '')
  akcia20()
  print("D")
  
def akcia5():
  print("A", end ='')
  akcia30()
  print("C", end = '')
  akcia10()
  akcia10()
  akcia10()
  akcia10()
  akcia10()
  print("D")
  
def akcia6():
  print("A", end = '')
  akcia50()
  print("C", end = '')
  print("B"*5, end = '')
  akcia40()
  akcia40()
  akcia40()
  akcia40()
  akcia40()
  print("D")


  
if x == 1:
    akcia1()

if x == 2:
    akcia2()
    
if x == 3:
    akcia3()
    
if x == 4:
    akcia4()
    
if x == 5:
    akcia5()
    
if x == 6:
    akcia6()


