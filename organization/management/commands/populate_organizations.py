import json
from os import name
from django.core.management import BaseCommand

from organization.models import Organization


class Command(BaseCommand):
    
    help = 'Prepopulating organization objects'
    
    def add_arguments(self, parser):
        parser.add_argument(
            'json_file',
            nargs='?',
            type=str,
            help='path of your json file',
            default='organization/fake_organizations.json'
        )
    
    def handle(self, *args, **options):        
                
        organization_count = 0
        organization_list = []
        
        with open(options['json_file'], 'r') as file:
            data = json.load(file)
            
            for item in data:
                organization = Organization(
                    name=item['name'],
                    url = item['url'],
                    description = item['description'],
                    logo = item['logo']                    
                )
                
                organization_list.append(organization)
                organization_count += 1
        
        Organization.objects.bulk_create(organization_list)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully: {organization_count} organization saved in database'))
