# -*- coding: utf-8 -*-
"""
Created on 9 Mar 2023
Name: DataCleaner_for_ML_LogisticRegressionExemplar.py
Purpose: Data Cleaning Program for Logistic Regression Model Machine Learning Algorithm
@author: Charles Umesi (charlesumesi)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from colorama import Fore

# Note: This code requires a virtual environment to function properly

# Introduction
print(Fore.YELLOW + "Welcome!\nThis program will enable your computer clean your data and make it suitable for the 'Logistic Regression Model' machine learning algorithm\n ")
print(Fore.WHITE + "Note that during the cleaning process, you may need to 'discard' some variables. This program will not tell which ones to discard")
print('That decision will be up to you\n ')
print('Also note that the output from this data cleaning process will be numerical values')
check = input('Do you require text values in the output of the data cleaning process? Y/N: ')
if check == 'Y':
  print('That means your data is unsuitable for this cleaner\n') 
  quit('Y')
elif check == 'N' or 'n' and check != 'y':
  # Prompt
  print(' \nMake sure your data document is in the form of a csv file and in the same directory as this program\n ')

  # Read file
  file = input('Enter the name of your file (with csv extension): ')
  data = pd.read_csv(file)

  # Initial processing
  print(' \nInitial processing... \n')
  print(data.isnull().head(8))
  sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
  plt.savefig('InitialHeatmap_for_LogR.png')

  print(" \nAll the values in your data have temporarily been converted into 'True' and 'False' values. The first 8 rows have been printed.")
  print("'True' means that NO VALUE IS AVAILABLE for the variable at that position in your data; 'False' means that a value is available for the variable at that position in your data.")
  print('Note that this initial process is not concerned with whether your original values were numerical or not.\n ')
  print(Fore.MAGENTA + 'You should also note two other things:')
  print(Fore.WHITE + 'First: The absence of True or False in the 8 rows displayed does not exclude their existence further down your data.')
  print('Second: It can be difficult to judge (accurately) the extent of True and False values in your reformatted data just by looking at the raw data.\n ')
  print('Therefore:')
  print("A heatmap (InitialHeatmap_for_LogR.png) has been generated. It is in the current directory.")
  print("Look at it now and check for 'yellow' blocks.")
  print('Yellow blocks indicate True and purple areas indicate False.\n ')
  print('Make a note of which variables/columns have yellow blocks.')
  print('Among those that have yellow blocks, decide:')
  print("1) Which variables/columns have such vast areas of yellow that the only 'realistic' option for this data cleaner is to discard the variable/column entirely.")
  print("2) Which variables/columns have small enough areas of yellow that you could fill them by 'imputation'.")
  print('(Age can be done that way but the yellow areas need to be small enough.)')
  print("3) Which variables/columns have only few yellow bars such that you could drop the relevant rows and not the entire column.\n ")
  print('Among those columns that do not have yellow blocks, identify:')
  print('Which variables/columns have numerical values and which ones have text values.\n ')
  print('Among the columns with text values, decide which ones could be converted into 0s and 1s.')
  print('(Gender can be done that way, including M/F/T, and so on).\n ')
  print('Among the columns with numerical values:') 
  print('Identify those with continuous values and those with descrete values.\n ')
  print('Among columns with descrete values, decide which ones you wish to convert into 0s and 1s and which ones you wish to use as they are.')
  print('(That, could affect performance.)\n ')

  decision = input('With all the information given, have you come to a decision about what next you want done with your data? (Y/N): ')
  if decision == 'N':
    print(' \nOkay, the program will terminate (so as to give you more time to think about the information given')
    quit('N')
  elif decision == 'Y' or 'y' and decision != 'n':
    print(' \nStarting with imputation, in this data cleaner, two imputation methods are available:')
    print('Your DEFAULT value and the MEDIAN value for the column.\n ')
    # Defaults
    imput_d_numbers = int(input('How many columns do you wish to treat with default values?: '))
    if imput_d_numbers > 0:
      imput_d = 'Enter the name of one column/variable exactly as it appears in your csv file and its default value in the form C,D where C is the column name and V is its default value: '
      imput_d_list = [list(input(imput_d)) for _ in [0]*imput_d_numbers]
    else:
      pass

    # Medians
    imput_m_numbers = int(input('How many columns do you wish to treat with median values?: '))
    if imput_m_numbers > 0:
      imput_m = 'Enter the name of one column/variable (to be treated that way) exactly as it appears in your csv file: '
      imput_m_list = [list(input(imput_m)) for _ in [0]*imput_m_numbers]
    else:
      pass

    # Binaries
    imput_b_numbers = int(input('How many columns do you wish to treat with 0s and 1s?: '))
    if imput_b_numbers > 0:
      imput_b = 'Enter the name of one column/variable (to be treated that way) exactly as it appears in your csv file: '
      imput_b_list = [list(input(imput_b)) for _ in [0]*imput_b_numbers]
    else:
      pass

    # Column-drops
    cd_numbers = int(input('How many columns do you wish to drop?: '))
    if cd_numbers > 0:
      cd = 'Enter the name of one column/variable (to be treated that way) exactly as it appears in your csv file: '
      cd_list = [list(input(cd)) for _ in [0]*cd_numbers]
    else:
      pass

    # Tidy the input lists by converting to string and reconverting back to a list
    # Defaults
    imput_d_tidylist = []
    if imput_d_numbers > 0:
      for i in imput_d_list:
        j = ''.join(i)
        imput_d_tidylist.append(j)
    else:
      pass
    # Medians
    imput_m_tidylist = []
    if imput_m_numbers > 0:
      for k in imput_m_list:
        l = ''.join(k)
        imput_m_tidylist.append(l)
    else:
      pass
    # Binaries
    imput_b_tidylist = []
    if imput_b_numbers > 0:
      for q in imput_b_list:
        r = ''.join(q)
        imput_b_tidylist.append(r)
    else:
      pass
    # Column-drops
    cd_tidylist = []
    if cd_numbers > 0:
      for s in cd_list:
        t = ''.join(s)
        cd_tidylist.append(t)
    else:
      pass

    # Chosen columns for replacing absent values with default values
    if imput_d_numbers > 0:
      for d in imput_d_tidylist:
        d_column = d.split(',')[0]
        string_d_value = d.split(',')[1]
        d_value = eval(string_d_value)
        data[d_column].fillna(value=d_value,inplace=True)
    else:
      pass

    # Chosen columns for replacing absent values with median values
    if imput_m_numbers > 0:
      for m in imput_m_tidylist:
        data[m].fillna(value=data[m].median(),inplace=True)
    else:
      pass

    # Chosen columns for replacing values with 0s and 1s
    if imput_b_numbers > 0:
      for b in imput_b_tidylist:
        b_bin = pd.get_dummies(data[b],drop_first=True)
        data = pd.concat([data,b_bin],axis=1)
    else:
      pass

    # Chosen columns for dropping
    if cd_numbers > 0:
      for cd in cd_tidylist:
        data.drop(cd,axis=1,inplace=True)
    else:
      pass

    # Any absent values left by this stage should be no more than a handful of rows (if the user has chosen appropriately)
    data.dropna(inplace=True)

    # Final check before dropping columns with text values
    sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.savefig('FinalHeatmap_for_LogR.png')

    print(" \nA second heatmap (FinalHeatmap_for_LogR.png) has now been generated. It is in the current directory.")
    print("Look at it now. There should be NO AREAS OR BLOCKS OF YELLOW.\n ")
    print('If you are still seeing areas of yellow then it means you missed out columns with absent values in your initial inputs.\n ')
    confirm = input('Can you see any areas or blocks of yellow in the second heatmap? (Y/N): ')
    if confirm == 'Y':
      print('Then it means you need to start again.')
      quit('Y')
    elif confirm == 'N' or 'n' and confirm != 'y':
      print(' \nAll columns with text values must now be dropped for the logistic regression model.\n ')
      drop_numbers = int(input('How many columns in your data have text values?: '))
      if drop_numbers > 0:
        drop = 'Enter the name of one column/variable (to be dropped) exactly as it appears in your csv file: '
        drop_list = [list(input(drop)) for _ in [0]*drop_numbers]

        # Tidy the drop list by converting to string and reconverting back to a list before dropping columns in the list
        drop_tidylist = []
        for i in drop_list:
          j = ''.join(i)
          drop_tidylist.append(j)

        # Drop the column(s) in the list
        data.drop(drop_tidylist,axis=1,inplace=True)
      else:
        pass
      data.to_csv('processed_' + file)
      print(Fore.GREEN + ' \nDone.')
      print(Fore.WHITE + "Your processed data has been saved as 'processed_' followed by the filename of your original data.")
