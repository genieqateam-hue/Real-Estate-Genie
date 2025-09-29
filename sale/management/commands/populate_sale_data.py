from django.core.management.base import BaseCommand
from django.utils import timezone
from sale.models import SaleProperty
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with 100 fake SaleProperty records'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Number of records to create (default: 100)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Property types (matching model choices)
        property_types = ['apartment', 'house', 'condo', 'townhouse', 'villa', 'penthouse', 'commercial']
        
        # Cities and states
        cities = [
            'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
            'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
            'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis',
            'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Nashville',
            'Detroit', 'Oklahoma City', 'Portland', 'Las Vegas', 'Memphis', 'Louisville'
        ]
        
        states = [
            'NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'FL', 'OH', 'NC', 'IN', 'WA', 'CO',
            'DC', 'MA', 'TN', 'MI', 'OK', 'OR', 'NV', 'KY', 'AL', 'SC', 'LA', 'UT',
            'IA', 'AR', 'MS', 'KS', 'NM', 'NE', 'WV', 'ID', 'HI', 'NH', 'ME', 'RI',
            'MT', 'DE', 'SD', 'ND', 'AK', 'VT', 'WY'
        ]
        
        # Street names and addresses
        street_names = [
            'Main St', 'Oak Ave', 'Pine St', 'Cedar Ln', 'Maple Dr', 'Elm St',
            'Park Ave', 'First St', 'Second St', 'Third St', 'Broadway', 'Washington St',
            'Lincoln Ave', 'Jefferson St', 'Madison Ave', 'Franklin St', 'Roosevelt Ave',
            'Kennedy Blvd', 'Johnson St', 'Wilson Ave', 'Adams St', 'Jackson St'
        ]

        self.stdout.write(f'Creating {count} SaleProperty records...')
        
        for i in range(count):
            # Generate random data
            property_type = random.choice(property_types)
            city = random.choice(cities)
            state = random.choice(states)
            street = random.choice(street_names)
            street_number = random.randint(100, 9999)
            zip_code = f"{random.randint(10000, 99999)}"
            
            # Generate random square footage
            sqft = random.randint(500, 4000)
            
            # Generate random pricing based on property type and size
            base_price_per_sqft = random.uniform(200, 800)
            price = round(Decimal(sqft * base_price_per_sqft), 2)
            
            # Generate random lot size
            lot_size = round(Decimal(random.uniform(2000, 15000)), 2)
            
            # Generate random investment metrics
            price_per_sqft = round(Decimal(base_price_per_sqft), 2)
            appreciation_rate = round(Decimal(random.uniform(2.0, 8.0)), 2)
            market_value = round(Decimal(float(price) * random.uniform(0.9, 1.1)), 2)
            
            # Generate random investment potential
            investment_potentials = ['high', 'medium', 'low']
            investment_potential = random.choice(investment_potentials)
            
            # Generate random availability
            is_sold = random.choice([True, False, False, False])  # 25% sold
            is_featured = random.choice([True, False, False, False])  # 25% featured
            
            # Generate random description
            descriptions = [
                f"Stunning {property_type} in prestigious {city}",
                f"Luxury {property_type} with breathtaking views",
                f"Exclusive {property_type} in prime location",
                f"Magnificent {property_type} with premium amenities",
                f"Elegant {property_type} perfect for discerning buyers",
                f"Spectacular {property_type} with modern design",
                f"Sophisticated {property_type} in desirable neighborhood",
                f"Exceptional {property_type} with high-end finishes"
            ]
            
            description = random.choice(descriptions)
            
            # Create the SaleProperty instance
            sale_property = SaleProperty.objects.create(
                title=f"{property_type.title()} in {city} #{i+1}",
                description=description,
                property_type=property_type,
                price=price,
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 4),
                square_feet=sqft,
                lot_size=lot_size,
                address=f"{street_number} {street}",
                city=city,
                state=state,
                zip_code=zip_code,
                price_per_sqft=price_per_sqft,
                appreciation_rate=appreciation_rate,
                market_value=market_value,
                investment_potential=investment_potential,
                is_sold=is_sold,
                is_featured=is_featured
            )
            
            if (i + 1) % 10 == 0:
                self.stdout.write(f'Created {i + 1} records...')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} SaleProperty records!')
        )