from skpy import Skype

slogin = Skype("rajgaming1526@gmail.com",1656655)

group = slogin.chats.create(["Live:.cid.142ff282aa27aaa","Live:.cid.142ff282as27aca"])

contact = slogin.contacts["Live:.cid.142ff282aa27aaa"]
with open("C:/USER/RAJHERO/DOWNLOADS/skg.png","rb") as f:
    contact.chat.sendFile(f,"skg.png",image=True)
# contact.chat.sendMsg('he who r you')

# for i in contact :
    # print(i)