import streamlit as st
import pandas as pd
st.title('House Price Prediction Web Application')
import pickle 

# Step 1: load the pickled model
model = open('project.pickle','rb')
project=pickle.load(model)
model.close()

# Step 2: create a UI for front end user
state = st.sidebar.selectbox('State',['ca', 'co', 'ct', 'dc', 'fl', 'de', 'ga', 'hi', 'id', 'il', 'in',
       'ia', 'ks', 'ky', 'la', 'me', 'mi', 'md', 'ma', 'mn', 'ms', 'nc',
       'mo', 'mt', 'ne', 'nv', 'nj', 'nm', 'ny', 'nh', 'oh', 'nd', 'ok',
       'or', 'pa', 'ri', 'sc', 'tn', 'sd', 'tx', 'ut', 'va', 'vt', 'wa',
       'wv', 'wi', 'wy', 'al', 'az', 'ak', 'ar'])
region=st.sidebar.selectbox('Region',('reno / tahoe', 'sacramento', 'boulder', 'visalia-tulare',
       'santa barbara', 'SF bay area', 'siskiyou county',
       'ventura county', 'san diego', 'san luis obispo', 'stockton',
       'santa maria', 'susanville', 'colorado springs', 'yuba-sutter',
       'denver', 'northwest CT', 'fort collins / north CO',
       'western slope', 'eastern CT', 'hartford', 'new haven',
       'washington, DC', 'high rockies', 'pueblo', 'daytona beach',
       'ft myers / SW florida', 'gainesville', 'jacksonville', 'ocala',
       'eastern CO', 'heartland florida', 'delaware', 'lakeland',
       'florida keys', 'north central FL', 'orlando', 'panama city',
       'pensacola', 'sarasota-bradenton', 'south florida',
       'okaloosa / walton', 'space coast', 'tallahassee',
       'tampa bay area', 'atlanta', 'augusta', 'brunswick', 'athens',
       'treasure coast', 'albany', 'st augustine',
       'macon / warner robins', 'columbus', 'northwest GA',
       'savannah / hinesville', 'hawaii', 'boise', 'east idaho',
       'statesboro', "spokane / coeur d'alene", 'valdosta',
       'bloomington-normal', 'champaign urbana', 'chicago', 'twin falls',
       'decatur', 'la salle co', 'quad cities, IA/IL', 'st louis, MO',
       'peoria', 'evansville', 'springfield', 'bloomington',
       'lewiston / clarkston', 'pullman / moscow', 'indianapolis',
       'fort wayne', 'rockford', 'south bend / michiana', 'ames',
       'richmond', 'southern illinois', 'mattoon-charleston',
       'muncie / anderson', 'western IL', 'lafayette / west lafayette',
       'kokomo', 'terre haute', 'cedar rapids', 'des moines',
       'omaha / council bluffs', 'wichita', 'fort dodge', 'lawrence',
       'salina', 'sioux city', 'bowling green', 'lexington',
       'eastern kentucky', 'iowa city', 'louisville', 'dubuque',
       'baton rouge', 'waterloo / cedar falls', 'manhattan', 'western KY',
       'topeka', 'lafayette', 'monroe', 'mason city', 'new orleans',
       'kansas city, MO', 'southeast IA', 'lake charles', 'southeast KS',
       'huntington-ashland', 'northwest KS', 'southwest KS', 'shreveport',
       'central louisiana', 'houma', 'owensboro', 'maine', 'lansing',
       'annapolis', 'baltimore', 'frederick', 'southern maryland',
       'boston', 'south coast', 'western massachusetts',
       'worcester / central MA', 'western maryland', 'ann arbor',
       'battle creek', 'detroit metro', 'holland', 'cumberland valley',
       'flint', 'kalamazoo', 'muskegon', 'saginaw-midland-baycity',
       'upper peninsula', 'eastern shore', 'cape cod / islands',
       'grand rapids', 'bemidji', 'central michigan', 'northern michigan',
       'jackson', 'southwest michigan', 'the thumb', 'port huron',
       'brainerd', 'duluth / superior', 'fargo / moorhead',
       'minneapolis / st paul', 'rochester', 'gulfport / biloxi',
       'st cloud', 'hattiesburg', 'asheville', 'north mississippi',
       'joplin', 'kirksville', 'mankato', 'southwest MS',
       'columbia / jeff city', 'southwest MN', 'st joseph', 'charlotte',
       'boone', 'billings', 'missoula', 'fayetteville', 'eastern NC',
       'greensboro', 'raleigh / durham / CH', 'hickory / lenoir',
       'lake of the ozarks', 'meridian', 'southeast missouri',
       'kansas city', 'st louis', 'bozeman', 'eastern montana',
       'kalispell', 'great falls', 'helena', 'butte', 'outer banks',
       'wilmington', 'winston-salem', 'lincoln', 'las vegas',
       'north platte', 'central NJ', 'north jersey', 'jersey shore',
       'south jersey', 'albuquerque', 'buffalo', 'ithaca', 'farmington',
       'long island', 'hudson valley', 'syracuse',
       'plattsburgh-adirondacks', 'catskills', 'watertown',
       'grand island', 'santa fe / taos', 'scottsbluff / panhandle',
       'new york city', 'binghamton', 'utica-rome-oneida',
       'new hampshire', 'elko', 'clovis / portales', 'finger lakes',
       'chautauqua', 'elmira-corning', 'las cruces', 'roswell / carlsbad',
       'glens falls', 'potsdam-canton-massena', 'oneonta',
       'twin tiers NY/PA', 'cincinnati', 'north dakota', 'akron / canton',
       'bismarck', 'grand forks', 'dayton / springfield', 'cleveland',
       'lima / findlay', 'toledo', 'northern panhandle', 'oklahoma city',
       'zanesville / cambridge', 'ashtabula', 'lawton', 'chillicothe',
       'texoma', 'tulsa', 'bend', 'corvallis/albany', 'tuscarawas co',
       'east oregon', 'eugene', 'medford-ashland', 'oregon coast',
       'portland', 'mansfield', 'stillwater', 'parkersburg-marietta',
       'northwest OK', 'sandusky', 'youngstown', 'fort smith, AR',
       'klamath falls', 'salem', 'roseburg', 'harrisburg', 'philadelphia',
       'erie', 'pittsburgh', 'lehigh valley', 'rhode island',
       'scranton / wilkes-barre', 'altoona-johnstown', 'reading',
       'charleston', 'williamsport', 'lancaster', 'state college',
       'columbia', 'greenville / upstate', 'myrtle beach', 'hilton head',
       'chattanooga', 'poconos', 'clarksville', 'meadville',
       'south dakota', 'cookeville', 'york', 'sioux falls / SE SD',
       'florence', 'northeast SD', 'rapid city / west SD',
       'pierre / central SD', 'knoxville', 'memphis', 'nashville',
       'amarillo', 'austin', 'college station', 'lubbock',
       'dallas / fort worth', 'abilene', 'el paso', 'corpus christi',
       'del rio / eagle pass', 'galveston', 'houston',
       'killeen / temple / ft hood', 'laredo', 'mcallen / edinburg',
       'tri-cities', 'brownsville', 'beaumont / port arthur',
       'deep east texas', 'odessa / midland', 'waco', 'san antonio',
       'san angelo', 'san marcos', 'tyler / east TX', 'victoria',
       'wichita falls', 'provo / orem', 'ogden-clearfield',
       'salt lake city', 'fredericksburg', 'charlottesville', 'lynchburg',
       'norfolk / hampton roads', 'roanoke', 'winchester', 'texarkana',
       'southwest TX', 'vermont', 'logan', 'st george', 'danville',
       'harrisonburg', 'new river valley', 'southwest VA', 'bellingham',
       'kennewick-pasco-richland', 'seattle-tacoma', 'moses lake',
       'olympic peninsula', 'yakima', 'morgantown', 'madison',
       'wenatchee', 'skagit / island / SJI', 'milwaukee',
       'west virginia (old)', 'wausau', 'janesville', 'kenosha-racine',
       'eastern panhandle', 'southern WV', 'green bay', 'la crosse',
       'wyoming', 'appleton-oshkosh-FDL', 'eau claire', 'sheboygan',
       'northern WI', 'auburn', 'birmingham', 'phoenix',
       'gadsden-anniston', 'huntsville / decatur', 'dothan', 'mobile',
       'montgomery', 'florence / muscle shoals', 'tuscaloosa',
       'anchorage / mat-su', 'fairbanks', 'flagstaff / sedona', 'tucson',
       'little rock', 'prescott', 'yuma', 'bakersfield',
       'fresno / madera', 'hanford-corcoran', 'humboldt county',
       'inland empire', 'los angeles', 'kenai peninsula',
       'southeast alaska', 'mohave county', 'fort smith', 'jonesboro',
       'show low', 'gold country', 'sierra vista', 'chico',
       'imperial county', 'modesto', 'orange county', 'mendocino county',
       'merced', 'palm springs', 'monterey bay', 'redding'))
sqfeet = st.sidebar.slider('Size of the house you are looking for (in sqfeet)',40,3000,25)
beds=st.sidebar.slider('Select number of beds you want',1,100,1)
baths=st.sidebar.slider('Select number of baths you want',1,100,1)
Type=st.sidebar.selectbox('Select the type of the house',['apartment', 'condo', 'house', 'duplex', 'townhouse', 'loft',
       'manufactured', 'cottage/cabin', 'flat', 'in-law', 'land',
       'assisted living'])
Lat = st.sidebar.slider('Latitude of the house location you prefer',-50,120,2)
Long = st.sidebar.slider('Longitude of the house location you prefer',-200,100,2)
parking_options = st.sidebar.radio('Parking type',('carport' ,'attached garage','off-street parking', 'detached garage',
 'street parking', 'no parking' ,'valet parking'))
price_per_sqft = st.sidebar.slider('What is you expectation of price per sqfeet',0,100,2)
#bed_and_bath = st.sidebar.slider('How many beds and baths you want in your house',2,20,1)
#amenities = st.sidebar.radio('Whether you prefer any amenities from the owner (1-Yes/ 0-No)',(1,0))
laundry = st.sidebar.radio('Select Laundry type',('w/d in unit', 'w/d hookups', 'laundry in bldg', 'laundry on site','no laundry on site'))
cats_allowed=st.sidebar.radio('You have cat? (1-Yes/ 0-No)',(1,0))
dogs_allowed= st.sidebar.radio('You have dog? (1-Yes/ 0-No)',(1,0))
smoking=st.sidebar.radio('You want a house where smoking is allowed? (1-Yes/ 0-No)',(1,0))
wheelchair=st.sidebar.radio('Whether you want a house with wheelchair access facility? (1-Yes/ 0-No)',(1,0))
electric_vehicle=st.sidebar.radio('Whether you want a electric vehicle charging facility? (1-Yes/ 0-No)',(1,0))
furnished=st.sidebar.radio('Whether you want a furnished house? (1-Yes/ 0-No)',(1,0))
# Step 3: Change user input as models input data
data={
    'state':state,
    'region':region,
    'sqfeet':sqfeet,
    'beds':beds,
    'baths':baths,
    'type':Type,
    'lat':Lat,
    'long':Long,
    'parking_options':parking_options,
    'price_per_sqft':price_per_sqft,
    #'Bed and Bath':bed_and_bath,
    #'Amenities':amenities,
   'laundry_options':laundry,
   'cats_allowed':cats_allowed,
    'dogs_allowed':dogs_allowed,
    'smoking_allowed':smoking,
    'wheelchair_access':wheelchair,
    'electric_vehicle_charge':electric_vehicle,
    'comes_furnished':furnished

}
input_data = pd.DataFrame([data])

# Step 4: get the prediction and print result
predictions = project.predict(input_data)[0]
if st.sidebar.button('Predict'):
    st.write('The price is {} USD'.format(predictions))
