import numpy as np 
p=0.3
ss=1000

bino=np.random.binomial(n=1,p=p,size=ss)
#print(bino)
# x=1 customer clicks the link
#x=0 customer does not click the link

#bernoulli distribution

number_of_clicks= np.sum(bino == 1)
number_of_no_clicks= np.sum(bino == 0)
print("Number of clicks:", number_of_clicks)
print("Number of no clicks:", number_of_no_clicks)
print()

#empirical adn theoretical pmf

emperical_pmf_clicks= number_of_clicks/ss
emperical_pmf_no_clicks= number_of_no_clicks/ss


print("Empirical PMF of clicks P(X=1): ", emperical_pmf_clicks)
print("Empirical PMF of no clicks P(X=0):", emperical_pmf_no_clicks)

theoretical_pmf_clicks = p
theoretical_pmf_no_clicks = 1 - p
print("Theoretical PMF of clicks P(X=1): ", p)
print("Theoretical PMF of no clicks P(X=0):", 1-p)

#mean and variance for empirical and theoretical distribution
mean_empirical = np.mean(bino)
mean_theoretical = p
variance_empirical = np.var(bino)
variance_theoretical = p * (1 - p)

print("Empirical Mean:", mean_empirical)
print("Theoretical Mean:", mean_theoretical)
print(f"Empirical Variance: {variance_empirical:.2f}")
print("Theoretical Variance:", variance_theoretical)

"""
import matplotlib.pyplot as plt
# Plotting the empirical and theoretical PMF
theoretic =[theoretical_pmf_no_clicks, theoretical_pmf_clicks]
empirical = [emperical_pmf_no_clicks, emperical_pmf_clicks]
labels = ['No Clicks (X=0)', 'Clicks (X=1)']

plt.bar(labels, theoretic, alpha=0.3, color='blue', label='Theoretical PMF')
plt.bar(labels, empirical, alpha=0.3, color='orange', label='Empirical PMF')

plt.title('Empirical vs Theoretical PMF of Customer Clicks')
plt.legend()
plt.show()


"""