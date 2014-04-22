import os

def populate():
    python_cat = add_cat('Python')

if __name__ == '__main__':
    print ("Starting Rango population Script",)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twd.settings')
    from rango.models import Category, Page
    populate()