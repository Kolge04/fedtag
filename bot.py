import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("โก Mษn  ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ\n๐๐ธ๐๐ Federasiyasฤฑnฤฑn Rษsmi Taฤ botuyam\nโก ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ ฤฐlษ Qrupunuzdakฤฑ รyษlษri Etiket Edษ Bilษrษm\nฦmrlษrlษ Tanฤฑล Olmaq รรงรผn __ฦMRLฦR__ Butonuna Toxun",
                    buttons=(
                   
		      [Button.url('โ โโ๐๐๐ธ ๐ผ๐๐ธ๐๐ผ ๐ผ๐ โ', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('โก ๐๐ธ๐๐ ๐ฝ๐น๐ธโ', f'https://t.me/XaosResmii')],
                      [Button.url('๐ฆ๐ฟ ๐๐โ๐ผโ ๐จโ๐ป', f'https://t.me/sesizKOLGE')],
                      [Button.inline("โ ฦ๐โ๐ฦ๐", data="help")],
                    ),
                    link_preview=False
		   )

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"**โก Mษn  ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ\n**๐๐ธ๐๐ Federasiyasฤฑnฤฑn Rษsmi Taฤ botuyam\nโก ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ ฤฐlษ Qrupunuzdakฤฑ รyษlษri Etiket Edษ Bilษrษm\nฦmrlษrlษ Tanฤฑล Olmaq รรงรผn __ฦMRLฦR__ Butonuna Toxun**", buttons=(
                      
                      [Button.url('โ โโ๐๐๐ธ ๐ผ๐๐ธ๐๐ผ ๐ผ๐ โ', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('โก ๐๐ธ๐๐ ๐ฝ๐น๐ธโ', f'https://t.me/XaosResmii')],
                      [Button.url('๐ฆ๐ฟ ๐๐โ๐ผโ ๐จโ๐ป', f'https://t.me/sesizKOLGE')],
                      [Button.inline("โ ฦ๐โ๐ฦ๐", data="help")],
                    ),
                    link_preview=False)

			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"โก ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ ฤฐn ฦmrlษri \n\nโช /sehidler <sษbษb> ลษhid Adlarฤฑ ฤฐlษ Taฤ Edษr\nโช /tag <sษbษb> - 5-li Taฤ Edษr\nโช /etag <sษbษb> - Emoji ฤฐlษ Taฤ Edษr\nโช /btag <sษbษb> - Bayraqlarla Taฤ Edษr\nโช /mtag <sษbษb>  Mafia Rollarฤฑ ฤฐlฤฑ Taฤ Edษr\nโช /rtag <sษbษb> Rayon Vษ ลษhษr Adlarฤฑ ฤฐlษ Taฤ Edษr\nโช /ttag <sษbษb> - Tษk Teษk Taฤ Edษr\nโช /admins <sษbษb> - Adminlษri Taฤ Edษr\nโช /cancel - Taฤ Prosesin Saxlayar\nโช /start - Botu Baลladar", buttons=(
                      [Button.url('โ โโ๐โ๐ธ ๐ผ๐๐ธ๐๐ผ ๐ผ๐ โ', 'https://t.me/XAOS_Tagbot?startgroup=a')],
	              [Button.inline("โน ๐โ๐ฝ๐", data="info")],
                      [Button.inline("๐ ๐น๐ธ๐พ๐๐ธ", data="start")],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"**รox รzษllikli Taฤ Botu Axtarmaฤa รalฤฑลan Qrub Sahiblษri  โก  ๐๐ธ๐๐ ๐๐ธ๐พ๐พ๐ผโ Bot Sizษ Gรถrษ:\n\nโ๏ธ๏ธ๏ธ ลษhid Adlarฤฑ ฤฐlษ Taฤ Edษr\nโ๏ธ๏ธ๏ธ 5-Li Taฤ\nโ๏ธ๏ธ๏ธ Emojilษrlษ Taฤ Edษr\nโ๏ธ๏ธ๏ธ Bayraqlarla Taฤ Edษr\nโ๏ธ๏ธ๏ธ Mafia Rollarฤฑ ฤฐlษ Taฤ Edษr\nโ๏ธ๏ธ๏ธ Rayon Vษ ลษhษr Adlarฤฑ ฤฐlษ Taฤ Edษr\nโ๏ธ๏ธ๏ธ Tษkli Taฤ\nโ๏ธ๏ธ๏ธ Yalnฤฑz Admimlษri Taฤ\n\n\nBelษ รox รzษllikli @XAOS_Tagbot 'u Qrupunuza Yรถnษtici Olaraq Alฤฑb Rahatlฤฑqla , Taฤ edษ bilirsiz**", buttons=(      
	              [Button.url('โ โโ๐โ๐ธ ๐ผ๐๐ธ๐๐ผ ๐ผ๐ โ', 'https://t.me/XAOS_Tagbot?startgroup=a')],
		      [Button.inline("โ ๐ผ๐๐ธ๐ ๐๐ผ๐โ๐", data="start")],
		    ),
                    link_preview=False)
                   
	
	

	
sehidler = "Qษzษnfษr Nษcษf Nurlan ฤฐnqilab Nicat Mirnษbi Mษhษmmษd Ramazan Telman Fazil Qษlษndษr Nofษl ฤฐbrahim Habil Elลษn Sabir Hษsษn Qษr๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟib Ceyhun Mรผbariz Polad Cษbrayฤฑl ".split(" ")


@client.on(events.NewMessage(pattern="^/sehidler ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qurup vษ kanallar รผรงรผn keรงษrlidi โ**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmr sadษcษ adminlษr istifadษ edษ bilษr ใฝ๏ธ**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("โ Keรงmiล Mesajlar รรงรผn Taฤ Edษ Bilmษrษm..")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รaฤฤฑrmaฤฤฑm รรงรผn Bir Sษbษb Yoxdur ")
  else:
    return await event.respond("๐ฃ ฤฐstifadษรงilษri Taฤ Edษ Bilmษyim รรงรผn Bir Sษbษb Yazฤฑn...!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ฅ [{random.choice(sehidler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ฅ [{random.choice(sehidler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	

seherler = "Aฤcabษdi Aฤdam Aฤdaล Aฤdษrษ Aฤฤฑstafa Aฤsu Astara Babษk Bakฤฑ Balakษn Beylษqan Bษrdษ Bilษsuvar Cษbrayฤฑl Cษlilabad Culfa Daลkษsษn Dษlimษmmษdli Xocalฤฑ Fรผzuli Gษdษbษy Gษncษ Goranboy Gรถyรงay Gรถygรถl Gรถytษpษ Hacฤฑqabul Horadiz Xaรงmaz Xankษndi Xocalฤฑ Xocavษnd Xฤฑrdalan Xฤฑzฤฑ Xudat ฤฐmiลli ฤฐsmayฤฑllฤฑ Kษlbษcษr Kรผrdษmir Qax Qazax Qษbษlษ Qobustan Qovlar Quba Qubadlฤฑ Qusar Laรงฤฑn Lerik Lษnkษran Liman Masallฤฑ Naftalan Naxรงฤฑvan Neftรงala Oฤuz Ordubad Saatlฤฑ Sabirabad Salyan Samux Siyษzษn Sumqayฤฑt ลuลa ลabran ลahbuz ลamaxฤฑ ลษki ลษmkir ลษrur ลirvan Tษrtษr Tovuz Ucar Yardฤฑmlฤฑ Yevlax Zaqatala Zษngilan Zษrdab๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ".split(" ")


@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qurup vษ kanallar รผรงรผn keรงษrlidi โ**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmr sadษcษ adminlษr istifadษ edษ bilษr ใฝ๏ธ**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**โ Keรงmiล mesajlar รผรงรผn tag edษ bilmษrษm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รงaฤฤฑrmaฤฤฑm รผรงรผn bir sษbษb yoxdur ")
  else:
    return await event.respond("**๐ฃ ฤฐstifadษรงilษri รงaฤฤฑrmaฤฤฑm รผรงรผn bir sษbษb yazฤฑn...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{random.choice(seherler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag prosesini dayandฤฑrdฤฑnฤฑz โ**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{random.choice(seherler)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag prosesi uฤurla dayandฤฑrฤฑldฤฑ โ\n\n**Buda sizin reklamฤฑnฤฑz ola bilษr @Vusaliw**โ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
mafia = "๐จโ๐พVษtษndaล ๐จโโ๏ธKomissar Kattani ๐จโ๐ผรavuล ๐จโโ๏ธDoktor ๐งโโ๏ธCadugar ๐ต๏ธSuiqษstรงi ๐งBomj ๐ฆBuqษlษmun ๐๐ปSecurฤฑty ๐ณ๐ปโโ๏ธSatฤฑcฤฑ ๐๐ปโโ๏ธOฤru ๐ท๐ปโโ๏ธMษdษnรงi โญ๏ธGeneral ๐ง๐ปโโ๏ธลษhzadษ ๐งDJ ๐ฆBankir ๐ดDon ๐บMafia ๐จโโ๏ธVษkil ๐๐ปโโ๏ธMษhbus ๐จ๐ปโ๐ฆฑDedektiv  ๐ฆฆKรถstษbษk ๐จ๐ปโ๐คSpecialist ๐ชManyak ๐คกJoker ๐ปRuh ๐ง๐ปโโ๏ธMษlษk ๐ฆน๐ปโโ๏ธBOSS ๐ฅทNinja ๐ฅทSUPER Ninja ๐จ๐ปโ๐ฆฒDษli ๐ฎReviver ๐Killer ๐ง๐ปโโ๏ธVampir๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ".split(" ")


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qurup vษ kanallar รผรงรผn keรงษrlidi โ**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmr sadษcษ adminlษr istifadษ edษ bilษr ใฝ๏ธ**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**โ Keรงmiล mesajlar รผรงรผn tag edษ bilmษrษm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รงaฤฤฑrmaฤฤฑm รผรงรผn bir sษbษb yoxdur ")
  else:
    return await event.respond("**๐ฃ ฤฐstifadษรงilษri รงaฤฤฑrmaฤฤฑm รผรงรผn bir sษbษb yazฤฑn...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag prosesini dayandฤฑrdฤฑnฤฑz โ**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{random.choice(mafia)}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag prosesi uฤurla dayandฤฑrฤฑldฤฑ โ\n\n**Buda sizin reklamฤฑnฤฑz ola bilษr  @Vusaliw**โ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
bayrag = "๐ฆ๐จ ๐ฆ๐ฉ ๐ฆ๐ช ๐ฆ๐ซ ๐ฆ๐ฌ ๐ฆ๐ฎ ๐ฆ๐ฑ ๐ฆ๐ด ๐ฆ๐ถ ๐ฆ๐ท ๐ฆ๐ธ ๐ฆ๐น๐ฆ๐บ ๐ฆ๐ผ ๐ฆ๐ฝ ๐ฆ๐ฟ ๐ง๐ฆ ๐ง๐ง ๐ง๐ฉ ๐ง๐ช ๐ง๐ซ ๐ง๐ฌ ๐ง๐ญ ๐ง๐ฎ๐ง๐ฏ ๐ง๐ฑ ๐ง๐ฒ ๐ง๐ณ ๐ง๐ด ๐ง๐ถ ๐ง๐ท ๐ง๐ธ ๐ง๐น ๐ง๐ป ๐ง๐ผ ๐ง๐พ๐ง๐ฟ ๐จ๐ฆ ๐จ๐จ ๐จ๐ฉ ๐จ๐ซ ๐จ๐ฌ ๐จ๐ญ ๐จ๐ฎ ๐จ๐ฐ ๐จ๐ฑ ๐จ๐ฒ ๐จ๐ณ๐จ๐ต ๐จ๐ท ๐จ๐บ ๐จ๐ป ๐จ๐ผ ๐จ๐ฝ ๐จ๐พ ๐จ๐ฟ ๐ฉ๐ช ๐ฉ๐ฌ ๐ฉ๐ฏ ๐ฉ๐ฐ๐ฉ๐ฒ ๐ฉ๐ด ๐ฉ๐ฟ ๐ช๐ฆ ๐ช๐จ ๐ช๐ช ๐ช๐ฌ ๐ช๐ญ ๐ช๐ท ๐ช๐ธ ๐ช๐น ๐ช๐บ๐ซ๐ฎ ๐ซ๐ฏ ๐ซ๐ฐ ๐ซ๐ฒ ๐ซ๐ด ๐ซ๐ท ๐ฌ๐ฆ ๐ฌ๐ง ๐ฌ๐ฉ ๐ฌ๐ช ๐ฌ๐ซ ๐ฌ๐ฌ๐ฌ๐ญ ๐ฌ๐ฎ ๐ฌ๐ฑ ๐ฌ๐ฒ ๐ฌ๐ณ ๐ฌ๐ต ๐ฌ๐ถ ๐ฌ๐ท ๐ฌ๐ธ ๐ฌ๐น ๐ฌ๐บ ๐ฌ๐ผ๐ฌ๐พ ๐ญ๐ฐ ๐ญ๐ฒ ๐ญ๐ณ ๐ญ๐ท ๐ญ๐น ๐ญ๐บ ๐ฎ๐จ ๐ฎ๐ฉ ๐ฎ๐ช ๐ฎ๐ฑ ๐ฎ๐ฒ๐ฎ๐ณ ๐ฎ๐ด ๐ฎ๐ถ ๐ฎ๐ท ๐ฎ๐ธ ๐ฎ๐น ๐ฏ๐ช ๐ฏ๐ฒ ๐ฏ๐ด ๐ฏ๐ต ๐ฐ๐ช ๐ฐ๐ฌ๐ฐ๐ญ ๐ฐ๐ฎ ๐ฐ๐ฒ ๐ฐ๐ณ ๐ฐ๐ต ๐ฐ๐ท ๐ฐ๐ผ ๐ฐ๐พ ๐ฐ๐ฟ ๐ฑ๐ฆ ๐ฑ๐ง ๐ฑ๐จ๐ฑ๐ฎ ๐ฑ๐ฐ ๐ฑ๐ท ๐ฑ๐ธ ๐ฑ๐น ๐ฑ๐บ ๐ฑ๐ป ๐ฑ๐พ ๐ฒ๐ฆ ๐ฒ๐จ ๐ฒ๐ฉ ๐ฒ๐ช๐ฒ๐ซ ๐ฒ๐ฌ ๐ฒ๐ญ ๐ฒ๐ฐ ๐ฒ๐ฑ ๐ฒ๐ฒ ๐ฒ๐ณ ๐ฒ๐ด ๐ฒ๐ต ๐ฒ๐ถ ๐ฒ๐ท ๐ฒ๐ธ๐ฒ๐น ๐ฒ๐บ ๐ฒ๐ป ๐ฒ๐ผ ๐ฒ๐ฝ ๐ฒ๐พ ๐ฒ๐ฟ ๐ณ๐ฆ ๐ณ๐จ ๐ณ๐ช ๐ณ๐ซ ๐ณ๐ฌ๐ณ๐ฎ ๐ณ๐ฑ ๐ณ๐ด ๐ณ๐ต ๐ณ๐ท ๐ณ๐บ ๐ณ๐ฟ ๐ด๐ฒ ๐ต๐ฆ ๐ต๐ช ๐ต๐ซ ๐ต๐ฌ๐ต๐ญ ๐ต๐ฐ ๐ต๐ฑ ๐ต๐ฒ ๐ต๐ณ ๐ต๐ท ๐ต๐ธ ๐ต๐น ๐ต๐ผ ๐ต๐พ ๐ถ๐ฆ ๐ท๐ช๐ท๐ด ๐ท๐ธ ๐ท๐บ ๐ท๐ผ ๐ธ๐ฆ ๐ธ๐ง ๐ธ๐จ ๐ธ๐ฉ ๐ธ๐ช ๐ธ๐ฌ ๐ธ๐ญ ๐ธ๐ฎ๐ธ๐ฏ ๐ธ๐ฐ ๐ธ๐ฑ ๐ธ๐ฒ ๐ธ๐ณ ๐ธ๐ด ๐ธ๐ท ๐ธ๐ธ ๐ธ๐น ๐ธ๐ป ๐ธ๐ฝ ๐ธ๐พ๐ธ๐ฟ ๐น๐ฆ ๐น๐จ ๐น๐ฉ ๐น๐ซ ๐น๐ฌ ๐น๐ญ ๐น๐ฏ ๐น๐ฐ ๐น๐ฑ ๐น๐ฒ ๐น๐ณ๐น๐ด ๐น๐ท ๐น๐น ๐น๐ป ๐น๐ผ ๐น๐ฟ ๐บ๐ฆ ๐บ๐ฌ ๐บ๐ฒ ๐บ๐ณ ๐บ๐ธ ๐บ๐พ๐บ๐ฟ ๐ป๐ฆ ๐ป๐จ ๐ป๐ช ๐ป๐ฌ ๐ป๐ฎ ๐ป๐ณ ๐ป๐บ ๐ผ๐ซ ๐ผ๐ธ ๐ฝ๐ฐ ๐พ๐ช๐พ๐น ๐ฟ๐ฆ ๐ฟ๐ฒ ๐ฟ๐ผ ๐ด๓?ง๓?ข๓?ฅ๓?ฎ๓?ง๓?ฟ ๐ด๓?ง๓?ข๓?ณ๓?ฃ๓?ด๓?ฟ ๐ด๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ๓?ง๓?ข๓?ท๓?ฌ๓?ณ๓?ฟ".split(" ")


@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("โ Bu ฦmr Sadษcษ Qruplarda Vษ Kanallarda Keรงษrlidir..")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("โ Bu ฦmrdษn Sadษcษ Adminlษr ฤฐsdifadษ Edษ Bilษr..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("โ Keรงmiล mesajlar รผรงรผn tag edษ bilmษrษm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รaฤฤฑrmaฤฤฑm รรงรผn Bir Sษbษb Yoxdur ")
  else:
    return await event.respond("โ ฤฐstifadษรงilษri Taฤ Edษ Bilmษyim รรงรผn Bir Sษbษb Yazฤฑn..")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Taฤ Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	
emoji = "๐ต ๐ฆ ๐ฏ ๐ฑ ๐ถ ๐บ ๐ป ๐จ ๐ผ ๐น ๐ญ ๐ฐ ๐ฆ ๐ฆ ๐ฎ ๐ท ๐ฝ ๐ ๐ฆ ๐ฆ ๐ด ๐ธ ๐ฒ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ข ๐ ๐ ๐ ๐ ๐ ๐ ๐ฉ ๐ ๐ฆฎ ๐โ๐ฆบ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฆ ๐ฆ ๐ฆฅ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆ ๐ฆง ๐ช ๐ซ ๐ฟ๏ธ ๐ฆจ ๐ฆก ๐ฆ ๐ฆฆ ๐ฆ ๐ ๐ ๐ฃ ๐ค ๐ฅ ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐๏ธ ๐ฆข ๐ฆฉ ๐ฆ ๐ฆ ๐ฆ ๐ง๐ฆ ๐ฌ ๐ ๐ณ ๐ ๐? ๐ก ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆช ๐ฆ ๐ท๏ธ ๐ฆ ๐ ๐ ๐ฆ ๐ฆ ๐ ๐ ๐ ๐ธ๏ธ ๐ ๐พ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คฃ ๐ญ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐คฉ ๐ฅณ ๐ค ๐ ๐ โบ๏ธ ๐ ๐ ๐ ๐ ๐คญ ๐ถ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คช ๐ค ๐คจ ๐ง ๐ ๐ ๐ค ๐? ๐คฌ โน๏ธ ๐ ๐ ๐ ๐ฅบ ๐ณ ๐ฌ ๐ค ๐คซ ๐ฐ ๐จ ๐ง ๐ฆ ๐ฎ ๐ฏ ๐ฒ ๐ฑ ๐คฏ ๐ข ๐ฅ ๐ ๐ ๐ ๐ฃ ๐ฉ ๐ซ ๐คค ๐ฅฑ ๐ด ๐ช ๐ ๐ ๐ ๐ ๐ ๐คข ๐คฎ ๐คง ๐ค ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅญ ๐ ๐ ๐ถ ๐ ๐ฅ ๐ ๐ ๐ ๐ ๐ ๐ฅ ๐? ๐ง ๐ฝ ๐ฅฆ ๐ฅ ๐ฅฌ ๐ฅ ๐ฅฏ ๐ฅ ๐ฅ ๐ ๐ฅ ๐ฐ ๐ฅ ๐ง ๐ ๐ง ๐ฅ ๐ฅ ๐ง ๐ฅ ๐ฅฉ ๐ ๐ ๐ฅ ๐ฏ ๐ฎ ๐ ๐ ๐ฅจ ๐ฅช ๐ญ ๐ ๐ง ๐ฅ ๐ ๐ฅซ ๐ฅฃ ๐ฅ ๐ฒ ๐ ๐ ๐ข ๐ฅ ๐ฑ ๐ ๐ฅก ๐ค ๐ฃ ๐ฆ ๐ฆช ๐ ๐ก ๐ฅ? ๐ฅฎ ๐ง ๐ง ๐จ".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("โ Bu ฦmr Sadษcษ Qruplarda Vษ Kanallarda Keรงษrlidir..")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("โ Bu ฦmr Sadษcษ Adminlษr ฤฐsdifadษ Edษ Bilษr..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Keรงmiล Mesajlar รรงรผn Taฤ Edษ Bilmษrษm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รaฤฤฑrmaฤฤฑm รรงรผn Bir Sษbษb Yoxdur")
  else:
    return await event.respond("โ ฤฐstifadษรงilษri Taฤ Edษ Bilmษyim รรงรผn Bir Sษbษb Yazฤฑn...")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("โ Bu ฦmr Sadษcษ Qruplarda Vษ Kanallarda Keรงษrlidir")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("โ Bu ฦmrdษn Sadษcษ Adminlษr ฤฐsdifadษ Edษ Bilษr..")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("โ Keรงmiล Mesajlar รรงรผn Taฤ Edษ Bilmษrษm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รaฤฤฑrmaฤฤฑm รรงรผn Bir Sษbษb Yoxdur")
  else:
    return await event.respond("๐ฃ ฤฐstifadษรงilษri Taฤ Edษ Bilmษyim รรงรผn Bir Sษbษb Yazฤฑn...!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โช [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/ttag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("โ Bu ฦmr Sadษcษ Qruplarda Vษ Kanallarda Keรงษrlidir")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("โ Bu ฦmrdษn Sadษcษ Adminlษr ฤฐsdifadษ Edษ Bilษr")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("โ Keรงmiล Mesajlar รรงรผn Taฤ Edษ Bilmษrษm")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("โ ฤฐstifadษรงilษri รaฤฤฑrmaฤฤฑm รรงรผn Bir Sษbษb Yoxdur")
  else:
    return await event.respond("๐ฃ ฤฐstifadษรงilษri Taฤ Edษ Bilmษyim รรงรผn Birr Sษbษb Yazฤฑn...!")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**๐ข [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"๐ข [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("โ Tag Prosesi Uฤurla Dayandฤฑrฤฑldฤฑ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot aktifdi bot hakda mษlumatฤฑ @sesizKOLGE dan ala bilษrsษn Versiya 1.7.5<<")
client.run_until_disconnected()
