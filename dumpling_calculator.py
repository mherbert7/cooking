# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:27:58 2022

@author: Marcus
"""

import sys

def increase_fat_ratio(total_weight, current_fat_percent, desired_fat_percent):
    current_ratio = current_fat_percent / 100
    desired_ratio = desired_fat_percent / 100

    cur_fat = total_weight * current_ratio
    cur_meat = total_weight - cur_fat
    
    numerator = desired_ratio * cur_meat + (desired_ratio - 1)*cur_fat
    denominator = (1 - desired_ratio)
    
    new_fat = numerator/denominator
    
    print("The current ratio is", 100*current_ratio, "% fat to", 
          100*(1 - current_ratio), "% meat.")
    print("Current fat:", int(cur_fat), "grams.")
    print("Current meat:", int(cur_meat), "grams.")
    print()
    
    print("To get the new ratio of", 100*desired_ratio, "% fat to",
          100*(1 - desired_ratio), "% meat, add", int(new_fat), 
           "grams of fat.")
    print("This will bring the total fat to approx.", int(cur_fat + new_fat),
          "grams, for a new approx. total weight of", int(cur_meat + cur_fat +\
                                                          new_fat), "grams.")
    	  
    	  
if __name__ == "__main__":
    total_weight = int(sys.argv[1])
    current_fat_percent = int(sys.argv[2])
    desired_fat_percent = int(sys.argv[3])
    increase_fat_ratio(total_weight, current_fat_percent, desired_fat_percent)