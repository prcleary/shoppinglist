from flask import Flask, render_template, request

def get_listitems(): 
    listitems = { "Miscellaneous" : ["Antihistamines", "Cards", "Newspaper", "Wrapping paper"], "Fruit and vegetables" : ["Apples", "Avocadoes", "Bananas", "Berries", "Broccoli", "Cabbage", "Carrots", "Cauliflower", "Celery", "Cherries", "Chillis", "Corn on cob", "Courgettes", "Cucumber", "Fresh herbs", "Garlic", "Ginger", "Grapes", "Lemons", "Lettuce", "Limes", "Mange tout", "Melons", "Mushrooms", "Nectarines", "Onions", "Oranges", "Peaches", "Pears", "Peppers", "Plums", "Potato", "Raspberries", "Salad leaves", "Shallots", "Spinach", "Strawberries", "Sugar snaps", "Sweet potato", "Tomatoes", "Watermelon"], "Meat" : ["Chicken", "Mince"], "Bakery" : ["Bagels", "Bread for kids", "Bread for parents", "Sliced bread", "Wraps"], "Lunch" : ["Hummus", "Oatcakes", "Pitta bread", "Quorn eggs"], "Dairy" : ["Butter (cooking)", "Butter (low fat)", "Cheese (block/grated)", "Cottage cheese", "Cream cheese", "Creme fraiche", "Eggs", "Milk", "Yogurt"], "Ingredients and condiments" : ["Brown sugar", "Cashew nuts", "Dried fruit", "Flour", "Honey", "Jam", "Ketchup", "Lea and Perrins", "Lemon juice", "Mayonnaise", "Mustard", "Olive oil", "Pasta", "Pepper", "Rice", "Salad dressing", "Salt", "Soy sauce", "Sugar", "Vegetable oil"], "Tins" : ["Baked beans", "Butter beans", "Chickpeas", "Kidney beans"], "Breakfast" : ["Muesli", "Peanut butter", "Porridge", "Weetabix"], "Desserts" : ["Ice cream", "Jelly"], "Household" : ["Batteries", "Bird food", "Bleach", "Cling film", "Cotton buds", "Dental floss", "Deodorant (Neena)", "Deodorant (Paul)", "Dishwasher tablets", "Dog food", "Freezer/sandwich bags", "Furniture polish", "Hand wash dispensers", "Kitchen foil", "Light bulbs", "Mouthwash", "Paper towels", "Plasters", "Razors (Neena)", "Razors (Paul)", "Rubbish bags", "Sandwich bags", "Shampoo (Paul)", "Shampoo for kids", "Shaving foam", "Soap", "Sponges /scrubbers", "Tissues", "Toilet paper", "Toothbrushes", "Toothpaste", "Washing powder", "Washing up liquid"], "Frozen" : ["Fish fingers", "Frozen pizzas", "Frozen vegetables"], "Snacks" : ["Biscuits", "Crackers", "Crisps", "Nuts", "Sweets"], "Drinks" : ["Beer", "Bottled water", "Chai", "Cocoa", "Coffee", "Fruit juice", "Herbal teas", "Rooibos", "Tea", "Vimto", "Wine"]}
    return listitems

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    return render_template('index.html', 
            listitems = get_listitems())

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

