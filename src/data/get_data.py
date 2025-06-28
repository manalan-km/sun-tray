from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_sunset_quality(api_key: str) -> str: 
    
    latitude =-38.15
    longitude = 144.35809
    date="2025-06-25"
    type="sunset"
    
    api = f"https://api.sunsethue.com/event?latitude={latitude}&longitude={longitude}&date={date}&type={type}"

    headers ={'x-api-key':api_key}
    
    response = requests.get(api,headers=headers)
    
    if response.ok:
        return response.json()['data']['quality_text']
    
    print(f"Error with the request: {response.status_code}: {response.json()}")
        
    
def get_image() -> str:
    
    key = os.getenv('SUNSET_HUE_API_KEY')
    
    sunset_quality = get_sunset_quality(key)
    
    image_path = ''
    
    print(f"Sunset quality: {sunset_quality}")
    
    match sunset_quality.lower():
        case 'poor':
            image_path = 'src/sunset-grey.png'
        case 'fair':
            image_path = 'src/sunset-blue.png'
        case 'good':
            image_path = 'src/sunset-green.png'
        case 'great':
            image_path = 'src/sunset-yellow.png'
        case 'excellent':
            image_path = 'src/sunset.png'
        case _:
            image_path = 'src/sunrise.png'
          
    return  image_path