import requests
import telebot,time
from telebot import types
import os
from agent import chk

def Tele(P):
                n = P.split('|')[0]
                mm=P.split('|')[1]
                yy=P.split('|')[2][-2:]
                cvc=P.split('|')[3].replace('\n', '')
                try:
                    data = requests.get('https://lookup.binlist.net/'+P[:6]).json()
                except:
                    pass
                try:
                    bank=(data['bank']['name']) 
                except:
                    bank=('unknown bank ??')
                try:
                    emj=(data['country']['emoji'])
                except:
                    emj=""
                try:
                    cn=(data['country']['name'])
                except:
                    cn=('unknown country ??')
                try:
                    dicr=(data['scheme'])
                except:
                    dicr=('unknown scheme ??')
                try:
                    typ=(data['type'])
                except:
                    typ=('unknown type ??')
                try:
                    url=(data['bank']['url'])
                except:
                    url=('unknown url ??')


dollar=50
GROUP_ID = ['-4241648367']
token = '7073759365:AAF90G4f5qFsGMEue22-VEPL18aWFyOwzYc'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = 843841687,6707467876

@bot.message_handler(commands=["start"])
def start(message):
	found='unpr'
	chat_id = message.chat.id
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	found='unpr'
	chat_id = message.chat.id
	current_dir = os.getcwd()
	for filename in os.listdir(current_dir):
		if filename.endswith(".start"):
			bot.reply_to(message, "هناك شخص اخر يستخدم البوت")
			return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			with open("start.start", "w") as yu:
				pass
			for cc in lino:
				time.sleep(20)
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @hhhh4x')
						os.remove('start.start')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(chk(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Eyad CHK Is Luanching ➜ @hhhh4x''', reply_markup=mes)
				
				print(last)
				if "live" in last :
					msg = f"""- {cc}
- 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
- Auhenticated. ✅
- Braintree Auth 1
━━━━━━━━━━━━━━━━━
BIN : {cc[:6]} - {dicr} - {typ} 
Country : {cn} - {emj} 
Bank : {bank}
URL : {url}
━━━━━━━━━━━━━━━━━
BY : @hhhh4x """
					bot.reply_to(message, msg)
					live += 1
				else:
					dd += 1
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @TheLord_III')
	os.remove('start.start')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("BOT HAS BEEN ACTIVATED\n@hhhh4x")
bot.polling()