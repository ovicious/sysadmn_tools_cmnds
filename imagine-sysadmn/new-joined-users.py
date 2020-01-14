 import csv                                                                        
 import datetime                                                                   
 import pytz                                                                       
 from django.contrib.auth.models import User                                       
                                                                                   
 # Define start and end date                                                       
 start_date  = datetime.datetime(2020, 1, 4, 00, 00, 00, 0, tzinfo=pytz.UTC)     
 end_date    = datetime.datetime(2020, 1, 12, 23, 59, 59, 999999, tzinfo=pytz.UTC)
                                       

                                                                                   
 def get_field(instance, field):                                                   
     field_path = field.split('.')                                                 
     attr = instance                                                               
     for elem in field_path:                                                       
         try:                                                                      
             attr = getattr(attr, elem)                                            
         except AttributeError:        
             return None               
     return attr                       
                                       
 # Object to dump to csv               
 usrs = User.objects.filter(date_joined__range=(start_date, end_date))
                                                                      
 # List of fields to export to csv.                                   
 field_list = ['first_name', 'last_name', 'email','username','date_joined','last_login']
 headers = ['First Name', 'Last Name', 'Email Address', 'Username', 'Date Joined', 'Last Login']
                                                                                                
 writer = csv.writer(open('user_joined_' + str(start_date)[0:10].replace('-','_') + '_to_' + str(end_date)[0:10].replace('-','_') + '.csv', 'w'
 ))                                                                                                                                            
                                                                                                                                               
 # Add CSV header if required                                                                                                                  
 writer.writerow(headers)                                                                                                                      
                                                                                                                                               
 # Write data content                                                                                                                          
 for user in usrs:                                                                                                                             
     row = []                
     for field in field_list:
         val = get_field(user, field)
         row.append(val)             
     writer.writerow(row)            
 print('User information exported successfully.')
                                     

