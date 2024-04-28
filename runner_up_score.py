number_of_participant=int(input("Enter number of participant: "))
scores=list(map(int,input("Enter scores separted by spaces: ").split()))
# list is written here because map object has no attribute sort
# map functipn used to change it into list
# split method is used to break or split the numbers in list
scores.sort() # sort function will help to make list from smallest to largest order
maximum = scores.index(max(scores))
runner_up_score = scores[maximum - 1]# after finding maximum index value of a number we will subtract -1 from index value so that we can get index value for runner up score 
print(f"Runner up score of the game is {runner_up_score}")