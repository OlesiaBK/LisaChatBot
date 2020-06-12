#Tests for my functions.

from functions import *
import pytest 
   
def test__send_message(): 
    assert callable(send_message)
    assert isinstance(send_message('test'), str)
    
def test_call_lisa():  
    assert callable(call_lisa)
    assert call_lisa() == None    
     
def test_print_menu():
    assert callable(print_menu) 
    
def test_last_sentence():
    assert callable(last_sentence)
    assert last_sentence() == None

def test_print_greeting():
    assert callable(print_greeting)
    assert print_greeting() == None
    
def test_get_name():
    assert callable(get_name)
    
def test_get_user_phone():
    assert callable(get_user_phone)
    
def test_get_user_info():
    assert callable(get_user_info)

def test_print_commands():
    assert callable(print_commands)
    
def test_get_address():
    assert callable(get_address)
    
def test_render_thx_img():
    assert callable(render_thx_img)
    assert render_thx_img() == None

def test_print_thx():
    assert callable(print_thx)
    assert print_thx(10) == None 
    
def test_split_price(price_str):
    assert callable(split_price)
    assert split_price("$3") == 3

def handle_user_interaction():
    assert callable(user_interaction)
    assert user_interaction() == None 
    
def test_calc_products_cost():
    assert callable(calc_products_cost)
    assert calc_products_cost(10,5) == 15
