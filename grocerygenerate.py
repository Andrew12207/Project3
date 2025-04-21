import random
import pandas as pd

random.seed(456)


def generate_store_prices(base_price):
    """Generate prices for all stores based on a single base price."""
    return {
        "Store A": round(base_price * 0.8, 2),  # lowest prices
        "Store B": round(base_price, 2),        # average prices
        "Store C": round(base_price * 1.2, 2),  # highest prices
        "Store D": round(random.uniform(0.99, 99.99), 2)  # random under $100
    }

# random brand prefix names to up the product count
brand_map = {
    "Bakery": ["DailyBread", "Baker's Lane", "Hearth & Grain", "Rising Dough", ""],
    "Beverages": ["CampusCafé", "ThirstQuench", "SipSational", "PurePour", ""],
    "Frozen Food": ["FrostyBite", "QuickFreeze", "Arctic Fresh", "ChillMaster", ""],
    "Dairy & Eggs": ["CreameryCo", "DairyFresh", "MilkyWay", "FarmFresh Finds", ""],
    "Health Care": ["WellCare", "MediRelief", "VitalityPlus", "NatureRemedy", ""],
    "Liquor": ["OakBarrel", "CampusCellars", "SpiritCraft", "VintageVault", ""],
    "Kitchen Supplies": ["KitchenEssentials", "HomeChef", "CulinaryCorner", "PrepPro", ""],
    "Oils & Spices": ["PurePress", "SpiceRoute", "FlavorFields", ""],
    "Deli": ["GourmetCuts", "DeliSelect", "PremiumSlice", "FreshCounter", ""],
    "Desserts": ["SweetTreats", "DessertDelight", "SugarRush", "FrostingFinesse", ""],
    "Condiments & Sauces": ["FlavorMakers", "SauceWorks", "ZestyTouch", "TastyCraft", ""],
    "Canned Goods": ["PantryPrime", "ShelfStable", "CanCraft", "PreserveSelect", ""],
    "Dry Goods & Pasta": ["GrainHouse", "PantryPrime", "NoodleNook", "StapleStock", ""],
    "Meat": ["Butcher'sBest", "PrimeCuts", "MarbleMasters", "ProteinPro", ""],
    "Seafood": ["SeaHarvest", "OceanFresh", "TidalTastes", "WaveCatch", ""],
    "Produce": [],
    "Pets": ["PetPals", "CritterCare", "FurryFriends", "TailWaggers", ""],
    "Snacks": ["SnackAttack", "CrunchTime", "MunchMasters", "BiteSized", ""],
    "Candy": ["SweetSpot", "CandyCraze", "SugarRush", "TreatTrove", ""],
    "Home Goods": ["HomeEase", "HouseHoldPro", "DwellWell", "NestNecessities", ""],
    "Personal Care & Hygiene": ["PureCare", "DailyGlow", "FreshEssence", "WellGroomed", ""]
}

# product list by category
data = {
    "Produce": {
        "items": [
            "Apples", "Bananas", "Oranges", "Grapes", "Strawberries", "Blueberries",
            "Raspberries", "Blackberries", "Pears", "Peaches", "Plums", "Cherries",
            "Mangoes", "Pineapples", "Watermelon", "Cantaloupe", "Honeydew",
            "Avocado", "Broccoli", "Cauliflower", "Carrots", "Celery", "Romaine Lettuce",
            "Iceberg Lettuce", "Spinach", "Kale", "Bell Peppers", "Tomatoes", "Onions",
            "Red Potatoes", "Russet Potatoes", "Sweet Potatoes", "Garlic", "Ginger",
            "Cucumbers", "Zucchini", "Eggplant", "Mushrooms", "Green Beans",
            "Asparagus", "Brussels Sprouts", "Cabbage", "Limes", "Lemons", "Cilantro",
            "Parsley", "Green Onions", "Radishes", "Beets", "Turnips", "Butternut Squash",
            "Acorn Squash", "Spaghetti Squash", "Pumpkin (whole)", "Corn on the Cob",
            "Artichokes", "Okra", "Snow Peas", "Sugar Snap Peas", "Bok Choy",
            "Swiss Chard", "Arugula", "Watercress", "Napa Cabbage", "Roma Tomatoes",
            "Heirloom Tomatoes", "Yellow Squash", "Red Bell Peppers", "Yellow Bell Peppers",
            "Orange Bell Peppers", "Jalapeño Peppers", "Serrano Peppers", "Habanero Peppers",
            "Poblano Peppers", "Tomatillos", "Plantains", "Papaya", "Kiwi", "Grapefruit",
            "Blood Oranges", "Lychee", "Dragon Fruit", "Passion Fruit",
            "Rhubarb", "Persimmons", "Pomegranates", "Star Fruit", "Guava",
            "Jicama", "Fennel", "Shallots", "Kohlrabi", "Endive", "Radicchio",
            "Collard Greens", "Mustard Greens", "Dandelion Greens", "Sprouts (Alfalfa)",
            "Sprouts (Bean)", "Fresh Basil", "Fresh Mint", "Fresh Rosemary", "Fresh Thyme",
            "Fresh Dill", "Fresh Oregano", "Fresh Sage", "Chestnuts", "Figs", "Dates",
            "Thai Chili Peppers", "Leeks", "Rutabagas", "Parsnips", "Microgreens",
            "Butter Lettuce", "Red Leaf Lettuce", "Green Leaf Lettuce", "Baby Spinach",
            "Baby Kale", "Baby Arugula", "Clementines", "Tangerines", "Kumquats",
            "Ugli Fruit", "Quince", "Cherimoya", "Jackfruit", "Longan",
            "Rainbow Chard", "Yuca Root", "Jerusalem Artichokes", "Daikon Radish",
            "Red Delicious Apples", "Granny Smith Apples", "Fuji Apples", "Honeycrisp Apples",
            "Gala Apples", "Pink Lady Apples", "Golden Delicious Apples", "McIntosh Apples",
            "Jazz Apples", "Envy Apples", "Ambrosia Apples", "Cripps Pink Apples",
            "Empire Apples", "Jonathan Apples", "Jonagold Apples", "Braeburn Apples",
            "Cortland Apples", "Rome Apples", "Winesap Apples", "Crabapples",
            "Green Bananas", "Yellow Bananas", "Plantain Bananas", "Red Bananas",
            "Apple Bananas", "Baby Bananas", "Blue Java Bananas", "Burro Bananas",
            "Navel Oranges", "Valencia Oranges", "Cara Cara Oranges", "Seville Oranges",
            "Mandarin Oranges", "Satsuma Oranges", "Moro Oranges", "Bergamot Oranges",
            "Red Grapes", "Green Grapes", "Black Grapes", "Cotton Candy Grapes",
            "Concord Grapes", "Moon Drop Grapes", "Champagne Grapes", "Witch Finger Grapes",
            "Flame Grapes", "Thompson Seedless Grapes", "Muscat Grapes", "Kyoho Grapes",
            "Albariño Grapes", "Pinot Noir Grapes", "Chardonnay Grapes", "Riesling Grapes",
            "Cabernet Sauvignon Grapes", "Merlot Grapes", "Syrah Grapes", "Zinfandel Grapes",
            "Wild Strawberries", "Driscoll Strawberries", "Seascape Strawberries", "Albion Strawberries",
            "Chandler Strawberries", "Hood Strawberries", "Sweet Charlie Strawberries", "Ozark Beauty Strawberries",
            "Tribute Strawberries", "Tristar Strawberries", "Camarosa Strawberries", "Diamante Strawberries",
            "Cultivated Blueberries", "Wild Blueberries", "Highbush Blueberries", "Lowbush Blueberries",
            "Rabbiteye Blueberries", "Duke Blueberries", "Bluecrop Blueberries", "Jersey Blueberries",
            "Elliott Blueberries", "Patriot Blueberries", "Legacy Blueberries", "Chandler Blueberries",
            "Red Raspberries", "Black Raspberries", "Golden Raspberries", "Purple Raspberries",
            "Summer-bearing Raspberries", "Everbearing Raspberries", "Primocane Raspberries", "Floricane Raspberries",
            "Heritage Raspberries", "Latham Raspberries", "Fall Gold Raspberries", "Caroline Raspberries",
            "Boysenberries", "Loganberries", "Tayberries", "Marionberries",
            "Dewberries", "Cloudberries", "Huckleberries", "Mulberries",
            "Red Mulberries", "White Mulberries", "Black Mulberries", "Elderberries",
            "Gooseberries", "Currants", "Red Currants", "Black Currants",
            "White Currants", "Cranberries", "Lingonberries", "Goji Berries",
            "Acai Berries", "Juniper Berries", "Bilberries", "Salmonberries",
            "Thimbleberries", "Serviceberries", "Chokeberries", "Crowberries",
            "Barberry", "Bearberry", "Hackberry", "Bayberry",
            "Bartlett Pears", "Anjou Pears", "Bosc Pears", "Comice Pears",
            "Seckel Pears", "Forelle Pears", "Asian Pears", "Concorde Pears",
            "Starkrimson Pears", "Red Bartlett Pears", "Flemish Beauty Pears", "Conference Pears",
            "Yellow Peaches", "White Peaches", "Donut Peaches", "Nectarines",
            "Freestone Peaches", "Clingstone Peaches", "Semi-freestone Peaches", "Saturn Peaches",
            "Hale Peaches", "Red Haven Peaches", "Elberta Peaches", "Belle of Georgia Peaches",
            "Black Plums", "Red Plums", "Yellow Plums", "Green Plums",
            "Italian Plums", "Damson Plums", "Mirabelle Plums", "Pluots",
            "Apriums", "Plumcots", "Greengage Plums", "Victoria Plums",
            "Sweet Cherries", "Sour Cherries", "Bing Cherries", "Rainier Cherries",
            "Black Cherries", "Morello Cherries", "Montmorency Cherries", "Lambert Cherries",
            "Duke Cherries", "Lapin Cherries", "Sweetheart Cherries", "Skeena Cherries",
            "Ataulfo Mangoes", "Tommy Atkins Mangoes", "Kent Mangoes", "Keitt Mangoes",
            "Haden Mangoes", "Francis Mangoes", "Honey Mangoes", "Alphonso Mangoes",
            "Green Mangoes", "Yellow Mangoes", "Kesar Mangoes", "Manila Mangoes",
            "Fresh Pineapples", "Golden Pineapples", "Smooth Cayenne Pineapples", "Queen Pineapples",
            "Abacaxi Pineapples", "Sugarloaf Pineapples", "Kona Sugarloaf Pineapples", "Pernambuco Pineapples",
            "Seedless Watermelon", "Seeded Watermelon", "Yellow Watermelon", "Mini Watermelon",
            "Crimson Sweet Watermelon", "Sugar Baby Watermelon", "Jubilee Watermelon", "Charleston Gray Watermelon",
            "Cantaloupe", "Tuscan Cantaloupe", "Charentais Cantaloupe", "Crenshaw Melon",
            "Casaba Melon", "Santa Claus Melon", "Persian Melon", "Galia Melon",
            "Canary Melon", "Sharlyn Melon", "Sprite Melon", "Winter Melon",
            "Bitter Melon", "Honeydew", "Orange Honeydew", "Golden Honeydew",
            "Hass Avocado", "Fuerte Avocado", "Bacon Avocado", "Pinkerton Avocado",
            "Reed Avocado", "Zutano Avocado", "Gwen Avocado", "Lamb Hass Avocado",
            "Broccoli Crowns", "Broccoli Florets", "Broccolini", "Broccoli Rabe",
            "Purple Cauliflower", "Orange Cauliflower", "Green Cauliflower", "Romanesco",
            "Baby Carrots", "Rainbow Carrots", "Purple Carrots", "White Carrots",
            "Yellow Carrots", "Red Carrots", "Black Carrots", "Thumbelina Carrots",
            "Baby Spinach", "Flat-leaf Spinach", "Savoy Spinach", "New Zealand Spinach",
            "Malabar Spinach", "Red Spinach", "Water Spinach", "Tree Spinach",
            "Purple Kale", "Green Kale", "Red Kale", "Lacinato Kale",
            "Redbor Kale", "Siberian Kale", "Chinese Kale", "Baby Kale",
            "Cherry Tomatoes", "Grape Tomatoes", "Beefsteak Tomatoes", "Plum Tomatoes",
            "Green Tomatoes", "Yellow Tomatoes", "Kumato Tomatoes", "Brandywine Tomatoes",
            "Campari Tomatoes", "Sun Gold Tomatoes", "Black Krim Tomatoes", "Pineapple Tomatoes",
            "Yellow Onions", "Red Onions", "White Onions", "Vidalia Onions",
            "Shallots", "Green Onions", "Pearl Onions", "Cipollini Onions",
            "Sweet Onions", "Maui Onions", "Walla Walla Onions", "Bermuda Onions",
            "New Potatoes", "Fingerling Potatoes", "Yukon Gold Potatoes", "Purple Potatoes",
            "White Potatoes", "Baby Potatoes", "All-purpose Potatoes", "Baking Potatoes",
            "Yellow Finn Potatoes", "Red Bliss Potatoes", "Adirondack Blue Potatoes", "Russian Banana Potatoes",
            "Garnet Sweet Potatoes", "Jewel Sweet Potatoes", "Japanese Sweet Potatoes", "Purple Sweet Potatoes",
            "Hannah Sweet Potatoes", "Okinawan Sweet Potatoes", "Beauregard Sweet Potatoes", "Covington Sweet Potatoes",
            "Elephant Garlic", "Hardneck Garlic", "Softneck Garlic", "Purple Stripe Garlic",
            "Porcelain Garlic", "Rocambole Garlic", "Silverskin Garlic", "Artichoke Garlic",
            "Fresh Ginger", "Baby Ginger", "Galangal", "Turmeric",
            "Horseradish", "Wasabi", "Fingerroot", "Greater Galangal",
            "Lesser Galangal", "Sand Ginger", "Krachai", "Torch Ginger",
            "English Cucumbers", "Persian Cucumbers", "Pickling Cucumbers", "Lemon Cucumbers",
            "Armenian Cucumbers", "Kirby Cucumbers", "Japanese Cucumbers", "Mediterranean Cucumbers",
            "Green Zucchini", "Yellow Zucchini", "Round Zucchini", "Pattypan Squash",
            "Crookneck Squash", "Straightneck Squash", "Chayote Squash", "Kabocha Squash",
            "Delicata Squash", "Hubbard Squash", "Turban Squash", "Carnival Squash",
            "Buttercup Squash", "Sweet Dumpling Squash", "Red Kuri Squash", "Blue Hubbard Squash",
            "Globe Eggplant", "Japanese Eggplant", "Chinese Eggplant", "Italian Eggplant",
            "White Eggplant", "Fairy Tale Eggplant", "Thai Eggplant", "Indian Eggplant",
            "Graffiti Eggplant", "Rosa Bianca Eggplant", "Little Finger Eggplant", "Turkish Orange Eggplant",
            "Button Mushrooms", "Cremini Mushrooms", "Portobello Mushrooms", "Shiitake Mushrooms",
            "Oyster Mushrooms", "Enoki Mushrooms", "Maitake Mushrooms", "King Trumpet Mushrooms",
            "Chanterelle Mushrooms", "Porcini Mushrooms", "Morel Mushrooms", "Lion's Mane Mushrooms",
            "Black Trumpet Mushrooms", "Wood Ear Mushrooms", "Beech Mushrooms", "Hedgehog Mushrooms",
            "Reishi Mushrooms", "Chaga Mushrooms", "Cordyceps Mushrooms", "Turkey Tail Mushrooms",
            "Haricots Verts", "Yellow Wax Beans", "Purple Beans", "Romano Beans",
            "Flat Beans", "Yard Long Beans", "Dragon Tongue Beans", "Winged Beans",
            "Lima Beans", "Edamame", "Fava Beans", "Black-eyed Peas",
            "White Asparagus", "Green Asparagus", "Purple Asparagus", "Wild Asparagus",
            "Jumbo Asparagus", "Baby Asparagus", "Pencil Asparagus", "Standard Asparagus",
            "Red Cabbage", "Green Cabbage", "Savoy Cabbage", "Napa Cabbage",
            "Bok Choy", "Baby Bok Choy", "Tatsoi", "Choy Sum",
            "Gai Lan", "Yu Choy", "Pea Shoots", "Fiddlehead Ferns",
            "Cardoons", "Purslane", "Sorrel", "Chickweed",
            "Lamb's Quarters", "Wood Sorrel", "Stinging Nettles", "Ramps",
            "Fennel Bulb", "Fennel Fronds", "Celery Root", "Salsify",
            "Scorzonera", "Burdock Root", "Lotus Root", "Water Chestnuts",
            "Cassava", "Taro Root", "Eddoe", "Malanga",
            "Crosne", "Sunchokes", "Oca", "Ulluco",
            "Mashua", "Arracacha", "Yakon", "Jicama",
            "Kohlrabi", "Rutabaga", "Celeriac", "Turnips",
            "Gilfeather Turnips", "White Turnips", "Purple Top Turnips", "Yellow Turnips",
            "Japanese Turnips", "Baby Turnips", "Black Radishes", "Watermelon Radishes",
            "Red Radishes", "White Radishes", "French Breakfast Radishes", "Easter Egg Radishes",
            "Green Meat Radishes", "Daikon Radishes", "China Rose Radishes", "Black Spanish Radishes",
            "Chioggia Beets", "Golden Beets", "Red Beets", "White Beets",
            "Baby Beets", "Cylindra Beets", "Sugar Beets", "Mangel-wurzel Beets",
            "White Corn", "Yellow Corn", "Bi-color Corn", "Blue Corn",
            "Sweet Corn", "Field Corn", "Popcorn", "Ornamental Corn",
            "Red Amaranth", "Green Amaranth", "Joseph's Coat Amaranth", "Love-lies-bleeding Amaranth",
            "Giant Amaranth", "Grain Amaranth", "Tampala", "Chinese Spinach",
            "Callaloo", "Orach", "Good King Henry", "Fat Hen",
            "Lamb's Lettuce", "Miner's Lettuce", "New Zealand Spinach", "Land Cress",
            "Upland Cress", "Garden Cress", "Winter Cress", "Spring Cress",
            "Watercress", "Nasturtium", "Mizuna", "Mache",
            "Escarole", "Frisee", "Belgian Endive", "Curly Endive",
            "Chicory", "Radicchio", "Puntarelle", "Catalogna",
            "Castelfranco Radicchio", "Treviso Radicchio", "Chioggia Radicchio", "Tardivo Radicchio",
            "Broccoli Microgreens", "Radish Microgreens", "Sunflower Microgreens", "Pea Microgreens",
            "Basil Microgreens", "Cilantro Microgreens", "Arugula Microgreens", "Kale Microgreens",
            "Amaranth Microgreens", "Beet Microgreens", "Buckwheat Microgreens", "Cabbage Microgreens",
            "Chervil", "Chives", "Garlic Chives", "Lemongrass",
            "Lovage", "Marjoram", "Summer Savory", "Winter Savory",
            "Tarragon", "Thyme", "Lemon Thyme", "Lemon Verbena",
            "Lavender", "Oregano", "Greek Oregano", "Mexican Oregano",
            "Syrian Oregano", "Sweet Bay", "Kaffir Lime Leaves", "Curry Leaves",
            "Thai Basil", "Holy Basil", "Lemon Basil", "Cinnamon Basil",
            "Purple Basil", "Greek Basil", "Italian Basil", "Genovese Basil",
            "African Blue Basil", "Lime Basil", "Spicy Globe Basil", "Boxwood Basil",
            "Spearmint", "Peppermint", "Chocolate Mint", "Apple Mint",
            "Pineapple Mint", "Orange Mint", "Ginger Mint", "Corsican Mint",
            "Banana Mint", "Mojito Mint", "Pennyroyal", "Horsemint",
            "Mountain Mint", "Calamint", "Catmint", "Catnip",
            "Scotch Bonnet Peppers", "Ghost Peppers", "Trinidad Scorpion Peppers", "Carolina Reaper Peppers",
            "Anaheim Peppers", "Banana Peppers", "Cherry Peppers", "Cubanelle Peppers",
            "Hungarian Wax Peppers", "Shishito Peppers", "Tabasco Peppers", "Thai Bird's Eye Peppers",
            "Piquillo Peppers", "Padrón Peppers", "Jimmy Nardello Peppers", "Friggitello Peppers",
            "Cayenne Peppers", "Fresno Peppers", "Paprika Peppers", "Peri-Peri Peppers",
            "Aji Amarillo Peppers", "Hatch Chile Peppers", "Pasilla Peppers", "Ancho Peppers",
            "Cascabel Peppers", "Guajillo Peppers", "New Mexico Peppers", "Rocoto Peppers",
            "Key Limes", "Persian Limes", "Kaffir Limes", "Finger Limes",
            "Calamansi", "Rangpur", "Yuzu", "Sudachi",
            "Bearss Limes", "Makrut Limes", "Mexican Limes", "Sweet Limes",
            "Meyer Lemons", "Eureka Lemons", "Lisbon Lemons", "Amalfi Lemons",
            "Femminello Lemons", "Ponderosa Lemons", "Primofiori Lemons", "Verna Lemons",
            "Buddha's Hand", "Etrog", "Bergamot", "Limequats",
            "Tangelos", "Lemons", "Lemon Hybrids", "Lime Hybrids",
            "Assorted Citrus Fruits", "Hybrid Citrus Fruits", "Unique Citrus Varieties", "Specialty Citrus"
        ],
        "price_range": (0.79, 4.29),
        "per_lb": True,
        "variants": ["Conventional", "Organic", "Local", "Imported"]
    },
    
    "Bakery": {
        "items": [
            "Sliced White Bread 20oz loaf", "Whole Wheat Bread 20oz loaf", "Multigrain Bread 24oz loaf",
            "Brioche Rolls 8ct", "Hamburger Buns 8ct", "Hot Dog Buns 8ct", "English Muffins 6ct",
            "Plain Bagels 6ct", "Everything Bagels 6ct", "Blueberry Muffins 4ct", "Croissants 4ct",
            "Chocolate Donuts 6ct", "Cinnamon Rolls 4ct", "Pita Bread 6ct", "Tortillas Flour 10ct",
            "Tortillas Corn 30ct", "Artisan Sourdough Loaf", "Dinner Rolls 12ct", "Pretzel Rolls 4ct",
            "Ciabatta Rolls 4ct", "Baguette", "Kaiser Rolls 6ct",
            "Focaccia Bread", "Naan Bread 4ct", "Challah Loaf", "Rye Bread 16oz loaf",
            "Garlic Bread Loaf", "Gluten-Free Bread 16oz loaf", "Breadsticks 12ct",
            "Bread Bowls 4ct", "Cranberry Walnut Bread", "Banana Bread Loaf",
            "Cornbread 8in square", "Scones Blueberry 4ct", "Scones Chocolate Chip 4ct",
            "Danish Pastries Assorted 4ct", "Sticky Buns 4ct", "Fruit Tarts Mini 6ct",
            "Eclairs 4ct", "Soft Pretzels 3ct", "Italian Bread Loaf", "French Bread Loaf",
            "Flatbread 4ct", "Onion Rolls 6ct", "Sesame Seed Buns 8ct", "Pumpernickel Bread 16oz loaf",
            "Cinnamon Raisin Bread 16oz loaf", "Asiago Cheese Bread", "Marble Rye Bread",
            "Bagels Cinnamon Raisin 6ct", "Bagels Sesame 6ct", "Bagels Blueberry 6ct",
            "Chocolate Croissants 4ct", "Almond Croissants 4ct",
            "Oat Bread 16oz loaf", "Potato Bread 20oz loaf", "Honey Wheat Bread 22oz loaf",
            "Sprouted Grain Bread 24oz loaf", "Keto Bread 16oz loaf", "Low-Carb Bread 16oz loaf",
            "Sunflower Seed Bread 20oz loaf", "Flaxseed Bread 18oz loaf", "Light Bread 16oz loaf",
            "Texas Toast Bread 22oz loaf", "Vienna Bread 16oz loaf", "Buttermilk Bread 20oz loaf",
            "Honey Oat Bread 22oz loaf", "Country White Bread 22oz loaf", "Split Top Bread 20oz loaf",
            "Thin Sliced Bread 16oz loaf", "Thick Sliced Bread 24oz loaf", "Sandwich Bread 24oz loaf",
            "Italian Herb Bread 20oz loaf", "Rosemary Olive Oil Bread 18oz loaf", "Jalapeño Cheddar Bread 18oz loaf",
            "Nine Grain Bread 24oz loaf", "Seven Grain Bread 22oz loaf", "12 Grain Bread 24oz loaf",
            "Honey Cracked Wheat Bread 22oz loaf", "San Francisco Sourdough 24oz loaf", "Rustic Sourdough 24oz loaf",
            "Sourdough Rounds 16oz", "Sourdough Boule 32oz", "Sourdough Batard 24oz",
            "Dark Rye Bread 16oz loaf", "Light Rye Bread 16oz loaf", "Seeded Rye Bread 18oz loaf",
            "Jewish Rye Bread 16oz loaf", "Swedish Rye Bread 16oz loaf", "Russian Black Bread 16oz loaf",
            "Limpa Bread 16oz loaf", "Dill Rye Bread 16oz loaf", "Caraway Rye Bread 16oz loaf",
            "Brioche Loaf 16oz", "Brioche Sliced 16oz loaf", "Brioche Bread Pudding 12oz",
            "Brioche Dinner Rolls 8ct", "Brioche Burger Buns 4ct", "Brioche Hot Dog Buns 6ct",
            "Sweet Hawaiian Rolls 12ct", "Hawaiian Burger Buns 8ct", "Hawaiian Hot Dog Buns 8ct",
            "Potato Rolls 8ct", "Potato Burger Buns 8ct", "Potato Hot Dog Buns 8ct",
            "Whole Wheat Burger Buns 8ct", "Whole Wheat Hot Dog Buns 8ct", "Multigrain Burger Buns 8ct",
            "Multigrain Hot Dog Buns 8ct", "Gluten-Free Burger Buns 4ct", "Gluten-Free Hot Dog Buns 4ct",
            "Pretzel Burger Buns",
            "English Muffins Sourdough 6ct", "English Muffins Whole Wheat 6ct", "English Muffins Cinnamon Raisin 6ct",
            "English Muffins Multi-Grain 6ct", "English Muffins Gluten-Free 4ct", "English Muffin Bread 16oz loaf",
            "Bagels Onion 6ct", "Bagels Poppy Seed 6ct", "Bagels Garlic 6ct",
            "Bagels Asiago Cheese 6ct", "Bagels Egg 6ct", "Bagels Salt 6ct",
            "Bagels Pumpernickel 6ct", "Bagels Whole Wheat 6ct", "Bagels Multigrain 6ct",
            "Flagels 4ct", "Mini Bagels 12ct", "Bagel Chips 6oz",
            "Bagel Thins 6ct", "Bialy Rolls 4ct", "Cinnamon Sugar Bagels 6ct",
            "Chocolate Chip Bagels 6ct", "Spinach Bagels 6ct", "French Toast Bagels 6ct",
            "Cranberry Orange Bagels 6ct", "Jalapeño Bagels 6ct", "Rainbow Bagels 6ct",
            "Gluten-Free Bagels 4ct", "Breadsticks Sesame 12ct", "Breadsticks Garlic 12ct",
            "Breadsticks Parmesan 12ct", "Breadsticks Whole Wheat 12ct", "Breadsticks Italian Herb 12ct",
            "Breadsticks Tomato Basil 12ct", "Breadsticks Gluten-Free 8ct", "Grissini 8oz",
            "French Breadsticks 8ct", "Sourdough Breadsticks 8ct", "Biscotti Almond 6ct",
            "Biscotti Chocolate 6ct", "Biscotti Anise 6ct", "Biscotti Cranberry Pistachio 6ct",
            "Pita Bread Whole Wheat 6ct", "Pita Bread Mini 12ct", "Pita Chips 6oz",
            "Pita Bread Gluten-Free 4ct", "Pita Pockets 6ct", "Greek Pita Bread 6ct",
            "Mediterranean Flatbread 4ct", "Lavash Bread 4ct", "Naan Bread Garlic 4ct",
            "Naan Bread Whole Wheat 4ct", "Naan Bread Onion 4ct", "Naan Bread Chili 4ct",
            "Roti 8ct", "Paratha 4ct", "Chapati 8ct",
            "Tortillas Wheat 8ct", "Tortillas Spinach 8ct", "Tortillas Tomato Basil 8ct",
            "Tortillas Low-Carb 8ct", "Tortillas Gluten-Free 6ct", "Tortilla Chips 12oz",
            "Flour Tortillas Burrito Size 8ct", "Flour Tortillas Fajita Size 10ct", "Flour Tortillas Taco Size 12ct",
            "Corn Tortillas White 30ct", "Corn Tortillas Blue 30ct", "Corn Tortillas Yellow 30ct",
            "Taco Shells Hard 12ct", "Taco Bowls 6ct", "Tostada Shells 12ct",
            "Croissants Mini 12ct", "Croissants Large 4ct", "Croissants Whole Wheat 4ct",
            "Croissants Ham & Cheese 4ct", "Croissants Spinach & Feta 4ct", "Croissants Breakfast 4ct",
            "Pain au Chocolat 4ct", "Pain aux Raisins 4ct", "Pain au Jambon 4ct",
            "Danish Cheese 4ct", "Danish Cherry 4ct", "Danish Apple 4ct",
            "Danish Raspberry 4ct", "Danish Apricot 4ct", "Danish Cinnamon 4ct",
            "Danish Cream Cheese 4ct", "Danish Pecan 4ct", "Danish Blueberry 4ct",
            "Danish Bear Claws 4ct", "Muffins Chocolate Chip 4ct", "Muffins Banana Nut 4ct",
            "Muffins Cranberry Orange 4ct", "Muffins Lemon Poppy Seed 4ct", "Muffins Bran 4ct",
            "Muffins Apple Cinnamon 4ct", "Muffins Corn 4ct", "Muffins Double Chocolate 4ct",
            "Muffins Morning Glory 4ct", "Muffins Gluten-Free Blueberry 4ct", "Muffin Tops 6ct",
            "Mini Muffins Assorted 12ct", "Scones Plain 4ct", "Scones Cranberry Orange 4ct",
            "Scones Cinnamon 4ct", "Scones Mixed Berry 4ct", "Scones Lemon 4ct",
            "Scones Maple Oat 4ct", "Scones Savory Cheese 4ct", "Scones Gluten-Free 4ct",
            "Donuts Glazed 6ct", "Donuts Powdered Sugar 6ct", "Donuts Jelly Filled 6ct",
            "Donuts Boston Cream 6ct", "Donuts Maple Frosted 6ct", "Donuts Sprinkles 6ct",
            "Donuts Blueberry 6ct", "Donuts Cinnamon Sugar 6ct", "Donuts Apple Fritter 4ct",
            "Donuts Old Fashioned 6ct", "Donuts Cake 6ct", "Donuts Cruller 6ct",
            "Donuts Long John 6ct", "Donuts Bear Claw 4ct", "Donuts Gluten-Free 4ct",
            "Donut Holes 24ct", "Cinnamon Rolls Jumbo 4ct", "Cinnamon Rolls Mini 12ct",
            "Cinnamon Rolls Iced 4ct", "Cinnamon Rolls Caramel Pecan 4ct", "Cinnamon Rolls Cream Cheese Frosting 4ct",
            "Cinnamon Twists 6ct", "Cinnamon Sugar Pull-Apart Bread", "Cinnamon Bread 16oz loaf",
            "Pecan Sticky Buns 4ct", "Caramel Sticky Buns 4ct", "Morning Buns 4ct",
            "Coffee Cake 8in", "Coffee Cake Crumb Top 8in", "Coffee Cake Cinnamon 8in",
            "Coffee Cake Raspberry 8in", "Coffee Cake Blueberry 8in", "Coffee Cake Apple 8in",
            "Coffee Cake Cheese 8in", "Streusel Cake 8in", "Crumb Cake 8in",
            "Babka Chocolate 16oz loaf", "Babka Cinnamon 16oz loaf", "Monkey Bread 14oz",
            "Churros 6ct", "Funnel Cake 2ct", "Elephant Ears 2ct",
            "Beignets 6ct", "Cream Puffs 6ct", "Cannoli 4ct",
            "Cannoli Shells 6ct", "Puff Pastry Sheets 2ct", "Phyllo Dough 16oz",
            "Paczki 6ct", "Kolaches Fruit 6ct", "Kolaches Sausage 6ct",
            "Rugelach 12ct", "Hamantaschen 6ct", "Mandel Bread 12oz",
            "Fruit Empanadas 4ct", "Conchas 6ct", "Pan Dulce Assorted 6ct",
            "Bolillos 6ct", "Telera Rolls 6ct", "Torta Rolls 4ct"
        ],
        "price_range": (1.99, 6.99)
    },
    
    "Oils & Spices": {
            "price_range": (1.49, 9.99),
            "items": [
                "Olive Oil", "Extra Virgin Olive Oil", "Canola Oil", "Vegetable Oil",
                "Coconut Oil", "Avocado Oil", "Sesame Oil", "Peanut Oil",
                "Sunflower Oil", "Grapeseed Oil", "Salt", "Sea Salt Grinder",
                "Kosher Salt", "Black Pepper", "Black Peppercorn Grinder", "Garlic Powder",
                "Onion Powder", "Paprika", "Smoked Paprika", "Chili Powder",
                "Cumin", "Curry Powder", "Oregano", "Basil", "Thyme",
                "Rosemary", "Parsley Flakes", "Italian Seasoning", "Cinnamon",
                "Nutmeg Ground", "Allspice", "Turmeric", "Ginger Ground",
                "Red Pepper Flakes", "Bay Leaves", "Coriander", "Clove Ground",
                "Cardamom", "Saffron",
                "Chili Oil", "Truffle Oil", "Walnut Oil", "Mustard Oil",
                "Hazelnut Oil", "Infused Olive Oil Garlic", "Infused Olive Oil Basil",
                "Vanilla Extract", "Almond Extract", "Mint Extract", "Lemon Extract",
                "Chili Flakes", "Fenugreek Seeds", "Star Anise Whole",
                "Caraway Seeds", "Fennel Seeds", "Mustard Seeds",
                "Celery Seeds", "Poppy Seeds", "Ancho Chili Powder",
                "Cayenne Pepper", "Pumpkin Pie Spice", "Apple Pie Spice",
                "Poultry Seasoning", "Dill Weed", "Sage", "Marjoram",
                "Berbere Spice Blend", "Za'atar Spice Blend", "Garam Masala",
                "Five Spice Powder", "Lemon Pepper", "Cajun Seasoning",
                "Light Olive Oil", "Pure Olive Oil", "Refined Olive Oil", "Pomace Olive Oil",
                "Unfiltered Olive Oil", "Cold Pressed Olive Oil", "Organic Olive Oil", "Greek Olive Oil",
                "Italian Olive Oil", "Spanish Olive Oil", "California Olive Oil", "Tuscan Olive Oil",
                "Arbequina Olive Oil", "Koroneiki Olive Oil", "Picual Olive Oil", "Frantoio Olive Oil",
                "High-Oleic Sunflower Oil", "Light Sesame Oil", "Toasted Sesame Oil", "Dark Sesame Oil",
                "Roasted Sesame Oil", "Refined Coconut Oil", "Virgin Coconut Oil", "Liquid Coconut Oil",
                "MCT Oil", "Unrefined Avocado Oil", "Refined Avocado Oil", "Cold Pressed Avocado Oil",
                "Organic Avocado Oil", "Unrefined Peanut Oil", "Refined Peanut Oil", "Roasted Peanut Oil",
                "Safflower Oil", "High-Oleic Safflower Oil", "Corn Oil", "Rice Bran Oil",
                "Almond Oil", "Macadamia Nut Oil", "Pistachio Oil", "Pecan Oil",
                "Cashew Oil", "Brazil Nut Oil", "Flaxseed Oil", "Hemp Seed Oil",
                "Pumpkin Seed Oil", "Camelina Oil", "Perilla Oil", "Argan Oil",
                "Black Seed Oil", "Chia Seed Oil", "Evening Primrose Oil", "Borage Oil",
                "Fish Oil", "Cod Liver Oil", "Krill Oil", "Salmon Oil",
                "Palm Oil", "Red Palm Oil", "Palm Kernel Oil", "Ghee",
                "Clarified Butter", "Brown Butter", "Beef Tallow", "Duck Fat",
                "Bacon Fat", "Lard", "Chicken Fat", "Goose Fat",
                "Schmaltz", "Margarine", "Shortening", "Cooking Spray",
                "Infused Olive Oil Lemon", "Infused Olive Oil Chili", "Infused Olive Oil Rosemary", "Infused Olive Oil Thyme",
                "Infused Olive Oil Herb", "Infused Olive Oil Pepper", "Wheat Germ Oil", "Cottonseed Oil",
                "Butter Flavored Oil", "Shallot Oil", "Garlic Oil", "Herb Oil",
                "White Truffle Oil", "Black Truffle Oil", "Smoked Oil", "Bacon Flavored Oil",
                "Table Salt", "Pink Himalayan Salt", "Hawaiian Red Salt", "Black Salt",
                "Fleur de Sel", "Celtic Sea Salt", "Truffle Salt", "Garlic Salt",
                "Onion Salt", "Celery Salt", "Seasoned Salt", "Herbed Salt",
                "Smoked Salt", "Salt Substitute", "Lite Salt", "Rock Salt",
                "Pickling Salt", "Curing Salt", "Iodized Salt", "Non-Iodized Salt",
                "Sea Salt Flakes", "Flavored Salt", "White Pepper Ground", "Pink Peppercorns",
                "Green Peppercorns", "Szechuan Peppercorns", "Tellicherry Peppercorns", "Rainbow Peppercorns",
                "White Peppercorns Whole", "Long Pepper", "Cubeb Pepper", "Grains of Paradise",
                "Garlic Granulated", "Garlic Minced", "Garlic Salt", "Roasted Garlic Powder",
                "Black Garlic Powder", "Onion Granulated", "Onion Minced", "Onion Salt",
                "Green Onion Flakes", "Roasted Onion Powder", "Shallot Powder", "Leek Powder",
                "Sweet Paprika", "Hot Paprika", "Hungarian Paprika", "Spanish Paprika",
                "Chipotle Powder", "Ancho Chile Powder", "Guajillo Chile Powder", "Pasilla Chile Powder",
                "Arbol Chile Powder", "Ghost Pepper Powder", "Habanero Powder", "Scotch Bonnet Powder",
                "Carolina Reaper Powder", "Jalapeño Powder", "Serrano Powder", "Poblano Powder",
                "Aleppo Pepper", "Espelette Pepper", "Ground Cumin", "Cumin Seeds",
                "Roasted Cumin Powder", "White Cumin", "Black Cumin", "Curry Leaves",
                "Madras Curry Powder", "Thai Curry Powder", "Green Curry Powder", "Red Curry Powder",
                "Yellow Curry Powder", "Japanese Curry Powder", "Caribbean Curry Powder", "Jamaican Curry Powder",
                "Dried Oregano", "Mexican Oregano", "Greek Oregano", "Italian Oregano",
                "Turkish Oregano", "Fresh Oregano", "Dried Basil", "Fresh Basil",
                "Thai Basil", "Holy Basil", "Lemon Basil", "Dried Thyme",
                "Fresh Thyme", "Lemon Thyme", "English Thyme", "French Thyme",
                "Dried Rosemary", "Fresh Rosemary", "Rosemary Leaves", "Ground Rosemary",
                "Fresh Parsley", "Curly Parsley", "Flat-Leaf Parsley", "Herbes de Provence",
                "Bouquet Garni", "Fine Herbs", "Greek Seasoning", "Tuscan Seasoning",
                "Sicilian Seasoning", "Mexican Seasoning", "Taco Seasoning", "Fajita Seasoning",
                "Chili Seasoning", "BBQ Seasoning", "Steak Seasoning", "Chicken Seasoning",
                "Seafood Seasoning", "Old Bay Seasoning", "Blackened Seasoning", "Meatloaf Seasoning",
                "Pot Roast Seasoning", "Jerk Seasoning", "Baharat", "Ras el Hanout",
                "Harissa Seasoning", "Dukkah", "Shichimi Togarashi", "Furikake",
                "Gomasio", "Nori Flakes", "Cassia Cinnamon", "Ceylon Cinnamon",
                "Vietnamese Cinnamon", "Korintje Cinnamon", "Cinnamon Sticks", "Cinnamon Sugar",
                "Saigon Cinnamon", "Ground Nutmeg", "Whole Nutmeg", "Mace",
                "Mace Blades", "Ground Allspice", "Whole Allspice Berries", "Ground Turmeric",
                "Fresh Turmeric", "Turmeric Root", "Golden Milk Blend", "Ground Ginger",
                "Crystallized Ginger", "Fresh Ginger", "Pickled Ginger", "Galangal Powder",
                "Crushed Red Pepper", "Aleppo Pepper Flakes", "Korean Chili Flakes", "Italian Chili Flakes",
                "Urfa Biber", "Green Bay Leaves", "Indian Bay Leaves", "California Bay Leaves",
                "Indonesian Bay Leaves", "Ground Coriander", "Coriander Seeds", "Cilantro Flakes",
                "Whole Cloves", "Clove Powder", "Green Cardamom Pods", "Black Cardamom Pods",
                "Ground Cardamom", "Cardamom Seeds", "Spanish Saffron", "Iranian Saffron",
                "Kashmir Saffron", "Greek Saffron", "Saffron Threads", "Ground Saffron",
                "Yellow Mustard Seeds", "Brown Mustard Seeds", "Black Mustard Seeds", "Ground Mustard",
                "Prepared Mustard", "Mustard Powder", "Hot Mustard Powder", "Chinese Hot Mustard",
                "Dijon Mustard", "Yellow Mustard", "Whole Fennel Seeds", "Ground Fennel",
                "Fennel Pollen", "Anise Seeds", "Ground Anise", "Licorice Root",
                "Licorice Powder", "Dill Seeds", "Dill Weed Dried", "Fresh Dill",
                "Dried Sage", "Fresh Sage", "Rubbed Sage", "Ground Sage",
                "Marjoram Dried", "Fresh Marjoram", "Ground Marjoram", "Lemon Verbena",
                "Lemongrass", "Lemongrass Powder", "Kaffir Lime Leaves", "Dried Mint",
                "Fresh Mint", "Spearmint", "Peppermint", "Tarragon Dried",
                "Fresh Tarragon", "French Tarragon", "Russian Tarragon", "Lavender",
                "Culinary Lavender", "Rose Petals", "Rose Water", "Orange Blossom Water",
                "Juniper Berries", "Carob Powder", "Sumac", "Sichuan Peppercorn Oil",
                "Chili Crisp", "Vanilla Beans", "Vanilla Bean Paste", "Vanilla Powder",
                "Imitation Vanilla", "Clear Vanilla Extract", "Mexican Vanilla Extract", "Tahitian Vanilla Extract",
                "Madagascar Vanilla Extract", "Double-Fold Vanilla Extract", "Rum Extract", "Brandy Extract",
                "Coconut Extract", "Coffee Extract", "Chocolate Extract", "Maple Extract",
                "Butter Extract", "Orange Extract", "Lemon Extract", "Lime Extract",
                "Peppermint Extract", "Anise Extract", "Root Beer Extract", "Banana Extract",
                "Strawberry Extract", "Raspberry Extract", "Cherry Extract", "Almond Extract",
                "Hazelnut Extract", "Pistachio Extract", "Walnut Extract", "Pecan Extract",
                "Rose Extract", "Lavender Extract", "Violet Extract", "Jasmine Extract",
                "Bergamot Extract", "Caramel Extract", "Butterscotch Extract", "Marshmallow Extract",
                "Smoke Extract", "Bacon Extract", "Anchovy Extract", "Mushroom Extract",
                "Truffle Extract", "Wasabi Extract", "Sriracha Extract", "Worcestershire Extract"
            ],
            "sizes": {
                "Olive Oil": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8},
                    {"size": "68oz", "price_multiplier": 3.0}
                ],
                "Extra Virgin Olive Oil": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8},
                    {"size": "68oz", "price_multiplier": 3.0}
                ],
                "Canola Oil": [
                    {"size": "24oz", "price_multiplier": 0.6},
                    {"size": "48oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.3},
                    {"size": "128oz", "price_multiplier": 2.4}
                ],
                "Vegetable Oil": [
                    {"size": "24oz", "price_multiplier": 0.6},
                    {"size": "48oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.3},
                    {"size": "128oz", "price_multiplier": 2.4}
                ],
                "Coconut Oil": [
                    {"size": "7oz", "price_multiplier": 0.6},
                    {"size": "14oz", "price_multiplier": 1.0},
                    {"size": "30oz", "price_multiplier": 2.0}
                ],
                "Avocado Oil": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "24oz", "price_multiplier": 1.5}
                ],
                "Sesame Oil": [
                    {"size": "5oz", "price_multiplier": 0.6},
                    {"size": "10oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.5}
                ],
                "Peanut Oil": [
                    {"size": "16oz", "price_multiplier": 0.6},
                    {"size": "32oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.8}
                ],
                "Sunflower Oil": [
                    {"size": "16oz", "price_multiplier": 0.6},
                    {"size": "32oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.8}
                ],
                "Grapeseed Oil": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.7}
                ],
                "Vanilla Extract": [
                    {"size": "1oz", "price_multiplier": 0.5},
                    {"size": "2oz", "price_multiplier": 1.0},
                    {"size": "4oz", "price_multiplier": 1.8},
                    {"size": "8oz", "price_multiplier": 3.0}
                ],
                "Garlic Powder": [
                    {"size": "2oz", "price_multiplier": 0.7},
                    {"size": "3oz", "price_multiplier": 1.0},
                    {"size": "6oz", "price_multiplier": 1.8}
                ],
                "Salt": [
                    {"size": "16oz", "price_multiplier": 0.7},
                    {"size": "26oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 1.6}
                ],
                "Kosher Salt": [
                    {"size": "16oz", "price_multiplier": 0.4},
                    {"size": "48oz", "price_multiplier": 1.0},
                    {"size": "80oz", "price_multiplier": 1.6}
                ]
            }
        },
        
        "Deli": {
            "price_range": (2.49, 14.99),
            "items": [
                "Sliced Turkey Breast", "Sliced Ham", "Sliced Roast Beef", "Salami Sliced",
                "Pepperoni Sliced", "Prosciutto", "Bologna", "Swiss Cheese Slices",
                "Cheddar Cheese Slices", "Provolone Cheese Slices", "Colby Jack Cheese Slices",
                "Muenster Cheese Slices", "Pepper Jack Cheese Slices", "Havarti Cheese Slices",
                "Hummus Classic", "Hummus Roasted Red Pepper", "Pico de Gallo",
                "Guacamole Fresh", "Deli Potato Salad", "Cole Slaw", "Macaroni Salad",
                "Rotisserie Chicken Whole", "Pre-made Turkey Sandwich", "Pre-made Italian Sub",
                "Sushi California Roll", "Sushi Spicy Tuna Roll",
                "Capicola", "Mortadella", "Pastrami", "Pancetta",
                "Chorizo", "Liverwurst", "Headcheese", "Smoked Turkey Breast",
                "Olive Medley", "Pepperoncini", "Sun-Dried Tomatoes",
                "Marinated Artichokes", "Stuffed Grape Leaves", "Antipasto Salad",
                "Egg Salad", "Chicken Salad", "Tuna Salad", "Greek Salad",
                "Caesar Salad", "Pasta Salad", "Rotisserie Chicken Half",
                "Prepared Meatloaf Slice", "Prepared Lasagna Slice", "Prepared Chicken Parmesan",
                "Sushi Veggie Roll", "Sushi Rainbow Roll", "Sushi Salmon Nigiri",
                "Prepared Chicken Tenders", "Prepared Buffalo Wings",
                "Honey Turkey Breast", "Cajun Turkey Breast", "Applewood Smoked Turkey Breast",
                "Oven Roasted Turkey Breast", "Turkey Pastrami", "Maple Honey Turkey",
                "Black Forest Ham", "Honey Ham", "Virginia Ham",
                "Tavern Ham", "Applewood Smoked Ham", "Honey Maple Ham",
                "Spiral Sliced Ham", "Country Ham", "Italian Ham",
                "Corned Beef", "London Broil Roast Beef", "Peppered Roast Beef",
                "Rare Roast Beef", "Medium Roast Beef", "Well Done Roast Beef",
                "Cajun Roast Beef", "Herb Crusted Roast Beef", "Seasoned Roast Beef",
                "Genoa Salami", "Hard Salami", "Cotto Salami",
                "Sopressata", "Picante Salami", "Peppered Salami",
                "Calabrese Salami", "Napoli Salami", "Finocchiona Salami",
                "Turkey Pepperoni", "Hot Pepperoni", "Cup & Char Pepperoni",
                "Prosciutto di Parma", "Prosciutto San Daniele", "Prosciutto Cotto",
                "Serrano Ham", "Speck", "Jamon Iberico",
                "Beef Bologna", "Garlic Bologna", "Lebanon Bologna",
                "Ring Bologna", "German Bologna", "Chicken Bologna",
                "Turkey Bologna", "Oscar Mayer Bologna", "Beef Salami",
                "Italian Dry Salami", "Sandwich Pepperoni", "Summer Sausage",
                "Beer Salami", "Thuringer", "Cervelat",
                "Bresaola", "Coppa", "Lomo",
                "Nduja", "Guanciale", "Landjaeger",
                "Braunschweiger", "Pate", "Chicken Liver Mousse",
                "Duck Rillettes", "Smoked Duck Breast", "Smoked Chicken Breast",
                "Oven Roasted Chicken Breast", "Buffalo Chicken Breast", "Blackened Chicken Breast",
                "Herb Roasted Chicken Breast", "Cajun Chicken Breast", "Grilled Chicken Breast",
                "Smoked Chicken", "Smoked Salmon", "Gravlax",
                "Lox", "Honey Smoked Salmon", "Peppered Smoked Salmon",
                "Smoked Whitefish", "Smoked Trout", "Smoked Mackerel",
                "Smoked Sable", "Baby Swiss Cheese", "Aged Swiss Cheese",
                "Emmentaler Cheese", "Gruyere Cheese", "Sharp Cheddar Cheese",
                "Extra Sharp Cheddar Cheese", "White Cheddar Cheese", "Yellow Cheddar Cheese",
                "Mild Cheddar Cheese", "Aged Cheddar Cheese", "Smoked Provolone Cheese",
                "Sharp Provolone Cheese", "Mild Provolone Cheese", "Monterey Jack Cheese",
                "Smoked Gouda Cheese", "Aged Gouda Cheese", "Baby Gouda Cheese",
                "Dill Havarti Cheese", "Caraway Havarti Cheese", "Jalapeno Havarti Cheese",
                "Fontina Cheese", "Jarlsberg Cheese", "Manchego Cheese",
                "Brie Cheese", "Camembert Cheese", "Blue Cheese",
                "Gorgonzola Cheese", "Stilton Cheese", "Roquefort Cheese",
                "Asiago Cheese", "Feta Cheese", "Goat Cheese",
                "American Cheese", "Edam Cheese", "Cotija Cheese",
                "Panela Cheese", "Queso Fresco", "Queso Blanco",
                "Hummus Garlic", "Hummus Jalapeno", "Hummus Kalamata Olive",
                "Hummus Pine Nut", "Hummus Lemon", "Hummus Artichoke",
                "Hummus Sun-Dried Tomato", "Hummus Everything Bagel", "Hummus Cilantro",
                "Baba Ganoush", "Tzatziki", "Tabouli",
                "Spinach Dip", "Artichoke Dip", "Spinach & Artichoke Dip",
                "Buffalo Chicken Dip", "French Onion Dip", "Ranch Dip",
                "Crab Dip", "Shrimp Dip", "Smoked Salmon Dip",
                "Bean Dip", "Seven Layer Dip", "Queso Dip",
                "Pimento Cheese Spread", "Herb Cream Cheese Spread", "Veggie Cream Cheese Spread",
                "Lox Cream Cheese Spread", "Strawberry Cream Cheese Spread", "Honey Walnut Cream Cheese Spread",
                "Salsa Mild", "Salsa Medium", "Salsa Hot",
                "Salsa Verde", "Mango Salsa", "Peach Salsa",
                "Corn Salsa", "Black Bean & Corn Salsa", "Chipotle Salsa",
                "Guacamole Spicy", "Guacamole Chunky", "Guacamole Smooth",
                "Bruschetta", "Olive Tapenade", "Sundried Tomato Tapenade",
                "Marinated Mushrooms", "Marinated Roasted Red Peppers", "Pickled Vegetables",
                "Kimchi", "Sauerkraut", "Coleslaw Vinegar Based",
                "Coleslaw Creamy", "Broccoli Slaw", "Carrot Raisin Slaw",
                "Asian Slaw", "Red Cabbage Slaw", "Brussels Sprout Slaw",
                "Potato Salad Traditional", "Potato Salad German", "Potato Salad Mustard",
                "Potato Salad Red Skin", "Potato Salad Ranch", "Sweet Potato Salad",
                "Macaroni Salad Classic", "Macaroni Salad With Ham", "Macaroni Salad Ranch",
                "Tuna Macaroni Salad", "Chicken Macaroni Salad", "Italian Pasta Salad",
                "Greek Pasta Salad", "Mediterranean Pasta Salad", "Asian Pasta Salad",
                "Orzo Pasta Salad", "Tortellini Pasta Salad", "Pesto Pasta Salad",
                "Caprese Pasta Salad", "Southwest Pasta Salad", "Caesar Pasta Salad",
                "Chicken Salad Traditional", "Chicken Salad Cranberry Walnut", "Chicken Salad Curry",
                "Chicken Salad Buffalo", "Chicken Salad Waldorf", "Chicken Salad Tarragon",
                "Chicken Salad Pesto", "Tuna Salad Classic", "Tuna Salad Spicy",
                "Tuna Salad Dill", "Tuna Salad Nicoise", "Tuna Salad Mediterranean",
                "Seafood Salad", "Lobster Salad", "Crab Salad",
                "Shrimp Salad", "Egg Salad Classic", "Egg Salad Bacon",
                "Egg Salad Avocado", "Egg Salad Dill", "Egg Salad Curried",
                "Ham Salad", "Bean Salad Three Bean", "Bean Salad Four Bean",
                "Quinoa Salad", "Couscous Salad", "Grain Salad",
                "Edamame Salad", "Fruit Salad Fresh", "Ambrosia Salad",
                "Waldorf Salad", "Carrot Raisin Salad", "Beet Salad",
                "Broccoli Salad", "Cucumber Salad", "Tomato Cucumber Salad",
                "Caprese Salad", "Greek Salad with Feta", "Mediterranean Salad",
                "Caesar Salad with Chicken", "Caesar Salad with Shrimp", "Chef Salad",
                "Cobb Salad", "Garden Salad", "House Salad",
                "Spinach Salad", "Arugula Salad", "Kale Salad",
                "Mixed Greens Salad", "Spring Mix Salad", "Rotisserie Chicken Lemon Herb",
                "Rotisserie Chicken BBQ", "Rotisserie Chicken Cajun", "Rotisserie Chicken Garlic",
                "Rotisserie Chicken Plain", "Fried Chicken Hot", "Fried Chicken Cold",
                "Fried Chicken Wings", "Fried Chicken Breast", "Fried Chicken Thighs",
                "Fried Chicken Legs", "Baked Chicken", "Grilled Chicken",
                "Prepared Ribs BBQ", "Prepared Pulled Pork", "Prepared Beef Brisket",
                "Prepared Turkey Breast Sliced", "Prepared Prime Rib Slices", "Prepared Pot Roast",
                "Prepared Meat Loaf", "Prepared Swedish Meatballs", "Prepared Italian Meatballs",
                "Prepared Stuffed Peppers", "Prepared Stuffed Cabbage", "Prepared Eggplant Parmesan",
                "Prepared Beef Stroganoff", "Prepared Salisbury Steak", "Prepared Stuffed Chicken Breast",
                "Prepared Chicken Cordon Bleu", "Prepared Chicken Marsala", "Prepared Chicken Piccata",
                "Prepared Chicken Alfredo", "Prepared Teriyaki Chicken", "Prepared Orange Chicken",
                "Prepared General Tso's Chicken", "Prepared Sesame Chicken", "Prepared Sweet & Sour Chicken",
                "Prepared Beef & Broccoli", "Prepared Lo Mein", "Prepared Fried Rice",
                "Prepared Mac & Cheese", "Prepared Baked Ziti", "Prepared Cheese Ravioli",
                "Prepared Meat Ravioli", "Prepared Tortellini", "Prepared Spaghetti & Meatballs",
                "Prepared Fettuccine Alfredo", "Prepared Garlic Bread", "Prepared Dinner Rolls",
                "Prepared Cornbread", "Prepared Biscuits", "Prepared Corn on the Cob",
                "Prepared Mashed Potatoes", "Prepared Roasted Potatoes", "Prepared Scalloped Potatoes",
                "Prepared Green Beans", "Prepared Glazed Carrots", "Prepared Mixed Vegetables",
                "Prepared Collard Greens", "Prepared Creamed Spinach", "Prepared Broccoli",
                "Prepared Cauliflower", "Prepared Brussels Sprouts", "Prepared Asparagus",
                "Prepared Vegetable Medley", "Prepared Baked Beans", "Prepared Black Beans",
                "Pre-made Ham & Cheese Sandwich", "Pre-made Roast Beef Sandwich", "Pre-made Club Sandwich",
                "Pre-made BLT Sandwich", "Pre-made Grilled Chicken Sandwich", "Pre-made Tuna Salad Sandwich",
                "Pre-made Chicken Salad Sandwich", "Pre-made Egg Salad Sandwich", "Pre-made PB&J Sandwich",
                "Pre-made Veggie Sandwich", "Pre-made Muffuletta Sandwich", "Pre-made Cubano Sandwich",
                "Pre-made Philly Cheesesteak", "Pre-made Reuben Sandwich", "Pre-made Buffalo Chicken Wrap",
                "Pre-made Chicken Caesar Wrap", "Pre-made Veggie Wrap", "Pre-made Greek Wrap",
                "Pre-made Turkey Bacon Ranch Wrap", "Pre-made Southwestern Wrap", "Pre-made Italian Hoagie",
                "Pre-made American Hoagie", "Pre-made Turkey Hoagie", "Pre-made Veggie Hoagie",
                "Sushi Philadelphia Roll", "Sushi Dragon Roll", "Sushi Shrimp Tempura Roll",
                "Sushi Spider Roll", "Sushi Dynamite Roll", "Sushi Caterpillar Roll",
                "Sushi Tiger Roll", "Sushi Alaska Roll", "Sushi Boston Roll",
                "Sushi Tuna Nigiri", "Sushi Salmon Nigiri", "Sushi Shrimp Nigiri",
                "Sushi Eel Nigiri", "Sushi Yellowtail Nigiri", "Sushi Octopus Nigiri",
                "Sushi Egg Nigiri", "Sushi Sashimi Platter", "Sushi Combo Platter",
                "Poke Bowl Salmon", "Poke Bowl Tuna", "Poke Bowl Shrimp",
                "Poke Bowl Chicken", "Poke Bowl Tofu", "Poke Bowl Veggie"
            ],
            "sizes": {
                "Sliced Turkey Breast": [
                    {"size": "0.5lb", "price_multiplier": 0.6},
                    {"size": "1lb", "price_multiplier": 1.0},
                    {"size": "1.5lb", "price_multiplier": 1.5}
                ],
                "Sliced Ham": [
                    {"size": "0.5lb", "price_multiplier": 0.6},
                    {"size": "1lb", "price_multiplier": 1.0},
                    {"size": "1.5lb", "price_multiplier": 1.5}
                ],
                "Sliced Roast Beef": [
                    {"size": "0.5lb", "price_multiplier": 0.6},
                    {"size": "1lb", "price_multiplier": 1.0},
                    {"size": "1.5lb", "price_multiplier": 1.5}
                ],
                "Salami Sliced": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "12oz", "price_multiplier": 1.5}
                ],
                "Cheddar Cheese Slices": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.8}
                ],
                "Swiss Cheese Slices": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.8}
                ],
                "Hummus Classic": [
                    {"size": "7oz", "price_multiplier": 0.7},
                    {"size": "10oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.5}
                ],
                "Deli Potato Salad": [
                    {"size": "0.5lb", "price_multiplier": 0.6},
                    {"size": "1lb", "price_multiplier": 1.0},
                    {"size": "2lb", "price_multiplier": 1.9}
                ],
                "Sushi California Roll": [
                    {"size": "6pc", "price_multiplier": 0.8},
                    {"size": "8pc", "price_multiplier": 1.0},
                    {"size": "12pc", "price_multiplier": 1.4}
                ],
                "Sushi Spicy Tuna Roll": [
                    {"size": "6pc", "price_multiplier": 0.8},
                    {"size": "8pc", "price_multiplier": 1.0},
                    {"size": "12pc", "price_multiplier": 1.4}
                ]
            }
        },
        
        "Canned Goods": {
            "price_range": (0.79, 4.99),
            "items": [
                "Canned Black Beans", "Canned Kidney Beans", "Canned Pinto Beans",
                "Canned Garbanzo Beans", "Canned Corn", "Canned Green Beans",
                "Canned Peas", "Canned Carrots", "Canned Diced Tomatoes",
                "Canned Crushed Tomatoes", "Canned Tomato Paste", "Canned Tomato Sauce",
                "Canned Tuna", "Canned Salmon", "Canned Chicken", "Canned Sardines",
                "Canned Chili", "Canned Beef Stew", "Canned Soup Chicken Noodle",
                "Canned Soup Tomato", "Canned Soup Cream Mushroom", "Canned Coconut Milk",
                "Canned Pumpkin", "Canned Peaches", "Canned Pears", "Canned Pineapple",
                "Canned Mandarin Oranges", "Canned Fruit Cocktail", "Canned Olives Sliced",
                "Canned Artichoke Hearts",
                "Canned Refried Beans", "Canned Lima Beans", "Canned White Beans",
                "Canned Baked Beans", "Canned Mixed Vegetables", "Canned Beets",
                "Canned Spinach", "Canned Mushrooms", "Canned Water Chestnuts",
                "Canned Bamboo Shoots", "Canned Soup Minestrone", "Canned Soup Clam Chowder",
                "Canned Soup French Onion", "Canned Soup Lentil", "Canned Chili Beans",
                "Canned Corned Beef Hash", "Canned Vienna Sausages", "Canned Mackerel",
                "Canned Anchovies", "Canned Clams", "Canned Crab Meat",
                "Canned Roast Beef", "Canned Ham", "Canned Spam",
                "Canned Tomato Sauce Italian Herbs", "Canned Tomatoes Fire Roasted",
                "Canned Spaghetti", "Canned Ravioli", "Canned Fruit Salad",
                "Canned Cranberry Sauce",
                "Canned Cannellini Beans", "Canned Navy Beans", "Canned Great Northern Beans",
                "Canned Black-Eyed Peas", "Canned Fava Beans", "Canned Lentils",
                "Canned Mixed Beans", "Canned Bean Salad", "Canned Adzuki Beans",
                "Canned Butter Beans", "Canned Kidney Beans Dark", "Canned Kidney Beans Light",
                "Canned Refried Black Beans", "Canned Refried Beans Fat Free", "Canned Refried Beans Spicy",
                "Canned Chili Beans Hot", "Canned Chili Beans Mild", "Canned Chili Beans Medium",
                "Canned Corn Cream Style", "Canned Corn Whole Kernel", "Canned Corn Mexican Style",
                "Canned Corn Fire Roasted", "Canned Green Beans French Style", "Canned Green Beans Cut",
                "Canned Green Beans Whole", "Canned Green Beans No Salt Added", "Canned Yellow Beans",
                "Canned Wax Beans", "Canned Italian Green Beans", "Canned Green Beans Organic",
                "Canned Peas Sweet", "Canned Peas & Carrots", "Canned Peas No Salt Added",
                "Canned Peas Early", "Canned Peas & Pearl Onions", "Canned Snap Peas",
                "Canned Carrots Sliced", "Canned Carrots Diced", "Canned Carrots Whole Baby",
                "Canned Carrots Julienned", "Canned Potatoes Whole", "Canned Potatoes Sliced",
                "Canned Potatoes Diced", "Canned New Potatoes", "Canned Sweet Potatoes",
                "Canned Yams", "Canned Pumpkin Pie Mix", "Canned Squash",
                "Canned Sauerkraut", "Canned Pickled Beets", "Canned Pickled Vegetables",
                "Canned Pickled Okra", "Canned Pickled Asparagus", "Canned Pickled Carrots",
                "Canned Asparagus", "Canned Okra", "Canned Collard Greens",
                "Canned Turnip Greens", "Canned Mustard Greens", "Canned Kale",
                "Canned Cabbage", "Canned Brussels Sprouts", "Canned Broccoli",
                "Canned Cauliflower", "Canned Zucchini", "Canned Yellow Squash", 
                "Canned Eggplant", "Canned Bell Peppers", "Canned Chili Peppers",
                "Canned Jalapenos", "Canned Green Chilies", "Canned Chipotle Peppers in Adobo",
                "Canned Roasted Red Peppers", "Canned Pimientos", "Canned Tomatoes Whole Peeled",
                "Canned Tomatoes Petite Diced", "Canned Tomatoes Italian Style", "Canned Tomatoes with Green Chilies",
                "Canned Tomatoes with Basil", "Canned Tomatoes with Garlic", "Canned Tomatoes San Marzano",
                "Canned Tomatoes Organic", "Canned Tomatoes Low Sodium", "Canned Tomato Puree",
                "Canned Tomato Sauce No Salt Added", "Canned Tomato Sauce Garlic & Onion", "Canned Tomato Sauce Basil & Garlic",
                "Canned Tomato Sauce Marinara", "Canned Tomato Sauce Pizza", "Canned Tomato Sauce Arrabbiata",
                "Canned Tomato Paste Italian", "Canned Tomato Paste Double Concentrated", "Canned Tomato Paste with Herbs",
                "Canned Salsa Mild", "Canned Salsa Medium", "Canned Salsa Hot",
                "Canned Salsa Verde", "Canned Enchilada Sauce Red", "Canned Enchilada Sauce Green",
                "Canned Taco Sauce", "Canned Sloppy Joe Sauce", "Canned Pasta Sauce Meat",
                "Canned Pasta Sauce Mushroom", "Canned Pasta Sauce Four Cheese", "Canned Pasta Sauce Garlic",
                "Canned Gravy Beef", "Canned Gravy Chicken", "Canned Gravy Turkey",
                "Canned Gravy Mushroom", "Canned Gravy Pork", "Canned Gravy Country",
                "Canned Soup Vegetable", "Canned Soup Beef", "Canned Soup Bean with Ham",
                "Canned Soup Chicken & Rice", "Canned Soup Chicken & Stars", "Canned Soup Cream of Chicken",
                "Canned Soup Cream of Celery", "Canned Soup Cream of Potato", "Canned Soup Cream of Broccoli",
                "Canned Soup Cream of Asparagus", "Canned Soup Broccoli Cheese", "Canned Soup Cheddar Cheese",
                "Canned Soup Split Pea", "Canned Soup Beef Barley", "Canned Soup Vegetable Beef",
                "Canned Soup Chicken Tortilla", "Canned Soup Black Bean", "Canned Soup Potato Leek",
                "Canned Soup Butternut Squash", "Canned Soup Tomato Basil", "Canned Soup Italian Wedding",
                "Canned Soup Chicken Corn Chowder", "Canned Soup Lobster Bisque", "Canned Soup New England Clam Chowder",
                "Canned Soup Manhattan Clam Chowder", "Canned Soup Crab", "Canned Soup Shrimp",
                "Canned Soup Miso", "Canned Soup Won Ton", "Canned Soup Hot & Sour",
                "Canned Soup Egg Drop", "Canned Chili Vegetarian", "Canned Chili Turkey",
                "Canned Chili White Chicken", "Canned Chili Beef", "Canned Chili Beef No Beans",
                "Canned Chili Beef & Beans", "Canned Chili Hot", "Canned Chili Mild",
                "Canned Chili White", "Canned Chili Green", "Canned Beef Stew with Vegetables",
                "Canned Chicken Stew", "Canned Turkey Stew", "Canned Vegetable Stew",
                "Canned Irish Stew", "Canned Brunswick Stew", "Canned Burgoo",
                "Canned Hash Beef", "Canned Hash Roast Beef", "Canned Hash Turkey",
                "Canned Corned Beef", "Canned Potted Meat", "Canned Deviled Ham",
                "Canned Luncheon Meat", "Canned Spam Lite", "Canned Spam Hot & Spicy",
                "Canned Spam Jalapeño", "Canned Spam Bacon", "Canned Spam Turkey",
                "Canned Vienna Sausages Chicken", "Canned Vienna Sausages BBQ", "Canned Vienna Sausages Smoked",
                "Canned Sausage Patties", "Canned Sausage Links", "Canned Liverwurst",
                "Canned Braunschweiger", "Canned Tamales", "Canned Menudo",
                "Canned Pozole", "Canned Chorizo", "Canned Meatballs",
                "Canned Meatballs Swedish", "Canned Meatballs Italian", "Canned Meatballs BBQ",
                "Canned Tuna in Water", "Canned Tuna in Oil", "Canned Tuna Chunk Light",
                "Canned Tuna Albacore", "Canned Tuna Yellow Fin", "Canned Tuna Solid White",
                "Canned Tuna Low Sodium", "Canned Tuna Flavored", "Canned Tuna Pouch",
                "Canned Salmon Pink", "Canned Salmon Red", "Canned Salmon Atlantic",
                "Canned Salmon Skinless Boneless", "Canned Salmon Smoked", "Canned Salmon With Skin & Bones",
                "Canned Sardines in Oil", "Canned Sardines in Water", "Canned Sardines in Mustard",
                "Canned Sardines in Tomato Sauce", "Canned Sardines Smoked", "Canned Sardines Spicy",
                "Canned Kippers", "Canned Herring", "Canned Herring in Wine Sauce",
                "Canned Anchovies Flat", "Canned Anchovies Rolled", "Canned Anchovies in Oil",
                "Canned Oysters", "Canned Mussels", "Canned Octopus",
                "Canned Squid", "Canned Shrimp", "Canned Crab Meat Lump",
                "Canned Crab Meat Claw", "Canned Lobster Meat", "Canned Smoked Trout",
                "Canned Smoked Oysters", "Canned Fish Curry", "Canned Evaporated Milk",
                "Canned Sweetened Condensed Milk", "Canned Coconut Milk Light", "Canned Coconut Cream",
                "Canned Cream of Coconut", "Canned Coconut Water", "Canned Almond Milk",
                "Canned Soy Milk", "Canned Goat Milk", "Canned Peaches Sliced",
                "Canned Peaches Halves", "Canned Peaches in Juice", "Canned Peaches in Syrup",
                "Canned Peaches Yellow", "Canned Peaches White", "Canned Pears Bartlett",
                "Canned Pears Asian", "Canned Pears Halves", "Canned Pears Diced",
                "Canned Pears in Juice", "Canned Pears in Syrup", "Canned Pineapple Chunks",
                "Canned Pineapple Slices", "Canned Pineapple Crushed", "Canned Pineapple Tidbits",
                "Canned Pineapple in Juice", "Canned Pineapple in Syrup", "Canned Mandarin Oranges in Juice",
                "Canned Mandarin Oranges in Syrup", "Canned Mandarin Oranges Light", "Canned Oranges",
                "Canned Grapefruit", "Canned Mixed Citrus", "Canned Lychee",
                "Canned Rambutan", "Canned Longan", "Canned Jackfruit",
                "Canned Young Jackfruit", "Canned Durian", "Canned Star Fruit",
                "Canned Guava", "Canned Mango", "Canned Mango Slices",
                "Canned Papaya", "Canned Apricots", "Canned Cherries",
                "Canned Cherries Pitted", "Canned Cherry Pie Filling", "Canned Apple Pie Filling",
                "Canned Blueberry Pie Filling", "Canned Blackberry Pie Filling", "Canned Strawberry Pie Filling",
                "Canned Peach Pie Filling", "Canned Mixed Berry Pie Filling", "Canned Apples",
                "Canned Apples Sliced", "Canned Apples Spiced", "Canned Applesauce",
                "Canned Applesauce Cinnamon", "Canned Applesauce Unsweetened", "Canned Figs",
                "Canned Prunes", "Canned Plums", "Canned Grapes",
                "Canned Fruit Cocktail in Juice", "Canned Fruit Cocktail in Syrup", "Canned Fruit Salad in Juice",
                "Canned Fruit Salad in Syrup", "Canned Tropical Fruit Salad", "Canned Mixed Fruit",
                "Canned Cranberry Sauce Whole Berry", "Canned Cranberry Sauce Jellied", "Canned Cranberry Sauce Organic",
                "Canned Olives Green", "Canned Olives Black", "Canned Olives Kalamata",
                "Canned Olives Stuffed", "Canned Olives Whole", "Canned Olives Pitted",
                "Canned Capers", "Canned Pickles Dill", "Canned Pickles Sweet",
                "Canned Pickles Bread & Butter", "Canned Pickle Relish", "Canned Sauerkraut Traditional",
                "Canned Sauerkraut Bavarian", "Canned Artichoke Hearts Marinated", "Canned Artichoke Hearts in Water",
                "Canned Artichoke Bottoms", "Canned Palm Hearts", "Canned Water Chestnuts Whole",
                "Canned Water Chestnuts Sliced", "Canned Bamboo Shoots Sliced", "Canned Bamboo Shoots Strips",
                "Canned Mushrooms Pieces", "Canned Mushrooms Whole", "Canned Mushrooms Stems & Pieces",
                "Canned Mushrooms Sliced", "Canned Mushrooms Straw", "Canned Mushrooms Portobellos",
                "Canned Mushrooms Shiitake", "Canned Kimchi", "Canned Sushi Ginger"
            ],
            "sizes": {
                "Canned Black Beans": [
                    {"size": "15oz", "price_multiplier": 1.0},
                    {"size": "29oz", "price_multiplier": 1.7}
                ],
                "Canned Kidney Beans": [
                    {"size": "15oz", "price_multiplier": 1.0},
                    {"size": "29oz", "price_multiplier": 1.7}
                ],
                "Canned Pinto Beans": [
                    {"size": "15oz", "price_multiplier": 1.0},
                    {"size": "29oz", "price_multiplier": 1.7}
                ],
                "Canned Diced Tomatoes": [
                    {"size": "14.5oz", "price_multiplier": 1.0},
                    {"size": "28oz", "price_multiplier": 1.8}
                ],
                "Canned Crushed Tomatoes": [
                    {"size": "14.5oz", "price_multiplier": 0.7},
                    {"size": "28oz", "price_multiplier": 1.0},
                    {"size": "106oz", "price_multiplier": 3.0}
                ],
                "Canned Tomato Paste": [
                    {"size": "6oz", "price_multiplier": 1.0},
                    {"size": "12oz", "price_multiplier": 1.8}
                ],
                "Canned Tuna": [
                    {"size": "5oz", "price_multiplier": 1.0},
                    {"size": "12oz", "price_multiplier": 1.9},
                    {"size": "66.5oz", "price_multiplier": 10.0}
                ],
                "Canned Soup Chicken Noodle": [
                    {"size": "10.5oz", "price_multiplier": 1.0},
                    {"size": "18.6oz", "price_multiplier": 1.6},
                    {"size": "26oz", "price_multiplier": 2.2}
                ],
                "Canned Peaches": [
                    {"size": "8.5oz", "price_multiplier": 0.7},
                    {"size": "15oz", "price_multiplier": 1.0},
                    {"size": "29oz", "price_multiplier": 1.8}
                ],
                "Canned Pineapple": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "20oz", "price_multiplier": 1.0},
                    {"size": "46oz", "price_multiplier": 2.0}
                ]
            }
        },
        
        "Dry Goods & Pasta": {
            "price_range": (0.99, 5.99),
        "items": [
            "White Rice", "Brown Rice", "Basmati Rice", "Jasmine Rice",
            "Quinoa", "Couscous", "Lentils Green", "Red Lentils",
            "Black Beans Dry", "Pinto Beans Dry", "Chickpeas Dry",
            "Kidney Beans Dry", "Rolled Oats", "Quick Oats", "Flour All-Purpose",
            "Flour Bread", "Sugar Granulated", "Sugar Brown", "Powdered Sugar",
            "Cornmeal", "Pancake Mix", "Baking Soda", "Baking Powder",
            "Yeast Instant", "Breadcrumbs", "Spaghetti", "Penne", "Rotini",
            "Macaroni", "Lasagna", "Ramen Noodles", "Rice Noodles",
            "Arborio Rice", "Wild Rice", "Sushi Rice", "Black Rice",
            "Orzo", "Barley", "Farro", "Bulgur Wheat",
            "Millet", "Amaranth", "Steel Cut Oats", "Fettuccine",
            "Linguine", "Bucatini", "Farfalle", "Rigatoni",
            "Tortellini Dry", "Ravioli Dry", "Israeli Couscous", "Tapioca Pearls",
            "Cornstarch", "Cake Flour", "Whole Wheat Flour", "Rye Flour",
            "Almond Flour", "Coconut Flour", "Gluten-Free Flour", "Sugar Raw",
            "Sugar Coconut", "Sugar Substitute", "Molasses", "Corn Syrup",
            "Chocolate Chips", "Panko Breadcrumbs", "Italian Breadcrumbs",
            "Valencia Rice", "Bomba Rice", "Calrose Rice", "Red Rice",
            "Purple Rice", "Glutinous Rice", "Parboiled Rice", "Instant Rice",
            "Rice Bran", "Tricolor Quinoa", "Red Quinoa", "Black Quinoa",
            "Pearl Couscous", "Whole Wheat Couscous", "Teff", "Spelt",
            "Kamut", "Buckwheat Groats", "Freekeh", "Wheat Berries",
            "Rye Berries", "Potato Starch", "Arrowroot Powder", "Tapioca Starch",
            "Rice Flour", "Semolina Flour", "Pastry Flour", "Self-Rising Flour",
            "00 Flour", "Masa Harina", "Oat Flour", "Spelt Flour",
            "Buckwheat Flour", "Chickpea Flour", "Cassava Flour", "Sorghum Flour",
            "Corn Flour", "Mochiko Sweet Rice Flour", "Rice Bran", "Wheat Germ",
            "Vital Wheat Gluten", "Xanthan Gum", "Psyllium Husk Powder", "Flaxseed Meal",
            "Chia Seeds", "Hemp Seeds", "Poppy Seeds", "Sesame Seeds",
            "Sunflower Seeds", "Pumpkin Seeds", "Caraway Seeds", "Fennel Seeds",
            "Anise Seeds", "Cream of Tartar", "Cream of Wheat", "Grits",
            "Polenta", "Pearl Tapioca", "Sago", "Black Beluga Lentils",
            "French Green Lentils", "Yellow Lentils", "Split Peas Green", "Split Peas Yellow",
            "Navy Beans Dry", "Great Northern Beans Dry", "Fava Beans Dry", "Lima Beans Dry",
            "Cannellini Beans Dry", "Black-Eyed Peas Dry", "Adzuki Beans Dry", "Mung Beans Dry",
            "Cranberry Beans Dry", "Pinto Beans Sprouting", "Lentils Sprouting", "Chickpeas Sprouting",
            "Sugar Demerara", "Sugar Turbinado", "Sugar Date", "Sugar Maple",
            "Sugar Muscovado", "Sugar Cane", "Honey Granules", "Agave Granules",
            "Monk Fruit Sweetener", "Erythritol", "Stevia Powder", "Date Sugar",
            "Brown Rice Syrup", "Maple Syrup", "Agave Syrup", "Date Syrup",
            "Honey", "Golden Syrup", "Malt Syrup", "High Maltose Corn Syrup",
            "Cane Syrup", "Sorghum Syrup", "Coconut Nectar", "Yacon Syrup",
            "Vanilla Extract", "Almond Extract", "Lemon Extract", "Mint Extract",
            "Orange Extract", "Coconut Extract", "Butter Extract", "Maple Extract",
            "Rum Extract", "Anise Extract", "Food Coloring", "Liquid Smoke",
            "Unsweetened Cocoa Powder", "Dutch Process Cocoa", "Cacao Powder", "Carob Powder",
            "White Chocolate Chips", "Dark Chocolate Chips", "Milk Chocolate Chips", "Butterscotch Chips",
            "Peanut Butter Chips", "Caramel Chips", "Espresso Chips", "Mini Chocolate Chips",
            "Chocolate Chunks", "Brownie Mix", "Cake Mix", "Cookie Mix",
            "Muffin Mix", "Biscuit Mix", "Pie Crust Mix", "Corn Bread Mix",
            "Pizza Dough Mix", "Bread Machine Mix", "Waffle Mix", "Scone Mix",
            "Gravy Mix", "Soup Mix", "Dip Mix", "Salad Dressing Mix",
            "Seasoning Mix", "Marinade Mix", "Sauce Mix", "Gelatin",
            "Pectin", "Agar Agar", "Nutritional Yeast", "Brewer's Yeast",
            "Active Dry Yeast", "Rapid Rise Yeast", "Sourdough Starter", "Baking Chocolate",
            "Cinnamon Sticks", "Vanilla Beans", "Broth Powder", "Bouillon Cubes",
            "Dried Mushrooms", "Dried Tomatoes", "Dried Onions", "Dried Garlic",
            "Dried Chilies", "Dried Bell Peppers", "Dried Herbs", "Dried Fruit",
            "Egg Replacer", "Protein Powder", "Powdered Milk", "Powdered Butter",
            "Powdered Cheese", "Powdered Eggs", "Powdered Peanut Butter", "Powdered Vinegar",
            "Angel Hair Pasta", "Vermicelli", "Capellini", "Spaghettini",
            "Thin Spaghetti", "Thick Spaghetti", "Bucatini", "Perciatelli",
            "Fedelini", "Trenette", "Linguine Fini", "Tagliatelle",
            "Fettuccine", "Pappardelle", "Mafaldine", "Reginette",
            "Fusilli", "Cavatappi", "Gemelli", "Strozzapreti",
            "Rotelle", "Radiatori", "Campanelle", "Casarecce",
            "Trofie", "Garganelli", "Penne Rigate", "Penne Lisce",
            "Ziti", "Rigatoni", "Tortiglioni", "Cannelloni",
            "Manicotti", "Jumbo Shells", "Medium Shells", "Small Shells",
            "Orecchiette", "Cavatelli", "Conchiglie", "Farfalle",
            "Farfalline", "Bow Tie Pasta", "Gigli", "Fusilli Bucati",
            "Ditalini", "Anelli", "Stelline", "Acini di Pepe",
            "Orzo", "Fregola", "Couscous", "Israeli Couscous",
            "Alphabet Pasta", "Pastina", "Quadrettini", "Tubettini",
            "Gnocchi Pasta", "Whole Wheat Pasta", "Gluten Free Pasta", "Protein Pasta",
            "Chickpea Pasta", "Lentil Pasta", "Black Bean Pasta", "Edamame Pasta",
            "Brown Rice Pasta", "Corn Pasta", "Quinoa Pasta", "Spinach Pasta",
            "Tomato Pasta", "Squid Ink Pasta", "Egg Noodles", "Wide Egg Noodles",
            "Lo Mein Noodles", "Chow Mein Noodles", "Soba Noodles", "Udon Noodles",
            "Somen Noodles", "Shirataki Noodles", "Vermicelli Rice Noodles", "Rice Stick Noodles",
            "Rice Paper Wrappers", "Wonton Wrappers", "Egg Roll Wrappers", "Dumpling Wrappers",
            "Lasagna Sheets", "No-Boil Lasagna", "Wide Rice Noodles", "Glass Noodles",
            "Cellophane Noodles", "Sweet Potato Noodles", "Potato Starch Noodles", "Kelp Noodles"
        ],
            "sizes": {
                "White Rice": [
                    {"size": "1lb", "price_multiplier": 0.6},
                    {"size": "2lb", "price_multiplier": 1.0},
                    {"size": "5lb", "price_multiplier": 2.2},
                    {"size": "20lb", "price_multiplier": 7.5}
                ],
                "Brown Rice": [
                    {"size": "1lb", "price_multiplier": 0.6},
                    {"size": "2lb", "price_multiplier": 1.0},
                    {"size": "5lb", "price_multiplier": 2.2}
                ],
                "Basmati Rice": [
                    {"size": "1lb", "price_multiplier": 0.6},
                    {"size": "2lb", "price_multiplier": 1.0},
                    {"size": "5lb", "price_multiplier": 2.2},
                    {"size": "10lb", "price_multiplier": 3.8}
                ],
                "Flour All-Purpose": [
                    {"size": "2lb", "price_multiplier": 0.5},
                    {"size": "5lb", "price_multiplier": 1.0},
                    {"size": "10lb", "price_multiplier": 1.9},
                    {"size": "25lb", "price_multiplier": 4.2}
                ],
                "Sugar Granulated": [
                    {"size": "1lb", "price_multiplier": 0.4},
                    {"size": "4lb", "price_multiplier": 1.0},
                    {"size": "10lb", "price_multiplier": 2.3}
                ],
                "Rolled Oats": [
                    {"size": "18oz", "price_multiplier": 0.6},
                    {"size": "42oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.5}
                ],
                "Spaghetti": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8}
                ],
                "Penne": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8}
                ],
                "Quinoa": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8}
                ],
                "Chocolate Chips": [
                    {"size": "6oz", "price_multiplier": 0.6},
                    {"size": "12oz", "price_multiplier": 1.0},
                    {"size": "24oz", "price_multiplier": 1.8}
                ]
            }
        },
        
        "Snacks": {
            "price_range": (0.99, 5.99),
        "items": [
            "Pretzels", "Popcorn Microwave", "Popcorn Kernels", "Potato Chips Original",
            "Potato Chips BBQ", "Tortilla Chips", "Pita Chips", "Corn Chips",
            "Cheese Crackers", "Whole Grain Crackers", "Rice Cakes Plain",
            "Rice Cakes Caramel", "Trail Mix", "Mixed Nuts", "Almonds Roasted",
            "Peanuts Salted", "Cashews", "Popcorn Ready-To-Eat", "Beef Jerky",
            "Turkey Jerky", "Snack Pack Pudding Chocolate", "Fruit Snacks",
            "Applesauce Cups", "Granola Bars Oats & Honey", "Protein Bars Chocolate",
            "Peanut Butter Crackers", "Cheese Sticks", "Veggie Straws",
            "Seaweed Snacks", "Pretzel Crisps", "Hummus & Pretzel Snack Pack",
            "Graham Crackers", "Animal Crackers", "Fruit Leather", "Pork Rinds",
            "Popcorn Seasoning Cheddar",
            "Cheese Puffs", "Chips Sour Cream & Onion", "Chips Salt & Vinegar",
            "Potato Chips Wavy", "Tortilla Chips Ranch", "Tortilla Chips Blue Corn",
            "Tortilla Chips Multigrain", "Pita Crackers", "Graham Cracker Sticks",
            "Cheese Straws", "Sesame Sticks", "Wasabi Peas", "Roasted Chickpeas",
            "Plantain Chips", "Rice Crackers", "Breadsticks", "Dried Mango",
            "Dried Apricots", "Dried Banana Chips", "Baked Cheese Crisps",
            "Kale Chips", "Sweet Potato Chips", "Veggie Chips", "Quinoa Chips",
            "Granola Clusters", "Protein Bites", "Yogurt Covered Pretzels",
            "Chocolate Covered Nuts", "Energy Balls", "Meat Sticks",
            "Pretzels Honey Mustard", "Pretzels Chocolate Covered", "Pretzels Peanut Butter Filled",
            "Pretzels Gluten Free", "Pretzels Sourdough", "Pretzels Soft Baked",
            "Popcorn Butter", "Popcorn Caramel", "Popcorn Kettle Corn",
            "Popcorn White Cheddar", "Popcorn Movie Theater", "Popcorn Sweet & Salty",
            "Popcorn Buffalo", "Popcorn Organic", "Popcorn Light",
            "Potato Chips Cheddar & Sour Cream", "Potato Chips Jalapeño", "Potato Chips Dill Pickle",
            "Potato Chips Honey BBQ", "Potato Chips Mesquite BBQ", "Potato Chips Ranch",
            "Potato Chips Loaded Baked Potato", "Potato Chips Lightly Salted", "Potato Chips No Salt",
            "Potato Chips Wavy Ranch", "Potato Chips Rippled", "Potato Chips Thick Cut",
            "Potato Chips Kettle Cooked", "Potato Chips Kettle Cooked Sea Salt", "Potato Chips Kettle Cooked Jalapeño",
            "Potato Chips Reduced Fat", "Potato Chips Sweet Potato", "Potato Chips Purple",
            "Potato Chips Truffle", "Potato Chips Parmesan Garlic", "Potato Chips Sriracha",
            "Tortilla Chips Lime", "Tortilla Chips Nacho Cheese", "Tortilla Chips Spicy Nacho",
            "Tortilla Chips Hint of Lime", "Tortilla Chips Queso", "Tortilla Chips Fiesta Ranch",
            "Tortilla Chips Organic", "Tortilla Chips White Corn", "Tortilla Chips Restaurant Style",
            "Tortilla Chips Cantina Style", "Tortilla Chips Thin & Crispy", "Corn Tortilla Strips",
            "Pita Chips Sea Salt", "Pita Chips Garlic Parmesan", "Pita Chips Everything",
            "Pita Chips Cinnamon Sugar", "Pita Chips Mediterranean Herb", "Pita Chips Multigrain",
            "Corn Chips Original", "Corn Chips BBQ", "Corn Chips Chili Cheese",
            "Corn Chips Ranch", "Corn Chips Flamin' Hot", "Corn Chips Lime & Chile",
            "Crackers Cheese Sandwich", "Crackers Cheese & Peanut Butter", "Crackers Cheese & Pepperoni",
            "Crackers Butter", "Crackers Whole Wheat", "Crackers Saltines",
            "Crackers Multigrain", "Crackers Rosemary & Olive Oil", "Crackers Sesame",
            "Crackers Club", "Crackers Crisp Bread", "Crackers Rye",
            "Crackers Water", "Crackers Wheat Thins", "Crackers Triscuit",
            "Crackers Cheez-It", "Crackers Goldfish", "Crackers Oyster",
            "Rice Cakes Apple Cinnamon", "Rice Cakes White Cheddar", "Rice Cakes Buttery",
            "Rice Cakes Chocolate", "Rice Cakes Mini", "Rice Cakes Brown Rice",
            "Trail Mix Energy", "Trail Mix Tropical", "Trail Mix Berry",
            "Trail Mix Chocolate", "Trail Mix Protein", "Trail Mix Nuts & Seeds",
            "Trail Mix Sweet & Salty", "Trail Mix Spicy", "Trail Mix Organic",
            "Trail Mix Omega-3", "Trail Mix Keto", "Trail Mix Mountain",
            "Mixed Nuts Deluxe", "Mixed Nuts Lightly Salted", "Mixed Nuts Honey Roasted",
            "Mixed Nuts Spicy", "Mixed Nuts Raw", "Mixed Nuts Dry Roasted",
            "Mixed Nuts Chocolate Covered", "Mixed Nuts Yogurt Covered", "Mixed Nuts Sweet & Spicy",
            "Almonds Raw", "Almonds Smoked", "Almonds Honey Roasted",
            "Almonds Cocoa Dusted", "Almonds Cinnamon", "Almonds Wasabi & Soy",
            "Almonds Salt & Vinegar", "Almonds BBQ", "Almonds Sriracha",
            "Peanuts Honey Roasted", "Peanuts Dry Roasted", "Peanuts Butter Toffee",
            "Peanuts Cajun", "Peanuts Hot & Spicy", "Peanuts Dill Pickle",
            "Peanuts Chili Lime", "Peanuts Chocolate Covered", "Peanuts Raw",
            "Cashews Honey Roasted", "Cashews Raw", "Cashews Sweet & Spicy",
            "Cashews Salted", "Cashews Chocolate Covered", "Cashews Yogurt Covered",
            "Beef Jerky Teriyaki", "Beef Jerky Peppered", "Beef Jerky Sweet & Spicy",
            "Beef Jerky Original", "Beef Jerky Spicy", "Beef Jerky Hickory Smoked",
            "Beef Sticks Original", "Beef Sticks Teriyaki", "Beef Sticks Hot",
            "Turkey Jerky Peppered", "Turkey Jerky Teriyaki", "Turkey Jerky Sweet & Spicy",
            "Turkey Sticks Original", "Venison Jerky", "Buffalo Jerky",
            "Salmon Jerky", "Tuna Jerky", "Pork Jerky",
            "Pudding Cups Vanilla", "Pudding Cups Banana", "Pudding Cups Butterscotch",
            "Pudding Cups Rice", "Pudding Cups Tapioca", "Pudding Cups Chocolate Fudge",
            "Fruit Snacks Mixed Berry", "Fruit Snacks Tropical", "Fruit Snacks Organic",
            "Fruit Snacks Sour", "Fruit Snacks Shapes", "Fruit Snacks Characters",
            "Applesauce Unsweetened", "Applesauce Cinnamon", "Applesauce Strawberry",
            "Applesauce Mixed Berry", "Applesauce Peach", "Applesauce Pouches",
            "Granola Bars Chocolate Chip", "Granola Bars Peanut Butter", "Granola Bars Almond",
            "Granola Bars Sweet & Salty", "Granola Bars Chewy", "Granola Bars Crunchy",
            "Protein Bars Peanut Butter", "Protein Bars Cookies & Cream", "Protein Bars Caramel",
            "Protein Bars Birthday Cake", "Protein Bars Chocolate Mint", "Protein Bars Coffee",
            "Energy Bars Apple Pie", "Energy Bars Cherry Pie", "Energy Bars Pumpkin Pie",
            "Energy Bars Banana Bread", "Cereal Bars Blueberry", "Cereal Bars Strawberry",
            "Cereal Bars Apple", "Breakfast Bars", "Diet Bars",
            "Nut Bars Almond", "Nut Bars Cashew", "Nut Bars Mixed Nuts",
            "Seaweed Snacks Wasabi", "Seaweed Snacks Teriyaki", "Seaweed Snacks Chili",
            "Hummus Snack Pack Classic", "Hummus Snack Pack Roasted Red Pepper", "Hummus Snack Pack Roasted Garlic",
            "Hummus Snack Pack Everything Bagel", "Veggie & Ranch Snack Pack", "Carrots & Ranch Snack Pack",
            "Celery & Peanut Butter Snack Pack", "Apples & Caramel Snack Pack", "Cheese & Crackers Snack Pack",
            "Graham Crackers Honey", "Graham Crackers Cinnamon", "Graham Crackers Chocolate",
            "Animal Crackers Chocolate", "Animal Crackers Iced", "Animal Crackers Organic",
            "Fig Bars", "Date Bars", "Marshmallows",
            "Rice Krispie Treats", "Crispy Rice Treats", "Chocolate Covered Pretzels",
            "Chocolate Covered Raisins", "Chocolate Covered Espresso Beans", "Chocolate Covered Almonds",
            "Chocolate Covered Peanuts", "Chocolate Covered Graham Crackers", "Chocolate Covered Blueberries",
            "Dried Cranberries", "Dried Blueberries", "Dried Cherries",
            "Dried Strawberries", "Dried Apple Rings", "Dried Pineapple",
            "Dried Kiwi", "Dried Papaya", "Dried Peaches",
            "Dried Dates", "Dried Figs", "Dried Plums",
            "Freeze Dried Strawberries", "Freeze Dried Bananas", "Freeze Dried Blueberries",
            "Freeze Dried Mango", "Freeze Dried Mixed Fruit", "Freeze Dried Vegetables",
            "Baked Cheese Crisps Parmesan", "Baked Cheese Crisps Cheddar", "Baked Cheese Crisps Jalapeno",
            "Moon Cheese", "Whisps", "Just The Cheese",
            "Sunflower Seeds Salted", "Sunflower Seeds BBQ", "Sunflower Seeds Ranch",
            "Pumpkin Seeds Salted", "Pumpkin Seeds Spicy", "Pumpkin Seeds Cinnamon Sugar",
            "Pistachios Salted", "Pistachios Chili Lime", "Pistachios Sweet Chili",
            "Macadamia Nuts", "Brazil Nuts", "Hazelnuts",
            "Walnuts", "Pecans", "Pine Nuts"
        ],
            "sizes": {
                "Potato Chips Original": [
                    {"size": "1.5oz", "price_multiplier": 0.3},
                    {"size": "9oz", "price_multiplier": 1.0},
                    {"size": "15.5oz", "price_multiplier": 1.6}
                ],
                "Potato Chips BBQ": [
                    {"size": "1.5oz", "price_multiplier": 0.3},
                    {"size": "9oz", "price_multiplier": 1.0},
                    {"size": "15.5oz", "price_multiplier": 1.6}
                ],
                "Tortilla Chips": [
                    {"size": "5.5oz", "price_multiplier": 0.6},
                    {"size": "13oz", "price_multiplier": 1.0},
                    {"size": "18oz", "price_multiplier": 1.4}
                ],
                "Pretzels": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8}
                ],
                "Trail Mix": [
                    {"size": "6oz", "price_multiplier": 0.5},
                    {"size": "14oz", "price_multiplier": 1.0},
                    {"size": "26oz", "price_multiplier": 1.8}
                ],
                "Mixed Nuts": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.9}
                ],
                "Popcorn Microwave": [
                    {"size": "3ct", "price_multiplier": 1.0},
                    {"size": "6ct", "price_multiplier": 1.7},
                    {"size": "12ct", "price_multiplier": 3.0}
                ],
                "Beef Jerky": [
                    {"size": "1oz", "price_multiplier": 0.4},
                    {"size": "3oz", "price_multiplier": 1.0},
                    {"size": "8oz", "price_multiplier": 2.5}
                ],
                "Granola Bars Oats & Honey": [
                    {"size": "6ct", "price_multiplier": 0.7},
                    {"size": "10ct", "price_multiplier": 1.0},
                    {"size": "18ct", "price_multiplier": 1.7}
                ],
                "Protein Bars Chocolate": [
                    {"size": "4ct", "price_multiplier": 0.7},
                    {"size": "6ct", "price_multiplier": 1.0},
                    {"size": "12ct", "price_multiplier": 1.9}
                ]
            }
        },
        
        "Frozen Food": {
            "price_range": (1.29, 8.99),
            "items": [
                "Frozen Mixed Vegetables", "Frozen Broccoli Florets", "Frozen Corn Kernels",
                "Frozen Peas", "Frozen Spinach", "Frozen Edamame", "Frozen Strawberries",
                "Frozen Blueberries", "Frozen Mango Chunks", "Frozen Waffles",
                "Frozen Pancakes", "Frozen French Fries", "Frozen Sweet Potato Fries",
                "Frozen Onion Rings", "Frozen Chicken Nuggets", "Frozen Chicken Tenders",
                "Frozen Veggie Burger", "Frozen Lasagna", "Frozen Burritos Bean",
                "Frozen Pot Pie Chicken", "Frozen Pizza Cheese", "Frozen Pizza Pepperoni",
                "Ice Cream Vanilla", "Ice Cream Chocolate", "Ice Pops Assorted",
                "Frozen Yogurt Strawberry", "Frozen Meatballs", "Frozen Shrimp Cooked",
                "Frozen Salmon Fillets", "Frozen Dumplings",
                "Frozen Pizza Rolls", "Frozen Garlic Bread", "Frozen Breakfast Sandwiches",
                "Frozen Spring Rolls Vegetable", "Frozen Egg Rolls Pork", "Frozen Quesadillas Cheese",
                "Frozen Naan", "Frozen Vegetable Stir Fry Mix", "Frozen Acai Packs",
                "Frozen Fruit Popsicles", "Frozen Fruit Bars Mango", "Frozen Cheesecake Slices",
                "Frozen Cookie Dough", "Frozen Pie Crust Shells", "Frozen Orange Juice Concentrate",
                "Frozen Breakfast Bowls", "Frozen Fish Sticks", "Frozen Stuffed Peppers",
                "Frozen Stuffed Shells", "Frozen Tater Tots", "Frozen Chicken Pot Stickers",
                "Frozen Vegetable Medley", "Frozen Cauliflower Rice", "Frozen Breakfast Burritos",
                "Frozen Pizza Supreme", "Frozen Ice Cream Sandwiches", "Frozen Pie Blueberry",
                "Frozen Pie Apple", "Frozen Hash Browns", "Frozen Broccoli Cheese Bites",
                "Frozen Asparagus Spears", "Frozen Green Beans", "Frozen Carrot Slices",
                "Frozen Brussels Sprouts", "Frozen Butternut Squash", "Frozen Kale",
                "Frozen Okra", "Frozen Bell Peppers", "Frozen Onions Diced",
                "Frozen Mushrooms", "Frozen Artichoke Hearts", "Frozen Zucchini Slices",
                "Frozen Riced Vegetables", "Frozen Vegetable Spirals", "Frozen Vegetable Pasta",
                "Frozen Vegetable Protein Blend", "Frozen Power Greens Mix", "Frozen Roasted Vegetables",
                "Frozen Succotash", "Frozen Lima Beans", "Frozen Black-Eyed Peas",
                "Frozen Collard Greens", "Frozen Southwest Blend", "Frozen Mediterranean Blend",
                "Frozen Asian Vegetable Blend", "Frozen California Blend", "Frozen Italian Blend",
                "Frozen Soup Vegetables", "Frozen Grilled Vegetables", "Frozen Seasoned Vegetables",
                "Frozen Raspberries", "Frozen Blackberries", "Frozen Mixed Berries",
                "Frozen Cherries", "Frozen Peaches", "Frozen Pineapple Chunks",
                "Frozen Banana Slices", "Frozen Pomegranate Arils", "Frozen Kiwi Slices",
                "Frozen Avocado Chunks", "Frozen Melon Mix", "Frozen Apple Slices",
                "Frozen Fruit Smoothie Mix", "Frozen Berry Medley", "Frozen Tropical Fruit Mix",
                "Frozen Watermelon Chunks", "Frozen Dragon Fruit", "Frozen Pitaya Packs",
                "Frozen Coconut Chunks", "Frozen Fruit Sorbet", "Frozen Berry Compote",
                "Frozen Belgian Waffles", "Frozen Protein Waffles", "Frozen Gluten-Free Waffles",
                "Frozen Blueberry Waffles", "Frozen Cinnamon Waffles", "Frozen Buttermilk Pancakes",
                "Frozen Blueberry Pancakes", "Frozen Chocolate Chip Pancakes", "Frozen Silver Dollar Pancakes",
                "Frozen Protein Pancakes", "Frozen French Toast", "Frozen French Toast Sticks",
                "Frozen Cinnamon Rolls", "Frozen Croissants", "Frozen Buttermilk Biscuits",
                "Frozen Dinner Rolls", "Frozen Breadsticks", "Frozen Texas Toast",
                "Frozen Waffle Fries", "Frozen Curly Fries", "Frozen Steak Fries",
                "Frozen Crinkle Cut Fries", "Frozen Shoestring Fries", "Frozen Seasoned Fries",
                "Frozen Potato Wedges", "Frozen Potato Skins", "Frozen Loaded Potato Bites",
                "Frozen Mashed Potatoes", "Frozen Twice Baked Potatoes", "Frozen Potato Pancakes",
                "Frozen Potato Puffs", "Frozen Potato Croquettes", "Frozen Potato Patties",
                "Frozen Corn Dogs", "Frozen Mini Corn Dogs", "Frozen Chicken Wings Buffalo",
                "Frozen Chicken Wings BBQ", "Frozen Chicken Patties", "Frozen Chicken Strips",
                "Frozen Breaded Chicken Breasts", "Frozen Grilled Chicken Strips", "Frozen Chicken Fajita Strips",
                "Frozen Chicken Alfredo", "Frozen Turkey Burgers", "Frozen Beef Burgers",
                "Frozen Black Bean Burgers", "Frozen Plant Protein Burgers", "Frozen Impossible Burgers",
                "Frozen Beyond Burgers", "Frozen Buffalo Chicken Dip", "Frozen Spinach Artichoke Dip",
                "Frozen Mozzarella Sticks", "Frozen Jalapeno Poppers", "Frozen Potato Skins Loaded",
                "Frozen Nachos", "Frozen Cheese Sticks", "Frozen Breaded Mushrooms",
                "Frozen Chicken Quesadillas", "Frozen Mac and Cheese Bites", "Frozen Fried Pickles",
                "Frozen Cheeseburger Sliders", "Frozen Buffalo Cauliflower", "Frozen Blooming Onion",
                "Frozen Macaroni and Cheese", "Frozen Fettuccine Alfredo", "Frozen Spaghetti and Meatballs",
                "Frozen Penne Vodka", "Frozen Beef Ravioli", "Frozen Cheese Ravioli",
                "Frozen Beef Tortellini", "Frozen Cheese Tortellini", "Frozen Gnocchi",
                "Frozen Chicken Parmesan", "Frozen Eggplant Parmesan", "Frozen Shrimp Scampi",
                "Frozen Tuna Noodle Casserole", "Frozen Chicken Enchiladas", "Frozen Beef Enchiladas",
                "Frozen Cheese Enchiladas", "Frozen Beef Tacos", "Frozen Chicken Tacos",
                "Frozen Burritos Beef", "Frozen Burritos Chicken", "Frozen Breakfast Sandwich Egg & Cheese",
                "Frozen Breakfast Sandwich Sausage", "Frozen Breakfast Sandwich Bacon", "Frozen Breakfast Skillet",
                "Frozen Breakfast Hash", "Frozen Quiche Lorraine", "Frozen Quiche Florentine",
                "Frozen Broccoli Cheddar Soup", "Frozen Chicken Noodle Soup", "Frozen Minestrone Soup",
                "Frozen Clam Chowder", "Frozen Beef Stew", "Frozen Chili",
                "Frozen Chicken Marsala", "Frozen Beef Stroganoff", "Frozen Salisbury Steak",
                "Frozen Swedish Meatballs", "Frozen Meatloaf", "Frozen Pot Roast",
                "Frozen Orange Chicken", "Frozen General Tso's Chicken", "Frozen Beef & Broccoli",
                "Frozen Sweet & Sour Chicken", "Frozen Kung Pao Chicken", "Frozen Teriyaki Chicken",
                "Frozen Fried Rice", "Frozen Lo Mein", "Frozen Pad Thai",
                "Frozen Vegetable Potstickers", "Frozen Pork Potstickers", "Frozen Shrimp Potstickers",
                "Frozen Crab Rangoon", "Frozen Vegetable Samosas", "Frozen Vegetable Pakoras",
                "Frozen Cheese Pizzas", "Frozen Veggie Pizzas", "Frozen Meat Lovers Pizza",
                "Frozen BBQ Chicken Pizza", "Frozen Four Cheese Pizza", "Frozen Margherita Pizza",
                "Frozen Gluten-Free Pizza", "Frozen Cauliflower Crust Pizza", "Frozen Pizza Bagels",
                "Frozen Calzones", "Frozen Stromboli", "Frozen Pizza Bites",
                "Frozen Turkey Pot Pie", "Frozen Beef Pot Pie", "Frozen Vegetable Pot Pie",
                "Frozen Shepherd's Pie", "Frozen Chicken Cordon Bleu", "Frozen Stuffed Chicken Breast",
                "Frozen Ice Cream Chocolate Chip", "Frozen Ice Cream Cookies & Cream", "Frozen Ice Cream Mint Chocolate Chip",
                "Frozen Ice Cream Strawberry", "Frozen Ice Cream Cookie Dough", "Frozen Ice Cream Butter Pecan",
                "Frozen Ice Cream Coffee", "Frozen Ice Cream Rocky Road", "Frozen Ice Cream Neapolitan",
                "Frozen Ice Cream Fudge Ripple", "Frozen Ice Cream Non-Dairy Vanilla", "Frozen Ice Cream Non-Dairy Chocolate",
                "Frozen Gelato Pistachio", "Frozen Gelato Chocolate", "Frozen Gelato Stracciatella",
                "Frozen Sherbet Rainbow", "Frozen Sherbet Orange", "Frozen Sherbet Lime",
                "Frozen Sorbet Lemon", "Frozen Sorbet Raspberry", "Frozen Sorbet Mango",
                "Frozen Yogurt Vanilla", "Frozen Yogurt Blueberry", "Frozen Yogurt Peach",
                "Frozen Tiramisu", "Frozen Chocolate Lava Cake", "Frozen Chocolate Mousse Cake",
                "Frozen Carrot Cake", "Frozen Red Velvet Cake", "Frozen New York Style Cheesecake",
                "Frozen Strawberry Cheesecake", "Frozen Turtle Cheesecake", "Frozen Chocolate Chip Cookie Dough",
                "Frozen Sugar Cookie Dough", "Frozen Peanut Butter Cookie Dough", "Frozen Oatmeal Raisin Cookie Dough",
                "Frozen Puff Pastry Sheets", "Frozen Phyllo Dough", "Frozen Pizza Dough",
                "Frozen Bread Dough", "Frozen Cinnamon Roll Dough", "Frozen Pretzel Dough"
            ],
            "sizes": {
                "Frozen Mixed Vegetables": [
                    {"size": "10oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.8}
                ],
                "Frozen French Fries": [
                    {"size": "19oz", "price_multiplier": 0.7},
                    {"size": "32oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 1.5}
                ],
                "Frozen Pizza Cheese": [
                    {"size": "6in", "price_multiplier": 0.5},
                    {"size": "12in", "price_multiplier": 1.0},
                    {"size": "16in", "price_multiplier": 1.8}
                ],
                "Ice Cream Vanilla": [
                    {"size": "16oz", "price_multiplier": 0.6},
                    {"size": "48oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.3},
                    {"size": "128oz", "price_multiplier": 2.5}
                ],
                "Frozen Chicken Nuggets": [
                    {"size": "12oz", "price_multiplier": 0.5},
                    {"size": "29oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 1.6}
                ],
                "Frozen Lasagna": [
                    {"size": "10oz", "price_multiplier": 0.4},
                    {"size": "38oz", "price_multiplier": 1.0},
                    {"size": "96oz", "price_multiplier": 2.3}
                ],
                "Frozen Meatballs": [
                    {"size": "14oz", "price_multiplier": 0.6},
                    {"size": "26oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 1.8}
                ],
                "Frozen Blueberries": [
                    {"size": "10oz", "price_multiplier": 0.7},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 2.7}
                ],
                "Frozen Shrimp Cooked": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.9}
                ],
                "Frozen Cookie Dough": [
                    {"size": "12oz", "price_multiplier": 0.8},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "30oz", "price_multiplier": 1.8}
                ]
            }
        },
        
        "Dairy & Eggs": {
            "price_range": (1.49, 6.99),
            "items": [
                "Butter Unsalted", "Butter Salted", "Cheddar Cheese Block", "Mozzarella Shredded",
                "Monterey Jack Cheese", "Parmesan Cheese Grated", "Swiss Cheese Slices",
                "American Cheese Singles", "Cottage Cheese", "Sour Cream", "Cream Cheese",
                "Greek Yogurt Plain", "Yogurt Strawberry", "Half & Half", "Heavy Cream",
                "Large Eggs", "Cage Free Eggs", "Egg Whites Carton", "Whipped Cream",
                "Chocolate Milk", "Lactose Free Milk", "String Cheese", "Feta Cheese Crumbles",
                "Goat Cheese Log",
                "Almond Milk Yogurt", "Coconut Milk Yogurt", "Kefir Plain",
                "Ricotta Cheese", "Mascarpone Cheese", "Blue Cheese Crumbles",
                "Brie Wheel", "Camembert Wheel", "Gouda Cheese", "Gruyere Cheese",
                "Burrata", "Queso Fresco", "Cotija Cheese", "Buttermilk",
                "Duck Eggs", "Quail Eggs", "Vegan Cheese Slices", "Vegan Butter",
                "Whey Protein Shake", "Ghee", "Provolone Cheese Slices", "Havarti Cheese",
                "Greek Yogurt Vanilla", "Greek Yogurt Blueberry", "Yogurt Drinks",
                "Medium Eggs", "Extra Large Eggs", "Jumbo Eggs", "Organic Eggs",
                "Mozzarella Cheese Fresh", "Ricotta Salata", "Asiago Cheese",
                "Whole Milk", "2% Milk", "1% Milk", "Skim Milk", "Raw Milk",
                "Oat Milk", "Almond Milk Unsweetened", "Almond Milk Vanilla", "Coconut Milk",
                "Soy Milk Plain", "Soy Milk Vanilla", "Rice Milk", "Cashew Milk",
                "Macadamia Milk", "Hemp Milk", "Pea Milk", "Flax Milk", "Banana Milk",
                "Goat Milk", "Sheep Milk", "Buffalo Milk", "A2 Milk",
                "Evaporated Milk", "Sweetened Condensed Milk", "Powdered Milk", "Malted Milk",
                "Barista Blend Oat Milk", "Barista Blend Almond Milk", "Buttermilk Powder",
                "Half & Half Fat Free", "Light Cream", "Table Cream", "Clotted Cream",
                "Crème Fraîche", "Mascarpone", "Cultured Butter", "European Style Butter",
                "Grass-Fed Butter", "Butter Quarters", "Butter Sticks", "Whipped Butter",
                "Dairy-Free Butter", "Plant-Based Butter", "Butter with Olive Oil", "Butter with Canola Oil",
                "Clarified Butter", "Brown Butter", "Flavored Butter Garlic", "Flavored Butter Herb",
                "Yogurt Plain", "Yogurt Vanilla", "Yogurt Peach", "Yogurt Blueberry",
                "Yogurt Mixed Berry", "Yogurt Honey", "Yogurt Banana", "Yogurt Cherry",
                "Yogurt Low-Fat", "Yogurt Non-Fat", "Yogurt Full-Fat", "Yogurt Whole Milk",
                "Greek Yogurt Honey", "Greek Yogurt Cherry", "Greek Yogurt Peach", "Greek Yogurt Mixed Berry",
                "Greek Yogurt 2%", "Greek Yogurt 0%", "Greek Yogurt Whole Milk", "Icelandic Yogurt Plain",
                "Icelandic Yogurt Vanilla", "Icelandic Yogurt Mixed Berry", "Australian Yogurt", "French Style Yogurt",
                "Yogurt Tubes", "Yogurt Cups Kids", "Drinkable Yogurt", "Kefir Strawberry",
                "Kefir Blueberry", "Kefir Raspberry", "Lassi Mango", "Lassi Plain",
                "Ayran", "Filmjölk", "Viili", "Skyr Plain",
                "Skyr Vanilla", "Skyr Mixed Berry", "Quark Plain", "Quark Vanilla",
                "Cottage Cheese Low Fat", "Cottage Cheese 4%", "Cottage Cheese 2%", "Cottage Cheese 1%",
                "Cottage Cheese Pineapple", "Cottage Cheese Chive", "Ricotta Part Skim", "Ricotta Whole Milk",
                "Cream Cheese Regular", "Cream Cheese Whipped", "Cream Cheese Light", "Cream Cheese Fat Free",
                "Cream Cheese Strawberry", "Cream Cheese Chive & Onion", "Cream Cheese Veggie", "Cream Cheese Honey Walnut",
                "Neufchâtel Cheese", "Fromage Blanc", "Sour Cream Regular", "Sour Cream Light",
                "Sour Cream Fat Free", "Sour Cream Cultured", "Crema Mexicana", "Creme Fraiche",
                "Cultured Cream", "Whipped Topping Dairy", "Whipped Topping Non-Dairy", "Whipped Cream Light",
                "Whipped Cream Extra Creamy", "Cheddar Cheese Mild", "Cheddar Cheese Sharp", "Cheddar Cheese Extra Sharp",
                "Cheddar Cheese White", "Cheddar Cheese Slices", "Cheddar Cheese Shredded", "Cheddar Cheese Snack Size",
                "Colby Cheese", "Colby Jack Cheese", "Pepper Jack Cheese", "Muenster Cheese",
                "Swiss Cheese Baby", "Swiss Cheese Block", "Emmental Cheese", "Jarlsberg Cheese",
                "Parmesan Cheese Block", "Parmesan Cheese Shaved", "Parmesan Cheese Wedge", "Pecorino Romano Cheese",
                "Grana Padano Cheese", "Mozzarella Cheese Block", "Mozzarella Cheese Balls", "Mozzarella Cheese Sticks",
                "Mozzarella Cheese Slices", "Provolone Cheese Block", "Smoked Provolone Cheese", "Fontina Cheese",
                "Gouda Cheese Baby", "Gouda Cheese Smoked", "Gouda Cheese Aged", "Edam Cheese",
                "Gruyère Cheese Block", "Comte Cheese", "Manchego Cheese", "Roquefort Cheese",
                "Gorgonzola Cheese", "Stilton Cheese", "Blue Cheese Danish", "Blue Cheese French",
                "Feta Cheese Block", "Feta Cheese Marinated", "Halloumi Cheese", "Queso Blanco",
                "Queso Oaxaca", "Panela Cheese", "Asadero Cheese", "Chihuahua Cheese",
                "Farmer Cheese", "Brick Cheese", "Limburger Cheese", "Port Salut Cheese",
                "Raclette Cheese", "Taleggio Cheese", "Chèvre Cheese", "Bucheron Cheese",
                "Crottin Cheese", "Goat Cheese Crumbles", "Cream Cheese Plant-Based", "Mozzarella Cheese Plant-Based",
                "Cheddar Cheese Plant-Based", "American Cheese Plant-Based", "Parmesan Cheese Plant-Based", "Feta Cheese Plant-Based",
                "Brown Eggs", "White Eggs", "Blue Eggs", "Green Eggs",
                "Fertile Eggs", "Pasture-Raised Eggs", "Free Range Eggs", "Grain-Fed Eggs",
                "Organic Egg Whites", "Powdered Eggs", "Liquid Eggs Whole", "Hard Boiled Eggs",
                "Deviled Eggs", "Egg Yolks Carton", "Quail Eggs Canned", "Turkey Eggs",
                "Goose Eggs", "Emu Eggs", "Ostrich Eggs", "Balut",
                "Century Eggs", "Salted Duck Eggs", "Tea Eggs", "Pickled Eggs"
            ],
            "sizes": {
                "Butter Unsalted": [
                    {"size": "4oz", "price_multiplier": 0.4},
                    {"size": "8oz", "price_multiplier": 0.7},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.9}
                ],
                "Butter Salted": [
                    {"size": "4oz", "price_multiplier": 0.4},
                    {"size": "8oz", "price_multiplier": 0.7},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.9}
                ],
                "Cheddar Cheese Block": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.8},
                    {"size": "32oz", "price_multiplier": 3.0}
                ],
                "Sour Cream": [
                    {"size": "8oz", "price_multiplier": 0.7},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "24oz", "price_multiplier": 1.4}
                ],
                "Cream Cheese": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.8}
                ],
                "Greek Yogurt Plain": [
                    {"size": "6oz", "price_multiplier": 0.4},
                    {"size": "16oz", "price_multiplier": 0.7},
                    {"size": "32oz", "price_multiplier": 1.0},
                    {"size": "48oz", "price_multiplier": 1.4}
                ],
                "Yogurt Strawberry": [
                    {"size": "6oz", "price_multiplier": 1.0},
                    {"size": "24oz", "price_multiplier": 3.3},
                    {"size": "32oz", "price_multiplier": 4.2}
                ],
                "Cottage Cheese": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "24oz", "price_multiplier": 1.4}
                ],
                "Half & Half": [
                    {"size": "16oz", "price_multiplier": 0.7},
                    {"size": "32oz", "price_multiplier": 1.0},
                    {"size": "64oz", "price_multiplier": 1.7}
                ],
                "Large Eggs": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "18ct", "price_multiplier": 1.4},
                    {"size": "24ct", "price_multiplier": 1.8},
                    {"size": "60ct", "price_multiplier": 4.2}
                ]
            }
        },
        
        "Meat": {
            "price_range": (2.49, 12.99),
            "per_lb": True,
            "items": [
                "Chicken Breast Boneless Skinless", "Chicken Thighs Bone-In", "Whole Chicken",
                "Ground Chicken", "Ground Turkey", "Ground Beef 80/20", "Ground Beef 93/7",
                "Beef Chuck Roast", "Beef Ribeye Steak", "Beef New York Strip Steak", "Beef Brisket",
                "Pork Loin Chop", "Pork Shoulder", "Pork Spare Ribs", "Bacon Thick Cut",
                "Italian Sausage", "Turkey Bacon", "Lamb Leg", "Lamb Shoulder", "Veal Cutlet",
                "Corned Beef", "Ham Steak", "Duck Breast", "Chicken Drumsticks", "Beef Short Ribs",
                "Beef Sirloin Steak", "Beef Filet Mignon", "Beef Skirt Steak", "Beef Flank Steak",
                "Beef Tri-Tip", "Beef Stew Meat", "Beef Liver", "Veal Shanks", "Pork Tenderloin",
                "Pork Belly", "Lamb Chops", "Lamb Shanks", "Ground Lamb", "Ground Bison",
                "Bison Steak", "Venison", "Turkey Breast", "Turkey Wings", "Chicken Livers",
                "Quail Whole", "Chicken Wings", "Chicken Quarters", "Turkey Thighs",
                "Pork Ribs Baby Back", "Pork Chops Boneless", "Breakfast Sausage Links",
                "Breakfast Sausage Patties", "Bratwurst", "Chorizo Sausage", "Kielbasa",
                "Chicken Tenders", "Chicken Gizzards", "Chicken Hearts", "Chicken Feet",
                "Cornish Game Hen", "Turkey Drumsticks", "Turkey Ground Dark Meat", "Turkey Cutlets",
                "Turkey Tenderloins", "Turkey Liver", "Turkey Necks", "Turkey Whole",
                "Beef Chuck Steak", "Beef Bottom Round Roast", "Beef Rump Roast", "Beef Eye of Round Roast",
                "Beef Top Round Steak", "Beef London Broil", "Beef Cube Steak", "Beef Tenderloin Whole",
                "Beef T-Bone Steak", "Beef Porterhouse Steak", "Beef Prime Rib Roast", "Beef Standing Rib Roast",
                "Beef Flat Iron Steak", "Beef Denver Steak", "Beef Hanger Steak", "Beef Bavette Steak",
                "Beef Shank", "Beef Oxtail", "Beef Tongue", "Beef Heart",
                "Beef Kidney", "Beef Suet", "Beef Marrow Bones", "Beef Soup Bones",
                "Beef Cheeks", "Beef Back Ribs", "Beef Plate Ribs", "Beef Neck Bones",
                "Ground Beef 70/30", "Ground Beef 85/15", "Ground Beef Grass-Fed", "Ground Beef Wagyu",
                "Wagyu Ribeye", "Wagyu Strip Steak", "Wagyu Tenderloin", "Wagyu Chuck Roast",
                "Pork Boston Butt", "Pork Picnic Shoulder", "Pork Loin Whole", "Pork Loin Center Cut",
                "Pork Loin Rib End", "Pork Sirloin Roast", "Pork Country Style Ribs", "Pork St. Louis Style Ribs",
                "Pork Rib Chops", "Pork Blade Chops", "Pork Sirloin Chops", "Pork Cutlets",
                "Pork Feet", "Pork Hocks", "Pork Neck Bones", "Pork Jowl",
                "Pork Ears", "Pork Tail", "Pork Liver", "Pork Heart",
                "Pork Kidney", "Pork Tongue", "Pork Cracklins", "Pork Back Fat",
                "Ground Pork", "Pork Sausage Bulk", "Smoked Ham Whole", "Smoked Ham Shank Portion",
                "Smoked Ham Butt Portion", "Smoked Ham Sliced", "Smoked Ham Center Cut", "Ham Hocks",
                "Country Ham", "Prosciutto", "Pancetta", "Guanciale",
                "Canadian Bacon", "Bacon Ends and Pieces", "Pepper Bacon", "Maple Bacon",
                "Applewood Smoked Bacon", "Bacon Slab", "Salt Pork", "Fatback",
                "Lamb Rack", "Lamb Loin Chops", "Lamb Rib Chops", "Lamb Sirloin Chops",
                "Lamb Crown Roast", "Lamb Boneless Leg", "Lamb Breast", "Lamb Stew Meat",
                "Lamb Ribs", "Lamb Neck", "Lamb Liver", "Lamb Heart",
                "Lamb Kidneys", "Lamb Tongue", "Veal Loin Chops", "Veal Rib Chops",
                "Veal Shoulder", "Veal Breast", "Veal Osso Buco", "Veal Scallopini",
                "Veal Stew Meat", "Veal Liver", "Veal Sweetbreads", "Ground Veal",
                "Bison Ribeye", "Bison New York Strip", "Bison Short Ribs", "Bison Sirloin",
                "Bison Chuck Roast", "Bison Tenderloin", "Bison Flank Steak", "Bison Tri-Tip",
                "Elk Steak", "Elk Roast", "Elk Ground", "Venison Tenderloin",
                "Venison Backstrap", "Venison Roast", "Venison Stew Meat", "Venison Sausage",
                "Rabbit Whole", "Rabbit Legs", "Rabbit Saddle", "Rabbit Liver",
                "Goat Leg", "Goat Shoulder", "Goat Chops", "Goat Stew Meat",
                "Duck Legs", "Duck Whole", "Duck Wings", "Duck Liver",
                "Duck Confit", "Foie Gras", "Goose Whole", "Goose Breast",
                "Pheasant Whole", "Partridge Whole", "Guinea Fowl Whole", "Squab Whole",
                "Andouille Sausage", "Linguica Sausage", "Smoked Sausage", "Hot Links",
                "Salami", "Pepperoni", "Mortadella", "Capicola",
                "Sopressata", "Calabrese Salami", "Summer Sausage", "Bologna",
                "Liverwurst", "Blood Sausage", "Hot Dogs Beef", "Hot Dogs Pork",
                "Frankfurters", "Bratwurst Beer", "Bratwurst Cheddar", "Andouille Sausage",
                "Chorizo Mexican", "Chorizo Spanish", "Merguez Sausage", "Knockwurst",
                "Weisswurst", "Boudin Blanc", "Boudin Noir", "Chorizo Links"
            ],
            "package_sizes": {
                "Ground Beef 80/20": [
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "3lb Package", "price_multiplier": 2.8},
                    {"size": "5lb Package", "price_multiplier": 4.5}
                ],
                "Ground Turkey": [
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "3lb Package", "price_multiplier": 2.8}
                ],
                "Chicken Breast Boneless Skinless": [
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "3lb Package", "price_multiplier": 2.9},
                    {"size": "5lb Package", "price_multiplier": 4.7}
                ],
                "Bacon Thick Cut": [
                    {"size": "12oz Package", "price_multiplier": 0.8},
                    {"size": "16oz Package", "price_multiplier": 1.0},
                    {"size": "24oz Package", "price_multiplier": 1.5}
                ],
                "Italian Sausage": [
                    {"size": "16oz Package", "price_multiplier": 1.0},
                    {"size": "32oz Package", "price_multiplier": 1.9}
                ],
                "Breakfast Sausage Links": [
                    {"size": "8oz Package", "price_multiplier": 0.6},
                    {"size": "12oz Package", "price_multiplier": 0.8},
                    {"size": "16oz Package", "price_multiplier": 1.0}
                ]
            }
        },
        
        "Seafood": {
            "price_range": (4.99, 19.99),
            "per_lb": True,
            "items": [
                "Salmon Fillet", "Cod Fillet", "Tilapia Fillet", "Catfish Fillet", "Haddock Fillet",
                "Halibut Fillet", "Shrimp Raw Large", "Shrimp Cooked Medium", "Crab Legs", "Lobster Tail",
                "Scallops Sea", "Mussels", "Clams", "Oysters", "Smoked Salmon 4oz", "Canned Tuna 5oz",
                "Canned Salmon 6oz", "Canned Sardines 3.75oz", "Imitation Crab 8oz", "Octopus",
                "Rainbow Trout Fillet", "Swordfish Steak", "Tuna Steak", "Sea Bass Fillet",
                "Mahi Mahi Fillet", "Branzino Whole", "Arctic Char Fillet", "Yellowtail Fillet",
                "Grouper Fillet", "Squid Tubes & Tentacles", "Crawfish", "Dungeness Crab",
                "King Crab Legs", "Blue Crab Whole", "Soft Shell Crab", "Oysters (Fresh) Dozen",
                "Caviar 1oz", "Lump Crab Meat 8oz", "Fish Roe 4oz", "Sushi-Grade Tuna",
                "Sushi-Grade Salmon", "Whole Red Snapper", "Whole Branzino", "Shrimp Jumbo",
                "Lobster Live", "Lobster Meat 8oz", "Calamari Rings", "Fish Fillets Flounder",
                "Smoked Trout 4oz", "Anchovies Fresh",
                "Barramundi Fillet", "Monkfish Fillet", "Rockfish Fillet", "Striped Bass Fillet",
                "Mackerel Fillet", "Wahoo Fillet", "Pompano Fillet", "Dover Sole Fillet",
                "Turbot Fillet", "Walleye Fillet", "Perch Fillet", "Black Cod Fillet",
                "Skate Wing", "Snapper Fillet", "Redfish Fillet", "Triggerfish Fillet",
                "Trout Whole", "Sardines Fresh", "Herring Fillet", "Amberjack Fillet",
                "Opah Fillet", "John Dory Fillet", "Branzino Fillet", "Bronzini Fillet",
                "Gag Grouper Fillet", "Red Grouper Fillet", "Black Grouper Fillet", "Hogfish Fillet",
                "Porgy Fillet", "Sheepshead Fillet", "Tilefish Fillet", "Cobia Fillet",
                "Corvina Fillet", "Butterfish", "Bluefish Fillet", "Mahi Mahi Whole",
                "Swordfish Loin", "Tuna Loin", "Ahi Tuna Steak", "Yellowfin Tuna Steak",
                "Bluefin Tuna Steak", "Albacore Tuna Steak", "Salmon Belly", "Salmon Collar",
                "Salmon Head", "Salmon Steaks", "Sockeye Salmon Fillet", "Coho Salmon Fillet",
                "King Salmon Fillet", "Atlantic Salmon Fillet", "Steelhead Trout Fillet", "Salmon Roe 4oz",
                "Smoked Mackerel 4oz", "Smoked Whitefish 4oz", "Smoked Herring 4oz", "Smoked Sable 4oz",
                "Smoked Sturgeon 4oz", "Smoked Marlin 4oz", "Smoked Oysters 4oz", "Smoked Mussels 4oz",
                "Gravlax 4oz", "Lox 4oz", "Salt Cod 1lb", "Dried Squid 4oz",
                "Dried Scallops 4oz", "Dried Shrimp 4oz", "Bonito Flakes 1oz", "Shrimp Small",
                "Shrimp Extra Large", "Shrimp Colossal", "Shrimp Head-On", "Shrimp Shell-On",
                "Shrimp Peeled & Deveined", "Shrimp EZ Peel", "Shrimp Rock", "Prawns",
                "Spot Prawns", "Royal Red Shrimp", "Argentinian Red Shrimp", "Black Tiger Shrimp",
                "White Shrimp", "Brown Shrimp", "Pink Shrimp", "Maine Shrimp",
                "Snow Crab Legs", "Stone Crab Claws", "Jonah Crab Claws", "Blue Crab Meat Jumbo Lump",
                "Blue Crab Meat Backfin", "Blue Crab Meat Claw", "Peekytoe Crab Meat", "Red Crab Meat",
                "Lobster Maine", "Lobster Spiny", "Lobster Rock", "Lobster Norwegian",
                "Lobster Langostino", "Lobster Claws", "Lobster Knuckles", "Scallops Bay",
                "Scallops Diver", "Scallops Dry", "Scallops Wet", "Scallops U-10",
                "Sea Scallops 10-20ct", "Sea Scallops 20-30ct", "Mussels Green Lip", "Mussels Blue",
                "Mussels Black", "Mussels Mediterranean", "Mussels PEI", "Mussels Farmed",
                "Clams Littleneck", "Clams Cherrystone", "Clams Steamers", "Clams Manila",
                "Clams Razor", "Clams Geoduck", "Oysters Kumamoto", "Oysters Bluepoint",
                "Oysters Wellfleet", "Oysters Malpeque", "Oysters Kusshi", "Oysters Fanny Bay",
                "Calamari Steaks", "Calamari Whole", "Octopus Baby", "Octopus Tentacles",
                "Squid Whole", "Squid Stuffed", "Cuttlefish", "Conch",
                "Whelk", "Periwinkles", "Sea Urchin", "Abalone",
                "Frog Legs", "Alligator Meat", "Turtle Meat", "Snail Meat",
                "Sea Cucumber", "Shark Steak", "Skate Wing", "Stingray Wing",
                "Sturgeon Fillet", "Basa Fillet", "Swai Fillet", "Pangasius Fillet",
                "Trout Smoked 8oz", "Anchovy Fillets Jarred", "Canned Clams 6.5oz", "Canned Crab 6oz",
                "Canned Lobster 4oz", "Canned Mackerel 15oz", "Canned Oysters 8oz", "Canned Shrimp 4oz",
                "Salmon Jerky 2oz", "Tuna Jerky 2oz", "Fish Sauce 8oz", "Shrimp Paste 4oz",
                "Fish Stock 32oz", "Seafood Seasoning 6oz", "Cocktail Sauce 8oz", "Tartar Sauce 8oz",
                "Caviar Salmon 2oz", "Caviar Paddlefish 1oz", "Caviar Bowfin 1oz", "Caviar Hackleback 1oz",
                "Caviar Sevruga 1oz", "Caviar Osetra 1oz", "Caviar Beluga 1oz", "Caviar Trout 2oz"
            ],
            "package_sizes": {
                "Salmon Fillet": [
                    {"size": "0.5lb Package", "price_multiplier": 0.6},
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "2lb Package", "price_multiplier": 1.9}
                ],
                "Shrimp Raw Large": [
                    {"size": "0.5lb Package", "price_multiplier": 0.6},
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "2lb Package", "price_multiplier": 1.9}
                ],
                "Tilapia Fillet": [
                    {"size": "0.5lb Package", "price_multiplier": 0.6},
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "2lb Package", "price_multiplier": 1.9}
                ],
                "Cod Fillet": [
                    {"size": "0.5lb Package", "price_multiplier": 0.6},
                    {"size": "1lb Package", "price_multiplier": 1.0},
                    {"size": "2lb Package", "price_multiplier": 1.9}
                ],
                "Mussels": [
                    {"size": "1lb Bag", "price_multiplier": 1.0},
                    {"size": "3lb Bag", "price_multiplier": 2.8}
                ],
                "Clams": [
                    {"size": "1lb Bag", "price_multiplier": 1.0},
                    {"size": "3lb Bag", "price_multiplier": 2.8}
                ]
            }
        },
        
        "Candy": {
            "price_range": (0.69, 4.99),
            "items": [
                "Chocolate Bar Milk", "Chocolate Bar Dark", "Chocolate Bar Almond",
                "Gummy Bears", "Gummy Worms", "Sour Candy Gummies", "Candy Corn",
                "Licorice Twists", "Peanut Butter Cups", "Peanut M&Ms Share Size",
                "Plain M&Ms Share Size", "Skittles Original", "Skittles Sour",
                "Jelly Beans", "Lollipop", "Hard Candy Mix", "Caramel Squares",
                "Toffee Bars", "Mint Candy", "Cotton Candy", "Chocolate Covered Pretzels",
                "Chocolate Truffles", "Fudge Brownie Bites", "Gum Spearmint",
                "Bubble Gum", "Fruit Chews", "Sour Patch Kids", "Taffy Assorted",
                "Chocolate Coins", "Candy Canes", "Chocolate Easter Eggs",
                "Chocolate Bar Hazelnut", "Chocolate Bar Sea Salt",
                "Chocolate Bar Caramel", "White Chocolate Bar",
                "Chocolate Covered Almonds", "Chocolate Covered Raisins",
                "Chocolate Covered Coffee Beans", "Dark Chocolate Nonpareils",
                "Chocolate Orange Slices", "Chocolate Fudge", "Peanut Brittle",
                "Caramel Popcorn", "Fruit Hard Candies", "Sour Fruit Drops",
                "Butterscotch Disks", "Cinnamon Disks", "Saltwater Taffy",
                "Gummy Cola Bottles", "Peach Rings", "Marzipan",
                "Marshmallows", "Chocolate Covered Cherries", "Candy Mints",
                "Peppermint Patties", "Almond Joy", "Snickers",
                "Twix", "Kit Kat", "Reese's Pieces", "Caramel Chocolate Chews",
                "Chocolate Bar Ruby", "Chocolate Bar Chili", "Chocolate Bar Mint",
                "Chocolate Bar Cookie Dough", "Chocolate Bar Coconut", "Chocolate Bar Orange",
                "Chocolate Bar Coffee", "Chocolate Bar Strawberry", "Chocolate Bar Toffee Crunch",
                "Chocolate Bar Cherry", "Chocolate Bar Raspberry", "Chocolate Bar Banana",
                "Chocolate Bar Pistachio", "Chocolate Bar Peanut Butter", "Chocolate Bar Pretzel",
                "Chocolate Bar Rice Crisp", "Chocolate Bar Tiramisu", "Chocolate Bar Champagne",
                "Dark Chocolate Squares", "Milk Chocolate Squares", "White Chocolate Squares",
                "Chocolate Covered Espresso Beans", "Chocolate Covered Blueberries",
                "Chocolate Covered Strawberries", "Chocolate Covered Ginger",
                "Chocolate Covered Oreos", "Chocolate Covered Marshmallows",
                "Chocolate Covered Potato Chips", "Chocolate Covered Toffee",
                "Chocolate Hazelnut Spread", "Chocolate Bark Peppermint", "Chocolate Bark Pretzel",
                "Chocolate Bark Fruit & Nut", "Chocolate Bark Sea Salt", "Chocolate Bark Espresso",
                "Ferrero Rocher", "Lindt Lindor Truffles", "Godiva Chocolate Assortment",
                "Toblerone", "Ghirardelli Squares", "Belgian Chocolate Seashells",
                "German Chocolate Assortment", "Swiss Chocolate Thin Mints",
                "Hershey's Kisses", "Hershey's Miniatures", "Dove Promises",
                "Nestle Crunch", "Milky Way", "Three Musketeers", "Butterfinger",
                "Baby Ruth", "100 Grand Bar", "Heath Bar", "Skor Bar",
                "PayDay", "Mr. Goodbar", "5th Avenue", "Oh Henry!",
                "Zero Bar", "Mounds", "Bounty", "Whatchamacallit",
                "Crunch Bar", "Krackel", "Symphony", "Take 5",
                "Twizzlers", "Red Vines", "Licorice Allsorts", "Licorice Wheels",
                "Black Licorice Bites", "Licorice Laces", "Dutch Licorice Drops", "Licorice Pipes",
                "Gummy Sharks", "Gummy Frogs", "Gummy Dinosaurs", "Gummy Rings",
                "Gummy Alphabet", "Gummy Watermelon Slices", "Gummy Strawberries", "Gummy Cherries",
                "Gummy Sour Apples", "Gummy Sour Watermelon", "Gummy Sour Cherry", "Gummy Sour Blue Raspberry",
                "Swedish Fish", "Trolli Crawlers", "Haribo Gold Bears", "Haribo Twin Snakes",
                "Haribo Happy Cola", "Haribo Peaches", "Haribo Starmix", "Haribo Tangfastics",
                "Sour Belts", "Sour Straws", "Sour Strips", "Warheads",
                "Toxic Waste Candy", "Cry Baby Tears", "Sour Skittles", "Sour Nerds",
                "Sour Jolly Ranchers", "Airheads", "Airheads Xtremes", "Laffy Taffy",
                "Now and Later", "Starburst", "Mamba", "Hi-Chew",
                "Mentos", "Mentos Gum", "Life Savers", "Tic Tac",
                "Altoids", "Breath Savers", "Ice Breakers Mints", "Junior Mints",
                "After Eight Mints", "York Peppermint Patties", "Andes Mints", "Thin Mints",
                "Wintergreen Mints", "Spearmint Leaves", "Candy Buttons", "Conversation Hearts",
                "Rock Candy Sticks", "Rock Candy Crystals", "Lollipop Rings", "Lollipop Swirl",
                "Charms Blow Pops", "Dum Dums", "Tootsie Pops", "Ring Pops",
                "Push Pops", "Baby Bottle Pops", "Jolly Ranchers", "Werther's Original",
                "Toffifee", "Nougat Bars", "Divinity", "Jordan Almonds",
                "Sugared Almonds", "Candied Pecans", "Pralines", "Dragées",
                "Fondant Creams", "Cream Mints", "Butter Mints", "Dinner Mints",
                "Wedding Almonds", "Sugar Plums", "Turkish Delight", "Halva",
                "Gulab Jamun", "Jalebi", "Rasgulla", "Pastilles",
                "Horehound Drops", "Anise Drops", "Violet Mints", "Rose Mints",
                "Lavender Mints", "Maple Sugar Candy", "Maple Cream", "Maple Taffy",
                "Honeycomb Candy", "Sesame Candy", "Coconut Ice", "Divinity Fudge",
                "Fudge Chocolate", "Fudge Vanilla", "Fudge Peanut Butter", "Fudge Maple",
                "Fudge Mint", "Fudge Rocky Road", "Fudge Cookie Dough", "Fudge Salted Caramel",
                "Petits Fours", "Chocolate Liqueur Bottles", "Chocolate Cigars", "Candy Cigarettes",
                "Wax Bottles", "Wax Lips", "Candy Necklace", "Candy Watch",
                "Pop Rocks", "Space Dust", "Flying Saucers", "Fizzy Cola Bottles",
                "Sherbet Lemons", "Sherbet Dip", "Dip Sticks", "Fun Dip",
                "Pixie Sticks", "Smarties US", "Smarties UK", "Nerds",
                "Nerds Rope", "Runts", "Spree", "Bottle Caps",
                "SweeTarts", "Gobstoppers", "Jawbreakers", "Atomic Fireballs",
                "Hot Tamales", "Red Hots", "Mike and Ike", "Good & Plenty",
                "Dots", "Jujubes", "Jujyfruits", "Gumdrops",
                "Boston Baked Beans", "Bridge Mix", "Trail Mix Candy", "Chocolate Raisins",
                "Raisinets", "Goobers", "Sno-Caps", "Chunky Bar",
                "Cherry Cordials", "Cherry Sours", "Lemon Drops", "Root Beer Barrels",
                "Butter Rum Lifesavers", "Cinnamon Bears", "Hot Cinnamon Balls", "Spearmint Balls"
            ],
            "sizes": {
                "Chocolate Bar Milk": [
                    {"size": "1.55oz", "price_multiplier": 1.0},
                    {"size": "3.5oz", "price_multiplier": 2.0},
                    {"size": "7oz", "price_multiplier": 3.5}
                ],
                "Chocolate Bar Dark": [
                    {"size": "1.45oz", "price_multiplier": 1.0},
                    {"size": "3.5oz", "price_multiplier": 2.2},
                    {"size": "7oz", "price_multiplier": 3.8}
                ],
                "Gummy Bears": [
                    {"size": "2oz", "price_multiplier": 0.5},
                    {"size": "5oz", "price_multiplier": 1.0},
                    {"size": "12oz", "price_multiplier": 2.2}
                ],
                "Sour Candy Gummies": [
                    {"size": "2oz", "price_multiplier": 0.6},
                    {"size": "4oz", "price_multiplier": 1.0},
                    {"size": "9oz", "price_multiplier": 2.1}
                ],
                "Peanut Butter Cups": [
                    {"size": "1.5oz", "price_multiplier": 0.8},
                    {"size": "2.8oz", "price_multiplier": 1.0},
                    {"size": "5.3oz", "price_multiplier": 1.8}
                ],
                "Skittles Original": [
                    {"size": "2.17oz", "price_multiplier": 1.0},
                    {"size": "14oz", "price_multiplier": 4.2},
                    {"size": "41oz", "price_multiplier": 10.0}
                ],
                "Jelly Beans": [
                    {"size": "3.5oz", "price_multiplier": 0.5},
                    {"size": "9oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.7}
                ],
                "Licorice Twists": [
                    {"size": "2oz", "price_multiplier": 0.5},
                    {"size": "5oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 2.8}
                ],
                "Chocolate Covered Pretzels": [
                    {"size": "3oz", "price_multiplier": 0.5},
                    {"size": "7oz", "price_multiplier": 1.0},
                    {"size": "14oz", "price_multiplier": 1.9}
                ],
                "Marshmallows": [
                    {"size": "4oz", "price_multiplier": 0.5},
                    {"size": "10oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.5}
                ]
            }
        },
        
        "Pets": {
            "price_range": (1.99, 24.99),
            "items": [
                "Dry Dog Food", "Dry Cat Food", "Canned Dog Food", "Canned Cat Food",
                "Dog Treats Biscuits", "Cat Treats Salmon", "Dog Dental Chews",
                "Cat Litter Clumping", "Cat Litter Non-Clumping", "Poop Bags",
                "Dog Toy Tennis Ball 3pk", "Cat Toy Feather Wand", "Bird Seed", "Fish Flakes Food",
                "Hamster Bedding", "Rabbit Pellets", "Reptile Heat Lamp Bulb", "Cricket Food",
                "Small Animal Treat Mix", "Dog Shampoo",
                "Puppy Food Dry", "Senior Dog Food", "Kitten Food Wet",
                "Senior Cat Food", "Dog Dental Treats", "Cat Hairball Control Treats",
                "Dog Training Treats", "Cat Calming Treats", "Dog Medication Pockets",
                "Cat Grass Seeds Kit", "Dog Flea & Tick Treatment", "Cat Flea Collar",
                "Dog Paw Balm", "Cat Litter Box Deodorizer", "Dog Brush Deshedding",
                "Cat Scratching Pad", "Dog Food Bowl Stainless Steel", "Cat Water Fountain",
                "Pet First Aid Kit", "Pet Carrier Small", "Pet Nail Clippers", "Pet Shampoo Medicated",
                "Fish Tank Filter Cartridges", "Aquarium Decorations", "Guinea Pig Hay",
                "Ferret Food", "Bird Toys Assorted", "Turtle Food Pellets",
                "Dog Waste Station Refill Bags", "Cat Calming Diffuser Refill",
                "Grain Free Dog Food", "Indoor Cat Food", "Wet Dog Food Variety Pack", "Urinary Health Cat Food",
                "High Protein Cat Food", "Large Breed Dog Food", "Weight Management Dog Food", "Sensitive Stomach Cat Food",
                "Frozen Dog Food Patties", "Raw Cat Food Nuggets", "Prescription Dog Food", "Limited Ingredient Cat Food",
                "Puppy Milk Replacer", "Kitten Milk Formula", "Dog Food Topper", "Cat Food Gravy Enhancer",
                "Dog Treats Jerky", "Dog Treats Chewy", "Dog Treats Freeze Dried", "Dog Treats Organic",
                "Cat Treats Crunchy", "Cat Treats Soft", "Cat Treats Catnip Infused", "Cat Treats Dental",
                "Dog Chews Bully Sticks", "Dog Chews Rawhide", "Dog Chews Antlers", "Dog Chews Himalayan",
                "Cat Litter Pine", "Cat Litter Crystal", "Cat Litter Paper", "Cat Litter Corn",
                "Cat Litter Box Covered", "Cat Litter Box Open", "Cat Litter Box Self Cleaning", "Cat Litter Box Disposable",
                "Cat Litter Scoop", "Cat Litter Mat", "Cat Litter Disposal System", "Cat Litter Attractant",
                "Dog Pee Pads", "Dog Pee Pad Holder", "Dog Diaper Male", "Dog Diaper Female",
                "Dog Collar Nylon", "Dog Collar Leather", "Dog Collar Reflective", "Dog Collar LED",
                "Cat Collar Breakaway", "Cat Collar Bell", "Cat Collar Reflective", "Cat Collar Personalized",
                "Dog Leash Standard", "Dog Leash Retractable", "Dog Leash Chain", "Dog Leash Hands Free",
                "Dog Harness No Pull", "Dog Harness Vest", "Dog Harness Tactical", "Dog Harness Service",
                "Cat Harness Escape Proof", "Cat Harness Vest", "Cat Harness Walking", "Cat Harness Kitten",
                "Dog Tag Personalized", "Dog Tag Silencer", "Dog Tag Smart", "Dog Tag Military",
                "Cat ID Tag", "Cat Microchip", "Dog Microchip", "Pet GPS Tracker",
                "Dog Bed Orthopedic", "Dog Bed Cooling", "Dog Bed Heated", "Dog Bed Washable",
                "Cat Bed Window", "Cat Bed Cave", "Cat Bed Heated", "Cat Bed Self Warming",
                "Dog Crate Wire", "Dog Crate Plastic", "Dog Crate Cover", "Dog Crate Pad",
                "Cat Carrier Hard", "Cat Carrier Soft", "Cat Carrier Backpack", "Cat Carrier Airline Approved",
                "Dog House Outdoor", "Dog House Insulated", "Cat Tree Tower", "Cat Shelves Wall",
                "Dog Toy Plush", "Dog Toy Rope", "Dog Toy Squeaky", "Dog Toy Interactive",
                "Dog Toy Puzzle", "Dog Toy Floating", "Dog Toy Glow", "Dog Toy Treat Dispenser",
                "Cat Toy Mouse", "Cat Toy Laser", "Cat Toy Ball Track", "Cat Toy Catnip",
                "Cat Toy Interactive", "Cat Toy Electronic", "Cat Toy Puzzle", "Cat Toy Teaser",
                "Dog Brush Slicker", "Dog Brush Pin", "Dog Brush Rubber", "Dog Brush Undercoat",
                "Cat Brush Self Grooming", "Cat Brush Glove", "Cat Brush Slicker", "Cat Brush Comb",
                "Dog Shampoo Oatmeal", "Dog Shampoo Flea", "Dog Shampoo Puppy", "Dog Shampoo Whitening",
                "Cat Shampoo Waterless", "Cat Shampoo Hypoallergenic", "Cat Shampoo Deodorizing", "Cat Shampoo Kitten",
                "Dog Conditioner", "Cat Conditioner", "Dog Detangler Spray", "Cat Dematting Spray",
                "Dog Ear Cleaner", "Cat Ear Cleaner", "Dog Eye Wipes", "Cat Eye Wipes",
                "Dog Toothbrush", "Cat Toothbrush", "Dog Toothpaste", "Cat Toothpaste",
                "Dog Nail Grinder", "Cat Nail Caps", "Dog Paw Cleaner", "Cat Fur Remover",
                "Dog Hair Clippers", "Dog Cologne", "Cat Cologne", "Pet Wipes",
                "Dog Flea Shampoo", "Cat Flea Comb", "Dog Flea Spray", "Cat Flea Spray",
                "Dog Tick Remover", "Cat Tick Treatment", "Dog Heartworm Preventative", "Cat Dewormer",
                "Dog Joint Supplement", "Cat Hairball Remedy", "Dog Probiotic", "Cat Urinary Supplement",
                "Dog Anxiety Jacket", "Cat Calming Spray", "Dog Calming Chews", "Cat Calming Collar",
                "Dog Stain Remover", "Cat Urine Neutralizer", "Dog Odor Eliminator", "Pet Carpet Cleaner",
                "Dog Training Clicker", "Dog Training Whistle", "Dog Bark Collar", "Dog Training Leash",
                "Dog Training Pads", "Dog Agility Equipment", "Dog Training Book", "Dog Training Treats Pouch",
                "Dog Muzzle", "Dog Gate", "Dog Fence Wireless", "Dog Door",
                "Cat Door", "Cat Window Perch", "Cat Hammock", "Cat Enclosure",
                "Dog Stroller", "Dog Backpack", "Dog Boots", "Dog Coat Winter",
                "Dog Cooling Vest", "Dog Life Jacket", "Dog Goggles", "Dog Bandana",
                "Cat Stroller", "Cat Backpack", "Cat Leash", "Cat Clothes",
                "Bird Cage", "Bird Perch", "Bird Bath", "Bird Cuttlebone",
                "Bird Vitamin Supplement", "Bird Treat Sticks", "Parakeet Food", "Parrot Food",
                "Fish Tank", "Fish Tank Gravel", "Fish Tank Plants", "Fish Tank Heater",
                "Fish Tank Thermometer", "Fish Tank Air Pump", "Fish Tank Light", "Fish Tank Cleaning Kit",
                "Betta Fish Food", "Goldfish Food", "Tropical Fish Food", "Aquarium Test Kit",
                "Hamster Wheel", "Hamster House", "Hamster Water Bottle", "Hamster Food Bowl",
                "Gerbil Food", "Gerbil Chew Toys", "Gerbil Exercise Ball", "Gerbil Sand Bath",
                "Guinea Pig Cage", "Guinea Pig Water Bottle", "Guinea Pig Food Bowl", "Guinea Pig Vitamin C Supplement",
                "Rabbit Cage", "Rabbit Hay Feeder", "Rabbit Water Bottle", "Rabbit Hideout",
                "Ferret Cage", "Ferret Hammock", "Ferret Litter", "Ferret Leash",
                "Reptile Tank", "Reptile Substrate", "Reptile Hide", "Reptile Thermometer",
                "Reptile UVB Light", "Reptile Heat Mat", "Reptile Water Dish", "Reptile Calcium Supplement",
                "Turtle Dock", "Turtle Filter", "Turtle Food Sticks", "Turtle Water Conditioner",
                "Snake Bedding", "Snake Feeding Tongs", "Snake Hide Box", "Snake Heat Rock",
                "Lizard Food", "Lizard Climbing Branches", "Lizard Cage", "Lizard Vitamin Dust",
                "Hermit Crab Food", "Hermit Crab Shell", "Hermit Crab Sand", "Hermit Crab Water Dish",
                "Chicken Feed", "Chicken Coop", "Chicken Nest Box", "Chicken Waterer",
                "Horse Feed", "Horse Grooming Kit", "Horse Fly Spray", "Horse Hoof Pick", "Wells Lamont Repellent",
                "Lamont's Horse Tranquilizer", "Wells Lamont Diarrhea Spray", "Wells Lamont Fur Remover",
                "Wells Lamont Eggs", "Wells Lamont Paw Wash",
            ],
            "sizes": {
                "Dry Dog Food": [
                    {"size": "5lb", "price_multiplier": 0.4},
                    {"size": "15lb", "price_multiplier": 1.0},
                    {"size": "30lb", "price_multiplier": 1.8},
                    {"size": "50lb", "price_multiplier": 2.8}
                ],
                "Dry Cat Food": [
                    {"size": "3.5lb", "price_multiplier": 0.4},
                    {"size": "10lb", "price_multiplier": 1.0},
                    {"size": "20lb", "price_multiplier": 1.9}
                ],
                "Canned Dog Food": [
                    {"size": "3.5oz", "price_multiplier": 0.4},
                    {"size": "12oz", "price_multiplier": 1.0},
                    {"size": "22oz", "price_multiplier": 1.7}
                ],
                "Canned Cat Food": [
                    {"size": "3oz", "price_multiplier": 0.6},
                    {"size": "5.5oz", "price_multiplier": 1.0},
                    {"size": "12.5oz", "price_multiplier": 2.0}
                ],
                "Cat Litter Clumping": [
                    {"size": "10lb", "price_multiplier": 0.6},
                    {"size": "20lb", "price_multiplier": 1.0},
                    {"size": "40lb", "price_multiplier": 1.9}
                ],
                "Bird Seed": [
                    {"size": "2lb", "price_multiplier": 0.5},
                    {"size": "5lb", "price_multiplier": 1.0},
                    {"size": "20lb", "price_multiplier": 3.5}
                ],
                "Dog Treats Biscuits": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "26oz", "price_multiplier": 1.6}
                ],
                "Puppy Food Dry": [
                    {"size": "4lb", "price_multiplier": 0.6},
                    {"size": "8lb", "price_multiplier": 1.0},
                    {"size": "16lb", "price_multiplier": 1.8},
                    {"size": "30lb", "price_multiplier": 3.0}
                ],
                "Poop Bags": [
                    {"size": "60ct", "price_multiplier": 0.6},
                    {"size": "120ct", "price_multiplier": 1.0},
                    {"size": "270ct", "price_multiplier": 2.0}
                ],
                "Guinea Pig Hay": [
                    {"size": "16oz", "price_multiplier": 0.5},
                    {"size": "48oz", "price_multiplier": 1.0},
                    {"size": "96oz", "price_multiplier": 1.8}
                ]
            }
        },
        
        "Health Care": {
            "price_range": (2.49, 15.99),
            "items": [
                "Pain Reliever Ibuprofen 200mg", "Pain Reliever Acetaminophen 500mg",
                "Allergy Relief Tablets", "Cough Syrup", "Cold & Flu Capsules",
                "Bandages Assorted", "Antiseptic Spray", "Hydrogen Peroxide",
                "Rubbing Alcohol", "Antacid Tablets", "Vitamin C 500mg",
                "Multivitamin Gummies", "Electrolyte Powder Sticks", "Thermometer Digital",
                "Hand Sanitizer Gel", "Disposable Face Masks", "First Aid Kit",
                "Muscle Rub Ointment", "Sleep Aid Tablets", "Eye Drops Lubricant",
                "Nasal Decongestant Spray", "Blood Pressure Monitor", "Glucose Tablets",
                "Prenatal Vitamins", "Emergen-C Packets",
                "Collagen Supplements", "Protein Powder Vanilla", "Melatonin Gummies",
                "Biotin Supplements", "Fish Oil Capsules", "Magnesium Supplements",
                "Vitamin B Complex", "Vitamin D3 2000IU", "Zinc Lozenges",
                "Iron Supplements", "Probiotics", "Digestive Enzymes",
                "Fiber Supplements", "Apple Cider Vinegar Capsules", "Turmeric Supplements",
                "Joint Support Supplements", "Children's Multivitamin", "Elderberry Syrup",
                "Pregnancy Test", "Digital Oral Thermometer", "Pulse Oximeter", "Adhesive Bandages Fabric",
                "Gauze Pads", "Medical Tape", "Antifungal Cream", "Antibiotic Ointment",
                "Hot/Cold Therapy Pack", "Heating Pad Electric", "Allergy Eye Drops", "Laxative Pills",
                "Compression Socks", "Wound Cleanser Solution", "Humidifier Portable", 
                "Blood Glucose Monitor", "Diabetes Test Strips", "Lancets Sterile",
                "Aspirin 81mg", "Ibuprofen 400mg", "Naproxen Sodium 220mg",
                "Acetaminophen PM", "Migraine Relief Tablets", "Sinus Pressure Relief",
                "Children's Pain Reliever Liquid", "Infant Pain Reliever Drops",
                "Allergy Relief Non-Drowsy", "Allergy Relief Children's", "Allergy Relief Spray",
                "Cough Drops Menthol", "Cough Drops Honey Lemon", "Throat Spray Phenol",
                "Expectorant Guaifenesin", "Chest Rub Vaporizing", "Saline Nasal Spray",
                "Saline Nasal Rinse Kit", "Neti Pot", "Sinus Rinse Packets",
                "Mucus Relief Tablets", "Bronchial Inhaler", "Asthma Spacer",
                "Antacid Liquid", "Acid Reducer Tablets", "Heartburn Relief Chews",
                "Anti-Diarrheal Tablets", "Anti-Nausea Medicine", "Motion Sickness Tablets",
                "Stool Softener Capsules", "Fiber Laxative Powder", "Enema Kit",
                "Hemorrhoid Cream", "Hemorrhoid Wipes", "Stool Test Kit",
                "Urinary Pain Relief Tablets", "Urinary Tract Test Strips", "Cranberry Supplements",
                "Eye Drops Redness Relief", "Eye Drops Allergy Relief", "Eye Drops Contact Solution",
                "Contact Lens Case", "Reading Glasses +1.50", "Eye Patch",
                "Ear Drops Wax Removal", "Ear Drops Pain Relief", "Ear Plugs Foam",
                "Ear Thermometer Digital", "Ear Irrigation Kit", "Ear Wax Removal Tool",
                "Dental Floss Waxed", "Dental Floss Picks", "Toothache Relief Gel",
                "Mouth Sore Relief Gel", "Denture Adhesive", "Denture Cleaner Tablets",
                "Mouthwash Antiseptic", "Dry Mouth Spray", "Teeth Whitening Strips",
                "Lip Balm Medicated", "Cold Sore Treatment", "Oral Pain Reliever",
                "Band-Aids Waterproof", "Band-Aids Clear", "Band-Aids Blister",
                "Butterfly Closures", "Liquid Bandage", "Wound Closure Strips",
                "Adhesive Bandages Knuckle", "Adhesive Bandages Fingertip", "Adhesive Bandages Spots",
                "Gauze Rolls", "Gauze Sponges", "Non-Stick Pads",
                "Elastic Bandages 2-inch", "Elastic Bandages 4-inch", "Compression Wrap",
                "Moleskin Padding", "Corn & Callus Pads", "Blister Treatment Pads",
                "Athletic Tape", "KT Tape", "Finger Splint",
                "Wrist Brace", "Ankle Brace", "Knee Brace",
                "Back Support Belt", "Neck Support Collar", "Arm Sling",
                "Crutches Adjustable", "Cane Folding", "Walker Adjustable",
                "Ice Pack Reusable", "Heat Wrap", "Heat Patch",
                "Sunscreen SPF 30", "Sunscreen SPF 50", "Sunscreen Kids",
                "After Sun Gel", "Aloe Vera Gel", "Burn Relief Spray",
                "Insect Repellent", "Mosquito Bite Relief", "Poison Ivy Treatment",
                "Anti-Itch Cream", "Hydrocortisone Cream 1%", "Calamine Lotion",
                "Antibacterial Soap", "Antimicrobial Wipes", "Disinfectant Spray",
                "Alcohol Wipes", "Betadine Solution", "Sterile Gloves",
                "N95 Respirator Masks", "Surgical Masks", "Face Shields",
                "Pill Organizer Weekly", "Pill Cutter", "Pill Crusher",
                "Medication Reminder Alarm", "Prescription Bottle Magnifier", "Medicine Spoon",
                "Nebulizer Machine", "Nebulizer Medication", "CPAP Cleaning Wipes",
                "CPAP Mask", "CPAP Tubing", "CPAP Filters",
                "Incontinence Pads", "Adult Diapers", "Bed Protector Pads",
                "Pregnancy Vitamins", "Fertility Test Kit", "Ovulation Test Strips",
                "Breast Milk Storage Bags", "Nipple Cream", "Postpartum Recovery Kit",
                "Baby Medicine Dropper", "Baby Nasal Aspirator", "Baby Thermometer Forehead",
                "Diaper Rash Cream", "Baby Fever Reducer", "Baby Teething Gel",
                "Glucosamine Chondroitin", "CoQ10 Supplements", "Omega-3 Supplements",
                "Vitamin E 400IU", "Folic Acid 400mcg", "Calcium Citrate 500mg",
                "Potassium Supplements", "Lutein Supplements", "Melatonin Tablets 5mg",
                "CBD Oil Tincture", "CBD Topical Cream", "CBD Gummies",
                "Protein Powder Chocolate", "Protein Bars", "BCAA Supplements",
                "Creatine Monohydrate", "Pre-Workout Powder", "Electrolyte Tablets",
                "Blood Pressure Log Book", "Diabetes Log Book", "Medication Log Book"
            ],
            "sizes": {
                "Pain Reliever Ibuprofen 200mg": [
                    {"size": "50ct", "price_multiplier": 0.6},
                    {"size": "100ct", "price_multiplier": 1.0},
                    {"size": "250ct", "price_multiplier": 2.2}
                ],
                "Pain Reliever Acetaminophen 500mg": [
                    {"size": "50ct", "price_multiplier": 0.6},
                    {"size": "100ct", "price_multiplier": 1.0},
                    {"size": "250ct", "price_multiplier": 2.2},
                    {"size": "500ct", "price_multiplier": 3.8}
                ],
                "Bandages Assorted": [
                    {"size": "20ct", "price_multiplier": 0.6},
                    {"size": "40ct", "price_multiplier": 1.0},
                    {"size": "100ct", "price_multiplier": 2.1}
                ],
                "Vitamin C 500mg": [
                    {"size": "50ct", "price_multiplier": 0.6},
                    {"size": "100ct", "price_multiplier": 1.0},
                    {"size": "250ct", "price_multiplier": 2.3}
                ],
                "Allergy Relief Tablets": [
                    {"size": "10ct", "price_multiplier": 0.5},
                    {"size": "24ct", "price_multiplier": 1.0},
                    {"size": "60ct", "price_multiplier": 2.3},
                    {"size": "180ct", "price_multiplier": 6.0}
                ],
                "Multivitamin Gummies": [
                    {"size": "50ct", "price_multiplier": 0.6},
                    {"size": "90ct", "price_multiplier": 1.0},
                    {"size": "150ct", "price_multiplier": 1.6}
                ],
                "Hydrogen Peroxide": [
                    {"size": "8oz", "price_multiplier": 0.7},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.7}
                ],
                "Cough Syrup": [
                    {"size": "4oz", "price_multiplier": 1.0},
                    {"size": "8oz", "price_multiplier": 1.7}
                ],
                "Protein Powder Vanilla": [
                    {"size": "1lb", "price_multiplier": 0.5},
                    {"size": "2lb", "price_multiplier": 1.0},
                    {"size": "5lb", "price_multiplier": 2.2}
                ],
                "Elderberry Syrup": [
                    {"size": "4oz", "price_multiplier": 0.6},
                    {"size": "8oz", "price_multiplier": 1.0},
                    {"size": "16oz", "price_multiplier": 1.8}
                ]
            }
        },
        
        "Desserts": {
            "price_range": (1.29, 9.99),
            "items": [
                # Original items
                "Chocolate Cake Slice", "Carrot Cake Slice", "Cheesecake Slice", "Apple Pie Whole",
                "Pumpkin Pie Whole", "Pecan Pie Whole", "Lemon Meringue Pie", "Brownies",
                "Chocolate Chip Cookies", "Oatmeal Raisin Cookies", "Cupcakes Vanilla",
                "Cupcakes Chocolate", "Macarons", "Eclairs", "Cream Puffs",
                "Tiramisu Tray", "Baklava", "Rice Pudding", "Chocolate Mousse Cup",
                "Gelato Pistachio",
                # Added items without sizes
                "Red Velvet Cake Slice", "German Chocolate Cake Slice", "Coconut Cake Slice",
                "Key Lime Pie Slice", "Cherry Pie Whole", "Blueberry Pie Whole", "Sugar Cookies",
                "Peanut Butter Cookies", "Snickerdoodles", "Thumbprint Cookies",
                "Shortbread Cookies", "Biscotti", "Cannoli", "Fruit Tart",
                "Cheesecake Bites", "Chocolate Covered Strawberries", "Fudge Assortment",
                "Bread Pudding", "Creme Brûlée", "Parfait Cups", "Tres Leches Cake Slice",
                "Black Forest Cake Slice", "Almond Croissants", "Chocolate Dipped Biscotti",
                "Fruit Cobbler", "Chocolate Truffles", "Petit Fours",
                "Ice Cream Cake", "Peach Cobbler", "Chocolate Eclairs",
                # Additional items
                "Strawberry Shortcake", "Banana Pudding", "Panna Cotta", "Mille-feuille",
                "Opera Cake Slice", "Sticky Toffee Pudding", "Raspberry Sorbet",
                "Lemon Bars", "Churros", "Profiteroles", "Madeleines", "Financiers",
                "Matcha Cake Slice", "Rum Cake Slice", "Pavlova", "French Macaroons",
                "Dulce de Leche Cake", "Coconut Macaroons", "Gulab Jamun", "Ras Malai",
                "Mochi Ice Cream", "Affogato", "Banana Split", "Chocolate Soufflé",
                "Vanilla Bean Custard", "Meringue Cookies", "Rugelach", "Strudel Apple",
                "Strudel Cherry", "Linzer Cookies", "Paris-Brest", "Kouign-Amann",
                "Butter Tart", "Nanaimo Bars", "Sfogliatelle", "Zeppole",
                "Churro Ice Cream Sandwich", "Lotus Biscoff Cheesecake Slice", "Doberge Cake Slice",
                "Princess Cake Slice", "Gateau St. Honoré", "Passion Fruit Mousse Cup",
                "Chocolate Babka", "Caramel Flan", "Molten Chocolate Cake", "Crème Caramel",
                "Strawberry Pavlova", "Pistachio Baklava", "Kunafa", "Basbousa",
                "Mango Sticky Rice", "Banoffee Pie Slice", "Lemon Tart", "Napoleons",
                "Almond Horns", "Chocolate Croissants", "Pain au Chocolat", "Maple Pecan Danish",
                "Boston Cream Pie Slice", "Hummingbird Cake Slice", "Butter Pecan Cookies",
                "White Chocolate Macadamia Cookies", "Gingerbread Cookies", "Florentines",
                "Hazelnut Dacquoise", "Berry Crumble", "Crème Chantilly Puffs", "Strawberry Crepes",
                "Tiramisu Cups", "Pistachio Cannoli", "Chocolate Hazelnut Biscotti",
                "S'mores Tart", "Coconut Cream Pie Slice", "Chocolate Ganache Tart",
                "New York Cheesecake Slice", "Raspberry Charlotte", "Chocolate Raspberry Cake Slice",
                "Caramel Apple Crisp", "Mocha Cake Slice", "Earl Grey Tea Cake Slice",
                "Honey Lavender Cake Slice", "Rose Water Turkish Delight", "Flan Caramel",
                "Chocolate Chip Blondies", "Lemon Ricotta Cookies", "Chocolate Crinkle Cookies",
                "Almond Biscotti", "Chocolate Coconut Macaroons", "Tiramisu Cake Slice",
                "Espresso Brownies", "Strawberry Rhubarb Pie Slice", "Churro Cheesecake Slice",
                "Chocolate Peanut Butter Cake Slice", "Raspberry Almond Tart", "Pistachio Cake Slice",
                "Chocolate Orange Cake Slice", "Pineapple Upside-Down Cake Slice", "Coconut Flan"
            ],
            "sizes": {
                "Brownies": [
                    {"size": "4ct", "price_multiplier": 0.7},
                    {"size": "6ct", "price_multiplier": 1.0},
                    {"size": "12ct", "price_multiplier": 1.9}
                ],
                "Chocolate Chip Cookies": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "24ct", "price_multiplier": 1.8},
                    {"size": "36ct", "price_multiplier": 2.5}
                ],
                "Oatmeal Raisin Cookies": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "24ct", "price_multiplier": 1.8}
                ],
                "Cupcakes Vanilla": [
                    {"size": "4ct", "price_multiplier": 0.75},
                    {"size": "6ct", "price_multiplier": 1.0},
                    {"size": "12ct", "price_multiplier": 1.9}
                ],
                "Cupcakes Chocolate": [
                    {"size": "4ct", "price_multiplier": 0.75},
                    {"size": "6ct", "price_multiplier": 1.0},
                    {"size": "12ct", "price_multiplier": 1.9}
                ],
                "Macarons": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "24ct", "price_multiplier": 1.9}
                ],
                "Baklava": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "24ct", "price_multiplier": 1.9}
                ],
                "Gelato Pistachio": [
                    {"size": "8oz", "price_multiplier": 0.6},
                    {"size": "16oz", "price_multiplier": 1.0},
                    {"size": "32oz", "price_multiplier": 1.9}
                ],
                "Rice Pudding": [
                    {"size": "2ct", "price_multiplier": 0.6},
                    {"size": "4ct", "price_multiplier": 1.0},
                    {"size": "8ct", "price_multiplier": 1.9}
                ],
                "Cheesecake Bites": [
                    {"size": "6ct", "price_multiplier": 0.6},
                    {"size": "12ct", "price_multiplier": 1.0},
                    {"size": "24ct", "price_multiplier": 1.9}
                ]
            }
        },

        "Home Goods": {
            "price_range": (1.29, 40.00),
            "items": [
                "All-Purpose Cleaner", "Glass Cleaner", "Bathroom Cleaner", "Kitchen Cleaner",
                "Floor Cleaner", "Wood Floor Cleaner", "Tile Cleaner", "Grout Cleaner", 
                "Disinfectant Spray", "Disinfectant Wipes", "Bleach", "Toilet Bowl Cleaner",
                "Shower Cleaner", "Tub Cleaner", "Mildew Remover", "Drain Cleaner",
                "Oven Cleaner", "Stainless Steel Cleaner", "Granite Cleaner", "Marble Cleaner",
                "Wood Cleaner", "Leather Cleaner", "Furniture Polish", "Carpet Cleaner",
                "Carpet Stain Remover", "Upholstery Cleaner", "Air Freshener Spray", "Air Freshener Plug-In",
                "Air Freshener Gel", "Air Freshener Automatic", "Fabric Refresher", "Odor Eliminator",
                "Laundry Detergent Liquid", "Laundry Detergent Pods", "Laundry Detergent Powder", "Laundry Detergent Sheets",
                "Fabric Softener Liquid", "Fabric Softener Sheets", "Stain Remover Spray", "Stain Remover Stick",
                "Bleach Alternative", "Color-Safe Bleach", "Laundry Booster", "Laundry Sanitizer",
                "Delicates Wash", "Wool & Cashmere Wash", "Lingerie Wash", "Sports Detergent",
                "Baby Laundry Detergent", "Pet Stain & Odor Remover", "Lint Roller", "Static Guard Spray",
                "Dishwasher Detergent Pods", "Dishwasher Detergent Liquid", "Dishwasher Detergent Powder", "Dishwasher Detergent Gel",
                "Dishwasher Rinse Aid", "Dishwasher Cleaner", "Dish Soap", "Dish Soap Antibacterial",
                "Dish Soap Concentrate", "Dish Soap Gentle", "Dish Soap Refill", "Dish Wand Refills",
                "Steel Wool Pads", "Scouring Pads", "Non-Scratch Scrubbers", "Copper Scrubbers",
                "Paper Towels", "Paper Towels Select-A-Size", "Paper Towels Reusable", "Paper Towels Multi-Surface",
                "Toilet Paper", "Toilet Paper Ultra Soft", "Toilet Paper Double Roll", "Toilet Paper Mega Roll",
                "Facial Tissues", "Facial Tissues With Lotion", "Facial Tissues Travel Pack", "Napkins Paper",
                "Napkins Cloth-Like", "Paper Plates", "Paper Bowls", "Paper Cups",
                "Plastic Cutlery", "Bamboo Cutlery", "Plastic Straws", "Paper Straws",
                "Food Storage Bags Small", "Food Storage Bags Medium", "Food Storage Bags Large", "Food Storage Bags Freezer",
                "Food Storage Containers", "Aluminum Foil", "Plastic Wrap", "Wax Paper",
                "Parchment Paper", "Garbage Bags Small", "Garbage Bags Tall Kitchen", "Garbage Bags Large",
                "Garbage Bags Drawstring", "Garbage Bags Flap Tie", "Trash Can Liners", "Compostable Bags",
                "Broom", "Dustpan", "Mop", "Mop Refill Heads",
                "Sponge Mop", "Sponges", "Magic Eraser", "Microfiber Cloths",
                "Dusting Cloths", "Dusting Wand", "Feather Duster", "Scrub Brush",
                "Toilet Brush", "Toilet Brush Refills", "Plunger", "Dish Brush",
                "Bottle Brush", "Vacuum Bags", "Carpet Sweeper", "Rubber Gloves",
                "Disposable Gloves", "Dust Masks", "Squeegee", "Cleaning Caddy",
                "Laundry Basket", "Laundry Hamper", "Clothespins", "Clothesline",
                "Ironing Board Cover", "Starch Spray", "Wrinkle Release Spray", "Dryer Balls",
                "Ant Killer", "Roach Killer", "Fly Swatter", "Fly Paper",
                "Mouse Traps", "Moth Balls", "Insect Repellent", "Mosquito Repellent",
                "Batteries AA", "Batteries AAA", "Batteries C", "Batteries D",
                "Batteries 9V", "Light Bulbs", "LED Light Bulbs", "Extension Cords",
                "Power Strips", "Flashlights", "Candles", "Matches",
                "Lighters", "Safety Pins", "Sewing Kit", "Super Glue",
                "Duct Tape", "Packing Tape", "Masking Tape", "Scissors",
                "Picture Hangers", "Command Strips", "WD-40", "Shoe Polish"
            ]
        }
}


def generate_grocery_data(unique_item_count=25000):
    """Generate grocery data with unique items across all stores, including size variants."""
    unique_items = []
    seen = set()

    # Generate items from defined categories
    for cat, info in data.items():
        base_items = info["items"]
        general_variants = info.get("variants", [""])  # produce variants or default
        size_variants = info.get("sizes", {})  # size variants for some items
        package_sizes = info.get("package_sizes", {})  # Package sizes for when we aren't pricing by lb
        per_lb = info.get("per_lb", False)
        price_lo, price_hi = info["price_range"]
        # choose category brands
        cat_brands = brand_map.get(cat, [""])
        if not cat_brands:
            cat_brands = [""]
            
        for item in base_items:
            # Check if this item has size variants
            if item in size_variants:
                # Add product for each size variant
                for brand in cat_brands:
                    for general_variant in general_variants:
                        for size_info in size_variants[item]:
                            size = size_info["size"]
                            price_multiplier = size_info["price_multiplier"]
                            
                            name_parts = []
                            if brand:
                                name_parts.append(brand)
                            if general_variant:
                                name_parts.append(general_variant)
                            name_parts.append(item)
                            name_parts.append(size)  # Add size to name
                            
                            full_name = " ".join(name_parts).strip()
                            if per_lb and "(per lb)" not in full_name:
                                full_name += " (per lb)"
                            
                            if full_name not in seen:
                                seen.add(full_name)
                                base_price = random.uniform(price_lo, price_hi)
                                adjusted_price = base_price * price_multiplier
                                unique_items.append((full_name, adjusted_price))
            
            elif item in package_sizes:
                for brand in cat_brands:
                    for general_variant in general_variants:
                        for package_info in package_sizes[item]:
                            size = package_info["size"]
                            price_multiplier = package_info["price_multiplier"]
                            
                            name_parts = []
                            if brand:
                                name_parts.append(brand)
                            if general_variant:
                                name_parts.append(general_variant)
                            name_parts.append(item)
                            name_parts.append(size)
                            
                            full_name = " ".join(name_parts).strip()
                            
                            if full_name not in seen:
                                seen.add(full_name)
                                base_price = random.uniform(price_lo, price_hi)
                                adjusted_price = base_price * price_multiplier
                                unique_items.append((full_name, adjusted_price))
            
            else:
                # Handle items without size variants
                for brand in cat_brands:
                    for variant in general_variants:
                        name_parts = []
                        if brand:
                            name_parts.append(brand)
                        if variant:
                            name_parts.append(variant)
                        name_parts.append(item)
                        full_name = " ".join(name_parts).strip()
                        if per_lb and "(per lb)" not in full_name:
                            full_name += " (per lb)"
                        
                        if full_name not in seen:
                            seen.add(full_name)
                            base_price = random.uniform(price_lo, price_hi)
                            unique_items.append((full_name, base_price))

    # Shuffle and limit to required count
    random.shuffle(unique_items)
    return unique_items[:unique_item_count]

def main():
    # Generate unique items with base prices
    unique_items = generate_grocery_data(25000)
    
    # Add unique IDs to items (1-25000)
    unique_items_with_ids = [(i+1, name, base_price) for i, (name, base_price) in enumerate(unique_items)]
    
    # Save initial CSV with just item IDs and names
    items_df = pd.DataFrame([(item_id, name) for item_id, name, _ in unique_items_with_ids], 
                           columns=["id", "name"])
    items_output_path = "unique_grocery_items.csv"
    items_df.to_csv(items_output_path, index=False)
    print(f"Saved {len(items_df)} unique items to {items_output_path}")
    
    # Generate prices for stores A-D for each unique item
    all_items = []
    for item_id, name, base_price in unique_items_with_ids:
        store_prices = generate_store_prices(base_price)
        for store, price in store_prices.items():
            all_items.append((item_id, name, store, price))
    
    # Create DataFrame with ID included
    df = pd.DataFrame(all_items, columns=["id", "name", "store", "price"])

    df = df.sample(frac=1).reset_index(drop=True) # Randomize rows
    
    # Save to CSV
    output_path = "grocery_items_refined.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Generated {len(df)} total rows ({len(unique_items)} unique items × 4 stores)")
    print(f"Saved to {output_path}")
    
    # Show basic statistics
    print("\nPrice statistics by store:")
    store_stats = df.groupby('store')['price'].agg(['min', 'mean', 'max'])
    print(store_stats)

if __name__ == "__main__":
    main()
