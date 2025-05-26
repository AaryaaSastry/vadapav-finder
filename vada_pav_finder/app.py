from flask import Flask, request, jsonify, render_template
import googlemaps

app = Flask(__name__)

# Replace with your actual Google Maps API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

def get_vada_pav_places(location, radius=1000):
    search_query = 'vada pav'
    places_result = gmaps.places_nearby(location=location, radius=radius, keyword=search_query)
    vada_pav_places = []
    for place in places_result['results']:
        place_details = {
            'name': place['name'],
            'address': place['vicinity'],
            'rating': place.get('rating', 'N/A'),
            'user_ratings_total': place.get('user_ratings_total', 'N/A'),
            'place_id': place['place_id']
        }
        vada_pav_places.append(place_details)
    return vada_pav_places

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    location = f"{lat},{lng}"
    places = get_vada_pav_places(location)
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)
