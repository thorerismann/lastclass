import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class ExtraCharts:
    """Provides the code for the extra charts produced in the report not affiliated to the replication."""

    @staticmethod
    def plot_coal_jobs(data_path):
        """Loads, formats and plots the coal job data from 1985 to 2024"""
        data = pd.read_csv(data_path, dtype='str')
        data.columns = [x.lower().strip().replace(' ', '') for x in data.columns]
        melted = data.melt(id_vars = 'year', value_vars=[x for x in data.columns if x != 'year'], var_name='month', value_name='coal jobs')
        melted['coal jobs'] = pd.to_numeric(melted['coal jobs'], errors='coerce')
        melted['time'] = melted['year'] + melted['month']
        melted['time'] = pd.to_datetime(melted['time'], format='%Y%b')
        melted = melted.set_index('time').drop(['year', 'month'], axis=1)
        sns.lineplot(data=melted)
        plt.show()

    @staticmethod
    def plot_random_non_random():
        """Demonstrate the low predictability of small effect sizes in situations of high variability."""
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