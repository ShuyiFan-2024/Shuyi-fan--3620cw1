import csv
import random

def load_data(file_name):
    age_array=[]
    hg_array=[]
    cls_array=[]
    with open(file_name,"r") as file:
        READ=csv.reader(file)
        next(READ)

        for row in READ:
            age=int(row[0])
            hg=int(row[1])
            cls=int(row[2])
            age_array.append(age)
            hg_array.append(hg)
            cls_array.append(cls)

    return age_array,hg_array,cls_array

def perceptron(age_array,hg_array,cls_array):
      random.seed(10)
      w0=random.uniform(-1,1)
      w_age=random.uniform(-1,1)
      w_hg=random.uniform(-1,1)
      for error_approach in (10000):
           error=0
           for i in range(len(cls_array)):
                y = w0 + w_age * age_array[i] + w_hg * hg_array[i]
                if cls_array[i]:
                        if y >=0:
                            continue
                        else:
                            w0=w0+1
                            w_age=w_age+age_array[i]
                            w_hg=w_hg+hg_array[i]
                            error=error+1
                else:
                        if y<0:
                            continue
                        else:
                            w0=w0-1
                            w_age=w_age-age_array[i]
                            w_hg=w_hg-hg_array[i]
                            error=error+1
           if error==0:
                break
      return w0,w_age,w_hg
            



                


                     

           