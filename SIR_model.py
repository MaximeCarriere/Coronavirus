#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:34:10 2020

@author: gz6009
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd

# Total population, N.
N = 60000000#0000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 #- R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta = 0.235
gamma = 0
# A grid of time points (in days)
time_end = 100
t = np.linspace(0, time_end, time_end)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T



## Death 
death = 0.07*I


## Recovered
recovered = np.zeros(len(I))
for i in range(len(I) - 28):
    recovered[i + 14] = I[i]*0.98
recovered[-14:] = recovered[-15]



# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, S, alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I, alpha=0.5, lw=2, label='Infected')
ax.plot(t, death, alpha=0.5, lw=2, label='Death')
ax.plot(t, recovered, alpha=0.5, lw=2, label='Recovered')
ax.set_xlabel('Time /days')
ax.set_ylabel('Infected Case (%)')
#ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()



coronavirus = pd.DataFrame(I)
coronavirus_death = pd.DataFrame(death)

d = pd.read_csv('/Users/gz6009/Downloads/covid_19_clean_complete-2.csv')

## Load data fr
#d = pd.read_csv('/Users/gz6009/Downloads/2019-nCoV.csv')
d = d.sort_values(by='Date')
d = d.set_index('Date')
d.index =  pd.to_datetime(d.index)
d = d.sort_index( ascending=True)

## Confirmed Cases
## From date
d = d[d['Province/State'] == 'France']

#df_fr = d[d['Status'] == 'Confirmed']
#df_fr_death = d[d['Status'] == 'Deaths']
df_fr_death = d['Deaths']
df_fr = d['Confirmed']



date_index = pd.date_range(start=d.index[0], end='4/20/2020')
len_date_index = len(pd.DataFrame(date_index).reset_index())


shift = 17
prediction_2 = pd.DataFrame(np.zeros(len(coronavirus)))
prediction_2 = coronavirus.shift(periods= shift, fill_value=1)
prediction_2_death = coronavirus_death.shift(periods= shift, fill_value=0)
prediction_2 = prediction_2.iloc[:len_date_index]
prediction_2.index = date_index
comparison_plot_2 = pd.concat([df_fr, prediction_2], axis = 1, join = 'outer')
comparison_plot_2.index = pd.to_datetime(comparison_plot_2.index)
comparison_plot_2.columns = ['CumulitiveCases', 'Prediction']



plt.plot()
plt.plot(comparison_plot_2.index, comparison_plot_2['CumulitiveCases'], "o", label = 'Number of Cases',  linewidth=1.0)
plt.plot(comparison_plot_2.index, comparison_plot_2['Prediction'], label = 'Prediction')
#plt.axvline(x='3/15/2020', label = 'Lockdown', color = 'r')
plt.xticks(rotation=45)
plt.ylabel('Cases')
plt.gcf().subplots_adjust(bottom=0.20, left = 0.15)
plt.title('France')
plt.legend()
#plt.savefig('Data_prediction_shifted.png',format='png', dpi=1200)
#


## Death
prediction_2_death_2 = prediction_2_death.iloc[:len(coronavirus_death)]
prediction_2_death_2 = prediction_2_death_2.iloc[:len_date_index]
prediction_2_death_2.index = date_index
comparison_plot_2_death = pd.concat([df_fr_death, prediction_2_death_2], axis = 1, join = 'outer')
comparison_plot_2_death.index = pd.to_datetime(comparison_plot_2_death.index)
comparison_plot_2_death.columns = ['Death', 'Prediction']



plt.plot()
plt.plot(comparison_plot_2_death.index, comparison_plot_2_death['Death'], "o",label = 'Death', linewidth=1.0)
plt.plot(comparison_plot_2_death.index, comparison_plot_2_death['Prediction'], label = 'Prediction')
plt.xticks(rotation=45)
#plt.axvline(x=comparison_plot_2_death.index[-1], label = 'Lockdown', color = 'r')
plt.ylabel('Deaths')
plt.title('France')
plt.gcf().subplots_adjust(bottom=0.20, left = 0.15)
plt.legend()
#plt.savefig('Data_prediction_shifted_death.png',format='png', dpi=1200)

#
#


## Confinement 
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = comparison_plot_2['CumulitiveCases'].iloc[len(df_fr) - 1], 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 #- R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta = 0.235/2
gamma = 0
# A grid of time points (in days)
time_end = 100
t = np.linspace(0, time_end, time_end)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T



## Death 
death_confinement = pd.DataFrame(0.02*I)


## Recovered
recovered = np.zeros(len(I))
for i in range(len(I) - 28):
    recovered[i + 14] = I[i]*0.98
recovered[-14:] = recovered[-15]

coronavirus_confinement = pd.DataFrame(I)



coronavirus_confinement_2 = coronavirus_confinement.shift(periods= (len(df_fr) - 1), fill_value=  np.nan)
coronavirus_confinement_2_2 = coronavirus_confinement_2.iloc[:len(comparison_plot_2)]
coronavirus_confinement_2_2.index = date_index
#coronavirus_confinement_2.iloc[len(df_fr) : len_date_index] = pd.DataFrame(coronavirus_confinement.iloc[:(len_date_index - len(df_fr))])
comparison_plot_2_confinement = pd.concat([df_fr, prediction_2, coronavirus_confinement_2_2], axis = 1, join = 'outer')
comparison_plot_2_confinement.index = pd.to_datetime(comparison_plot_2_confinement.index)
comparison_plot_2_confinement.columns = ['CumulitiveCases', 'Prediction', 'Prediction with quarantine']


plt.plot()
plt.plot(comparison_plot_2_confinement.index, comparison_plot_2_confinement['CumulitiveCases'],"o", label = 'Number of Cases',  linewidth=1.0)
plt.plot(comparison_plot_2_confinement.index, comparison_plot_2_confinement['Prediction'], label = 'Prediction')
plt.plot(comparison_plot_2_confinement.index, comparison_plot_2_confinement['Prediction with quarantine'], label = 'Prediction with quarantine')
plt.axvline(x='3/15/2020', label = 'Lockdown', color = 'r')
plt.xticks(rotation=45)
plt.ylabel('Cases')
plt.title('Number of Cases in France')
plt.gcf().subplots_adjust(bottom=0.20, left = 0.15)
plt.legend()
plt.savefig('Data_prediction_quarantine_short.png',format='png', dpi=1200)



## Deaths

coronavirus_confinement_2_death = death_confinement.shift(periods= (len(df_fr) - 1), fill_value=  np.nan)
coronavirus_confinement_2_death_2 = coronavirus_confinement_2_death.iloc[:len(comparison_plot_2)]
coronavirus_confinement_2_death_2.index = date_index
comparison_plot_2_death_confinement = pd.concat([df_fr_death, prediction_2_death_2, coronavirus_confinement_2_death_2], axis = 1, join = 'outer')
comparison_plot_2_death_confinement.index = pd.to_datetime(comparison_plot_2_death_confinement.index)
comparison_plot_2_death_confinement.columns = ['Death', 'Prediction', 'Prediction with quarantine']


plt.plot()
plt.plot(comparison_plot_2_death_confinement.index, comparison_plot_2_death_confinement['Death'],"o", label = 'Number of Deaths',  linewidth=1.0)
plt.plot(comparison_plot_2_death_confinement.index, comparison_plot_2_death_confinement['Prediction'], label = 'Prediction')
plt.plot(comparison_plot_2_death_confinement.index, comparison_plot_2_death_confinement['Prediction with quarantine'], label = 'Prediction with quarantine')
plt.axvline(x='3/15/2020', label = 'Lockdown', color = 'r')
plt.xticks(rotation=45)
plt.ylabel('Deaths')
plt.title('Number of Deaths in France')
plt.gcf().subplots_adjust(bottom=0.20, left = 0.15)
plt.legend()
plt.savefig('Data_prediction_quarantine__deaths_short.png',format='png', dpi=1200)



