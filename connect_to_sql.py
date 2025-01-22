import pyodbc

server = 'footballservervk20.database.windows.net'
database = 'footballstatsdbvk20'
username = 'CloudSA77c31788'
password = 'Jalkapallo20@'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")

cursor = conn.cursor()

cursor.execute('''
    IF OBJECT_ID('PlayerStats', 'U') IS NULL
    BEGIN
    CREATE TABLE PlayerStats (
    PlayerID INT PRIMARY KEY,
    PlayerName NVARCHAR(100),
    Team NVARCHAR(100),
    Goals INT,
    Assists INT
    )
    END
''')

# Lisää tietoa tauluun
# cursor.execute('''
#     INSERT INTO PlayerStats (PlayerID, PlayerName, Team, Goals, Assists)
#     VALUES
#     (1, 'Lionel Messi', 'Miami', 30, 20),
#     (2, 'Cristiano Ronaldo', 'Al-Nassr', 25, 10),
#     (3, 'Erling Haaland', 'Manchester City', 35, 15)
# ''')

# Hae tiedot taulusta
cursor.execute('SELECT * FROM PlayerStats')
rows = cursor.fetchall()

print("PlayerStats table data:")
for row in rows:
    print(row)

conn.commit()
print("Table 'PlayerStats' created successfully!")

conn.close()

