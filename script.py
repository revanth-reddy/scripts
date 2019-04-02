from xml.dom import minidom

from apps.models import App
import sys
def run():
    print 'Starting Bakefile parser . . .\nPlease enter the name of xml file to read\n(don\'t include .xml in name)'
    file = raw_input('Name of xml file: ')
    # apps = App.objects.all()
    file = 'scripts/'+file+'.xml'
    # for app in apps:
    #     print(app)
    print '\n'
    # parse an xml file by name
    try:
        xmlfile = minidom.parse(file)
    except:
        print("File not found !\nTry with another file name\n")
        print 'Stopping Parser !!!'
        sys.exit()


    if(xmlfile.getElementsByTagName('modules')):
        modules = xmlfile.getElementsByTagName('module')

    if modules:
        module_name = modules[0].attributes['name'].value
        module_title = module_name
        app_type = 'M'  # M - module F - fork
        abstract = 'NA'
        description = 'App description'
        Active = True
        Stars = 0
        Votes = 0
        Downloads = 0
        
        print 'Name: '+module_name
        print 'Title: '+module_title
        print 'App type: '+app_type
        print 'Abstract: '+abstract
        print 'Description: '+description
        print 'Active: '+str(Active)
        print 'Stars:'+ str(Stars)
        print 'Votes:'+ str(Votes)
        print 'Downloads:'+ str(Downloads)

        """
        Creating an APP object in DB.
        """
        # no editor at present
        
        our_app = App.objects.create(name = module_name, title = module_title, app_type = app_type, abstract = abstract, description = description, stars = Stars, votes = Votes, downloads = Downloads)
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        admins = User.objects.filter(is_superuser=True)
        # making all admins/superusers as editors
        for admin in admins:
            our_app.editors.add(admin)
        
        print '\nApp added to DB \n'
        print 'App Details in DB:'
        print 'App ID: ' + str(our_app.id)
    else:
        print 'Something is not right !'
