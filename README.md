# ETL INDIAN House Price Data

A comprehensive ETL (Extract, Transform, Load) pipeline for Indian residential property data scraped from MagicBricks.com. This project collects, cleans, and stores house pricing data from major Indian cities for academic research and personal projects.

## 📊 Project Overview

This repository contains a complete data pipeline that:
- **Extracts** real estate data from MagicBricks.com using web scraping
- **Transforms** raw JSON data into structured, clean datasets
- **Loads** processed data into a PostgreSQL database for analysis

The dataset covers residential properties (apartments, flats, and houses) across 12 major Indian metropolitan cities.

## 🏙️ Cities Covered

- **NCR Region**: Ghaziabad, New Delhi, Faridabad, Gurugram, Noida
- **West India**: Ahmedabad, Mumbai, Pune
- **South India**: Bangalore, Chennai, Hyderabad
- **East India**: Kolkata

## ✨ Features

- **Automated Data Scraping**: Python scripts to fetch property listings from MagicBricks API
- **Data Cleaning Pipelines**: Jupyter notebooks for each city with comprehensive cleaning operations
- **PostgreSQL Integration**: Structured database storage with JSONB support
- **Comprehensive Dataset**: Multiple property attributes including price, area, location, amenities, etc.
- **SQL Dump Available**: Pre-populated database export (`House_data.sql`) for quick setup

## 📁 Repository Structure

```
ETL-INDIAN-House-Price-Data/
├── Data Scraping & Cleaning/
│   ├── magic.py                          # Web scraping script for MagicBricks API
│   ├── save2db.py                        # Database insertion script
│   ├── HouseDataCleaningAhmedabad.ipynb  # Data cleaning notebook for Ahmedabad
│   ├── HouseDataCleaningBangalore.ipynb  # Data cleaning notebook for Bangalore
│   ├── HouseDataCleaningFaridabad.ipynb  # Data cleaning notebook for Faridabad
│   ├── HouseDataCleaningGhaziabad.ipynb  # Data cleaning notebook for Ghaziabad
│   ├── HouseDataCleaningGurugram.ipynb   # Data cleaning notebook for Gurugram
│   ├── HouseDataCleaningHyderabad.ipynb  # Data cleaning notebook for Hyderabad
│   ├── HouseDataCleaningKolkata.ipynb    # Data cleaning notebook for Kolkata
│   ├── HouseDataCleaningMumbai.ipynb     # Data cleaning notebook for Mumbai
│   ├── HouseDataCleaningNew_Delhi.ipynb  # Data cleaning notebook for New Delhi
│   ├── HouseDataCleaningNoida.ipynb      # Data cleaning notebook for Noida
│   └── HouseDataCleaningPune.ipynb       # Data cleaning notebook for Pune
├── House_data.sql                        # PostgreSQL database dump
├── Read_SQL_USING_PANDAS.ipynb          # Example notebook for querying the database
└── README.md                             # Project documentation
```

## 🔧 Prerequisites

- Python 3.7+
- PostgreSQL 12+
- Jupyter Notebook/JupyterLab

### Required Python Packages

```bash
pip install requests pandas psycopg2 sqlalchemy simplejson
```

## 🚀 Getting Started

### Option 1: Using the Pre-populated Database (Recommended)

1. **Install PostgreSQL** and create a database:
   ```sql
   CREATE DATABASE House_Data;
   ```

2. **Import the SQL dump**:
   ```bash
   psql -U postgres -d House_Data < House_data.sql
   ```

3. **Query the data** using the provided notebook:
   - Open `Read_SQL_USING_PANDAS.ipynb`
   - Update the connection string with your PostgreSQL credentials
   - Run the cells to explore the data

### Option 2: Scraping Fresh Data

1. **Scrape data from MagicBricks**:
   ```bash
   cd "Data Scraping & Cleaning"
   python magic.py
   ```
   This will create JSON files for each city (`resultsGhaziabad.json`, `resultsNoida.json`, etc.)

2. **Clean and process the data**:
   - Open the respective city's Jupyter notebook (e.g., `HouseDataCleaningBangalore.ipynb`)
   - Run all cells to clean and process the data
   - The notebook will extract relevant features and prepare data for database insertion

3. **Load data into PostgreSQL**:
   ```bash
   python save2db.py
   ```
   Make sure to update the database connection string in `save2db.py`:
   ```python
   engine = create_engine('postgresql://postgres:YOUR_PASSWORD@localhost:5432/House_Data')
   ```

## 📊 Data Schema

Each city table contains the following attributes:

| Column | Type | Description |
|--------|------|-------------|
| possStatusD | text | Possession status (Ready to Move, Under Construction, etc.) |
| price | integer | Property price in INR |
| priceD | text | Formatted price display |
| powerStatusD | text | Power backup availability |
| carpetArea | double precision | Carpet area in sq.ft |
| coveredArea | double precision | Covered/Built-up area in sq.ft |
| sqFtPrice | double precision | Price per square foot |
| furnishedD | text | Furnishing status (Furnished, Semi-Furnished, Unfurnished) |
| balconiesD | double precision/text | Number of balconies |
| bathD | double precision/text | Number of bathrooms |
| bedroomD | double precision/text | Number of bedrooms (BHK) |
| parkingD | text | Parking availability |
| facingD | text | Property facing direction |
| floors | double precision/text | Floor number |
| ctName | text | Locality/Area name |
| carpAreaUnit | text | Unit of area measurement |
| areaPercent | double precision | Area percentage |

*Note: Some columns may vary slightly between cities based on data availability*

## 💡 Usage Examples

### Connecting to Database with Pandas

```python
import pandas as pd
from sqlalchemy import create_engine

# Create database connection
engine = create_engine('postgresql://postgres:root@localhost:5432/House_Data')

# Read data from a specific city
df_bangalore = pd.read_sql_table('Bangalore', engine)

# Query specific properties
query = "SELECT * FROM Bangalore WHERE price < 5000000 AND bedroomD = '2'"
affordable_2bhk = pd.read_sql_query(query, engine)
```

### Analyzing Data

```python
# Get average price per city
cities = ['Bangalore', 'Mumbai', 'Delhi', 'Pune']
for city in cities:
    df = pd.read_sql_table(city, engine)
    print(f"{city} - Average Price: ₹{df['price'].mean():,.2f}")
```

## 📈 Data Analysis Potential

This dataset can be used for:
- **Price Prediction Models**: Build machine learning models to predict house prices
- **Market Analysis**: Analyze real estate trends across different cities
- **Location Intelligence**: Study price variations by locality
- **Feature Impact Analysis**: Understand how amenities affect pricing
- **Comparative Studies**: Compare real estate markets across Indian metros

## ⚠️ Important Notes

- **Data Source**: All data is scraped from MagicBricks.com
- **Usage Rights**: This dataset is for **academic and personal projects ONLY**
- **Not for Commercial Use**: Commercial use of this data is strictly prohibited
- **Data Freshness**: Web scraping may need to be updated periodically as website structure changes
- **Ethical Scraping**: Please respect the website's robots.txt and terms of service

## 🛠️ Troubleshooting

### Connection Issues
If you face database connection errors, ensure:
- PostgreSQL service is running
- Database `House_Data` exists
- Credentials in connection string are correct
- Port 5432 is not blocked by firewall

### Scraping Issues
If `magic.py` fails:
- Check internet connectivity
- Verify MagicBricks API endpoint is accessible
- API structure may have changed (update the script accordingly)

## 📝 License

This project is open-source and available for academic and personal use. The data is scraped from a third-party website and should be used responsibly.

**Disclaimer**: This dataset is provided "as is" without any warranty. The authors are not responsible for any misuse of the data or violations of the source website's terms of service.

## 🤝 Contributing

Contributions are welcome! If you'd like to:
- Add data for more cities
- Improve data cleaning pipelines
- Add new analysis notebooks
- Fix bugs or improve documentation

Please feel free to submit a pull request.

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

**Note**: Always verify and validate the data before using it for any critical analysis or decision-making purposes.
