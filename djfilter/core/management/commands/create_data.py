from django.core.management.base import BaseCommand
import random,datetime
from core.models import author,category,journal

categories = ['Biometric', 'Nuclear', 'Technology', 'Programming', 'Sports', 'Economy', 'CyberSecurity']
authors = ['Jhon', 'Michael', 'Luke', 'Sally', 'Joe', 'Dude', 'Barbara', 'July']

def generate_author_name():
    index= random.randint(0,7)
    return authors[index]
def generate_category_name():
    index = random.randint(0,6)
    return categories[index]
def generate_views_count():
    return random.randint(0,100)
def generate_is_reviewed():
    val = random.randint(0,1)
    if val==1:
        return True
    return False
def generate_publish_date():
    year = random.randint(2000, 2030)
    month = random.randint(1,12)
    day = random.randint(1,28)
    print(datetime.datetime(year,month,day))
    return datetime.date(year,month,day)

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type = str, help='The txt file contains the journal title')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title =row
                author_name = generate_author_name()
                category_name =generate_category_name()
                publish_date =generate_publish_date()
                views = generate_views_count()
                reviewed =generate_is_reviewed()
                #print(title, author_name, category_name, publish_date)

                author_data = author.objects.get_or_create(name=author_name)
                category_data = category.objects.get_or_create(name=category_name)
                journal_data = journal(
                    title = title,
                    author = author.objects.get(name=author_name),
                    publish_date = publish_date,
                    views = views,
                    reviewed = reviewed
                )
                journal_data.save()
                journal_data.categories.add(category.objects.get(name=category_name))
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
