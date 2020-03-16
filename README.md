# Covid-19 Model

The goal of this model is to predict and explain the spread of the Covid-19. 

- First Part explanation of the Model
- Focus in France (coming soon)


## The model

This model is an modified version of the SIR model [1]. This epidemiologic model is well used for the spread of virus such as influenza, Ebola and now Covid-19.

The model predict over time: 

- Number of infected cases
- Number of recovered cases
- Number of susceptibile cases
- Number of deaths (in our adaptation)



![Explanation_SIR](https://user-images.githubusercontent.com/55028120/76786234-283d3f00-67b7-11ea-96f4-9fdf743e3325.png)

To do so, the model uses two parameters: 

- Gamma: The rate an infected recovers and moves into the resistant phase.
- Beta: The parameter controlling how often a susceptible-infected contact results in a new infection.

The model is based on 3 intereconneted differential equations using the parameters:

<p align="center">
<img width="350" alt="differential_equation" src="https://user-images.githubusercontent.com/55028120/76787601-b0244880-67b9-11ea-82b9-776a9efe16da.png">
</p>


## Understand the parameters
### Gamma

Gamma control the recovery and the resistant phase. For the Covid-19, an infected case who has recovered is still susceptible to be re-infected. Indeed, a Japaneese tour bus guide has been tested positive after having recovered from an earlier infection [2]. A Chinese report also claimed that 14% of Recovered Covid-19 Patients in Guangdong Tested Positive Again [3] 

Thus, the immunity parameter in the SIR model cannot be applied for the Covid-19. In our modification this parameter is, therefore, set to 0. The recovered rate is now governed by the probability of surviving the virus. This might change in future update. 

The death rate for the Covid-19 differs according to age, gender and underlying disorders. Previous research showed that it could reach 12% in infection site [4], but the death rate based on actual data is around 7% [5].

Moreover, the duration of hospitalisation or quarantine before a full recovery varies with the symptome severity. According to expert sources, the mean time is around 14 days. 

Thus, our model for recovery is now: 

**Recovered(t) = Infected(t-14)*(1-0.93)**

## References 

[1] http://systems-sciences.uni-graz.at/etextbook/sw2/sir.html

[2] https://www.reuters.com/article/us-china-health-japan/japanese-woman-confirmed-as-coronavirus-case-for-2nd-time-weeks-after-initial-recovery-idUSKCN20L0BI

[3] https://www.caixinglobal.com/2020-02-26/14-of-recovered-covid-19-patients-in-guangdong-tested-positive-again-101520415.html

[4] https://wwwnc.cdc.gov/eid/article/26/6/20-0233_article

[5] https://www.worldometers.info/coronavirus/
