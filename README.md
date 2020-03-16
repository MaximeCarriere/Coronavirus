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

<p align="center"> 
  Recovered(t) = Infected(t-14)*(1-0.07)
</p>

This means that the number of recovered cases at the time t is equal to the number of infected cases 14 days before times 93%, since 7% will die. This simplification of the model is allow to change over time.

### Beta

Beta controlls the infection rate. This means how many people an infected case will infect others. The transmission rate for a seasonal flue is around 1.3 [6], 2.7 for Ebola [7] and 2.35 for the Covid_19 [8]. In the later cited paper, the study showed that the transmission rate might change. A further analysis will show the importance of quarantine. 


## References 

[1] http://systems-sciences.uni-graz.at/etextbook/sw2/sir.html

[2] https://www.reuters.com/article/us-china-health-japan/japanese-woman-confirmed-as-coronavirus-case-for-2nd-time-weeks-after-initial-recovery-idUSKCN20L0BI

[3] https://www.caixinglobal.com/2020-02-26/14-of-recovered-covid-19-patients-in-guangdong-tested-positive-again-101520415.html

[4] https://wwwnc.cdc.gov/eid/article/26/6/20-0233_article

[5] https://www.worldometers.info/coronavirus/

[6] https://www.healthline.com/health-news/how-deadly-is-the-coronavirus-compared-to-past-outbreaks#So,-when-will-things-calm-down-with-COVID-19?-

[7] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4843458/

[8] https://www.thelancet.com/action/showPdf?pii=S1473-3099%2820%2930144-4







