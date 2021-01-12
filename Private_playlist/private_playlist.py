#BQBLUaVC44OmOFeMBt81ijsb7YopwNCcHNht0EZo9b065VHkFXt_G_kKdF5IpS9YATHjAdNUSXKHdCsWQmgU0h83toOlUbUzP3hE9GX_H68VqBbFb0yC-GL0PIW3hFW6NQPhuSBLC6lLtHbaX2rQ6gbFN7R1Ooau5vSlzPdvq8nMWN8XbgFmaGJ2iGcGZK4
import requests
endpoint_url = "GET https://api.spotify.com/v1/recommendations"

limit=10
market="ES"
seed_genres="classical"
target_danceability=0.9

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":"BQBLUaVC44OmOFeMBt81ijsb7YopwNCcHNht0EZo9b065VHkFXt_G_kKdF5IpS9YATHjAdNUSXKHdCsWQmgU0h83toOlUbUzP3hE9GX_H68VqBbFb0yC-GL0PIW3hFW6NQPhuSBLC6lLtHbaX2rQ6gbFN7R1Ooau5vSlzPdvq8nMWN8XbgFmaGJ2iGcGZK4"})

json_response = response.json()

for i in json_response['tracks']:
            uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")
