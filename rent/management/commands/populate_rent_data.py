from django.core.management.base import BaseCommand
from django.utils import timezone
from rent.models import RentProperty
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with 100 fake RentProperty records'

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
        property_types = ['apartment', 'house', 'condo', 'townhouse', 'studio', 'loft']
        
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

        self.stdout.write(f'Creating {count} RentProperty records...')
        
        for i in range(count):
            # Generate random data
            property_type = random.choice(property_types)
            city = random.choice(cities)
            state = random.choice(states)
            street = random.choice(street_names)
            street_number = random.randint(100, 9999)
            zip_code = f"{random.randint(10000, 99999)}"
            
            # Generate random square footage
            sqft = random.randint(400, 2500)
            
            # Generate random pricing
            base_price = random.randint(800, 5000)
            monthly_rent = round(Decimal(base_price), 2)
            
            # Generate random investment metrics
            annual_rental_yield = round(Decimal(random.uniform(4.0, 12.0)), 2)
            cap_rate = round(Decimal(random.uniform(5.0, 10.0)), 2)
            cash_flow = round(Decimal(random.uniform(200, 1500)), 2)
            roi = round(Decimal(random.uniform(6.0, 15.0)), 2)
            
            # Generate random availability
            is_available = random.choice([True, True, True, False])  # 75% available
            is_featured = random.choice([True, False, False, False])  # 25% featured
            
            # Generate random description
            descriptions = [
                f"Beautiful {property_type} in the heart of {city}",
                f"Modern {property_type} with stunning city views",
                f"Spacious {property_type} perfect for professionals",
                f"Luxury {property_type} with premium amenities",
                f"Charming {property_type} in a quiet neighborhood",
                f"Contemporary {property_type} with modern finishes",
                f"Elegant {property_type} with high-end features",
                f"Cozy {property_type} ideal for urban living"
            ]
            
            description = random.choice(descriptions)
            
            # Create the RentProperty instance
            rent_property = RentProperty.objects.create(
                title=f"{property_type.title()} in {city} #{i+1}",
                description=description,
                property_type=property_type,
                monthly_rent=monthly_rent,
                bedrooms=random.randint(1, 4),
                bathrooms=random.randint(1, 3),
                square_feet=sqft,
                address=f"{street_number} {street}",
                city=city,
                state=state,
                zip_code=zip_code,
                annual_rental_yield=annual_rental_yield,
                cap_rate=cap_rate,
                cash_flow=cash_flow,
                roi=roi,
                is_available=is_available,
                is_featured=is_featured
            )
            
            if (i + 1) % 10 == 0:
                self.stdout.write(f'Created {i + 1} records...')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} RentProperty records!')
        )
