from flask import Flask, render_template, request

def get_misc(): 
    misc = ["Antihistamines", "Cards", "Newspaper", "Wrapping paper"]
    return misc

def get_fruitveg(): 
    fruitveg = ["Apples", "Avocadoes", "Bananas", "Berries", "Broccoli", "Cabbage", "Carrots", "Cauliflower", "Celery", "Cherries", "Chillis", "Corn on cob", "Courgettes", "Cucumber", "Fresh herbs", "Garlic", "Ginger", "Grapes", "Lemons", "Lettuce", "Limes", "Mange tout", "Melons", "Mushrooms", "Nectarines", "Onions", "Oranges", "Peaches", "Pears", "Peppers", "Plums", "Potato", "Raspberries", "Salad leaves", "Shallots", "Spinach", "Strawberries", "Sugar snaps", "Sweet potato", "Tomatoes", "Watermelon"]
    return fruitveg

def get_meat(): 
    meat = ["Chicken", "Mince"]
    return meat

def get_bakery(): 
    bakery = ["Bagels", "Bread for kids", "Bread for parents", "Sliced bread", "Wraps"]
    return bakery

def get_lunch(): 
    lunch = ["Hummus", "Oatcakes", "Pitta bread", "Quorn eggs"]
    return lunch

def get_dairy(): 
    dairy = ["Butter (cooking)", "Butter (low fat)", "Cheese (block/grated)", "Cottage cheese", "Cream cheese", "Creme fraiche", "Eggs", "Milk", "Yogurt"]
    return dairy

def get_ingcond(): 
    ingcond = ["Brown sugar", "Cashew nuts", "Dried fruit", "Flour", "Honey", "Jam", "Ketchup", "Lea and Perrins", "Lemon juice", "Mayonnaise", "Mustard", "Olive oil", "Pasta", "Pepper", "Rice", "Salad dressing", "Salt", "Soy sauce", "Sugar", "Vegetable oil"]
    return ingcond

def get_tins(): 
    tins = ["Baked beans", "Butter beans", "Chickpeas", "Kidney beans"]
    return tins

def get_breakfast(): 
    breakfast = ["Muesli", "Peanut butter", "Porridge", "Weetabix"]
    return breakfast

def get_desserts(): 
    desserts = ["Ice cream", "Jelly"]
    return desserts

def get_household(): 
    household = ["Batteries", "Bird food", "Bleach", "Cling film", "Cotton buds", "Dental floss", "Deodorant (Neena)", "Deodorant (Paul)", "Dishwasher tablets", "Dog food", "Freezer/sandwich bags", "Furniture polish", "Hand wash dispensers", "Kitchen foil", "Light bulbs", "Mouthwash", "Paper towels", "Plasters", "Razors (Neena)", "Razors (Paul)", "Rubbish bags", "Sandwich bags", "Shampoo (Paul)", "Shampoo for kids", "Shaving foam", "Soap", "Sponges /scrubbers", "Tissues", "Toilet paper", "Toothbrushes", "Toothpaste", "Washing powder", "Washing up liquid"]
    return household

def get_frozen(): 
    frozen = ["Fish fingers", "Frozen pizzas", "Frozen vegetables"]
    return frozen

def get_snacks(): 
    snacks = ["Biscuits", "Crackers", "Crisps", "Nuts", "Sweets"]
    return snacks

def get_drinks(): 
    drinks = ["Beer", "Bottled water", "Chai", "Cocoa", "Coffee", "Fruit juice", "Herbal teas", "Rooibos", "Tea", "Vimto", "Wine"]
    return drinks


app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    return render_template('index.html', 
            misc = get_misc(), 
            fruitveg = get_fruitveg(),
            meat = get_meat(),
            bakery = get_bakery(),
            lunch = get_lunch(),
            dairy = get_dairy(),
            ingcond = get_ingcond(),
            tins = get_tins(),
            breakfast = get_breakfast(),
            desserts = get_desserts(),
            household = get_household(),
            frozen = get_frozen(),
            snacks = get_snacks(),
            drinks = get_drinks())

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

