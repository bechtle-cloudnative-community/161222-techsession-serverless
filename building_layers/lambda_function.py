import requests

def lambda_handler(event, context):
  # Make sure a Pokemon name (or ID) was passed in the event object:
  pokemon = event.get("pokemon").lower()
  if not pokemon:
      return {
          "statusCode": 400,
          "body": "Please pass a Pokemon name or ID to get its weight!"
      }

  # If we have a pokemon name/ID passed in, try to get info for it:
  res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

  if res.status_code == 200:
      status_code = 200
      data = res.json()
      poke_weight = data["weight"]
      # get name of pokemon in case you passed ID
      poke_name = data["name"].capitalize()
      # json.dumps creates JSON in string format (json.dump() writes JSON to file)
    #   body = json.dumps(f"{poke_name} weigths {poke_weight} pounds! Did you know?")
      body = f"{poke_name} weights {poke_weight} pounds! Did you know?"
  else:
      status_code = res.status_code
      body = f"Error! Could not get information for {pokemon}"

  # Response object of Lamda function:
  return {
      "statusCode": status_code,
      "body": body
  }