# -*- coding: utf-8 -*-
"""Exploratory_data_analysis_covid19_India.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NOs9u6v6FDHA54QYZkZKCV-BGKOoS3_4
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm

data_region_details = pd.read_csv('/content/region_details.csv')
data_state = pd.read_csv('/content/state_level_latest.csv')

data_state.columns

data_state = data_state[['state','statecode','confirmed','active','deaths','recovered','deltaconfirmed', 'deltadeaths','deltarecovered']]

data_region_details.columns

data_region = data_region_details.copy()

data_region.head()

data_state.head()

data_state.sort_values(by=['state'], inplace=True)

data_region.sort_values(by=['region'], inplace=True)

data_state.reset_index(drop=True, inplace=True)

data_region.reset_index(drop=True, inplace=True)

big_data = pd.merge(data_state, data_region, how='inner', left_on='state', right_on='region')

big_data

big_data.shape

big_data.drop(['region'], inplace=True,axis=1)



from sklearn import preprocessing

x = big_data[['population','active']] #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
small_df = pd.DataFrame(x_scaled)

from matplotlib.cm import ScalarMappable
x_pos = np.arange(len(big_data))
labels = big_data['statecode']
data_color = small_df[1]/small_df[0]
my_cmap = plt.cm.get_cmap('seismic')
colors = my_cmap(data_color)
fig, ax = plt.subplots()
barlist=ax.bar(x_pos,big_data['active'],  align='center', ecolor='black', capsize=10,color=colors)
fig.set_size_inches(25, 10)
#plt.axhline(y=y, color='slategrey', linestyle='-')
ax.set_ylabel('active_cases')
ax.set_xlabel('statecode')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_ylim([0,20000])
sm = ScalarMappable(cmap=my_cmap)
sm.set_array([])
ax.set_title('active cases vs state')
cbar = plt.colorbar(sm)
cbar.set_label('color represents active cases by population ratio(normalized)', rotation=270,labelpad=25)

big_data.columns

big_data=big_data[['state', 'statecode', 'confirmed', 'active', 'deaths', 'recovered',
       'population','density','poverty', 'hdi']]

big_data.head()

from sklearn import preprocessing

x = big_data[['density','active']] #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
small_df_ = pd.DataFrame(x_scaled)

from matplotlib.cm import ScalarMappable
x_pos = np.arange(len(big_data))
labels = big_data['statecode']
data_color = small_df_[1]/small_df_[0]
my_cmap = plt.cm.get_cmap('seismic')
colors = my_cmap(data_color)
fig, ax = plt.subplots()
barlist=ax.bar(x_pos,big_data['active'],  align='center', ecolor='black', capsize=10,color=colors)
fig.set_size_inches(25, 10)
#plt.axhline(y=y, color='slategrey', linestyle='-')
ax.set_ylabel('active_cases')
ax.set_xlabel('statecode')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_ylim([0,20000])
sm = ScalarMappable(cmap=my_cmap)
sm.set_array([])
ax.set_title('active cases vs state')
cbar = plt.colorbar(sm)
cbar.set_label('color represents active cases by density ratio(normalized)', rotation=270,labelpad=25)

big_data.corr()



f = plt.figure(figsize=(10,10))
plt.matshow(big_data.corr(), fignum=f.number)
ax=f.gca()
#labels
column_labels = ['s','confirmed','active','deaths','recovered','population','density','poverty','hdi']
row_labels = ['s','confirmed','active','deaths','recovered','population','density','poverty','hdi']
ax.set_xticklabels(column_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=20)
plt.title('Correlation Matrix', fontsize=16);

corr = big_data.corr()
corr.style.background_gradient(cmap='coolwarm')



fig = plt.figure(figsize=(30,15))
from matplotlib import gridspec
gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1]) 
ax =plt.subplot(gs[0])
x_pos = np.arange(len(big_data))
labels = big_data['statecode']
data_color = small_df[1]/small_df[0]
my_cmap = plt.cm.get_cmap('seismic')
colors = my_cmap(data_color)
barlist=ax.bar(x_pos,big_data['active'],  align='center', ecolor='black', capsize=10,color=colors)
ax.set_ylabel('active_cases')
ax.set_xlabel('statecode')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
plt.xticks(rotation=60)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_ylim([0,20000])
sm = ScalarMappable(cmap=my_cmap)
sm.set_array([])
ax.set_title('active cases vs state')
cbar = plt.colorbar(sm)
cbar.set_label('color represents active cases by population ratio(normalized)', rotation=270,labelpad=25)


ax1 = plt.subplot(gs[1])
ax1.matshow(big_data.corr())
#labels
my_cmap = plt.cm.get_cmap('gist_heat')
column_labels = ['s','confirmed','active','deaths','recovered','population','density','poverty','hdi']
row_labels = ['s','confirmed','active','deaths','recovered','population','density','poverty','hdi']
ax1.set_xticklabels(column_labels, minor=False)
ax1.set_yticklabels(row_labels, minor=False)
figure_title = "correlation between different variables of populations across country"
plt.title(figure_title, y=1.3)
plt.xticks(rotation=45)
sm= ScalarMappable(cmap=my_cmap)
cb = plt.colorbar(sm)
cb.ax.tick_params(labelsize=20)
cb.ax.set_yticklabels(['-0.6','-0.2','0','0.2','0.6','1.0'])
cb.set_label('correlation coeffecient', rotation=270,labelpad=25)
#plt.title('Correlation Matrix', fontsize=16);

from google.colab import files
plt.savefig('test.png')
files.download('test.png')



