import requests
import json

city = {"Ghaziabad": 6146, "New Delhi": 2624, "Faridabad": 2944, "Gurugram":2951, "Noida":6403, "Ahmedabad":2690, "Pune":4378, "Kolkata":6903, "Hyderabad":2060, "Chennai":5136, "Bangalore":3327, "Mumbai":4320}

def make_request(page, groupstart, code):
    url = "https://www.magicbricks.com/mbsrp/propertySearch.html"
    params = {
        "editSearch": "Y",
        "category": "S",
        "propertyType": "10002,10003,10021,10022,10001,10017",
        "bedrooms": "11701,11702",
        "city": code,
        "page": page,
        "groupstart": groupstart,
        "offset": "0",
        "maxOffset": "710",
        "sortBy": "premiumRecent",
        "postedSince": "-1",
        "pType": "10002,10003,10021,10022,10001,10017",
        "isNRI": "N",
        "multiLang": "en",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve page {page}, groupstart {groupstart}")
        return None



for city_name, city_code in city.items():
    # Storing results in a list
    results = {}

    # Starting from page 2 and groupstart 30, repeating for subsequent pages and groupstarts
    for i in range(2, 1000):  # Assuming you want to go up to page 7
        page = i
        groupstart = (page - 1) * 30
        result = make_request(page, groupstart, city_code)
        if result:
            result = json.loads(result)
            results[page] = result
            # print(result)
        print(f"Page {page}, groupstart {groupstart} done")

    # save the results to a file as json
    with open(f"results{city_name}.json", "w") as f:
        json.dump(results, f)
