import pandas as pd

cities = ['Ghaziabad', 'Noida', 'Gurugram', 'Faridabad', 'New_Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
for city in cities:
    data = pd.read_json(f'results{city}.json')

    data.drop(['societyExpertResultList','nsrResultList'], axis=0, inplace=True)

    df = data.iloc[0,:]

    pages = len(df)
    house_per_page = 30
    house_dataset = []

    for i in range(pages):
        for j in range(house_per_page):
            house = df.iloc[i][j]
            # add house to dataset
            house_dataset.append(house)

    house_data = pd.DataFrame(house_dataset)

    house_data["city"] = city

    # save data in postgreSQL database name "house_data" and table name "Ghaziabad"
    from sqlalchemy import create_engine
    import json
    from psycopg2.extras import Json
    from psycopg2 import sql
    engine = create_engine('postgresql://postgres:root@localhost:5432/House_Data')

    # Replace all NaN values with None
    house_data = house_data.where(pd.notnull(house_data), None)

    # Convert the house_data dataframe to a list of tuples
    house_data_tuples = [tuple(x) for x in house_data.values]

    # Import simplejson
    import simplejson as json

    # Convert each tuple to a JSON string
    house_data_json = [json.dumps(x, ignore_nan=True) for x in house_data_tuples]

    # Establish a connection
    conn = engine.raw_connection()

    # Create a cursor object
    cur = conn.cursor()

    # Create the table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {city} (data JSONB)"
    cur.execute(create_table_query)

    # Commit the transaction
    conn.commit()

    # Insert the JSON strings into the database
    insert_query = f"INSERT INTO {city} (data) VALUES (%s)"
    cur.executemany(insert_query, [(x,) for x in house_data_json])

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    print(f"Data saved in postgreSQL database {city}")