'''
mojgan:
ostad line 180 rahnamayee konid lotfan



APM:

salam ,bebinid aval bayad tamame device haro az har goroh bekeshid biroon
masalan

all_devices=[]
for devices in groups.values():
    for device in devices:
        all_devices.append(device)

hamchin chizaee
hala tooye all_devices for bezanid device haro bekeshid biron ye attribute daran b name device_type baayd ba 
device_type i k function migire moghayese she ag barabar bood statuse oon device gerefte beshe
yekam fkr konid roosh ag baz didid nmishe hamin paeen comment bzarid bishtr rahnamaee konm
moafagh bashid
'''




class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        print(f'device"{self.device_name}",created')

    def turn_on(self):
        print(f'device"{self.device_name}",is turn on')
        self.status='on'
        #--_.code ejra mishe

    def turn_off(self):
        print(f'device"{self.device_name}",is turn off')
        self.status='off'
        #code ejra mishe 
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        

class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
        return 25




class control_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            print(f'device"{device_name}"sakhte shod')
            self.groups[group_name].append(new_device)
            print(f'device"{device_name}",ezafe shode dar goroh"{group_name}")
            
        else:
            print('agha in esm vojod ndre') #...
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print(f'{group_name}group mojod nist')
            
            
            
    def get_devices(self,group_name):
        
        devices=self.groups[group_name]
        print(f'list devices group {group_name}')
        return devices
        
        
        
    def trun_on_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices=self.get_devices(group_name)
            
            for device in devices:
                device.turn_on()
            print(f'devices turn on')
            
        else:
            print(f'{group_name} group mojod nist')

    
            
            
            
    def turn_off_in_group(self,group_name):
        if group_name in self.groups:

            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_on()
            print(f'devices turn off')

        else:
            print(f'{group_name} group mojod nist')

    
    def turn_on_all(self):
        
        for devices in self.group.values():
            device.turn_on()
        print ('all device is turn on')
          
    
    
    def turn_off_all(self):
        for devices in self.group.values():
            device.turn_off()
        print ('all device is turn off')
        
        
        
    
    
    def get_status_in_group(self,group_name):
       if  group_name in self.groups:
            for device in self.groups[group_name]:
               status='on' 
            if device.get_status==status:
                print(f'dastgah:{status}')
            else:
                print(f'dastgah is off')
      else:
          print("group is not")


    def get_status_in_device_type(self,dvice_type):
        
        '''
        varaye kole devicd haee k hasan
        bere device_typeshono      
        fght lamparo bere check kone
        
        lamps -->lampa
        doors --L> fght doora
        (too ch groupi , device_type)
        
        statuseshono bede

        
        '''
        pass
    
    
    
    def create_sensor(self):
        0
    
    def create_multiple_sensor(self):
        pass
    
    
    
    
