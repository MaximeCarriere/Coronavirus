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

<img width="200" alt="differential_equation" src="https://user-images.githubusercontent.com/55028120/76787601-b0244880-67b9-11ea-82b9-776a9efe16da.png">






## References 

[1] http://systems-sciences.uni-graz.at/etextbook/sw2/sir.html
