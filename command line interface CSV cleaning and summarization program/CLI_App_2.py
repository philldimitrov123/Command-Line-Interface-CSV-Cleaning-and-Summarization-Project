import pandas as pd

df = pd.read_csv("cleaned_gdp_data.csv")

def get_summary_statistics(df):
    name = input("""
╔════════════════════════════════════════════════════════════════╗
║         Welcome to the GDP per Capita Database!                ║
╚════════════════════════════════════════════════════════════════╝

This database holds historic GDP per capita data from 1960 to 2024!

Enter the country name to get GDP per capita summary: """
                 ).title()
    
    if name not in dict(df['Country Name']).values():
        raise ValueError("Please enter a valid country name")
    
    country = df[df['Country Name'] == name]
    mean_gdp = country.iloc[:,6:].mean(axis=1)
    median_gdp = country.iloc[:,6:].median(axis=1)
    max = country.iloc[:,6:].max(axis=1)
    min = country.iloc[:,6:].min(axis=1)
    cagr = (country.iloc[:, -1] / country.iloc[:, 6]) ** (1/(len(country.columns) - 1)) - 1
    best_year = ""
    worst_year = ""
    
    for item in country.iloc[:,6:].items():
        if float(item[1]) == float(max):
            best_year = item[0]
        if float(item[1]) == float(min):
            worst_year = item[0]


    print(f"""
    *** All Values in US Dollars ***            
    Your Country: {name}   
    {name}'s mean GDP per capita: ${(round(float(mean_gdp), 2))}
    {name}'s median GDP per capita: ${round(float(median_gdp), 2)}
    {name}'s GDP per capita range: ${round(float(min), 2)} - ${round(float(max), 2)} 
    {name}'s CAGR of GDP per capita: {round(float(cagr) * 100, 2)} %
    {name}'s best year: {best_year}
    {name}'s worst year: {worst_year}
    """)

get_summary_statistics(df)



    

