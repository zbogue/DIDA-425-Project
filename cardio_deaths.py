import pandas
import matplotlib.pyplot as plt


from cardio_LA import cardio_deaths_la_grouped
from cardio_NY import cardio_deaths_ny_grouped
from cardio_AZ import cardio_deaths_az_grouped
from cardio_TX import cardio_deaths_tx_grouped
from cardio_IL import cardio_deaths_il_grouped


#PLOTTING CARDIOVASCULAR DISEASE DEATHS 
fig, ax = plt.subplots(figsize=(10,6))

cardio_deaths_tx_grouped.plot(ax=ax, x='year', y='value', label='Houston, TX', linewidth=2, color='#33a02c')
cardio_deaths_la_grouped.plot(ax=ax, x='year', y='value', label='Los Angeles, CA', linewidth=2, color='#a6cee3')
cardio_deaths_il_grouped.plot(ax=ax, x='year', y='value', label='Chicago, IL', linewidth=2, color='black')
cardio_deaths_ny_grouped.plot(ax=ax, x='year', y='value', label='New York City, NY', linewidth=2, color='#1f78b4')
cardio_deaths_az_grouped.plot(ax=ax, x='year', y='value', label='Phoenix, AZ', linewidth=2, color='#b2df8a')

#ax.legend(labels=["Los Angeles", "New York City", "Phoenix"])
ax.legend()
plt.ylabel('Number of Deaths (Per 100,000)')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Cardiovascular Disease Deaths from 2010-2022')
plt.ylim(170, 280)

plt.show()