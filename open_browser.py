
# importing modules



from webbrowser import open_new, open_new_tab
import pywhatkit
import importants 
import sys
from termcolor import colored, cprint

#creating CLass

class WebBrowser():

    def __init__(self,url:str):
        self.url = url;
        print(importants.statement)
    
    
    def openingbro(self):
        
        #creating the method to open the browser
        
        # if the user doesn't start with https:// then it will fail to run this if statement 
        if self.url.startswith("https://"):
            print("Its working")
            try: 
                opening_url =  open_new_tab(self.url)


                if bool(opening_url) != False:
                    no_pro = "Everything is fine"
                    def running():
                        print(no_pro)
                    running()
                    print(opening_url)
            except Exception as e:
                print(e)


                
        if not self.url.startswith("https://"):
            print("Not working")

        if self.url == "youtube":
            try:

                what_video_you_want_to_watch:str = input("Type the video name or channel:")
                searching  = pywhatkit.playonyt(what_video_you_want_to_watch)
                print(importants.searching_for_the_vid)

            except:
                something_went_wrong = lambda er: er 
                print(something_went_wrong("Error caused!!!"))
                
                    
    #creating a method to open google 
    def openingwithgoogle(self):


        if self.url == "google":
            print("Its working")
            try:
                opening_url = pywhatkit.search(self.url)
            except:
                error: str = "Could not open Google"
                print(f"Error:{error}")
            finally:
                print("Running....")

    #creating new method 
    def No(self):

        #if the user type None then it will execuse this function

        if self.url == "None":

            do_you_want_any_info: str = input("Ask anything about any topic:")

            #puttiing try catch function just in case of errors 
            
            try:

                if do_you_want_any_info != False:
                    asking = pywhatkit.info(do_you_want_any_info, lines=49)
                    successful = colored("Successfully created", "red", attrs=["reverse","blink"])
                    print(successful)
                    if asking != False:
                        def anyproblem(nope):
                            return nope
                        print(anyproblem("Nope"))
                    else:
                        print("Successfully Completed")

            except:
                #just prinint out of there are errors
                print("An Unkown Error Occurred")



#running the class or instance of class
def ru():
    
    browser = WebBrowser(url=input(f"""
    Do you want to open browser then type the url otherwise watch youtube videos then type youtube
     or you want to search something 
    then type google, 
    if none of it then type {importants.Non}:"""))

    browser.openingbro()

    browser.openingwithgoogle()

    browser.No()
    

ru()