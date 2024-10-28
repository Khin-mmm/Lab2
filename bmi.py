def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height) 
    print("BMI = " + str(bmi))   

    if(bmi < 18.5): 
        print("Under Weight")
        value = -1

    if(bmi > 25.0): 
        print("Over Weight")
        value = 1
    
    else: 
        print("Normal Weight")
        value = 0

    return value

#calculate_bmi(weight="57",height="1.73")

calculate_bmi(weight=57,height=1.73)