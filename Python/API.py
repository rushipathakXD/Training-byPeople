import requests

def get_data_from_api():
    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url)
    data = response.json()

    if(data["success"] and "data" in data):
        dog_data = data["data"]
        bred_purpose = dog_data["bred_for"]
        dog_height = dog_data["height"]["metric"]

        return bred_purpose, dog_height
    
    else:
        raise Exception("Failed to retrieve data from API")
    
def main():
    try:
        bred_purpose, dog_height = get_data_from_api()
        print(f"Bred Purpose: {bred_purpose}")
        print(f"Dog Height (Metric): {dog_height}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":    
    main()