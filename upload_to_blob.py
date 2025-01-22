from azure.storage.blob import BlobServiceClient

# Yhdistä Blob Storageen
connect_str = "<Kopioitu Connection String>"  # Vaihda tähän Connection String Access Keys -asetuksista
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Kontin nimi ja tiedoston nimi
container_name = "football-data"  # Vaihda oman kontin nimeksi
blob_name = "data.json"  # Vaihda ladattavan tiedoston nimi
local_file_path = "local_data.json"  # Tiedoston sijainti omalla koneellasi

# Lataa tiedosto konttiin
try:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"File '{local_file_path}' uploaded to Blob Storage container '{container_name}' as '{blob_name}'.")
except Exception as ex:
    print(f"An error occurred: {ex}")
