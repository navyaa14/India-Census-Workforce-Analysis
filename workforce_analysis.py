import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Excel
df = pd.read_excel("datasetcensus.xlsx", sheet_name="PCA")

# Create folder
output_dir = "output_visualizations"
os.makedirs(output_dir, exist_ok=True)

# Select relevant columns
df = df.iloc[:, [91, 92, 97, 98]]
df.columns = ['Marginal_Workers_Male', 'Marginal_Workers_Female',
              'Non_Working_Pop_Male', 'Non_Working_Pop_Female']
df.dropna(inplace=True)

# Bar Chart: Total Non-working
totals = {
    'Male': df['Non_Working_Pop_Male'].sum(),
    'Female': df['Non_Working_Pop_Female'].sum()
}
plt.bar(totals.keys(), totals.values(), color=['blue', 'pink'])
plt.title('Total Non-Working Population by Gender')
plt.ylabel('Population')
plt.savefig(f"{output_dir}/non_working_comparison.png")
plt.close()

# Histogram
plt.hist(df['Non_Working_Pop_Male'], bins=30, alpha=0.7, label='Male', color='blue')
plt.hist(df['Non_Working_Pop_Female'], bins=30, alpha=0.7, label='Female', color='pink')
plt.title('Distribution of Non-Working Population')
plt.xlabel('Population Count')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.savefig(f"{output_dir}/non_working_distribution.png")
plt.close()

print("✅ Analysis complete. Visualizations saved in 'output_visualizations/' folder.")
