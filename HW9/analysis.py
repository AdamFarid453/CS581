"""
    Python program to analyze Pew Survey Data and output the results.

    Author: Adam Farid
"""
# imports and external python packages used listed here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
# To run the program make sure you are running the command python3 farid.py

def age_group_analysis():
    # open the file
    file = open("Pew_Survey.csv", "r")
    # read the file
    data = pd.read_csv(file)
    facebookDF = data[['age','web1c']]
    snapChatDF = data[['age','web1d']]

    
    #*******************************************************************************************
    # FACEBOOK ANALYSIS
    # ---- Number of people who use Facebook ---- #
    # ---- Number of people under 25 ---- #
    # find the number of people under 25 who answered yes to the question and store it in a variable
    facebook_under_twentyfive_yes = np.sum([facebookDF[facebookDF['age']<=25]['web1c']==1])
    # find the number of people under 25 who answered no to the question and store it in a variable
    facebook_under_twentyfive_no = np.sum([facebookDF[facebookDF['age']<=25]['web1c']==2])

    
    # ---- Number of people who are between 26 and 35 ---- #
    #find the number of people between 26 and 35 who answered yes to the question and store it in a variable
    facebook_between_twentyfive_thirtyfive_yes = np.sum([facebookDF[(facebookDF['age']>25) & (facebookDF['age']<=35)]['web1c']==1])
    #find the number of people between 26 and 35 who answered no to the question and store it in a variable
    facebook_between_twentyfive_thirtyfive_no = np.sum([facebookDF[(facebookDF['age']>25) & (facebookDF['age']<=35)]['web1c']==2])


    # ---- Number of people who are between 36 and 45 ---- #
    facebook_thirtysix_fortyfive_yes = np.sum([facebookDF[(facebookDF['age']>35) & (facebookDF['age']<=45)]['web1c']==1])
    facebook_thirtysix_fortyfive_no = np.sum([facebookDF[(facebookDF['age']>35) & (facebookDF['age']<=45)]['web1c']==2])
 
    # ---- Number of people who are between 46 and 55 ---- #
    facebook_fortysix_fiftyfive_yes = np.sum([facebookDF[(facebookDF['age']>45) & (facebookDF['age']<=55)]['web1c']==1])
    facebook_fortysix_fiftyfive_no = np.sum([facebookDF[(facebookDF['age']>45) & (facebookDF['age']<=55)]['web1c']==2])


    # ---- Number of people who are over 55 ---- #
    facebook_fiftysix_over_yes = np.sum([facebookDF[facebookDF['age']>55]['web1c']==1])
    facebook_fiftysix_over_no = np.sum([facebookDF[facebookDF['age']>55]['web1c']==2])


    #---- Total number of people ----#
    total_people = facebook_under_twentyfive_no + facebook_under_twentyfive_yes + facebook_between_twentyfive_thirtyfive_yes + facebook_between_twentyfive_thirtyfive_no + facebook_thirtysix_fortyfive_yes + facebook_thirtysix_fortyfive_no + facebook_fortysix_fiftyfive_yes + facebook_fortysix_fiftyfive_no + facebook_fiftysix_over_yes + facebook_fiftysix_over_no


    # ---- Percentages of people who use Facebook ---- #
    # find the percentage of people who use Facebook and store it in a variable
    percentage_facebook = (facebook_under_twentyfive_yes + facebook_between_twentyfive_thirtyfive_yes + facebook_thirtysix_fortyfive_yes + facebook_fortysix_fiftyfive_yes + facebook_fiftysix_over_yes)/total_people



    #*******************************************************************************************
    # SNAPCHAT ANALYSIS
    # ---- Number of people who use Snapchat ---- #
    # ---- Number of people under 25 ---- #
    # find the number of people under 25 who answered yes to the question and store it in a variable
    snap_under_twentyfive_yes = np.sum([snapChatDF[snapChatDF['age']<=25]['web1d']==1])
    # find the number of people under 25 who answered no to the question and store it in a variable
    under_twentyfive_no = np.sum([snapChatDF[snapChatDF['age']<=25]['web1d']==2])

    # ---- Number of people who are between 26 and 35 ---- #
    #find the number of people between 26 and 35 who answered yes to the question and store it in a variable
    between_twentyfive_thirtyfive_yes = np.sum([snapChatDF[(snapChatDF['age']>25) & (snapChatDF['age']<=35)]['web1d']==1])
    #find the number of people between 26 and 35 who answered no to the question and store it in a variable
    between_twentyfive_thirtyfive_no = np.sum([snapChatDF[(snapChatDF['age']>25) & (snapChatDF['age']<=35)]['web1d']==2])


    # ---- Number of people who are between 36 and 45 ---- #
    thirtysix_fortyfive_yes = np.sum([snapChatDF[(snapChatDF['age']>35) & (snapChatDF['age']<=45)]['web1d']==1])
    thirtysix_fortyfive_no = np.sum([snapChatDF[(snapChatDF['age']>35) & (snapChatDF['age']<=45)]['web1d']==2])
  

    # ---- Number of people who are between 46 and 55 ---- #
    fortysix_fiftyfive_yes = np.sum([snapChatDF[(snapChatDF['age']>45) & (snapChatDF['age']<=55)]['web1d']==1])
    fortysix_fiftyfive_no = np.sum([snapChatDF[(snapChatDF['age']>45) & (snapChatDF['age']<=55)]['web1d']==2])


    # ---- Number of people who are over 55 ---- #
    fiftysix_over_yes = np.sum([snapChatDF[snapChatDF['age']>55]['web1d']==1])
    fiftysix_over_no = np.sum([snapChatDF[snapChatDF['age']>55]['web1d']==2])

    #---- Total number of people ----#
    total_people = under_twentyfive_no + snap_under_twentyfive_yes + between_twentyfive_thirtyfive_yes + between_twentyfive_thirtyfive_no + thirtysix_fortyfive_yes + thirtysix_fortyfive_no + fortysix_fiftyfive_yes + fortysix_fiftyfive_no + fiftysix_over_yes + fiftysix_over_no

    # ---- Percentages of people who use Snapchat ---- #
    # find the percentage of people who use Snapchat and store it in a variable rounded to 2 decimal places
    percentage_snapchat = (snap_under_twentyfive_yes + between_twentyfive_thirtyfive_yes + thirtysix_fortyfive_yes + fortysix_fiftyfive_yes + fiftysix_over_yes)/total_people   
    

    print("AGE GROUP ANALYSIS: 18-25")
    print("                 Facebook:     Snapchat:")
    print("Yes:               ", str(facebook_under_twentyfive_yes)+ "           "+str(snap_under_twentyfive_yes)) 
    print("No:                ", str(facebook_under_twentyfive_no)+ "            "+str(under_twentyfive_no))
    print("\n")
    print("AGE GROUP ANALYSIS: 26-35")
    print("                 Facebook:     Snapchat:")
    print("Yes:               ", str(facebook_between_twentyfive_thirtyfive_yes)+ "           "+str(between_twentyfive_thirtyfive_yes))
    print("No:                ", str(facebook_between_twentyfive_thirtyfive_no)+ "            "+str(between_twentyfive_thirtyfive_no))
    print("\n")
    print("AGE GROUP ANALYSIS: 36-45")
    print("                 Facebook:     Snapchat:")
    print("Yes:               ", str(facebook_thirtysix_fortyfive_yes)+ "           "+str(thirtysix_fortyfive_yes))
    print("No:                ", str(facebook_thirtysix_fortyfive_no)+ "            "+str(thirtysix_fortyfive_no))
    print("\n")
    print("AGE GROUP ANALYSIS: 46-55")
    print("                 Facebook:     Snapchat:")
    print("Yes:               ", str(facebook_fortysix_fiftyfive_yes)+ "           "+str(fortysix_fiftyfive_yes))
    print("No:                ", str(facebook_fortysix_fiftyfive_no)+ "            "+str(fortysix_fiftyfive_no))
    print("\n")
    print("AGE GROUP ANALYSIS: 56+")
    print("                 Facebook:     Snapchat:")
    print("Yes:               ", str(facebook_fiftysix_over_yes)+ "           "+str(fiftysix_over_yes))
    print("No:                ", str(facebook_fiftysix_over_no)+ "            "+str(fiftysix_over_no))
    print("\n")
    print("TOTAL NUMBER OF PEOPLE:", total_people+3)

    print("Percentage of all people who use Facebook:", round(percentage_facebook,2))
    print("Percentage of all people who don't use Facebook:", 1- round(percentage_facebook,2))
    print("\n")

    print("Percentage of all people who use Snapchat:", round(percentage_snapchat,2))
    print("Percentage of all people who don't use Snapchat:", 1- round(percentage_snapchat,2))

    
    return percentage_facebook, percentage_snapchat, facebook_under_twentyfive_yes, facebook_under_twentyfive_no, snap_under_twentyfive_yes, under_twentyfive_no, facebook_fiftysix_over_yes, fiftysix_over_yes, facebook_fiftysix_over_no, fiftysix_over_no

def plot(fb,snap):
    #plot the data for both Facebook and Snapchat
    plt.figure(figsize=(10,5))
    # use a nice font
    plt.rc('font', family='Futura', size=12)
    plt.bar(['Facebook','Snapchat'],[fb,snap],color=['deepskyblue','yellow'], edgecolor='black')
    plt.ylim(0, 100)
    plt.xlabel('Social Media')
    plt.ylabel('Facebook vs. Snapchat Percentages') 
    plt.title('What Social Media Platform do Users Use?')
    # saving the absolute path of the file
    my_path = os.path.abspath(os.path.dirname(__file__))
    plt.savefig(os.path.join(my_path, 'facebook_snapchat.png'))
    
def plot_young_adults(yes_facebook, yes_snapchat, no_facebook, no_snapchat):
    # bar plot for young adults
    plt.figure(figsize=(12,5))
    # use a nice font
    plt.rc('font', family='Futura', size=10)
    plt.bar(['Uses Facebook','Does not use Facebook','Uses Snapchat', 'Does not use Snapchat'],[yes_facebook,no_facebook, yes_snapchat, no_snapchat],color=['lightblue','red','yellow','red'], edgecolor='black')
    plt.xlabel('Social Media Uses among Young Adults')
    plt.ylabel('Number of young adult survey participants')
    plt.title('18-25 Year olds that use Facebook and Snapchat')
    # saving the absolute path of the file
    my_path = os.path.abspath(os.path.dirname(__file__))
    plt.savefig(os.path.join(my_path, 'young_adults.png'))

def plot_old_adults(yes_facebook, yes_snapchat, no_facebook, no_snapchat):
    # bar plot for young adults
    plt.figure(figsize=(12,5))
    # use a nice font
    plt.rc('font', family='Futura', size=10)
    plt.bar(['Uses Facebook','Does not use Facebook','Uses Snapchat', 'Does not use Snapchat'],[yes_facebook,no_facebook, yes_snapchat, no_snapchat],color=['lightblue','red','yellow','red'], edgecolor='black')
    plt.xlabel('Social Media Users among older demographics')
    plt.ylabel('Number of 55Yrs+ adult survey participants')
    plt.title('55+ Year olds that use Facebook and Snapchat')
    # saving the absolute path of the file
    my_path = os.path.abspath(os.path.dirname(__file__))
    plt.savefig(os.path.join(my_path, 'final_output.png'))
# Python main method
if __name__ == '__main__':
    print("\n")
    print("Instagram and Facebook Usages among Age Groups")
    print("-----------------------------------------------")
    percentage_facebook, percentage_snapchat, facebook_under_twentyfive_yes, facebook_under_twentyfive_no, snap_under_twentyfive_yes, under_twentyfive_no, facebook_fiftysix_over_yes, fiftysix_over_yes, facebook_fiftysix_over_no, fiftysix_over_no = age_group_analysis()
    plot(percentage_facebook*100, percentage_snapchat*100)
    plot_young_adults(facebook_under_twentyfive_yes, snap_under_twentyfive_yes, facebook_under_twentyfive_no,under_twentyfive_no)
    plot_old_adults(facebook_fiftysix_over_yes, fiftysix_over_yes, facebook_fiftysix_over_no, fiftysix_over_no)
