import logging
from genai_manager import Gen_ai_Manager

logger = logging.getLogger('my_logger')

def ask_AI(question):
    q = Gen_ai_Manager(question)
    return q.generate_response()

if __name__ == '__main__':
    print(ask_AI(''))    