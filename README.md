# AutoEvernote
This Project is a auto machine which aiming to make the everntoe more easy to use. it can help to deal all the repetitive works automactily.

meanwhile, extending the properties of tag and note is one of the most important outcome of this project. all the properties will be automaticly added, checked and updated including some common use tags of notes.

the extended properties will help user more easy to filter and arrange their notes. and the operation of this auto machine will strictly following the user rules. it will never be smart. which means that it will never do confusing operation. as we all know, in most of the times, smart mahcine will always waste our times like the smart filter in evernote clipper.

with the help fo the ext properities and autoevernote, the notes in everntoe will achieve a tight coupling between notes.

what's more, all the variables and configuation in autoevernote are stored in evernote page as text type. use can see and edited them easily. 



# notepage properties
the kind of note properities of evernote is too less. it will be better for user to defined out own properities ourselves like using Notion.
## note type
for different kind of 
### user's note
should be the most important notes in evernote. however, it will be always submerge into the notes season and will never be able to find out if you don't have a good habit. but my think is, why should I have a good habit? I'm using a assistant software to arrange my notes, why can't the software do it automactily?
### webpage clipping
should be the last in priority. everday i clipping dozen of webpage. they are useful but i may not able to see them again until the next time i meet a question.
### published content: book, paper and thesis
should be the most valueable notes. 
### markdown notes
### handwriting notes
### mind mapping notes

## note ext attributes
### when
created time
updated time
content pubilished time
content updated time
reminder time
last reviewed time
next reviewed time
totally time cost in this note
### how
creater of note
author of note content
how do you find this note?
how do you clipping or writing this note?
how this note be published? in which blos, which site, which column, which forlum? which book?
### where
hyperlink
fatherbook
reference note
cited notes
same refered note
same cited note
related note
### what
remark and commit
content type
importance
reviewed times
value of content

### More
user defined properities

## reference net

## remark and commit of this note
the remarks should be able to be put into user's sight before user open a note.
autoevernote will be able to put the remark into summary page and sync it the same with in-note one. this is a compromise for this time, the everntoe editor not good enough.

# Tag Properties
this project defined many new properties to tags. and this properties will be stored in a csv file as a rescrouse in evernote. most of the new properties will be added by AutoEvernote itself. some other can be added 
by use with the help and guide from user.

## tag's summary page
the summary page of a tag will provide a more visible method to user to see their notes. seems like the different views of databse in notion.
however, different with notion, the summary page will more fixable than notion. cause it is not just a table.
the autoevernote will add the notes with this tag to the summary page itself. so, in brief, the basic function fo the summary page is: creaete a outline view automacily. 
in my opion, all the use of tag is to help the autoevernote generate a summary page.
## tag's relationship
with the growthing number of tags, it will be harder to consider a tags position. for eaxmple, will you put 'London' under the 'cities' tag or 'England' tag?
the simple tag tree will never help this problem. evernote noticed this point. so they cancelled all the relationship of tags in ios and android. it is a good news for user, so we will never be confused in and waste time in clearing up our tags.
however, in my mind. i don't think it is a good idea for a note user. it is good to put all the tags into the same level, but it will be better to add more relationships between tags.

in the view of autoevernote, the relationship belowing will be added to the properties of tags. however, due to my tech level, it should be edited by use themselves.
### father and son tags
ex. London and England, Country, Toturist,
### same meaning tags
ex. London and london, great london,
### related tags
ex. London and Southampton
ex. python and perl
this can be edited automactily, we can simply add all the tags who as the same father tags as ralated tags.
## tags type
as mentioned before. for one note, it exists 2 deminsions to classify the note: one for property, one for content.
due to the lack of some necessary properties in evernote's note. we have to add some tags to a note ourselves manually as properities, like the importance, type, reviewed, come from, value and some others.
according to is for property or for content, the type of a tag will be divided to 2 class.
the property tags will be further classified into different kind of classes. which can help the tags more easily to use.
## tags rules
for adding tags automactily, user should be able to set some rules like the gmail did.

# main thread in autoevernote
## Update Tags properties
## update notes

# Further more
## editor for evernote
