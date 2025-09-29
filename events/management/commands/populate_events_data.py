from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with 100 fake Event records'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Number of records to create (default: 100)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Event types (matching model choices)
        event_types = ['investment_seminar', 'property_tour', 'networking', 'workshop', 'conference', 'webinar']
        
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
        
        # Venue names
        venues = [
            'Convention Center', 'Business Center', 'Conference Hall', 'Auditorium',
            'Hotel Ballroom', 'Community Center', 'University Hall', 'Plaza',
            'Business Park', 'Financial Center', 'Investment Center', 'Real Estate Center'
        ]
        
        # Event descriptions
        descriptions = [
            "Join us for an exclusive investment opportunity presentation featuring premium real estate properties with exceptional ROI potential.",
            "Discover the latest market trends and investment strategies in our comprehensive real estate seminar.",
            "Learn from industry experts about profitable real estate investment opportunities in emerging markets.",
            "Explore high-yield investment properties and network with successful real estate investors.",
            "Gain insights into market analysis techniques and investment portfolio optimization strategies.",
            "Attend our property showcase featuring luxury real estate investments with guaranteed returns.",
            "Participate in our investment workshop and learn advanced real estate investment strategies.",
            "Connect with top real estate professionals and discover exclusive investment opportunities."
        ]
        
        # Target audiences
        target_audiences = [
            'Accredited Investors', 'First-time Investors', 'Experienced Investors',
            'Real Estate Professionals', 'Property Managers', 'Investment Advisors',
            'High Net Worth Individuals', 'Institutional Investors', 'Retail Investors'
        ]
        
        # Investment focuses
        investment_focuses = [
            'Residential Real Estate', 'Commercial Properties', 'REITs',
            'Property Development', 'Real Estate Syndication', 'Market Analysis',
            'Investment Strategies', 'Portfolio Management', 'Risk Assessment'
        ]
        
        # Speaker names
        speaker_names = [
            'John Smith', 'Sarah Johnson', 'Michael Brown', 'Emily Davis',
            'David Wilson', 'Lisa Anderson', 'Robert Taylor', 'Jennifer Martinez',
            'William Garcia', 'Amanda Rodriguez', 'Christopher Lee', 'Michelle White'
        ]
        
        # Speaker titles
        speaker_titles = [
            'Senior Investment Advisor', 'Real Estate Expert', 'Market Analyst',
            'Investment Strategist', 'Property Consultant', 'Financial Advisor',
            'Real Estate Developer', 'Investment Manager', 'Portfolio Manager',
            'Market Research Director', 'Investment Banking VP', 'Real Estate CEO'
        ]

        self.stdout.write(f'Creating {count} Event records...')
        
        for i in range(count):
            # Generate random data
            event_type = random.choice(event_types)
            city = random.choice(cities)
            state = random.choice(states)
            venue = random.choice(venues)
            location = f"{venue}, {city}, {state}"
            
            # Generate random event date (between now and 6 months from now)
            start_date = timezone.now() + timedelta(days=random.randint(1, 180))
            
            # Generate random duration (1-4 hours)
            duration_hours = random.randint(1, 4)
            end_date = start_date + timedelta(hours=duration_hours)
            
            # Generate random capacity
            max_attendees = random.randint(20, 200)
            
            # Generate random registration fee
            registration_fee = round(random.uniform(0, 500), 2)  # Some events are free
            
            # Generate random status
            is_active = random.choice([True, True, True, False])  # 75% active
            is_featured = random.choice([True, False, False, False])  # 25% featured
            
            # Generate random data
            description = random.choice(descriptions)
            target_audience = random.choice(target_audiences)
            investment_focus = random.choice(investment_focuses)
            speaker_name = random.choice(speaker_names)
            speaker_title = random.choice(speaker_titles)
            
            # Create the Event instance
            event = Event.objects.create(
                title=f"{event_type.replace('_', ' ').title()} #{i+1}",
                description=description,
                event_type=event_type,
                date=start_date,
                end_date=end_date,
                location=location,
                city=city,
                state=state,
                max_attendees=max_attendees,
                registration_fee=registration_fee,
                target_audience=target_audience,
                investment_focus=investment_focus,
                speaker_name=speaker_name,
                speaker_title=speaker_title,
                is_active=is_active,
                is_featured=is_featured
            )
            
            if (i + 1) % 10 == 0:
                self.stdout.write(f'Created {i + 1} records...')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} Event records!')
        )
