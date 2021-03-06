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

The death rate for the Covid-19 differs according to age, gender and underlying disorders. Previous research showed that it could reach 12% in infection site [4], but the death rate based on actual data is around 7% [5]. However, this number might also vary depending of the strength of the health care system. For example in France the death rate in only of 2%. 

Moreover, the duration of hospitalisation or quarantine before a full recovery varies with the severity of the symptoms. According to expert sources, the mean time is around 14 days. 

Thus, our model for recovery is now: 

<p align="center"> 
  Recovered(t) = Infected(t-14)*(1-0.07)
</p>

This means that the number of recovered cases at the time t is equal to the number of infected cases 14 days before times 93%, since 7% will die. This simplification of the model would be updated over time.

### Beta

Beta controlls the infection rate. This means how many people an infected case will infect others. The transmission rate for a seasonal flue is around 1.3 [6], 2.7 for Ebola [7] and 2.35 for the Covid_19 [8]. In the later cited paper, the study showed that the transmission rate might change. A further analysis will show the importance of quarantine. 

![Beta_explanation](https://user-images.githubusercontent.com/55028120/76792161-b539c580-67c2-11ea-8ac9-093d24a9f4d5.png)

As it can be seen, the spread of infected cases is much faster for Ebola and Covid-19 than it is for the seasonal flue. Only the Beta has beed modified. 


## Test the model 
### Number of Cases

![Drawing_Data_prediction](https://user-images.githubusercontent.com/55028120/76892931-bd116c80-688b-11ea-8757-f58b82ae7874.png)

When the model is tested, it does not seem to fit the actual data. This is due to the few number of cases at the begining that makes the strength of the spread lower at the start that expected in the model. To fit the current data, a simple task is to calibrate the model on the point of inflection. Thus, the point of inflexion appears 17 days in the actual data than prediction. If the predictions is shifted of 17 days the new comparison looks like that: 

![Data_prediction_shifted](https://user-images.githubusercontent.com/55028120/76893489-b9cab080-688c-11ea-920f-fba1a4cf4898.png)


The model seems now a way better an even accurate.

### Number of Deaths

![Data_prediction_shifted_death](https://user-images.githubusercontent.com/55028120/76893811-45444180-688d-11ea-98a9-242678930923.png)

Similarly the model seems also accurate for the number of deaths. 

## Effect of quarantine

The French governement has lockdowned the country with high restrictions. It is now forbidden to go out, except for necessary grocery or for medical purposes. Thus, the infection rate should now be greatly diminished. In our model, we divided the transmission rate by 2 and observe the effect for a couple of days and for a month. 

### Number of Cases

![Quarantine_cases_2](https://user-images.githubusercontent.com/55028120/76902377-28633a80-689c-11ea-93ee-67bb43fbb5fe.png)

For a short period, the number of cases seems to increase at a high pace, even in quarantine. However, when the period is extended over a month the effect of the quarantine is now extremely important. Indeed, without any quarantine almost all of the French population would have been infected at the end of April. Obviously, this would only be the case if absolutly no restriction was take. The fear of the virus itself would be enough to slow down this high progression. When a strict quarantine is set the number of infection remains relatively low. This shows the effect of quarantine and the necessity to respect it. 

### Number of Deaths

![Quarantine_Death](https://user-images.githubusercontent.com/55028120/76902734-ed153b80-689c-11ea-8c98-8c114c30edd6.png)

Here the effect of quarantine appears to be strong for the short period. For the long period, the effect of quarantine is consequent with less than 8000 deaths at the end of April agains 500 000 without. The latter number may sound extreme and could be related to the previous explanation about the fear itself of the virus and the self-restriction that population would have taken. However, with hundreeds of thousands of infected cases hospitals would be overwhelmed, hence the level of care would considerably diminished increasing the death rate. 








## References 

[1] http://systems-sciences.uni-graz.at/etextbook/sw2/sir.html

[2] https://www.reuters.com/article/us-china-health-japan/japanese-woman-confirmed-as-coronavirus-case-for-2nd-time-weeks-after-initial-recovery-idUSKCN20L0BI

[3] https://www.caixinglobal.com/2020-02-26/14-of-recovered-covid-19-patients-in-guangdong-tested-positive-again-101520415.html

[4] https://wwwnc.cdc.gov/eid/article/26/6/20-0233_article

[5] https://www.worldometers.info/coronavirus/

[6] https://www.healthline.com/health-news/how-deadly-is-the-coronavirus-compared-to-past-outbreaks#So,-when-will-things-calm-down-with-COVID-19?-

[7] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4843458/

[8] https://www.thelancet.com/action/showPdf?pii=S1473-3099%2820%2930144-4







