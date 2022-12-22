import sys
from datetime import date, timedelta
import random
import argparse
import math

# Birthday paradox: probability that in a classroom of size n, at leaast 2 ppl will share the same bday 

# accept input from user
parser = argparse.ArgumentParser()
parser.add_argument("param", help="enter classroom size and number of simulations", type = int, nargs='*')
args = parser.parse_args()

def sim_bday(size, num_simulations):
	# runs simultation num_simulations times with size
    shared_bday = 0
    for sim in range(num_simulations):
        dates = generate_dates(size) 
        setOfElems = set()
        for elem in dates:
            if elem not in setOfElems:
                setOfElems.add(elem) 
            else:
                shared_bday += 1
                break
    prob = shared_bday/num_simulations
    return prob      

def generate_dates(size):
    # https://www.geeksforgeeks.org/python-generate-k-random-dates-between-two-other-dates/
	# generate random set of n dates
    
    # initializing dates ranges 
    test_date1, test_date2 = date(2022,1,1), date(2022,12,31)

    # initializing K
    K = size
      
    # getting days between dates
    dates_bet = test_date2 - test_date1
    total_days = dates_bet.days
      
    res = []
    for idx in range(K):
        random.seed(a=None)
          
        # getting random days
        randay = random.randrange(total_days)
          
        # getting random dates 
        res.append(test_date1 + timedelta(days=randay))
    return res
      
def main():
    size = args.param[0]
    num_simulations = args.param[1]
    print(sim_bday(size, num_simulations))
    
if __name__ == '__main__':
    main()
