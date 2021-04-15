import math
import matplotlib.pyplot as plt

def p_corr(w):
    total_votes = w+10
    prob = 0
    # strong classifier is correct:
    necc = math.floor((total_votes/2))+1-w # necessary votes from the weak classifiers
    if necc > 10: # sanity check
        return 0
    if necc < 0: # sanity check
        return 0
    for k in range(necc, 11): # formula
        prob += 0.75 * math.factorial(10)/math.factorial(k)/math.factorial(10-k)*math.pow(0.6,k)*math.pow(0.4,10-k)

    # strong classifier is incorrect:
    necc = math.floor((total_votes/2))+1 # necessary votes from the weak classifiers
    if necc > 10: # sanity check
        return 0
    for k in range(necc, 11): # formula
        prob += 0.25 * math.factorial(10)/math.factorial(k)/math.factorial(10-k)*math.pow(0.6,k)*math.pow(0.4,10-k)
    
    return prob

# weights = [w for w in range(0, 12)]

probs = [p_corr(w) for w in weights]

plt.figure()
plt.plot(weights, probs)
plt.xlabel('Weight')
plt.ylabel('P_correct')
plt.show()