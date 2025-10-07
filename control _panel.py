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
            
            self.groups[group_name].append(new_device)
            print('///////bamofghtia')
            
        else:
            print('agha in esm vojod ndre') #...
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print('....')
            
            
            
    def get_devices(self,group_name):
        
        devices=self.groups[group_name]
        return devices
        
        
        
    def trun_on_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices=self.get_devices(group_name)
            
            for device in devices:
                device.turn_on()
            
        else:
            print('....') 
            
            
            
    def turn_off_in_group(self,group_name):
        '''
        biad dakhele oon group_name doone doone ro
        khamoosh kone 
        
        
        '''
        pass
    
    
    def turn_on_all(self):
        '''
        tamame device haro roshan kone
        too livign toome parking hgarjaa
        hamaroo roshan kone
        '''
        pass
    
    
    def turn_off_all(self):
        '''
        hamaro khamoosh kone
        '''
        
        
        pass
    
    
    def get_status_in_group(self,group_name):
        '''
        be ezaye device haye tooye masalan felan group
        living_room --> bebine roshanan ya khamoshan
        porint kone
        
        a.get_status_in_group('living_room')
        
        device {name} is on
        ... ..  .. ois off
        .. .. .. is on
        '''
        
    def get_status_in_device_type(self,dvice_type):
        
        '''
        varaye kole devicd haee k hasan
        bere device_typeshono check kone
        
        fght lamparo bere check kone
        
        lamps -->lampa
        doors --L> fght doora
        (too ch groupi , device_type)
        
        statuseshono bede

        
        '''
        pass
    
    
    #tabe ee bename create_device???
    
    def create_sensor(self):
        pass
    
    def create_multiple_sensor(self):
        pass
    
    
    
    
