import pandas as pd
from ftfy import fix_text

# Load the XLSX file
df = pd.read_excel("Transfer-players-ToClubs.xlsx", engine="openpyxl")

# Apply encoding fix to all columns
df = df.applymap(lambda x: fix_text(str(x)) if isinstance(x, str) else x)

# Save the cleaned file
df.to_excel("cleaned_file.xlsx", index=False, engine="openpyxl")

print("Encoding issues fixed! Cleaned file saved as 'cleaned_file.xlsx'")
