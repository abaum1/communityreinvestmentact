# communityreinvestmentact

Scripts and limited results from my senior Thesis for Urban Studies B.A. at UC Berkeley, for which I am advised my Carolina Reid. I employ statistical modeling techniques such as OLS regression and multinomial logit models to quantitatively investigate the effect of community development policy (Community Reinvestment Act) on "gentrification" and neighborhood change. 

models: OLS-Models-all years.ipynb, UDP Multinomial Logistic Regression models.ipynb

model data prep: Model Data prep 2009.ipynb, Model Data prep 2013-2014 & Plots (to be separated).ipynb, Model Data prep 2015-2017 .ipynb

mapping prep: Mappable files script.ipynb, Point Visualization.ipynb

script for calcualting geographic neighbors: Neighbors script.ipynb



Project Description

The Community Reinvestment Act (CRA) was passed in 1977 as a means of mitigating the institutional effects of redlining, a practice encouraged by the Federal Housing Administration (FHA) from the 1930s to the 1970s. The FHA refused to ensure mortgage and home improvement loans made to neighborhoods with high populations of People of Color, as well as Jews and southern Italians. 

The Home Mortgage Disclosure Act (1975) requires banks to report demographic and geographic information for all loans originated, purchased or denied. This data is published every year and is publicly available through the Consumer Financial Protection Bureau. Under the CRA, banks get credit for loans originated to low income borrowers OR in low income census tracts, providing an avenue for them to recive CRA credit for lending to middle and high income borrowers living in low income census tracts ("gentrifiers"). This theory is currently being debated in financial and community development circles, and this study provides an approach to quantitatively evaluate its relevance in the Bay Area.  


Study Design

Causal study designs are unobtainable in most social science contexts. In an attempt to isolate CRA eligibility as a driving factor of loan activity, this study uses a regression discontinuity design to compare geographically similar census tracts that sit just over or just under the tract median income CRA eligibility threshold of 80%. CRA eligibility is coded as a dummy variable in all of the models used in this study, and the demographic variables from the ACS data are used as covariates.
Because census tract boundaries are arbitrary, they are not expected to correspond to demographic or socioeconomic discontinuities. In order to restrict the sample to census tracts that physically border each other but differ in CRA eligibility, the python spatial analysis library geopandas was used to iterate through TIGER LINE tract shapefiles to select only geographically neighboring tracts that differ in CRA eligibility. The effect of this filtering is to exclude homogeneous neighborhoods from the sample. For example, the process excludes the homogeneously wealthy parts of west San Mateo county, Marin county and hilly areas of eastern Alameda county. CRA activity is not expected to be prevalent in these areas due to their high socioeconomic status. 

Models

In this study two models are used to investigate the role of CRA on lending patterns in different types of neighborhoods. Both models are constructed for each of three time periods: 2009, 2013-2014, and 2015-2017, which were selected to represent the economic slump during and immediately after the 2008 financial crisis, and two stages of recovery afterward. 2017 is currently the most recent year of data available for the Home Mortgage Disclosure Act and American Community Survey.

A linear regression (OLS) model is used to relate the total number of loans originated in a tract with the tract’s CRA eligibility and 7 other demographic covariates.
A linear regression model is appropriate for predicting discretized values of quantitative variables. The relationship between CRA eligibility and total loan volume helps assess whether the CRA increases access to credit compared to neighborhoods that are geographically and demographically similar, but are not CRA eligible.

A multinomial logit model is used to relate the Urban Displacement Project (UDP) classification of a tract with it’s CRA eligibility and the same 7 covariates. A multinomial logit model is a logistic regression) model generalized to a multi class environment. This type of model does not assume complete independence of covariates, but relatively low collinearity is required for meaningful results. Collinearity was minimized by avoiding features that explain similar trends or are linearly dependent, as measured by a Variance Inflation Factor (VIF). 

Dependent Variables

The total number of loans originated in a tract is the dependent variable for the linear OLS model. A loan of counted towards this total if it was originated in one of the years in the model time period, filtered according to the description described earlier in the “Data” section. 

Urban Displacement Project, a UC Berkeley research initiative, has developed an 8 class typology for describing the extent and ways in which census tracts experience the complex effects of gentrification, displacement and exclusion. Low income census tracts are categorized as either not losing low income households, at risk of gentrification, or experiencing ongoing gentrification and displacement of low income households. Moderate to high income tracts are categorized as either not losing low income households, at risk of exclusion, experiencing ongoing exclusion, experiencing advanced exclusion, or experiencing advanced gentrification. 5 of these 8 classes are used as dependent variables in the a multinomial logit model. Since the focus of this research is on tracts that are near or below the eligibility threshold, middle and high income tracts at risk of exclusion, or experiencing ongoing or advanced exclusion were excluded from the model. 


Explanatory Variables

Seven demographic covariates (pct non-hispanic white, pct with bachelor’s degree, pct below poverty level, pct owner occupied units, total number of housing units, median home value, median income) are included in the models based on their pertinence to existing theories of lending patterns and availability of data. Research suggests that the racial demographics of a tract influence how many loans are made in the tract due to the credit extending and restricting effects of discrimination, desirability and bank location. Housing market characteristics such as the share of single family homes, the share of owner occupied dwellings, median home value, size of the tract and number of housing units in the tract have also been shown to be related to the number of loan originations. CRA policy requiring banks to invest in middle and low income communities lies in the understanding that socioeconomic conditions effects their access to credit. 


For all three time periods, the seven selected demographic covariates (pct non-hispanic white, pct with bachelor’s degree, pct below poverty level, pct owner occupied units, total number of housing units, median home value, median income) are from the 2009 ACS 5 Year estimates. CRA eligibility is recorded as a dummy variable (1 indicates that the tract is CRA eligible), and is derived from income information from the 2000 and 2010 censuses. In 2009, a bank’s CRA eligibility references income to the tract’s status as of the 2000 census. Starting in 2012, banks were accountable to the revised tract definitions from the 2010 census, so the 2013-2014 models reference the tract’s status according to the 2010 census. 


Results and findings are still being edited and will be finalized over the next month. 
