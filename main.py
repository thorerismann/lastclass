import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_path = Path.cwd() / 'data'

print('stop')

def load_plot_coal_jobs(data_path):
    data = pd.read_csv(data_path / 'coal_jobs.csv',dtype='str')
    data.columns = [x.lower().strip().replace(' ', '') for x in data.columns]
    melted = data.melt(id_vars = 'year', value_vars=[x for x in data.columns if x != 'year'], var_name='month', value_name='coal jobs')
    melted['coal jobs'] = pd.to_numeric(melted['coal jobs'], errors='coerce')
    melted['time'] = melted['year'] + melted['month']
    melted['time'] = pd.to_datetime(melted['time'], format='%Y%b')
    melted = melted.set_index('time').drop(['year', 'month'], axis=1)
    sns.lineplot(data=melted)
    plt.show()
    return  melted

def plot_random_non_random():
    # Generate data for subtle pattern
    np.random.seed(42)
    x_pattern = np.random.rand(500) * 100
    y_pattern = 0.04 * x_pattern + np.random.normal(0, 10, 500)

    # generate random data
    x_random = np.random.rand(500) * 100
    y_random = np.random.normal(0, 10, 500)

    # Convert to DataFrame for Seaborn
    data_with_pattern = pd.DataFrame({'X': x_pattern, 'Y': y_pattern})
    data_no_pattern = pd.DataFrame({'X': x_random, 'Y': y_random})

    # Plot scatter plots with regression lines
    plt.figure(figsize=(12, 6))

    # Subtle pattern
    plt.subplot(1, 2, 1)
    sns.regplot(data=data_with_pattern, x='X', y='Y', scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Subtle Pattern (Impact of 0.04*X)')

    # No pattern
    plt.subplot(1, 2, 2)
    sns.regplot(data=data_no_pattern, x='X', y='Y', scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('No Pattern (Purely Random)')

    plt.tight_layout()
    plt.show()

print('load coal jobs')
df = load_plot_coal_jobs(data_path)
plot_random_non_random()
print('loaded coal jobs')
