import requests
import json

def post_request(url, doc, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.post(url, data=doc)
    except:
        # If any error occurs
        pass

def post_review(doc, **kwargs):
    result = post_request("https://2123c0db.eu-gb.apigw.appdomain.cloud/api/test2", doc, **kwargs)
    return result
reviews = {
  "reviews": [
    {
      "id": 1,
      "name": "Berkly Shepley",
      "dealership": 15,
      "review": "Total grid-enabled service-desk",
      "purchase": True,
      "purchase_date": "07/11/2020",
      "car_make": "Audi",
      "car_model": "A6",
      "car_year": 2010
    },
    {
      "id": 2,
      "name": "Gwenora Zettoi",
      "dealership": 23,
      "review": "Future-proofed foreground capability",
      "purchase": True,
      "purchase_date": "09/17/2020",
      "car_make": "Pontiac",
      "car_model": "Firebird",
      "car_year": 1995
    },
    {
      "id": 3,
      "name": "Lion Reames",
      "dealership": 29,
      "review": "Expanded global groupware",
      "purchase": True,
      "purchase_date": "10/20/2020",
      "car_make": "Mazda",
      "car_model": "MX-5",
      "car_year": 2003
    },
    {
      "id": 4,
      "name": "Iorgos Colley",
      "dealership": 13,
      "review": "Optional heuristic software",
      "purchase": False,
      "purchase_date": "03/28/2020",
      "car_make": "Kia",
      "car_model": "Spectra",
      "car_year": 2002
    },
    {
      "id": 5,
      "name": "Kissee Noirel",
      "dealership": 46,
      "review": "Diverse client-server success",
      "purchase": False,
      "purchase_date": "04/12/2020",
      "car_make": "GMC",
      "car_model": "Yukon",
      "car_year": 1992
    },
    {
      "id": 6,
      "name": "Derron Masedon",
      "dealership": 49,
      "review": "Re-contextualized leading edge software",
      "purchase": True,
      "purchase_date": "10/05/2020",
      "car_make": "Chevrolet",
      "car_model": "Aveo",
      "car_year": 2007
    },
    {
      "id": 7,
      "name": "Casey Pallasch",
      "dealership": 11,
      "review": "Synergistic cohesive budgetary management",
      "purchase": False,
      "purchase_date": "05/17/2020",
      "car_make": "Toyota",
      "car_model": "4Runner",
      "car_year": 1994
    },
    {
      "id": 8,
      "name": "Marmaduke Ashbe",
      "dealership": 17,
      "review": "Polarised asynchronous Graphical User Interface",
      "purchase": True,
      "purchase_date": "05/06/2020",
      "car_make": "BMW",
      "car_model": "530",
      "car_year": 2006
    },
    {
      "id": 9,
      "name": "Rudy Lougheed",
      "dealership": 41,
      "review": "Proactive bottom-line attitude",
      "purchase": True,
      "purchase_date": "07/05/2020",
      "car_make": "Cadillac",
      "car_model": "Escalade ESV",
      "car_year": 2003
    },
    {
      "id": 10,
      "name": "Inglebert Keech",
      "dealership": 22,
      "review": "Distributed transitional policy",
      "purchase": False,
      "purchase_date": "05/18/2020",
      "car_make": "Dodge",
      "car_model": "Ram Van 3500",
      "car_year": 1997
    },
    {
      "id": 11,
      "name": "Cosme Spolton",
      "dealership": 13,
      "review": "Reactive background implementation",
      "purchase": True,
      "purchase_date": "11/06/2020",
      "car_make": "Audi",
      "car_model": "A6",
      "car_year": 1999
    },
    {
      "id": 12,
      "name": "Olympe Chippindall",
      "dealership": 28,
      "review": "Cloned clear-thinking strategy",
      "purchase": True,
      "purchase_date": "10/14/2020",
      "car_make": "Saab",
      "car_model": "9-5",
      "car_year": 1999
    },
    {
      "id": 13,
      "name": "Alvan Hawthorne",
      "dealership": 42,
      "review": "Multi-channelled secondary archive",
      "purchase": True,
      "purchase_date": "07/25/2020",
      "car_make": "Lotus",
      "car_model": "Exige",
      "car_year": 2004
    },
    {
      "id": 14,
      "name": "Mildred Penhale",
      "dealership": 45,
      "review": "Customer-focused responsive moderator",
      "purchase": True,
      "purchase_date": "09/17/2020",
      "car_make": "Alfa Romeo",
      "car_model": "Spider",
      "car_year": 1994
    },
    {
      "id": 15,
      "name": "Lisabeth Izatson",
      "dealership": 27,
      "review": "Upgradable neutral matrix",
      "purchase": False,
      "purchase_date": "12/31/2020",
      "car_make": "BMW",
      "car_model": "550",
      "car_year": 2006
    },
    {
      "id": 16,
      "name": "Zaria Mattusevich",
      "dealership": 34,
      "review": "Seamless exuding budgetary management",
      "purchase": True,
      "purchase_date": "02/05/2021",
      "car_make": "Ford",
      "car_model": "F-Series",
      "car_year": 2007
    },
    {
      "id": 17,
      "name": "Bradley Summerell",
      "dealership": 45,
      "review": "Distributed intermediate methodology",
      "purchase": False,
      "purchase_date": "01/13/2021",
      "car_make": "BMW",
      "car_model": "Z3",
      "car_year": 2001
    },
    {
      "id": 18,
      "name": "Jacky Spurrior",
      "dealership": 40,
      "review": "Function-based non-volatile throughput",
      "purchase": True,
      "purchase_date": "06/20/2020",
      "car_make": "Ford",
      "car_model": "Taurus",
      "car_year": 1996
    },
    {
      "id": 19,
      "name": "Dalenna Foxen",
      "dealership": 2,
      "review": "Profound discrete definition",
      "purchase": False,
      "purchase_date": "11/14/2020",
      "car_make": "Mercedes-Benz",
      "car_model": "S-Class",
      "car_year": 2003
    },
    {
      "id": 20,
      "name": "Cathi Tschierasche",
      "dealership": 25,
      "review": "De-engineered static customer loyalty",
      "purchase": False,
      "purchase_date": "01/12/2021",
      "car_make": "BMW",
      "car_model": "M5",
      "car_year": 2008
    },
    {
      "id": 21,
      "name": "Jordan Surgood",
      "dealership": 31,
      "review": "Configurable attitude-oriented core",
      "purchase": True,
      "purchase_date": "10/23/2020",
      "car_make": "Mitsubishi",
      "car_model": "Lancer",
      "car_year": 2010
    },
    {
      "id": 22,
      "name": "Raphael Hicks",
      "dealership": 45,
      "review": "Universal real-time archive",
      "purchase": False,
      "purchase_date": "05/01/2020",
      "car_make": "Mitsubishi",
      "car_model": "Endeavor",
      "car_year": 2004
    },
    {
      "id": 23,
      "name": "Talya Crudgington",
      "dealership": 34,
      "review": "User-centric logistical product",
      "purchase": True,
      "purchase_date": "06/12/2020",
      "car_make": "Volkswagen",
      "car_model": "riolet",
      "car_year": 1993
    },
    {
      "id": 24,
      "name": "Nani Fullbrook",
      "dealership": 35,
      "review": "Object-based multi-state throughput",
      "purchase": False,
      "purchase_date": "08/30/2020",
      "car_make": "Mazda",
      "car_model": "RX-8",
      "car_year": 2009
    },
    {
      "id": 25,
      "name": "Audre Camplejohn",
      "dealership": 21,
      "review": "Assimilated encompassing parallelism",
      "purchase": False,
      "purchase_date": "03/06/2020",
      "car_make": "Volkswagen",
      "car_model": "New Beetle",
      "car_year": 2001
    },
    {
      "id": 26,
      "name": "Alexandra Thomke",
      "dealership": 46,
      "review": "Reduced explicit frame",
      "purchase": True,
      "purchase_date": "05/16/2020",
      "car_make": "Volkswagen",
      "car_model": "Passat",
      "car_year": 1987
    },
    {
      "id": 27,
      "name": "Valencia Eate",
      "dealership": 10,
      "review": "Fully-configurable local workforce",
      "purchase": True,
      "purchase_date": "04/09/2020",
      "car_make": "Ford",
      "car_model": "Explorer Sport Trac",
      "car_year": 2000
    },
    {
      "id": 28,
      "name": "Jackson Lexa",
      "dealership": 11,
      "review": "Profound web-enabled approach",
      "purchase": True,
      "purchase_date": "01/27/2021",
      "car_make": "Porsche",
      "car_model": "911",
      "car_year": 2007
    },
    {
      "id": 29,
      "name": "Andros Bamsey",
      "dealership": 22,
      "review": "Vision-oriented analyzing access",
      "purchase": True,
      "purchase_date": "06/17/2020",
      "car_make": "Honda",
      "car_model": "Odyssey",
      "car_year": 1996
    },
    {
      "id": 30,
      "name": "Thebault Pelos",
      "dealership": 18,
      "review": "Persevering asymmetric knowledge user",
      "purchase": True,
      "purchase_date": "05/23/2020",
      "car_make": "Mercedes-Benz",
      "car_model": "CL-Class",
      "car_year": 2010
    },
    {
      "id": 31,
      "name": "Olivie Howen",
      "dealership": 12,
      "review": "Optional next generation database",
      "purchase": True,
      "purchase_date": "11/13/2020",
      "car_make": "Pontiac",
      "car_model": "GTO",
      "car_year": 2004
    },
    {
      "id": 32,
      "name": "Ulberto Duerdin",
      "dealership": 22,
      "review": "Organized foreground methodology",
      "purchase": True,
      "purchase_date": "12/11/2020",
      "car_make": "Kia",
      "car_model": "Sedona",
      "car_year": 2006
    },
    {
      "id": 33,
      "name": "Rey Bannell",
      "dealership": 17,
      "review": "Up-sized mission-critical initiative",
      "purchase": True,
      "purchase_date": "10/31/2020",
      "car_make": "Pontiac",
      "car_model": "GTO",
      "car_year": 2004
    },
    {
      "id": 34,
      "name": "Editha Averies",
      "dealership": 9,
      "review": "Horizontal disintermediate methodology",
      "purchase": True,
      "purchase_date": "02/08/2021",
      "car_make": "Mazda",
      "car_model": "Mazda6",
      "car_year": 2013
    },
    {
      "id": 35,
      "name": "Cosimo Samples",
      "dealership": 10,
      "review": "Balanced intangible open architecture",
      "purchase": False,
      "purchase_date": "08/12/2020",
      "car_make": "Chevrolet",
      "car_model": "TrailBlazer",
      "car_year": 2004
    },
    {
      "id": 36,
      "name": "Gabriela Tourry",
      "dealership": 49,
      "review": "Re-contextualized asynchronous budgetary management",
      "purchase": True,
      "purchase_date": "10/18/2020",
      "car_make": "Chevrolet",
      "car_model": "Suburban 1500",
      "car_year": 2001
    },
    {
      "id": 37,
      "name": "Albrecht Collen",
      "dealership": 15,
      "review": "Pre-emptive heuristic solution",
      "purchase": True,
      "purchase_date": "10/10/2020",
      "car_make": "Lexus",
      "car_model": "IS F",
      "car_year": 2009
    },
    {
      "id": 38,
      "name": "Prudi Minchi",
      "dealership": 15,
      "review": "Mandatory homogeneous groupware",
      "purchase": True,
      "purchase_date": "01/06/2021",
      "car_make": "Saturn",
      "car_model": "L-Series",
      "car_year": 2001
    },
    {
      "id": 39,
      "name": "Donn Wick",
      "dealership": 17,
      "review": "Cross-group multimedia firmware",
      "purchase": False,
      "purchase_date": "04/29/2020",
      "car_make": "Buick",
      "car_model": "Terraza",
      "car_year": 2006
    },
    {
      "id": 40,
      "name": "Ronda Peppin",
      "dealership": 42,
      "review": "Right-sized optimizing implementation",
      "purchase": False,
      "purchase_date": "09/06/2020",
      "car_make": "Mazda",
      "car_model": "B-Series",
      "car_year": 2005
    },
    {
      "id": 41,
      "name": "Frank Edmenson",
      "dealership": 23,
      "review": "Advanced motivating benchmark",
      "purchase": True,
      "purchase_date": "12/20/2020",
      "car_make": "Isuzu",
      "car_model": "Rodeo",
      "car_year": 1999
    },
    {
      "id": 42,
      "name": "Sarita Dionisio",
      "dealership": 44,
      "review": "Pre-emptive modular extranet",
      "purchase": True,
      "purchase_date": "04/13/2020",
      "car_make": "Plymouth",
      "car_model": "Voyager",
      "car_year": 1998
    },
    {
      "id": 43,
      "name": "Glennis Hackett",
      "dealership": 17,
      "review": "Triple-buffered upward-trending conglomeration",
      "purchase": False,
      "purchase_date": "08/20/2020",
      "car_make": "Nissan",
      "car_model": "Altima",
      "car_year": 2008
    },
    {
      "id": 44,
      "name": "Gerardo Kernaghan",
      "dealership": 39,
      "review": "Sharable secondary model",
      "purchase": False,
      "purchase_date": "07/06/2020",
      "car_make": "Isuzu",
      "car_model": "i-350",
      "car_year": 2006
    },
    {
      "id": 45,
      "name": "Jerri Largen",
      "dealership": 14,
      "review": "Polarised client-driven challenge",
      "purchase": False,
      "purchase_date": "05/29/2020",
      "car_make": "Volkswagen",
      "car_model": "Passat",
      "car_year": 1996
    },
    {
      "id": 46,
      "name": "Reece Fronczak",
      "dealership": 2,
      "review": "Polarised client-server methodology",
      "purchase": True,
      "purchase_date": "07/04/2020",
      "car_make": "BMW",
      "car_model": "760",
      "car_year": 2005
    },
    {
      "id": 47,
      "name": "Lorilee Veasey",
      "dealership": 12,
      "review": "Organic user-facing paradigm",
      "purchase": True,
      "purchase_date": "02/08/2021",
      "car_make": "Maybach",
      "car_model": "57",
      "car_year": 2012
    },
    {
      "id": 48,
      "name": "Rupert Silberschatz",
      "dealership": 6,
      "review": "Intuitive coherent monitoring",
      "purchase": True,
      "purchase_date": "06/10/2020",
      "car_make": "Saturn",
      "car_model": "S-Series",
      "car_year": 2001
    },
    {
      "id": 49,
      "name": "Jo-anne Szwandt",
      "dealership": 7,
      "review": "Self-enabling maximized focus group",
      "purchase": True,
      "purchase_date": "01/26/2021",
      "car_make": "Mercedes-Benz",
      "car_model": "CL-Class",
      "car_year": 1999
    },
    {
      "id": 50,
      "name": "Sherwood Brogan",
      "dealership": 34,
      "review": "Stand-alone holistic model",
      "purchase": False,
      "purchase_date": "05/10/2020",
      "car_make": "Cadillac",
      "car_model": "DeVille",
      "car_year": 1995
    }
  ]
}

for review in reviews["reviews"]:
    post_review(review)

