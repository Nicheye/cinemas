from django.core.management.base import BaseCommand
from main.models import Cinema
import requests
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch films data from an external API and save to database'

    def handle(self, *args, **options):
        # Your scraping logic here
        base_url = 'https://opendata.mkrf.ru/v2'
        endpoint = '/cinema/$?schema'
        api_key = '874a9e9a4d4c7ba0d9562b3a9794b52fe5db86b1bdc35f1bdb7e5a3fa163aec3'
        headers = {'X-API-KEY': api_key}
        final_url = base_url + endpoint
        
        # Define parse function before calling it
        def parse(url):
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                # Inside your parse function
                # Inside your parse function
                cinemas_to_create = []

                for opium in data['data']:
                    gener = opium['data']['general']
                    cin_obj = Cinema(
                        title=gener['name'],
                        location=gener['locale']['name'],
                        street=gener['address']['street'],
                        ur_name=gener['organization']['name'],
                        map=gener['address']['mapPosition']['coordinates']
                    )

                    # Check if 'contacts' key exists before accessing 'website'
                    if 'contacts' in gener:
                        cin_obj.website = gener['contacts'].get('website', '')
                    else:
                        cin_obj.website = ''

                    # Check if 'organization' key exists before accessing 'inn'
                    if 'organization' in gener:
                        cin_obj.inn = gener['organization'].get('inn', '')
                    else:
                        cin_obj.inn = ''

                    cinemas_to_create.append(cin_obj)

                # Bulk insert into the database
                Cinema.objects.bulk_create(cinemas_to_create)



            
            if 'nextPage' in data and data['nextPage'] != '':
                new_url = data['nextPage']
                parse(new_url)

        # Call the parse function after its definition
        parse(final_url)
