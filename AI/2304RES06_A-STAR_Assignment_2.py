#from collections import deque
import matplotlib.pyplot as plt
import time
import tracemalloc
import math

GS=[[1,2,3],[4,5,6],[7,8,0]]

#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def Blank_Tile_Position(matrix) :

  p=0
  q=0

  for i in range (0,3,1) :
    for j in range (0,3,1) :
      if (matrix[i][j]==0) :
        p=i
        q=j
        pos=[p,q]
  return (pos)


#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def Any_Tile_Position(num, matrix) :

  p=0
  q=0

  for i in range (0,3,1) :
    for j in range (0,3,1) :
      if (matrix[i][j]==num) :
        p=i
        q=j
        pos=[p,q]
  return (pos)

#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def convergence_calculator(matrix) :

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]

  row_major_order=[a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2]]
  row_major_order.remove(0)
  #print(f"\nRow Major Order form of Input Matrix : {matrix} is given as : {row_major_order} and it's length is : {len(row_major_order)}")

  k=0

  for i in range (0,8,1) :
    for j in range (0,8,1) :
      if ((i<j) and (row_major_order[i]>row_major_order[j])) :
        k=k+1

  #print (f"\nNo. of Inversions in this given 8-Puzzle Problem is {k}")

  if (k%2 == 0) :
    print(f"\nGiven Matrix : {matrix} has {k} numbers of inversions and since it's an EVEN Integer, this 8-Puzzle Problem will CONVERGE to the Goal State!")
    conv=1
  else :
    print(f"\nGiven Matrix : {matrix} has {k} numbers of inversions and since it's an ODD Integer, this 8-Puzzle Problem will NOT CONVERGE to the Goal State!")
    conv=0


  return conv

#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def h1(matrix) :

  return 0

#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def h2(matrix) :

  misplaced_tiles=0

  for i in range(0,3,1) :
    for j in range(0,3,1) :

      if ((i==0) and (matrix[i][j]!=(i+j+1))) :
        misplaced_tiles=misplaced_tiles+1

      elif ((i==1) and (matrix[i][j]!=(i+j+3))) :
        misplaced_tiles=misplaced_tiles+1

      elif ((i==2) and (matrix[i][j]!=(i+j+5))) :
        misplaced_tiles=misplaced_tiles+1
  #print(f"\nNumber of misplaced tiles is {misplaced_tiles-1}")
  misplaced_tiles=misplaced_tiles-1
  return misplaced_tiles


#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def h3(matrix) :

  manhattan_distance=0


  for i in range (1,9,1) :
    pos1=Any_Tile_Position(i, matrix)
    pos2=Any_Tile_Position(i, GS)

    cartesian_euclidean_dist=math.sqrt(((pos1[0]-pos2[0])**2) + ((pos1[1]-pos2[1])**2))

    if (int(cartesian_euclidean_dist)==0) :
      continue
    elif ((cartesian_euclidean_dist)%1==0) :
      manhattan_distance = manhattan_distance + int(cartesian_euclidean_dist)
    elif ((cartesian_euclidean_dist)==math.sqrt(8)) :
      p=0
      p=int(cartesian_euclidean_dist)+2
      manhattan_distance = manhattan_distance + p
    else :
      k=0
      k=int(cartesian_euclidean_dist)+1
      manhattan_distance = manhattan_distance + k

  return manhattan_distance


#****************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************

def h4(matrix) :

  position_squared_weightage=0

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]

  row_major_order=[a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2]]
  row_major_order.remove(0)

  k=0

  for i in range (0,8,1) :
    for j in range (0,8,1) :
      if ((i<j) and (row_major_order[i]>row_major_order[j])) : #[12835674]
        k=k+1

  if k<=10 :
    for i in range (0, 8, 1) :
      position_squared_weightage=position_squared_weightage + (row_major_order[i]*((i+1)**2))

    position_squared_weightage_relative = 1296 - position_squared_weightage

  if k>10 :
    for i in range (0, 8, 1) :
      position_squared_weightage=position_squared_weightage + ((row_major_order[i]**2)*((i+1)**2))

    position_squared_weightage_relative = 9999 - position_squared_weightage

  return position_squared_weightage_relative



#*************************************************************************************************************************
#*************************************************************************************************************************

def Move_Generator(matrix) :

  neighbour_set=[]
  a2=Blank_Tile_Position(matrix)

  if (matrix==[[1,2,3],[4,5,6],[7,8,0]]) :
    neighbour_set = []
    print (f"\nDetected in Move_Generator() : Goal State is reached!")
    print (matrix)

  else :

    s1=matrix[0][:]
    s2=matrix[1][:]
    s3=matrix[2][:]
    Neighbour_Down=[s1,s2,s3]

    ns1=matrix[0][:]
    ns2=matrix[1][:]
    ns3=matrix[2][:]
    Neighbour_Left=[ns1,ns2,ns3]

    ss1=matrix[0][:]
    ss2=matrix[1][:]
    ss3=matrix[2][:]
    Neighbour_Right=[ss1,ss2,ss3]

    nss1=matrix[0][:]
    nss2=matrix[1][:]
    nss3=matrix[2][:]
    Neighbour_Up=[nss1,nss2,nss3]

    if (a2==[0,0]) :
      n_down=Neighbour_Down
      n_right=Neighbour_Right

      temp_down = n_down[1][0]
      n_down[1][0]=0
      n_down[0][0]=temp_down

      temp_right = n_right[0][1]
      n_right[0][1]=0
      n_right[0][0]=temp_right

      neighbour_set=[n_down,n_right]

    elif(a2==[0,1]) :
      n_down=Neighbour_Down
      n_right=Neighbour_Right
      n_left=Neighbour_Left

      temp_down = n_down[1][1]
      n_down[1][1]=0
      n_down[0][1]=temp_down

      temp_right = n_right[0][2]
      n_right[0][2]=0
      n_right[0][1]=temp_right

      temp_left = n_left[0][0]
      n_left[0][0]=0
      n_left[0][1]=temp_left

      neighbour_set=[n_down,n_right,n_left]

    elif(a2==[0,2]) :
      n_down=Neighbour_Down
      n_left=Neighbour_Left

      temp_down = n_down[1][2]
      n_down[1][2]=0
      n_down[0][2]=temp_down

      temp_left = n_left[0][1]
      n_left[0][1]=0
      n_left[0][2]=temp_left

      neighbour_set=[n_down,n_left]

    elif(a2==[1,0]) :
      n_down=Neighbour_Down
      n_right=Neighbour_Right
      n_up=Neighbour_Up

      temp_down = n_down[2][0]
      n_down[2][0]=0
      n_down[1][0]=temp_down

      temp_right = n_right[1][1]
      n_right[1][1]=0
      n_right[1][0]=temp_right

      temp_up = n_up[0][0]
      n_up[0][0]=0
      n_up[1][0]=temp_up

      neighbour_set=[n_down,n_right,n_up]

    elif(a2==[1,1]) :
      n_down=Neighbour_Down
      n_right=Neighbour_Right
      n_left=Neighbour_Left
      n_up=Neighbour_Up

      temp_down = n_down[2][1]
      n_down[2][1]=0
      n_down[1][1]=temp_down

      temp_right = n_right[1][2]
      n_right[1][2]=0
      n_right[1][1]=temp_right

      temp_left = n_left[1][0]
      n_left[1][0]=0
      n_left[1][1]=temp_left

      temp_up = n_up[0][1]
      n_up[0][1]=0
      n_up[1][1]=temp_up

      neighbour_set=[n_down,n_right,n_left,n_up]

    elif(a2==[1,2]) :
      n_down=Neighbour_Down
      n_left=Neighbour_Left
      n_up=Neighbour_Up

      temp_down = n_down[2][2]
      n_down[2][2]=0
      n_down[1][2]=temp_down

      temp_left = n_left[1][1]
      n_left[1][1]=0
      n_left[1][2]=temp_left

      temp_up = n_up[0][2]
      n_up[0][2]=0
      n_up[1][2]=temp_up

      neighbour_set=[n_down,n_left,n_up]

    if (a2==[2,0]) :
      n_right=Neighbour_Right
      n_up=Neighbour_Up

      temp_right = n_right[2][1]
      n_right[2][1]=0
      n_right[2][0]=temp_right

      temp_up = n_up[1][0]
      n_up[1][0]=0
      n_up[2][0]=temp_up

      neighbour_set=[n_right,n_up]

    elif(a2==[2,1]) :
      n_right=Neighbour_Right
      n_left=Neighbour_Left
      n_up=Neighbour_Up

      temp_right = n_right[2][2]
      n_right[2][2]=0
      n_right[2][1]=temp_right

      temp_left = n_left[2][0]
      n_left[2][0]=0
      n_left[2][1]=temp_left

      temp_up = n_up[1][1]
      n_up[1][1]=0
      n_up[2][1]=temp_up

      neighbour_set=[n_right,n_left,n_up]

    elif(a2==[2,2]) :
      n_left=Neighbour_Left
      n_up=Neighbour_Up

      temp_left = n_left[2][1]
      n_left[2][1]=0
      n_left[2][2]=temp_left

      temp_up = n_up[1][2]
      n_up[1][2]=0
      n_up[2][2]=temp_up
      neighbour_set=[n_left,n_up]

  return neighbour_set

#*************************************************************************************************************************
#*************************************************************************************************************************

def heuristics_monotonicity_checker(lis,num) :

  #lis is the 'path' output from the A* Search Algorithm!

  monotonicity_flag=0

  if (num==3) :
    int_3=[]
    for p3 in range (0, len(lis), 1) :
      int_3.append(h3(lis[p3]))

    k1=int_3
    #print(int_2)
    k1.sort(reverse=True)
    int_3_sorted = k1

    monotonicity_flag = (int_3_sorted==int_3)
    if monotonicity_flag :
      print ("\nh3(n) or Sum of Manhattan distances is a consistent & monotonic Heuristic!\n")
    else :
      print("\nMONOTONICITY CHECK FAILURE\n")



  elif (num==2) :
    int_2=[]
    for p2 in range (0, len(lis), 1) :
      int_2.append(h2(lis[p2]))

    k=int_2
    #print(int_2)
    k.sort(reverse=True)
    int_2_sorted = k

    #print(int_2_sorted)
    monotonicity_flag = (int_2_sorted==int_2)
    if monotonicity_flag :
      print ("\nh2(n) or Numbers of Misplaced Tiles is a consistent & monotonic Heuristic!\n")
    else :
      print("\nMONOTONICITY CHECK FAILURE\n")


  elif (num==1) :
    int_1=[]
    for p1 in range (0, len(lis), 1) :
      int_1.append(h1(lis[p1]))

    k2=int_1
    #print(int_2)
    k2.sort(reverse=True)
    int_1_sorted = k2

    #print(int_2_sorted)
    monotonicity_flag = (int_1_sorted==int_1)
    if monotonicity_flag :
      print ("\nh1(n)=0 a consistent & admissible Heuristic!\n")
    else :
      print("\nMONOTONICITY CHECK FAILURE\n")

  elif (num==4) :
    int_4=[]
    for p4 in range (0, len(lis), 1) :
      int_4.append(h4(lis[p4]))
    #print(f"\nInt_4 : {int_4}\n")

    k4=int_4
    #print(int_2)
    k4.sort(reverse=True)
    int_4_sorted = k4

    #print(f"\nInt_4_Sorted : {int_4_sorted}\n")

    #print(int_2_sorted)
    monotonicity_flag = (int_4_sorted==int_4)
    if monotonicity_flag :
      print ("\nh4(n) or, Position-Squared-Weightage-Relative a consistent & admissible Heuristic for the given initial state!\n")
    else :
      print("\nMONOTONICITY CHECK FAILURE\n")

  return monotonicity_flag


#*************************************************************************************************************************
#*************************************************************************************************************************

def astar_h1(matrix) :

  conv=convergence_calculator(matrix)

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]
  root=[a,b,c]

  clist=[]
  olist=[(root,0)]
  CP_list=[(root,"START")]
  I=0
  parent=[]


  while olist :

    I=I+1


    #print("\n\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    print(f"\nIteration Number :{I}\n")

    #print("\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

    heur=[]
    list_int=([],0)
    list_decider=[]

    for i in range (0, len(olist), 1) :
      pot_elmt, depth_pot_elmt = olist[i]
      score = h1(pot_elmt)
      decider = score + depth_pot_elmt
      list_int = (pot_elmt,decider)
      heur.append(list_int)

    #print(f"\nIn Iteration Number {I}, Members(n) of the Open-List and their corresponding [g(n) + h2(n)] scores : {heur}\n")

    for i1 in range(0, len(heur), 1) :
      pot_decider = heur[i1][1]
      list_decider.append(pot_decider)

    min_decider=min(list_decider)
    #print(f"\nMinimum value of [g(n) + h2(n)] Score : {min_decider}\n")
    min_decider_ind=list_decider.index(min_decider)
    #print(f"\nAND it is appearing at index '{min_decider_ind}' of the Open List\n")

    popped, steps = olist[min_decider_ind]
    clist.append(olist[min_decider_ind])
    olist.remove(olist[min_decider_ind])

    if (I==2000 and popped!=GS and conv==0) :
      print("\n\nFAILURE MESSAGE !!!\n\nSince we know beforehand from the convergence-calculator function, that the given initial State will not converge, we are exiting the A* Algorithm !!!\n\nThis is done due to hardware constraints as the compilation platform is unable to keep computing until Open_List=[] !!!\n\n")
      print("\n")
      return -1, I, -1, len(clist), olist, clist
      break

    if (popped==[[1,2,3],[4,5,6],[7,8,0]]) :
        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")
        #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

        print(f"\n\nSUCCESS MESSAGE!!!\n\nSTART STATE: {matrix}\n\nGOAL STATE : {GS}\n\nWITH A* ALGORITHM, GOAL STATE IS REACHED IN ITERATION No. :'{I}' AND IT APPEARS AFTER '{steps}' STEPS FROM INITIAL STATE, \n")

        Num_Explored_Nodes= len(clist)
        print(f"\nTotal Number of nodes explored to reach goal state : {Num_Explored_Nodes}\n")

        #print(f"\n{CP_list}\n")

        def index_finder(element,lis) :
          i_element=0
          for x in range(len(lis)-1,0,-1) :
            if (CP_list[x][0]==element) :
              i_element=x
              break
          return i_element

        t=index_finder(GS,CP_list)
        while t:
          q1=CP_list[t][1]
          parent.append(q1)
          t=index_finder(q1,CP_list)
        parent.insert(0,GS)

        path=parent[::-1]

        print(f"\nTotal Number of States in the Optimal path : {len(path)}\n")
        print("\nIn A* Algorithm using h(n)=0 as a heuristic , the path to goal state looks like this :\n")

        for y in range(0, len(path)-1,1) :
          print(f"\n{path[y]}==>\n")
        print(f"\n{GS}\n")

        heuristics_monotonicity_checker(path,1)


        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")

        return steps, I, path, Num_Explored_Nodes, olist, clist
        break

    neighbours=Move_Generator(popped)
    #print(f"\nFor Iteration {I}, and Popped State : {popped}, set of possible neighbours : {neighbours}\n")

    olist_elements=[]
    clist_elements=[]

    for k in range (0, len(olist), 1) :
      olist_elements.append(olist[k][0])

    for k1 in range (0, len(clist), 1) :
      clist_elements.append(clist[k1][0])

    for neighbour in neighbours:
        if ((neighbour not in olist_elements) and (neighbour not in clist_elements)) :
            olist.append((neighbour, steps+1))
            CP_list.append((neighbour,popped))



#*************************************************************************************************************************
#*************************************************************************************************************************

def astar_h2(matrix) :

  conv=convergence_calculator(matrix)

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]
  root=[a,b,c]

  clist=[]
  olist=[(root,0)]
  CP_list=[(root,"START")]
  I=0
  parent=[]


  while olist :

    I=I+1


    #print("\n\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    print(f"\nIteration Number :{I}\n")

    #print("\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

    heur=[]
    list_int=([],0)
    list_decider=[]

    for i in range (0, len(olist), 1) :
      pot_elmt, depth_pot_elmt = olist[i]
      score = h2(pot_elmt)
      decider = score + depth_pot_elmt
      list_int = (pot_elmt,decider)
      heur.append(list_int)

    #print(f"\nIn Iteration Number {I}, Members(n) of the Open-List and their corresponding [g(n) + h2(n)] scores : {heur}\n")

    for i1 in range(0, len(heur), 1) :
      pot_decider = heur[i1][1]
      list_decider.append(pot_decider)

    min_decider=min(list_decider)
    #print(f"\nMinimum value of [g(n) + h2(n)] Score : {min_decider}\n")
    min_decider_ind=list_decider.index(min_decider)
    #print(f"\nAND it is appearing at index '{min_decider_ind}' of the Open List\n")

    popped, steps = olist[min_decider_ind]
    clist.append(olist[min_decider_ind])
    olist.remove(olist[min_decider_ind])

    if (I==2000 and popped!=GS and conv==0) :
      print("\n\nFAILURE MESSAGE !!!\n\nSince we know beforehand from the convergence-calculator function, that the given initial State will not converge, we are exiting the A* Algorithm !!!\n\nThis is done due to hardware constraints as the compilation platform is unable to keep computing until Open_List=[] !!!\n\n")
      print("\n")
      return -1, I, -1, len(clist), olist, clist
      break

    if (popped==[[1,2,3],[4,5,6],[7,8,0]]) :
        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")
        #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

        print(f"\n\nSUCCESS MESSAGE!!!\n\nSTART STATE: {matrix}\n\nGOAL STATE : {GS}\n\nWITH A* ALGORITHM, GOAL STATE IS REACHED IN ITERATION No. :'{I}' AND IT APPEARS AFTER '{steps}' STEPS FROM INITIAL STATE, \n")

        Num_Explored_Nodes= len(clist)
        print(f"\nTotal Number of nodes explored to reach goal state : {Num_Explored_Nodes}\n")

        #print(f"\n{CP_list}\n")

        def index_finder(element,lis) :
          i_element=0
          for x in range(len(lis)-1,0,-1) :
            if (CP_list[x][0]==element) :
              i_element=x
              break
          return i_element

        t=index_finder(GS,CP_list)
        while t:
          q1=CP_list[t][1]
          parent.append(q1)
          t=index_finder(q1,CP_list)
        parent.insert(0,GS)

        path=parent[::-1]

        print(f"\nTotal Number of States in the Optimal path : {len(path)}\n")
        print("\nIn A* Algorithm using No.s of misplaced tiles as a heuristic, the path to goal state looks like this :\n")

        for y in range(0, len(path)-1,1) :
          print(f"\n{path[y]}==>\n")
        print(f"\n{GS}\n")

        heuristics_monotonicity_checker(path,2)


        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")

        return steps, I, path, Num_Explored_Nodes, olist, clist
        break

    neighbours=Move_Generator(popped)
    #print(f"\nFor Iteration {I}, and Popped State : {popped}, set of possible neighbours : {neighbours}\n")

    olist_elements=[]
    clist_elements=[]

    for k in range (0, len(olist), 1) :
      olist_elements.append(olist[k][0])

    for k1 in range (0, len(clist), 1) :
      clist_elements.append(clist[k1][0])

    for neighbour in neighbours:
        if ((neighbour not in olist_elements) and (neighbour not in clist_elements)) :
            olist.append((neighbour, steps+1))
            CP_list.append((neighbour,popped))



#*************************************************************************************************************************
#*************************************************************************************************************************

def astar_h3(matrix) :

  conv=convergence_calculator(matrix)

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]
  root=[a,b,c]

  clist=[]
  olist=[(root,0)]
  CP_list=[(root,"START")]
  I=0
  parent=[]


  while olist :

    I=I+1


    #print("\n\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    print(f"\nIteration Number :{I}\n")

    #print("\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

    heur=[]
    list_int=([],0)
    list_decider=[]

    for i in range (0, len(olist), 1) :
      pot_elmt, depth_pot_elmt = olist[i]
      score = h3(pot_elmt)
      decider = score + depth_pot_elmt
      list_int = (pot_elmt,decider)
      heur.append(list_int)

    #print(f"\nIn Iteration Number {I}, Members(n) of the Open-List and their corresponding [g(n) + h2(n)] scores : {heur}\n")

    for i1 in range(0, len(heur), 1) :
      pot_decider = heur[i1][1]
      list_decider.append(pot_decider)

    min_decider=min(list_decider)
    #print(f"\nMinimum value of [g(n) + h2(n)] Score : {min_decider}\n")
    min_decider_ind=list_decider.index(min_decider)
    #print(f"\nAND it is appearing at index '{min_decider_ind}' of the Open List\n")

    popped, steps = olist[min_decider_ind]
    clist.append(olist[min_decider_ind])
    olist.remove(olist[min_decider_ind])

    if (I==2000 and popped!=GS and conv==0) :
      print("\n\nFAILURE MESSAGE !!!\n\nSince we know beforehand from the convergence-calculator function, that the given initial State will not converge, we are exiting the A* Algorithm !!!\n\nThis is done due to hardware constraints as the compilation platform is unable to keep computing until Open_List=[] !!!\n\n")
      print("\n")
      return -1, I, -1, len(clist), olist, clist
      break

    if (popped==[[1,2,3],[4,5,6],[7,8,0]]) :
        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")
        #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

        print(f"\n\nSUCCESS MESSAGE!!!\n\nSTART STATE: {matrix}\n\nGOAL STATE : {GS}\n\nWITH A* ALGORITHM, GOAL STATE IS REACHED IN ITERATION No. :'{I}' AND IT APPEARS AFTER '{steps}' STEPS FROM INITIAL STATE, \n")

        Num_Explored_Nodes= len(clist)
        print(f"\nTotal Number of nodes explored to reach goal state : {Num_Explored_Nodes}\n")

        #print(f"\n{CP_list}\n")

        def index_finder(element,lis) :
          i_element=0
          for x in range(0,len(lis),1) :
            if (CP_list[x][0]==element) :
              i_element=x
              break
          return i_element

        t=index_finder(GS,CP_list)
        while t:
          q1=CP_list[t][1]
          parent.append(q1)
          t=index_finder(q1,CP_list)
        parent.insert(0,GS)

        path=parent[::-1]

        print(f"\nTotal Number of States in the Optimal path : {len(path)}\n")
        print("\nIn A* Algorithm using sum of manhattan distances as a heuristic, the path to goal state looks like this :\n")

        for y in range(0, len(path)-1,1) :
          print(f"\n{path[y]}==>\n")
        print(f"\n{GS}\n")

        heuristics_monotonicity_checker(path,3)


        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")

        return steps, I, path, Num_Explored_Nodes, olist, clist
        break

    neighbours=Move_Generator(popped)
    #print(f"\nFor Iteration {I}, and Popped State : {popped}, set of possible neighbours : {neighbours}\n")

    olist_elements=[]
    clist_elements=[]

    for k in range (0, len(olist), 1) :
      olist_elements.append(olist[k][0])

    for k1 in range (0, len(clist), 1) :
      clist_elements.append(clist[k1][0])

    for neighbour in neighbours:
        if ((neighbour not in olist_elements) and (neighbour not in clist_elements)) :
            olist.append((neighbour, steps+1))
            CP_list.append((neighbour,popped))



##########################################################################################################################

def astar_h4(matrix) :

  conv=convergence_calculator(matrix)

  a=matrix[0][:]
  b=matrix[1][:]
  c=matrix[2][:]
  root=[a,b,c]

  clist=[]
  olist=[(root,0)]
  CP_list=[(root,"START")]
  I=0
  parent=[]


  while olist :

    I=I+1

    #print("\n\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    print(f"\nIteration Number :{I}\n")

    #print("\n*****************************************************************************************************************************************************************************************************************************")
    #print("*****************************************************************************************************************************************************************************************************************************\n")

    #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

    heur=[]
    list_int=([],0)
    list_decider=[]

    for i in range (0, len(olist), 1) :
      pot_elmt, depth_pot_elmt = olist[i]
      score = h4(pot_elmt)
      decider = score + depth_pot_elmt
      list_int = (pot_elmt,decider)
      heur.append(list_int)

    #print(f"\nIn Iteration Number {I}, Members(n) of the Open-List and their corresponding [g(n) + h2(n)] scores : {heur}\n")

    for i1 in range(0, len(heur), 1) :
      pot_decider = heur[i1][1]
      list_decider.append(pot_decider)

    min_decider=min(list_decider)
    #print(f"\nMinimum value of [g(n) + h2(n)] Score : {min_decider}\n")
    min_decider_ind=list_decider.index(min_decider)
    #print(f"\nAND it is appearing at index '{min_decider_ind}' of the Open List\n")

    popped, steps = olist[min_decider_ind]
    clist.append(olist[min_decider_ind])
    olist.remove(olist[min_decider_ind])

    if (I==2000 and popped!=GS and conv==0) :
      print("\n\nFAILURE MESSAGE !!!\n\nSince we know beforehand from the convergence-calculator function, that the given initial State will not converge, we are exiting the A* Algorithm !!!\n\nThis is done due to hardware constraints as the compilation platform is unable to keep computing until Open_List=[] !!!\n\n")
      print("\n")
      return -1, I, -1, len(clist), olist, clist
      break


    if (popped==[[1,2,3],[4,5,6],[7,8,0]]) :
        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")
        #print(f"\n\nFor Iteration No. {I}:\n\nMembers of Open-List are : \n{olist}\n\nMembers of Closed-List are : \n{clist}\n\n")

        print(f"\n\nSUCCESS MESSAGE!!!\n\nSTART STATE: {matrix}\n\nGOAL STATE : {GS}\n\nWITH A* ALGORITHM, GOAL STATE IS REACHED IN ITERATION No. :'{I}' AND IT APPEARS AFTER '{steps}' STEPS FROM INITIAL STATE, \n")

        Num_Explored_Nodes= len(clist)
        print(f"\nTotal Number of nodes explored to reach goal state : {Num_Explored_Nodes}\n")

        #print(f"\n{CP_list}\n")

        def index_finder(element,lis) :
          i_element=0
          for x in range(len(lis)-1,0,-1) :
            if (CP_list[x][0]==element) :
              i_element=x
              break
          return i_element

        t=index_finder(GS,CP_list)
        while t:
          q1=CP_list[t][1]
          parent.append(q1)
          t=index_finder(q1,CP_list)
        parent.insert(0,GS)

        path=parent[::-1]

        print(f"\nTotal Number of States in the Optimal path : {len(path)}\n")
        print("\nIn A* Algorithm using relative position squared weightage, as a heuristic, the path to goal state looks like this :\n")

        for y in range(0, len(path)-1,1) :
          print(f"\n{path[y]}==>\n")
        print(f"\n{GS}\n")

        heuristics_monotonicity_checker(path,4)


        #print("\n*****************************************************************************************************************************************************************************************************************************")
        #print("*****************************************************************************************************************************************************************************************************************************\n")

        return steps, I, path, Num_Explored_Nodes, olist, clist
        break

    neighbours=Move_Generator(popped)
    #print(f"\nFor Iteration {I}, and Popped State : {popped}, set of possible neighbours : {neighbours}\n")

    olist_elements=[]
    clist_elements=[]

    for k in range (0, len(olist), 1) :
      olist_elements.append(olist[k][0])

    for k1 in range (0, len(clist), 1) :
      clist_elements.append(clist[k1][0])

    for neighbour in neighbours:
        if ((neighbour not in olist_elements) and (neighbour not in clist_elements)) :
            olist.append((neighbour, steps+1))
            CP_list.append((neighbour,popped))



##########################################################################################################################

def explored_states_inclusivity_checker (LIST_1,LIST_2): #LIST_1 is closed list of superior heuristic, LIST_2 is closed list of inferior heuristic
  clist_elements_1 = []
  clist_elements_2 = []

  for k1 in range(0, len(LIST_1), 1):
    clist_elements_1.append(LIST_1[k1][0])
  for k2 in range(0, len(LIST_2), 1):
    clist_elements_2.append(LIST_2[k2][0])

  inclusivity_counter=0

  for element in clist_elements_1 :
    if element in clist_elements_2:
      inclusivity_counter=inclusivity_counter+1
    #else :
      #print(element)
      #indx=clist_elements_1.index(element)
      #print(indx)

  #print (len(clist_elements_1))

  #print (len(clist_elements_2))

  #print (inclusivity_counter)

  if inclusivity_counter==len(LIST_1) :
    print("\n\nAll states explored by Superior Heuristics are also expanded by Inferior heuristics\n\n")
  else :
    print ("\n\nInclusivity Check Failed!!!")

##########################################################################################################################

tracemalloc.start()
BEGINNING=time.time()

##########################################################################################################################

IS2=[[1,2,3],[4,5,6],[0,7,8]]
#h2(n): Converging, Iterations : 3, Steps : 2, Time : 0.0017s, Peak RAM : 24.68kB

IS3=[[1,2,3],[4,0,5],[7,8,6]]
#h2(n): Converging, Iterations : 3, Steps : 2, Time : 0.0019s, Peak RAM : 25.40kB

IS5=[[1,2,0],[4,5,3],[7,8,6]]
#h2(n): Converging, Iterations : 3, Steps : 2, Time : 0.0015s, Peak RAM : 25.20kB

##########################################################################################################################

IS1 = [[0,1,2],[4,5,3],[7,8,6]]
#h1(n): Converging, Iterations : 30, Steps : 4, Time : 0.033s, Peak RAM : 54.34kB
#h2(n): Converging, Iterations : 5, Steps : 4, Time : 0.026s, Peak RAM : 38.36kB
#h3(n): Converging, Iterations : 5, Steps : 4, Time : 0.012s, Peak RAM : 30.55kB
#h4(n): Converging, Iterations :5, Steps :4, Time : 0.018s, Peak RAM : 33.95kB

##########################################################################################################################

IS4=[[4,1,2],[7,5,3],[8,0,6]]
#h1(n): Converging, Iterations : 140, Steps : 7, Time : 0.08s, Peak RAM : 2654.9kB
#h2(n): Converging, Iterations : 8, Steps : 7, Time : 0.06s, Peak RAM : 40.98kB
#h3(n): Converging, Iterations : 8, Steps : 7, Time : 0.02s, Peak RAM : 34.34kB
#h4(n): Converging, Iterations : 9, Steps :7, Time : 0.036s, Peak RAM : 37.07kB

##########################################################################################################################

IS6=[[5,0,8],[4,2,1],[7,3,6]]
#h1(n): Converging, Iterations : 64353, Steps : 21, Time : 11609.743s, Peak RAM : 42834.66kB
#h2(n): Converging, Iterations : 5782, Steps : 21, Time : 145.91s, Peak RAM : 4304.39kB
#h3(n): Converging, Iterations : 2094, Steps : 21, Time : 172.41s, Peak RAM : 1598.38kB
#h4(n): Converging, Iterations : 1075, Steps : 27, Time : 13.98, Peak RAM : 814.02kB

##########################################################################################################################

IS7=[[0,1,2],[3,4,5],[6,7,8]]
#h2(n): Converging, Iterations : 8300, Steps : 22, Time : 369.89s, Peak RAM : 6231.75kB
#h3(n): Converging, Iterations : 1306, Steps : 22, Time : 70.06s, Peak RAM : 2965.59kB
#h4(n): Converging, Iterations : 2275, Steps : 22, Time : 63.53s, Peak RAM : 1722.46kB

##########################################################################################################################

ISN=[[1,2,3],[4,5,6],[8,7,0]]
#h1(n): Non-Converging
#h2(n): Non-Converging
#h3(n): Non-Converging
#h4(n): Non-Converging


##########################################################################################################################

ISQ=[[3,2,1],[4,5,6],[8,7,0]]
#h1(n): Converging, Iterations : 130544, Steps : 24, Time : 19988.6s, Peak RAM : 185036.82kB
#h2(n): Converging, Iterations : 18700, Steps : 24, Time : 1115.48s, Peak RAM : 11679.06kB
#h3(n): Converging, Iterations : 3299, Steps : 24, Time : 415.66s, Peak RAM : 2617.29kB
#h4(n): Converging, Iterations : 1824, Steps : 38, Time : 38.79s, Peak RAM : 1387.54kB

[STEPS_1, ITERATIONS_1, RECONSTRUCTED_PATH_1, No_of_EXPLORED_NODES_1, OPEN_LIST_1, CLOSED_LIST_1] = astar_h1(ISQ)
[STEPS_2, ITERATIONS_2, RECONSTRUCTED_PATH_2, No_of_EXPLORED_NODES_2, OPEN_LIST_2, CLOSED_LIST_2] = astar_h2(ISQ)
[STEPS_3, ITERATIONS_3, RECONSTRUCTED_PATH_3, No_of_EXPLORED_NODES_3, OPEN_LIST_3, CLOSED_LIST_3] = astar_h3(ISQ)
[STEPS_4, ITERATIONS_4, RECONSTRUCTED_PATH_4, No_of_EXPLORED_NODES_4, OPEN_LIST_4, CLOSED_LIST_4] = astar_h4(ISQ)


##########################################################################################################################

#Demo for verifying that all the states expanded by better heuristics are also developed by inferior heuristics.

[STEPS_2, ITERATIONS_2, RECONSTRUCTED_PATH_2, No_of_EXPLORED_NODES_2, OPEN_LIST_2, CLOSED_LIST_2] = astar_h2(IS7)
[STEPS_3, ITERATIONS_3, RECONSTRUCTED_PATH_3, No_of_EXPLORED_NODES_3, OPEN_LIST_3, CLOSED_LIST_3] = astar_h3(IS7)

explored_states_inclusivity_checker(CLOSED_LIST_3, CLOSED_LIST_2)

#*************************************************************************************************************************
#*************************************************************************************************************************

CONCLUSION=time.time()

TOTAL_TIME=CONCLUSION-BEGINNING

print(f"\nTotal Time taken in this execution is :{TOTAL_TIME} seconds")

CURRENT_MEM, PEAK_MEM = tracemalloc.get_traced_memory()

print(f"\nRAM CONSUMPTION DETAILS :\nCurrent Memory Consumption is : {CURRENT_MEM/1024} kB and the Peak Memory Consumption is : {PEAK_MEM/1024} kB")

tracemalloc.stop()