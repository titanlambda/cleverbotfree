import cleverbotfree.cbfree
import sys
cb = cleverbotfree.cbfree.Cleverbot()
try:
    cb.browser.get(cb.url)
except:
    cb.browser.close()
    sys.exit()
try:
    cb.get_form()
except:
    sys.exit()

def chat(userInput):
    cb.send_input(userInput)
    response = cb.get_response()    
    return response


if __name__ == '__main__':
    while True:
	    userInput = input('User: ')
	    if userInput == 'quit':
	    	cb.browser.close()
	    	break
	    response = chat(userInput)
	    print('Cleverbot: ', response)



