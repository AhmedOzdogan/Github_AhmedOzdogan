from django.core.management.base import BaseCommand
from mainapp.models import MenuItem
from django.core.files.images import ImageFile
from pathlib import Path

class Command(BaseCommand):
    help = 'Loads menu items from local images'

    def handle(self, *args, **kwargs):
        image_dir = Path('media/menu_images')

        items = [
            ("Arancini", "Crispy fried rice balls with cheese.", 6.99, 'starter', "arancini.jpg"),
            ("Beer", "Chilled Italian beer.", 4.50, 'drink', "beer.jpg"),
            ("Bruschetta", "Toasted bread with tomatoes and basil.", 5.99, 'starter', "bruschetta.jpg"),
            ("Caprese Salad", "Fresh tomatoes, mozzarella & basil.", 7.49, 'starter', "caprese_salad.jpg"),
            ("Coke", "Refreshing Coca-Cola.", 2.99, 'drink', "coke.jpg"),
            ("Fettuccine Alfredo", "Creamy pasta with parmesan.", 11.99, 'main', "fettuccine_alfredo.jpg"),
            ("Lasagna", "Traditional meat and cheese lasagna.", 12.99, 'main', "lasagna.jpg"),
            ("Lemonade", "Freshly squeezed lemonade.", 3.50, 'drink', "lemonade.jpg"),
            ("Penne Arrabbiata", "Spicy penne with tomato sauce.", 10.49, 'main', "penne_arrabbiata.jpg"),
            ("Pizza Calzone", "Folded pizza with rich fillings.", 12.49, 'main', "pizza_calzone.jpg"),
            ("Pizza Focaccia", "Simple pizza with rosemary & oil.", 9.99, 'main', "pizza_focaccia.jpg"),
            ("Four Cheese Pizza", "Pizza with 4 Italian cheeses.", 13.50, 'main', "pizza_four_cheese.jpg"),
            ("Pizza Margherita", "Classic tomato and mozzarella pizza.", 10.99, 'main', "pizza_margherita.jpg"),
            ("Ravioli", "Stuffed pasta with ricotta and spinach.", 11.49, 'main', "ravioli.jpg"),
            ("Spaghetti Carbonara", "Creamy pasta with pancetta.", 11.99, 'main', "spaghetti_carbonara.jpg"),
            ("Water", "Bottled still water.", 1.99, 'drink', "water.jpg"),
        ]

        for name, desc, price, category, image_name in items:
            image_path = image_dir / image_name
            if not image_path.exists():
                self.stdout.write(self.style.WARNING(f"Image not found: {image_path}"))
                continue

            with open(image_path, 'rb') as img_file:
                menu_item = MenuItem(
                    name=name,
                    description=desc,
                    price=price,
                    category=category,
                )
                menu_item.image.save(image_name, ImageFile(img_file), save=True)
                self.stdout.write(self.style.SUCCESS(f"Added: {name}"))
