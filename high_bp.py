import pandas
import matplotlib.pyplot as plt


from cardio_LA import real_bp_la_grouped
from cardio_NY import real_bp_ny_grouped
from cardio_AZ import real_bp_az_grouped
from cardio_TX import real_bp_tx_grouped
from cardio_IL import real_bp_il_grouped

fig, ax = plt.subplots(figsize=(10,6))

real_bp_tx_grouped.plot(ax=ax, x='year', y='value', label='Houston, TX', linewidth=2, color='#33a02c')
real_bp_il_grouped.plot(ax=ax, x='year', y='value', label='Chicago, IL', linewidth=2, color='black')
real_bp_ny_grouped.plot(ax=ax, x='year', y='value', label='New York City, NY', linewidth=2, color='#1f78b4')
real_bp_az_grouped.plot(ax=ax, x='year', y='value', label='Phoenix, AZ', linewidth=2, color='#b2df8a')
real_bp_la_grouped.plot(ax=ax, x='year', y='value', label='Los Angeles, CA', linewidth=2, color='#a6cee3')

ax.legend()
plt.ylabel('Percentage of Adults')
plt.xlabel('Year')
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.title('Percentage of Adults with High Blood Pressure from 2010-2022')
plt.ylim(25, 33)

plt.show()