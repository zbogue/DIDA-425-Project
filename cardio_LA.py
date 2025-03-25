#CARDIOVASCULAR DISEASE
#LOS ANGELES, CA


import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols 
from sklearn.linear_model import LinearRegression

big_health = pandas.read_csv("/Users/zebbogue/Documents/GitHub/DIDA-425-Project/BigCitiesHealth-1.csv")

big_health.shape

set(big_health["geo_label_citystate"]) #getting all unique values for geo_label_citystate2

set(big_health["metric_source_label_fn"])

top_five_cities = ['New York City, NY', 'Los Angeles, CA', 'Houston, TX', 'Phoenix, AZ', 'Chicago, IL']

big_health = big_health[big_health['geo_label_citystate'].isin(top_five_cities)]
big_health

#renaming all columns
big_health = big_health.rename(columns={'metric_item_label':'item', 'geo_label_citystate':'city_state', 'date_label':'year', 'metric_source_label_fn':'source',
                           'strata_race_label':'race', 'strata_sex_label':'sex', 'strata_race_sex_label':'race_sex', 'metric_cat_label':'category',
                           'metric_subcat_label':'subcat', 'metric_item_label_subtitle':'item_subtitle', 'metric_cat_item_yaxis_label':'item_yaxis', 
                           'geo_label_proxy_or_real':'geo_proxy', 'geo_label_proxy_footnote':'geo_note', 'geo_fips_desc':'geo_unit', 'date_label_proxy_or_real': 'date_proxy',
                           'date_label_proxy_footnote':'date_note', 'value_ci_flag_yesno':'value_ci', 'value_95_ci_low': 'ci_low', 'value_95_ci_high':'ci_high'})

big_health.dtypes 

big_health.columns

big_health

set(big_health['subcat'])

#LOOKING AT CARDIOVSACULAR DISEASE DEATHS

cardio_health = big_health[big_health['subcat'] == 'Cardiovascular Disease'] 

set(cardio_health['item']) #contains {'High Blood Pressure', 'Cardiovascular Disease Deaths', 'Heart Disease Deaths'}

cardio_la = cardio_health[cardio_health['city_state'] == 'Los Angeles, CA']

cardio_deaths_la = cardio_la[cardio_la['item'] == 'Cardiovascular Disease Deaths']

cardio_deaths_la_grouped = cardio_deaths_la.groupby('year', as_index=False)['value'].mean() #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

#PLOTTING CARDIOVASCULAR DISEASE DEATHS IN LA FROM 2010-2022 (NO REGRESSION LINE)
plt.figure(figsize=(10, 5))
plt.plot(cardio_deaths_la_grouped['year'], cardio_deaths_la_grouped['value'])
plt.ylabel('Number of Deaths (Per 100,000)')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Cardiovascular Disease Deaths in Los Angeles from 2010-2022')
plt.ylim(200, 280)
plt.show()

#PLOTTING RESIDUALS TO DETERMINE VALIDITY OF LINEAR REGRESSION
#https://www.geeksforgeeks.org/how-to-create-a-residual-plot-in-python/

linear_model = ols('value ~ year', data=cardio_deaths_la_grouped).fit() 
print(linear_model.summary())

fig = plt.figure(figsize=(14, 8))

fig = sm.graphics.plot_regress_exog(linear_model, 'year', fig=fig) 
plt.show()

#BASIC REGRESSION LINE FOR CARDIOVASCULAR DISEASE DEATHS
#https://www.kaggle.com/code/ryanholbrook/linear-regression-with-time-series

fig, ax = plt.subplots(figsize=(10,5))
ax.plot('year', 'value', data=cardio_deaths_la_grouped, color='0.75')
ax = sns.regplot(x='year', y='value', data=cardio_deaths_la_grouped, ci=None, scatter_kws=dict(color='0.25'))
ax.set_title('Cardiovascular Disease Deaths in Los Angeles, CA from 2010-2022')
ax.set_ylim(220,260)
plt.show()

#LAG PLOT
cardio_deaths_la_grouped['Lag_1'] = cardio_deaths_la_grouped['value'].shift(1)
df = cardio_deaths_la_grouped.reindex(columns=['value', 'Lag_1'])
df.head()

fig, ax = plt.subplots()
ax = sns.regplot(x='Lag_1', y='value', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_aspect('equal')
ax.set_title('Lag Plot of CVD deaths in LA (2010-2022)')
plt.show()
#lag plot shows clear relationship between values and lag values indicating 


#FITTING A LINEAR REGRESSION MODEL
X = cardio_deaths_la_grouped.loc[:, ['year']]  # features
Y = cardio_deaths_la_grouped.loc[:, 'value']  # target

#Training the model
model = LinearRegression()
model.fit(X, Y)

y_pred = pandas.Series(model.predict(X), index=X.index)

plot_params = {
    'color': 'gray',         
    'marker': 'o',           
    'linestyle': '-',        
    'alpha': 0.7,
    'figsize': (10,6)
    }

ax = Y.plot(**plot_params)
ax = y_pred.plot(ax=ax, linewidth=3)
ax.set_title('Time Plot of CVD deaths in LA (2010-2022)')
plt.show()


#LOOKING AT HEART DISEASE
heart_disease_la = cardio_la[cardio_la['item'] == 'Heart Disease Deaths']

heart_disease_la_grouped = heart_disease_la.groupby('year', as_index=False)['value'].mean() #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

plt.figure(figsize=(10, 5))
plt.plot(heart_disease_la_grouped['year'], heart_disease_la_grouped['value'])
plt.ylabel('Number of Deaths (Per 100,000)')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Heart Disease Deaths in Los Angeles from 2010-2022')
plt.ylim(150, 210)
plt.show()

#High Blood Pressure
high_bp_la = cardio_la[cardio_la['item'] == 'High Blood Pressure']

high_bp_la_grouped = high_bp_la.groupby('year', as_index=False)['value'].mean() #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

real_bp_la = high_bp_la[high_bp_la['date_proxy'] == 'real']

real_bp_la_grouped = real_bp_la.groupby('year', as_index=False)['value'].mean()


plt.figure(figsize=(10, 5))
plt.plot(real_bp_la_grouped['year'], real_bp_la_grouped['value'])
plt.ylabel('Percentage of Adults')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('High Blood Pressure in Los Angeles from 2010-2022')
plt.ylim(24, 28)
plt.show()