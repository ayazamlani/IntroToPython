from student import Student

# install and import PIL
from PIL import Image
import json

with open('students.json', 'r') as f:
    data = json.loads(f.read())
    for student in data['students']:
        name = student['name']
        present = input(f'Is {name} here? (y/n)')
        if present == 'y':
            print(f'{name} marked present')
        else:
            img = Image.open(student['qr'])
            print(f'Here is {name}\'s contact information')
            img.show()
