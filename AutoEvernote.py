#!/usr/bin/env python2
#coding=utf8
#Code:Tyskin
#reference: 
#           Evernote API Docs
#           Evernote API Python 2
#           Evernote Controller in https://github.com/littlecodersh/EasierLife/tree/master/Programs/Evernote/PackMemo

#-------------------------------------------------------------------
#libs
import evernote
import sys
import hashlib #to calculate the md5 of rescrouce
import binascii #to trans hash into main content
#from oauth import oauth
#from storage import storage
import evernote.edam.type.ttypes as Types             #include all the types of evernote
import evernote.edam.notestore.NoteStore as NoteStore #include the method of notestore,  however, the method can all be get in api.client
from evernote.api.client import EvernoteClient        #the only 2 class in api, the other one is Store
import subprocess
#Vars
SANDBOX = False
SERVICE_HOST = 'app.yinxiang.com' 
OAUTH_MODE=False #if is true, client can get token automactcly, unfortunally, this function hasn't been developed done
SPECIAL_DEV_TOKEN = True
DEV_TOKEN =''
LOCAL_STORAGE = False
#put your home page guid here
HOMEPAGE=''
LANGUAGE= 'CN'  #'EN' #CN
import subprocess

#main strueture of this class
#self.client
#self.token
#self.userStore
#self.noteStore
#self.user          (username,name,shardID,id)
#self.homepage      (guid,)
#self.CODING_IS_UTF8=True

class AutoEvernote:
    'this Class provide the basic control method of evernote.\n use this to log into your acccount \n'
    
    #login and create the 2 key classes: usestore and notestore
    def __init__(self,dev_token=DEV_TOKEN,homepage_guid=HOMEPAGE):
        self.sys_login(dev_token=dev_token)
        self.sys_check_coding()
        self.homepage_checker(homepage_guid=homepage_guid)
        
    def __set_storage(self):
        print ('Loading Storage')
        #self.storage = Storage(self.noteStore, self.token)
        print ('Storage loaded')
    def homepage_checker(self,homepage_guid=HOMEPAGE):
        self.homepage=Types.Note()
        self.homepage.guid=homepage_guid
        sys.stdout.write('checking homepage \n')
        while self.homepage.guid == '':
                print("You Haven't set your home page\n Do you want to set home page yourself[1] or let me find it out?[2] \n")
                decision=input()
                if decision==1:
                    self.homepage.guid=input("Please input the Guid of your home page with '':")
                elif decision == 2:
                    self.homepage.guid=self.homepage_guid_finder()
                else:
                    print("input error")        
        self.hompage=self.noteStore.getNote(self.token,self.homepage.guid,True,True,True,True)        
        self.printf("Load Home Page Succeed:"+self.hompage.title)
    def homepage_guid_finder(self):
        filter = NoteStore.NoteFilter()
        filter.words = "intitle:'home page'" 
        spec = NoteStore.NotesMetadataResultSpec()
        spec.includeTitle = True
        spec.includeCreated=True
        spec.includeDeleted=True
        ourNoteList = self.noteStore.findNotesMetadata(self.token, filter, 0, 10, spec)
        filter.words = "intitle:'首页'" 
        ourNoteList.notes += self.noteStore.findNotesMetadata(self.token, filter, 0, 10, spec).notes
        
        print("For the operation of AutoEvernote, We need you create a home page to store the necessary data of AutoEvernote. \n Which of notes belowing is your home page? \n input the index number of your note or 999 if no note below you want to use it as your home page.\n if your answer is '999', we will create one for you in your default notebook\n")
        index=0
        for note in ourNoteList.notes:
            print str(index), 
            print ':',
            print ' Created:',
            print self.time_timestamp_2_localtime(note.created),
            print " Guid:",
            print note.guid,
            self.printf(note.title)                        
            index+=1
        index=input()
        if index==999:
            note = Types.Note()
            note.title = 'Home Page'
            note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            note.content += "<en-note>" 
            
            note.content += '</en-note>'
            
            note = self.noteStore.createNote(self.token, note)
            return note.guid
        else:
            return ourNoteList.notes[index].guid
    def tagsMap_checker(self):
        print("")
    def tagsMap_creater(self):
        #creat in local
        #tags=self.noteStore.listTags(self.token)
        #f=open('advancedTagsMap.csv','w+')
        #for tag in tags: f.write(str(tag.updateSequenceNum)+','+tag.guid+','+tag.name+','+str(tag.parentGuid)+'\n')
        #f.close()
        
        #1 prepare resourse:tagmapcsv
        ##create in memory        
        tagmapcsv=Types.Resource()
        tagmapcsv.data=Types.Data()        
        ##import data.body
        tags=self.noteStore.listTags(self.token)
        tagmapcsv.data.body=""
        for tag in tags: 
            bodyline=str(tag.updateSequenceNum)+','+tag.guid+','+tag.name+','+str(tag.parentGuid)+'\n'
            tagmapcsv.data.body += bodyline
        ##calculate data.hash: and hexhash
        m2 = hashlib.md5() 
        m2.update(tagmapcsv.data.body) 
        tagmapcsv.data.bodyHash=m2.digest()
        hexhash = binascii.hexlify(tagmapcsv.data.bodyHash)
        ##set the file 
        tagmapcsv.mime='application/csv'
        ratt=Types.ResourceAttributes()
        ratt.fileName="Advanced Tags Mapping.csv"
        ratt.attachment=True
        tagmapcsv.attributes=ratt
        #tagmapcsv.attributes.append(ratt)
        
        #2 add resource to main content
        note=Types.Note()
        note.title = 'Advanced Tags Mapping'
        note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content +="<en-note>"
        note.content +="<br /><en-media hash=\"%s\" type=\"%s\" /><br />" % (hexhash,tagmapcsv.mime)
        note.content +="</en-note>"
        
        
        
        #3 add resource to resource list
        if note.resources==None: note.resources=[]        
        note.resources.append(tagmapcsv)
        
        #4 upload note
        note = self.noteStore.createNote(self.token, note)
        
        #print("") 
        return note
    def tagsMap_updater(self):
        print("find and replace before and after")
    def resourse_append(self,note_in,resource_str,resource_name):
        #0 preparation 
        note=Types.Note
        note.guid=""
        if type(note_in)==type(note):
            note=note_in
            print("append and update")
        if type(note_in)==type(note.guid):
            note.guid=note_in
            note=self.noteStore.getNote(self.token,note.guid,True,True,True,True)
            print("load, append and update")
            
        #1 prepare resource
        ## create in memory        
        resource=Types.Resource()
        resource.data=Types.Data()        
        ## import data.body        
        resource.data.body=resource_str        
        ## calculate data.hash: and hexhash
        m2 = hashlib.md5() 
        m2.update(resource.data.body) 
        resource.data.bodyHash=m2.digest()
        hexhash = binascii.hexlify(resource.data.bodyHash)
        ## set the file 
        resource.mime='application/octet-stream'
        ratt=Types.ResourceAttributes()
        ratt.fileName=resource_name
        ratt.attachment=True
        resource.attributes=ratt
        #resource.attributes.append(ratt)
        
        #2 add resource tag to the end of main content        
        resource_tag_start=note.content.rfind("</en-note>")
        newcontent=note.content[0:resource_tag_start]
        newcontent+="<br /><en-media hash=\"%s\" type=\"%s\" /><br />" % (hexhash,resource.mime)
        newcontent+=note.content[resource_tag_start:]
        note.content=newcontent
        #3 add resource to list
        if note.resources==None: note.resources=[] 
        note.resources.append(resource)
        
        #4 update note
        self.noteStore.updateNote(self.token, note)
        print("appended one resource at the end of note page")
    def note_createblank(self):
        print("")
    def sys_check_coding(self):
        if sys.platform=='win32':
            process = subprocess.Popen("chcp", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            command_output = process.stdout.read().decode('utf-8')
            if    '936'  in command_output:  self.CODING=936    #GB2312
            elif '1200'  in command_output:  self.CODING=1200   #unicode
            elif '65001' in command_output:  self.CODING=65001  #utf-8
    def sys_login(self,dev_token=DEV_TOKEN):
        loginsucceed = False        
        while loginsucceed == False:
            if OAUTH_MODE == False:
                if dev_token == '':
                    ready = False
                    while ready == False:
                        try:
                            self.token = input("Please input your DeveloperToken with '': \n     if you don't have, looking for https://app.yinxiang.com/api/DeveloperToken.action \n")
                        except SyntaxError:
                            print("Error: Please input your DeveloperToken with '': \n Example: \n     'S=xxx :P= xxx1cd:A=en-devtoken:V=2:H= xxx' \n\n")
                        else:
                            sys.stdout.write('good\r')
                            ready=True
                else:
                    self.token = dev_token
            else:
                pass
                #self.token = oauth()
                
            sys.stdout.write('Logging\r')
            if SANDBOX:
                self.client = EvernoteClient(token=self.token)
            else:
                self.client = EvernoteClient(token=self.token, service_host=SERVICE_HOST)
            
            self.userStore = self.client.get_user_store()
            self.noteStore = self.client.get_note_store()
            
            if LOCAL_STORAGE: self.__set_storage()
            try:
                self.user=self.userStore.getUser()                
                print ('Login Succeed as ' + self.user.username + '\n')
                loginsucceed = True
            except:
                print('Something Wrong, maybe your tkoken not good \n')
    def printf(self,a,end='\n'):
        a=str(a)
        b=a.decode('utf-8')
        if end=='\n':
            print(b)
        else:
            print b+end,
    def time_timestamp_2_localtime(self,timestamp,style=0):
        import time
        sint=123
        slong=1569119627000
        teim=0
        if   type(timestamp)==type(sint):   teim=timestamp
        elif type(timestamp)==type(slong):  teim=int(timestamp/1000)
        else: return None
        time_local = time.localtime(teim)
        if style == 0:
            return time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        else:
            return time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        
#-----------------------------------------------------------------
if __name__ == '__main__':
    e = AutoEvernote()        

#IN TERMINAL
#from AutoEvernote import AutoEvernote 
#e = AutoEvernote() 
#e.hompage_checker()
#e.homepage_guid_finder()
#e.tagsMap_creater()

