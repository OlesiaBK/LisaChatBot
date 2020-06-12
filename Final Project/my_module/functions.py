"""A collection of function for doing my project."""

import apiai, json
import ipywidgets as widgets
from IPython.display import display

# constant
# list of items
MENU = {"Cheese Cake": "$7","Coffee":"$3","Pancakes":"$5","Cookie":"$3"}

#The idea of the basic structure of code set-up is coming from solkogan
#(https://github.com/solkogan/dialogflow_example/blob/master/dialogai.py)
def send_message(text):
    
    """Connects to DialogFlow Id, starts the Chatbot, specifying the language
    
     Parameters
     ----------
     l: string
         Input Message
     
     Returns
     -------
     response: string
          If the response exists
     
     """
    # token API connects to DialogFlow
    request = apiai.ApiAI('ba2fa62a475d4984abeebf8b4d8b14ee').text_request()
    
    #Choosing the language 
    request.lang = 'en'
    
    #Connecting to the training session
    request.session_id = 'Lisa'
    
    #Setting the message 
    request.query = text 
    
    #Unpacking JSON and getting the response
    
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))    
    response = responseJson['result']['fulfillment']['speech'] 
    
    #If chatbot has a response, it gives a response
    if response:
        return response

    
def print_greeting():
    """Print greating message
    
     Parameters
     ----------
     None
     
     Returns
     -------
     None
     
     """

    intro = "Good morning, you are in the bakery shop"
    print(intro)

    
def get_name():
    """Get user name

     Parameters
     ----------
     None

     Returns
     -------
     name: string

    """

    name = input('Enter your name: ')
    return name


def get_address():
    """Get user address
    
     Parameters
     ----------
     None
     
     Returns
     -------
     address: string
     
     """

    address = input('Enter your address:')
    return address


def get_user_phone():
    """Get user phone number
    
     Parameters
     ----------
     None
     
     Returns
     -------
     phone: string
     
     """

    phone = input('Enter your phone:')
    return phone


def get_user_info():
    """Run user diolog to collect user data
    
     Parameters
     ----------
     None
     
     Returns
     -------
     None
     
     """
 
    name = get_name()
    print(name, ' welcome')

    address = get_address()
    print("address " + address + " is saved")

    phone = get_user_phone()
    print('thx, we have saved phone:' + phone)

    
def print_commands():
    """Print commands info
    
     Parameters
     ----------
     None
     
     Returns
     -------
     None
  
    """
    
    commands_info = '''
call menu - write "menu"
if u wanna quite - "quit"
'''
    print(commands_info)

    
def print_menu():        
    """Loop over dict, print items and return choosen user product
    
     Parameters
     ----------
     None
     
     Returns
     -------
     product: String
  
     """

    for item in MENU:
        print(item, MENU.get(item))

    product = input('Choose product ')
    return product


def split_price(price_str):
    """Get price string and convert to int
    
     Parameters
     ----------
     price_str: string
     
     Returns
     -------
     price_int: int
  
     """

    data = price_str.split("$")
    str_value = data[1]
    price_int = int(str_value)
    return price_int
    
def calc_products_cost(prev_total, current_price):
    """Calculate total price
    
     Parameters
     ----------
     prev_total: int
     current_price: int
     
     Returns
     -------
     total: int
  
     """
    total = prev_total + current_price
    return total


# https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Image
# https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html
def render_thx_img():
    """ Render image with thx
    
     Parameters
     ----------
     None
     
     Returns
     -------
     None
  
     """

    file = open("images/thx.jpg", "rb")
    image = file.read()
    img = widgets.Image(
        value=image,
        format='jpg',
        width=200,
    )
    display(img)

    
def print_thx(total):
    """Print thx message with total price, info and render image
    
     Parameters
     ----------
     total: Int
     
     Returns
     -------
     None
  
     """
 
    text = "Total order: " + str(total) + "$. " + "Thank you for your order. See you next time."
    print(text)
    print_commands()
    render_thx_img()

    
def print_last_sentence():  
    """Creates and defines the last sentence in the dialog
    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
 
    last=""" 
    Nice Talking to you! Goodbye!
    """

    l = input(last)


def handle_user_interaction():
    """Handle user messages and respond to them
    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """

    message =''
    total_cost = 0

    # run loop to handle eache message
    while(message != 'quit'):
        #handle first loop without user message
        if message == '':
            print_commands()
 
        message = input('Enter your message: ')

        if message == "menu":
            message = print_menu()
        # handle according to choosed product
        if message.capitalize() in MENU:
            current_price = split_price(MENU.get(message.capitalize()))
            total_cost = total_cost + current_price
            print_thx(total_cost)
        # handle quit
        elif message == "quit":
            print_last_sentence()
        # send message to dialog flow
        else:
            print(send_message(message))

#Includes: displaying intro, finishing the conversation functions, engages the Menu Function that allows menu display.
def call_lisa(): 
    """ This is a main chatbot Lisa function,displays the introduction and quits the dialog
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """

    print_greeting()

    get_user_info()

    handle_user_interaction()

            
            
            
           