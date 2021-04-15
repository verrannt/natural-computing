import numpy as np
import math
import matplotlib.pyplot as plt

def p_corr(w_strong, w_weak=1, p_w=0.6): # a generalized version of formula of question 3b I thought we needed but apparently not
    total_votes = w_strong + 10*w_weak
    prob = 0
    # strong classifier is correct:
    necc = math.floor((total_votes/2))+1-w_strong # necessary votes from the weak classifiers
    necc = math.ceil(necc / w_weak)
    if necc > 10: # sanity check
        return 0
    if necc < 0: # sanity check
        return 0
    for k in range(necc, 11): # formula
        prob += 0.75 * math.factorial(10)/math.factorial(k)/math.factorial(10-k)*math.pow(p_w,k)*math.pow(1-p_w,10-k)

    # strong classifier is incorrect:
    necc = math.floor((total_votes/2))+1 # necessary votes from the weak classifiers
    necc = math.ceil(necc / w_weak)
    if necc > 10: # sanity check
        return 0
    for k in range(necc, 11): # formula
        prob += 0.25 * math.factorial(10)/math.factorial(k)/math.factorial(10-k)*math.pow(p_w,k)*math.pow(1-p_w,10-k)
    
    return prob
# 3c
w_strong = 1
err = 1 - p_corr(w_strong)
a_m = np.log((1-err)/err)
w_strong = w_strong * math.exp(a_m * 1) # * 1 because we assumed we made the correct vote
print(w_strong)

# 3d
pe = np.arange(0.01,1,0.01) # presumed error rates of a learner
ws = []
for p in pe:
    a_m = np.log((1-p)/p)
    w = math.exp(a_m * p) # * p because in 1-p times it is * 0 and else * 1 thus on average * p
    ws.append(w)

plt.figure()
plt.plot(pe, ws)
plt.ylabel('Weight')
plt.xlabel('P_error')
plt.show()