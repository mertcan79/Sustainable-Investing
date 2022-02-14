import numpy as np
import pandas as pd
from functions import *

data = pd.read_csv("data/final_data.csv")

data.drop("Unnamed: 0",axis=1,inplace=True)

n,p = params(data)

obj_i = 4

constraints = [
                0.09 # return
               ,0.6 # sustainability
               ,2   # dividend yield
               ,1   # clean energy use
               ]
b_tol = 0.1

if __name__ == '__main__':

    solve_problem(p,n,obj_i,constraints,b_tol)