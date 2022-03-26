import os
from pyrogram import Client, filters
import tgcrypto

Ganesh = Client("Sow",
    bot_token="5279132519:AAFnMj_0lzOsgznPkskD8LUlqDe8HJJyxkQ",
    api_id=14823538,
    api_hash="69853ae221a52fe7a3e6adf572fa831a"
)
@Ganesh.on_message(filters.command("start"))
async def start(bot, message):
        text = '\n 🙋 Hey my name is Guruji 🙋\n' \
               '\nHow can I help you ? 🤔\n' \
               '\n/DOCUMENTS :- All the addmission related documents 📑\n' \
               '\n/SCOLARSHIPE :- Scolarships According to your Caste 📃\n' \
               '\n/COLLEGE_RECOMMENDATION :- Get your college based on your score 🏫\n' \
               '\n/WEBSITE :- Website of one of the leading engineering institutes in the country 🖇️'
        await message.reply(text, quote=True)
        return
@Ganesh.on_message(filters.regex("/DOCUMENTS"))
async def hii(bot, message):
    text = "\nSelect Your Caste :-\n" \
           "\n/OPEN : Open Caste\n" \
           "\n/OBC  : OBC Caste \n" \
            "\n /SC_ST : SC-ST Caste\n"\
           "\n /VJNT_SBC : VJNT-SBC Caste\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex("/OPEN"))
async def hii(bot, message):
    text = "\n1) 10th & 12th Marksheet\n" \
           "\n2) CET Marksheet\n" \
           "\n3) Leaving Certificate\n" \
           "\n4) Residentinal Certificate\n" \
           "\n5) Income Certificate\n" \
           "\n6) Nationality & Domicile Certificate\n" \
           "\n7) Bank-pass book\n" \
           "\n8) Retion Card\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex("/OBC"))
async def hii(bot, message):
    text = "\n1) 10th & 12th Marksheet\n" \
           "\n2) CET Marksheet\n" \
           "\n3) Leaving Certificate\n" \
           "\n4) Residentinal Certificate\n" \
           "\n5) Income Certificate\n" \
           "\n6) Nationality & Domicile Certificate\n" \
           "\n7) Bank-pass book\n" \
           "\n8) Retion Card\n" \
           "\n9) Caste Certificate\n" \
           "\n10) Caste Validity\n" \
           "\n11) Non-Creamy Layer Certificate"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex("SC_ST"))
async def hii(bot, message):
    text = "\n1) 10th & 12th Marksheet\n" \
           "\n2) CET Marksheet\n" \
           "\n3) Leaving Certificate\n" \
           "\n4) Residentinal Certificate\n" \
           "\n5) Income Certificate\n" \
           "\n6) Nationality & Domicile Certificate\n" \
           "\n7) Bank-pass book\n" \
           "\n8) Retion Card\n" \
           "\n9) Caste Certificate\n" \
           "\n10) Caste Validity\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex("VJNT_SBC"))
async def hii(bot, message):
    text = "\n1) 10th & 12th Marksheet\n" \
           "\n2) CET Marksheet\n" \
           "\n3) Leaving Certificate\n" \
           "\n4) Residentinal Certificate\n" \
           "\n5) Income Certificate\n" \
           "\n6) Nationality & Domicile Certificate\n" \
           "\n7) Bank-pass book\n" \
           "\n8) Retion Card\n" \
           "\n9) Caste Certificate\n" \
           "\n10) Caste Validity\n" \
           "\n11) Non-Creamy Layer Certificate"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex("/SCOLARSHIPE"))
async def hii(bot, message):
    text = "\nSelect Your Caste :-\n" \
           "\n/Open : Open Caste\n" \
           "\n/Obc : OBC Caste \n" \
           "\n /Sc_St: SC-ST Caste\n" \
           "\n /Vjnt_Sbc : VJNT-SBC Caste\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex('Open'))
async def hii(bot, message):
    text = "\n1)Rajarshi Chhatrapati Shahu Maharaj Fee Reimbursement Scheme.\n" \
           "\n2)Dr. Panjabrao Deshmukh Vasatigruh Nirvah Bhatta Yojna.\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex('Obc'))
async def hii(bot, message):
    text = "\n1) Scholarship Scheme\n" \
           "\n2) Freeship Scheme\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex('Vjnt_Sbc'))
async def hii(bot, message):
    text = "\n1) Scholarship Scheme\n" \
           "\n2) Freeshipe Scheme\n" \
           "\n3) Vidhayvetan Scheme\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex('Sc_St'))
async def hii(bot, message):
    text = "\n1) Scholarship Scheme\n" \
           "\n2) Freeshipe Scheme\n" \
           "\n3) Vidhayvetan Scheme\n"
    await message.reply(text, quote=True)
    return
@Ganesh.on_message(filters.regex('WEBSITE'))
async def hii(bot, message):
    text = "\n1) www.iisc.ac.in \n" \
           "\n2) www.iitb.ac.in\n" \
           "\n3) www.iitk.ac.in\n" \
           "\n4) www.iitg.ernet.in\n" \
           "\n5) www.iitm.ac.in\n" \
           "\n6) www.iith.ac.in\n"
    await message.reply(text, quote=True)
    return


Ganesh.run()
