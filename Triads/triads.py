"""
    Python program to process provided input file and identify triads.
    Author: Adam Farid
"""

# To run the program make sure you are running the command python3 triads.py
# You will then be prompted to enter a file name (csv) for any epinion data to be processed
# Make sure the epinions csv is located in the same directory


# Public import for networkx and runtime
import networkx as nx
import timeit

# We call this start script in order to structure our print statements properly
def start_script(file_name):
    print("*** START ***\n")
    print(f"RESULTS FOR FILE: {file_name}")
    return ""

# This file is responsible to creating the networkx graph and adding all of the triad
# edges. We also count the edges here and the trust and distrust 
def openFile(file_name):
    # Creating the networkx graph
    G = nx.Graph()

    # Variable instantiation
    edges=0
    not_used=0
    trust=0
    distrust=0

    with open(file_name) as f:
        for line in f:
            #split each line into an array by commas : ex -> [30, 25, -1]
            lines = (list(map(int,line.strip().split(","))))
            #checking if reviewee and reviewer node is a self-loop
            if(lines[0] == lines[1]):
                not_used+=1
            # if the weight is negative we increment the distrust counter
            if(lines[2]==-1) and lines[0]!= lines[1]:
                distrust+=1
            # if the weight is positive we increment the trust counter
            if(lines[2]==1) and lines[0]!= lines[1]:
                trust+=1
            edges+=1
            G.add_edge(lines[0], lines[1], weight=lines[2])
    return edges,not_used,trust,distrust,G



def main():
    # Starting the timer
    start = timeit.default_timer()
    #Prompting user for input
    userInput = input("Please enter a file name (.csv): ")
    print(start_script(userInput))
    edges,not_used,trust,distrust,G = openFile(userInput)

    # Initializing variables to be used later
    triads = []
    num_TTT = 0
    num_TTD = 0
    num_TDD = 0
    num_DDD = 0

    # Finds all the triads in the graph and append it to the traids list
    for nodes in nx.enumerate_all_cliques(G):
        if len(nodes) == 3:
            triads.append(nodes)
    # looping through the triads
    for first,second,third in triads:
        # we now add up the weights for each triad
        weights = G[first][second]['weight'] + G[first][third]['weight'] + G[second][third]['weight']
        # incrementing the network relationships based on the total weight 
        if (weights == 1):
            num_TTD += 1
        if (weights == -1):
            num_TDD += 1
        if (weights == 3):
            num_TTT+=1
        if (weights == -3):
            num_DDD+= 1

    probability_of_positive = trust / edges
    probability_of_negative = 1 - probability_of_positive
    ttt = probability_of_positive* probability_of_positive*probability_of_positive * 100
    ttd = 3 * probability_of_positive *probability_of_positive * probability_of_negative * 100
    tdd = 3 * probability_of_positive *probability_of_negative* probability_of_negative * 100
    ddd = probability_of_negative*probability_of_negative *probability_of_negative * 100

    #number of expected distributions for the triads
    tttNum = ttt * len(triads) * 0.01
    ttdNum = ttd * len(triads) * 0.01
    tddNum = tdd * len(triads) * 0.01
    dddNum = ddd * len(triads) * 0.01
    #calculation for the actual number of the triad types
    tttAct = num_TTT / len(triads) * 100
    ttdAct = num_TTD / len(triads) * 100
    tddAct = num_TDD / len(triads) * 100
    dddAct = num_DDD / len(triads) * 100
    print(f"traingles {len(triads)}")
    print(f"TTT: {num_TTT}                Edges used:    {str(edges).rjust(4)}")
    print(f"TTD: {num_TTD}                trust edges:    {str(trust).rjust(4)}       probability %:   {format(probability_of_positive, '.2f')}")
    print(f"TDD: {num_TDD}                distrust edges: {str(distrust).rjust(4)}      probability %: {format(probability_of_negative, '.2f').rjust(8)}")
    print(f"DDD: {num_DDD}                total:          {str(edges-not_used).rjust(4)}                    {str(100.00).rjust(9)}\n")
    print("Expected Distribution*                Actual Distribution")
    print("      percent   number                     percent     number")
    #Using str operator right adjust function in order for easier readibility for the user
    print(f"TTT:    {format(ttt, '.2f').rjust(4)}     {format(tttNum, '.2f').rjust(4)}                    {format(tttAct, '.2f').rjust(4)}     {str(num_TTT).rjust(4)}")
    print(f"TTD:    {format(ttd, '.2f').rjust(4)}     {format(ttdNum, '.2f').rjust(4)}                    {format(ttdAct, '.2f').rjust(4)}     {str(num_TTD).rjust(4)}")
    print(f"TDD:    {format(tdd, '.2f').rjust(4)}     {format(tddNum, '.2f').rjust(4)}                    {format(tddAct, '.2f').rjust(4)}     {str(num_TDD).rjust(4)}")
    print(f"DDD:    {format(ddd, '.2f').rjust(4)}     {format(dddNum, '.2f').rjust(4)}                    {format(dddAct, '.2f').rjust(4)}     {str(num_DDD).rjust(4)}")
    print(f"Total:  {format(ttt+ttd+tdd+ddd, '.2f')}  {format(tttNum+ttdNum+tddNum+dddNum, '.2f')}        {format(tttAct+ttdAct+tddAct+dddAct, '.2f').rjust(18)}  {str(num_TTT+num_TTD+num_TDD+num_DDD).rjust(7)}\n")  
    print("*** END ***\n")
    #stopping the timer
    stop = timeit.default_timer()

    print('Program runtime: ', format(stop - start, '.2f'),"seconds")

# Python main method
if __name__ == '__main__':
    main()