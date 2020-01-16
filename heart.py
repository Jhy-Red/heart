#!/bin/ python3.8


#Projet numéro 2
#Read Definition for more medical description.
#Read Readme for more sources.

# DataFrame : CSV - UTF 8
import pandas as pd

# Windows : 
#data = pd.read_csv("DATA/heart.csv", encoding ="utf8")
# Ubuntu :
data = pd.read_csv('/media/jhy/JHY/Etudes/Projets/Work in progress/Projets 2/DATA/heart.csv', encoding = "utf8")

#Import graph
import matplotlib.pyplot as plt

# Disable chain limit
pd.options.mode.chained_assignment = None

# Shortcut for DataFrame
age,sex = data['age'],data['sex']
chest_pain, blood_pressure = data['cp'], data['trestbps']
cholesterol ,fast_sugars = data['chol'],data['fbs']
rest_cardiogram,maximun_heartrate = data['restecg'],data['thalach']
pain_exercice, depression_rest = data['exang'],data['oldpeak']
slope, big_vessel = data['slope'],data['ca']
diag, heart_faillure = data['thal'],data['target']

#correction : target was swap 0 mean heart attack, 1 mean no trouble
heart_faillure[heart_faillure == 0] = "Accident"
heart_faillure[heart_faillure == 1] = "Nothing"

#ajustement
sex[sex == 1] = "Male"
sex[sex == 0] = "Female"

#Age to target
def hp_faillure():
    cpt = 0
    cpt_tot = 0
    for x in heart_faillure:
        if x is True : 
            cpt +=1
        else : 
            cpt_tot +=1
    total = cpt + cpt_tot
    percent = round((cpt / total)*100,2)
    return percent

age_target = round(age.mean()),hp_faillure()

#print(parite_HF)

############################################################################################################################
######################################          DATA TRENDS          #######################################################
############################################################################################################################

# Parity

men = 0
women = 0
for x in sex :
    if x == "Male" :
        men += 1 
    elif x == "Female" :
        women += 1
    else : 
        print('check database')
        pass

men_target = sex[sex == 'Male'][heart_faillure =="Accident"].count()
women_target = sex[sex == 'Female'][heart_faillure =="Accident"].count()

parite_HF = round(women / (women+men)*100,2)
age_man_target = age[sex=="Male"][heart_faillure=="Accident"]
age_man_untarget = age[sex=="Male"][heart_faillure=="Nothing"]
age_woman_target = age[sex=="Female"][heart_faillure=="Accident"]
age_woman_untarget = age[sex=="Female"][heart_faillure=="Nothing"]
# Cholesterols

avg_cholesterol = round(cholesterol.mean(),2)
#Target
cholesterol_male_target = cholesterol[sex=="Male"][heart_faillure=="Accident"]
cholesterol_female_target = cholesterol[sex=="Female"][heart_faillure=="Accident"]
#Untarget
cholesterol_male_untarget = cholesterol[sex=="Male"][heart_faillure=="Nothing"]
cholesterol_female_untarget = cholesterol[sex=="Female"][heart_faillure=="Nothing"]

#Diabetes
# > 125mg = True = Diabetes
#target
diab_male_target = fast_sugars[sex=="Male"][heart_faillure=="Accident"][fast_sugars ==1]
diab_female_target = fast_sugars[sex=="Female"][heart_faillure=="Accident"][fast_sugars ==1]
#untarget
diab_male_untarget = fast_sugars[sex=="Male"][heart_faillure=="Nothing"]
diab_female_untarget = fast_sugars[sex=="Female"][heart_faillure=="Nothing"]

#Resting blood pressure
avg_bloodpress = round(blood_pressure.mean(),2)
# > 90 risk trouble health
#target
bloodpress_male_target = blood_pressure[sex=='Male'][heart_faillure=='Accident']
bloodpress_female_target = blood_pressure[sex=='Female'][heart_faillure=='Accident']
#untarget
bloodpress_male_untarget = blood_pressure[sex=='Male'][heart_faillure=='Nothing']
bloodpress_female_untarget = blood_pressure[sex=='Female'][heart_faillure=='Nothing']

#chest pain
# 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic
#Male
#Target
chest_type1_men_target = chest_pain[sex=='Male'][heart_faillure=='Accident'][chest_pain == 1]
chest_type2_men_target = chest_pain[sex=='Male'][heart_faillure=='Accident'][chest_pain == 2]
chest_type3_men_target = chest_pain[sex=='Male'][heart_faillure=='Accident'][chest_pain == 3]
chest_type4_men_target = chest_pain[sex=='Male'][heart_faillure=='Accident'][chest_pain == 4]
#Untarget
chest_type1_men_untarget = chest_pain[sex=='Male'][heart_faillure=='Nothing'][chest_pain == 1] 
chest_type2_men_untarget = chest_pain[sex=='Male'][heart_faillure=='Nothing'][chest_pain == 2]
chest_type3_men_untarget = chest_pain[sex=='Male'][heart_faillure=='Nothing'][chest_pain == 3]
chest_type4_men_untarget = chest_pain[sex=='Male'][heart_faillure=='Nothing'][chest_pain == 4]
#Female
#Target
chest_type1_women_target = chest_pain[sex=='Female'][heart_faillure=='Accident'][chest_pain == 1]
chest_type2_women_target = chest_pain[sex=='Female'][heart_faillure=='Accident'][chest_pain == 2]
chest_type3_women_target = chest_pain[sex=='Female'][heart_faillure=='Accident'][chest_pain == 3]
chest_type4_women_target = chest_pain[sex=='Female'][heart_faillure=='Accident'][chest_pain == 4]
#Untarget
chest_type1_women_untarget = chest_pain[sex=='Female'][heart_faillure=='Nothing'][chest_pain == 1]
chest_type2_women_untarget = chest_pain[sex=='Female'][heart_faillure=='Nothing'][chest_pain == 2]
chest_type3_women_untarget = chest_pain[sex=='Female'][heart_faillure=='Nothing'][chest_pain == 3]
chest_type4_women_untarget = chest_pain[sex=='Female'][heart_faillure=='Nothing'][chest_pain == 4]


#############################################################################################################################
#---------------------------------------------------Graphique----------------------------------------------------------------
# Disparité cholesterol
plt.scatter(age,cholesterol,c ='Yellow', linewidths= 5)
plt.scatter(age_man_target, cholesterol_male_target, c ='Blue')
plt.scatter(age_woman_target,cholesterol_female_target, c = 'Pink')
plt.ylabel("CHOLESTEROLS RATES")
plt.xlabel("AGES")
plt.title("DATA FROM 300 PATIENTS : HEART ATTACK CORRELATION BETWEEN CHOLESTEROLS")
legends_chol=["Health","Male Heart Attack","Female Heart Attack"]
plt.legend(legends_chol,bbox_to_anchor = (1,1))
plt.ylim(0,600)
plt.xlim(0,90)
plt.show()

#disparité diabetes
#can only be use in scoring

#Resting blood pressure
plt.scatter(age,blood_pressure,c ='Yellow', linewidths= 5)
plt.scatter(age_man_target, bloodpress_male_target, c ='Blue')
plt.scatter(age_woman_target,bloodpress_female_target,c = 'Pink')
plt.ylabel("BLOOD PRESSURES")
plt.xlabel("AGES")
plt.title("DATA FROM 300 PATIENTS : HEART ATTACK CORRELATION BETWEEN BLOOD PRESSURES")
plt.legend(legends_chol,bbox_to_anchor = (1,1))
plt.ylim(0,250)
plt.xlim(0,90)
plt.show()

# chest