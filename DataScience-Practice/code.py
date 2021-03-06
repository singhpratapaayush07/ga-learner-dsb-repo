# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
data=np.genfromtxt(path,delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record),axis=0)




# --------------
#Code starts here
age=census[:,0]

max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)

age_std=np.std(age)
#print(age,max_age,min_age,age_mean,age_std, sep='\n')


# --------------
#Code starts here
race=census[:,2]

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority=min(len_0,len_1,len_2,len_3,len_4)

minority_race=10

if(len_0==minority):
    minority_race=0
elif(len_1==minority):
    minority_race=1
elif(len_2==minority):
    minority_race=2
elif(len_3==minority):
    minority_race=3
elif(len_4==minority):
    minority_race=4

#print(minority_race,len_0,len_1,len_2,len_3,len_4,sep='\n')





# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=(np.mean(high,axis=0)[7])
avg_pay_low=(low.sum(axis=0)[7])/len(low)




