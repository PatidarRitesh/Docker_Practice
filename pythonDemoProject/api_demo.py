import requests

def fetch_random_cat_fact():
   url = "https://meowfacts.herokuapp.com/"

   try:
      response = requests.get(url)
      response.raise_for_status()

      fact = response.text
      return fact
   except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
   

if __name__ == "__main__":
    fact = fetch_random_cat_fact()
    print(fact)


    
