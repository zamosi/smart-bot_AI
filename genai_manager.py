from config import API_key
import google.generativeai as genai

class Gen_ai_Manager(object):
    def __init__(self,question):
        self.question = question


    def generate_response (self):


        genai.configure(api_key=API_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(self.question)
        return response.text