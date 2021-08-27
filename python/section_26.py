from typing import TextIO


class Square:
    def __init__ (self, side_length):
        self.side_length = side_length
        
    def compute_area(self):
        return pow(self, side_length, 2)
    
if __name__ == "__main__":
    example_square = Square(15)
    print(example_square.compute_area())
    
    small_square = Square(2)
    print(small_square.compute_area())

class Email:
    def __init__(self, to, subject, body):
        self.to = to
        self.subject = subject
        self.body = body

    def send(self):
        print(f'Sending email with subject': {self.subject} and body: {self.body} to: {self.to} )

if __name__ == "__main__":
    greeting_email = Email("bob@nasa.gov", "welcome", "Welcome to python!")
    greeting_email.send()