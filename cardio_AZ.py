#CARDIOVASCULAR DISEASE
#PHOENIX, AZ

import pandas
import matplotlib.pyplot as plt

big_health = pandas.read_csv("/Users/zebbogue/Documents/GitHub/DIDA-425-Project/BigCitiesHealth-1.csv")

top_five_cities = ['New York City, NY', 'Los Angeles, CA', 'Houston, TX', 'Phoenix, AZ', 'Chicago, IL']

big_health = big_health[big_health['geo_label_citystate'].isin(top_five_cities)]

big_health = big_health.rename(columns={'metric_item_label':'item', 'geo_label_citystate':'city_state', 'date_label':'year', 'metric_source_label_fn':'source',
                           'strata_race_label':'race', 'strata_sex_label':'sex', 'strata_race_sex_label':'race_sex', 'metric_cat_label':'category',
                           'metric_subcat_label':'subcat', 'metric_item_label_subtitle':'item_subtitle', 'metric_cat_item_yaxis_label':'item_yaxis', 
                           'geo_label_proxy_or_real':'geo_proxy', 'geo_label_proxy_footnote':'geo_note', 'geo_fips_desc':'geo_unit', 'date_label_proxy_or_real': 'date_proxy',
                           'date_label_proxy_footnote':'date_note', 'value_ci_flag_yesno':'value_ci', 'value_95_ci_low': 'ci_low', 'value_95_ci_high':'ci_high'})

cardio_health = big_health[big_health['subcat'] == 'Cardiovascular Disease'] 

cardio_az = cardio_health[cardio_health['city_state'] == 'Phoenix, AZ']

#Cardiovascular Disease
cardio_deaths_az = cardio_az[cardio_az['item'] == 'Cardiovascular Disease Deaths']

cardio_deaths_az_grouped = cardio_deaths_az.groupby('year', as_index=False)['value'].mean()

plt.figure(figsize=(10, 5))
plt.plot(cardio_deaths_az_grouped['year'], cardio_deaths_az_grouped['value'])
plt.ylabel('Number of Deaths (Per 100,000)')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Cardiovascular Disease Deaths in Phoenix, Arizona from 2010-2022')
plt.ylim(160, 240)
plt.show()

#Heart Disease
heart_disease_az = cardio_az[cardio_az['item'] == 'Heart Disease Deaths']

heart_disease_az_grouped = heart_disease_az.groupby('year', as_index=False)['value'].mean() #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

plt.figure(figsize=(10, 5))
plt.plot(heart_disease_az_grouped['year'], heart_disease_az_grouped['value'])
plt.ylabel('Number of Deaths (Per 100,000)')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Heart Disease Deaths in Phoenix, Arizona from 2010-2022')
plt.ylim(100, 190)
plt.show()

#High Blood Pressure
high_bp_az = cardio_az[cardio_az['item'] == 'High Blood Pressure']

high_bp_az_grouped = high_bp_az.groupby('year', as_index=False)['value'].mean() #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

real_bp_az = high_bp_az[high_bp_az['date_proxy'] == 'real']

real_bp_az_grouped = real_bp_az.groupby('year', as_index=False)['value'].mean()

plt.figure(figsize=(10, 5))
plt.plot(real_bp_az_grouped['year'], real_bp_az_grouped['value'])
plt.ylabel('Percentage of Adults')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('High Blood Pressure in Phoenix, Arizona from 2010-2022')
plt.ylim(25, 30)
plt.show()