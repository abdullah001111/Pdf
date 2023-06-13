file_name = "plugins/dm/textToPdf/callBack.py"
author_name = "telegram.dog/nabilanavab"
source_code = "https://github.com/nabilanavab/ilovepdf"

import                   os
from plugins.utils       import *
from configs.log         import log
from fpdf                import FPDF
from logger              import logger
from pyrogram.types      import InputMediaPhoto
from configs.config      import settings, images
from .                   import FONT, COLOR, PAGE_SIZE
from pyrogram            import filters, Client as ILovePDF

@ILovePDF.on_callback_query(filters.regex("^t2p"))
async def text_to_pdf_cb(bot, callbackQuery):
    try:
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        if await render.header(bot, callbackQuery, lang_code=lang_code):
            return
        await callbackQuery.answer()
        logger.debug(callbackQuery)
        logger.debug(callbackQuery.data)
        if len(callbackQuery.data.split("|")) == 1:
            # callbackQuery.data = t2p|{text_font}
            tTXT, _ = await util.translate(text="pdf2TXT['size_btn']", lang_code=lang_code)
            tTXT = await util.createBUTTON(tTXT, "121")
            return await callbackQuery.edit_message_media(
                media=InputMediaPhoto(media="https://graph.org/file/c301b7af1e637f642a520.jpg",
                                      caption=callbackQuery.message.caption), reply_markup=tTXT
            )
        
        else:
            if len(callbackQuery.data.split("|")) == 2:
                tTXT, _ = await util.translate(text="pdf2TXT['fifteen']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_HEAD_FONT", lang_code=lang_code)
            elif len(callbackQuery.data.split("|")) == 3:
                tTXT, _ = await util.translate(text="pdf2TXT['fifteen']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_PARA_FONT", lang_code=lang_code)
            elif len(callbackQuery.data.split("|")) == 4:
                tTXT, _ = await util.translate(text="pdf2TXT['fifteen']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_COLOR", lang_code=lang_code)
            elif len(callbackQuery.data.split("|")) == 5:
                tTXT, _ = await util.translate(text="pdf2TXT['five']", lang_code=lang_code)
                front, _ = await util.translate(text="_SELECT_BG_COLOR", lang_code=lang_code)
            else:
                front = " "
            tTXT = await util.editDICT(inDir=tTXT, value=f"{callbackQuery.data}", front=front)
            if len(callbackQuery.data.split("|")) in [ 2, 3, 4 ]:
                tTXT = await util.createBUTTON(tTXT, "15551")
            else:
                tTXT = await util.createBUTTON(tTXT, "1321")
            return await callbackQuery.edit_message_media(
                media=InputMediaPhoto(media="https://graph.org/file/c301b7af1e637f642a520.jpg",
                                      caption=callbackQuery.message.caption), reply_markup=tTXT
            )
        
    except Exception as Error:
        logger.exception("1️⃣ 🐞 %s: %s" %(file_name, Error), exc_info=True)

# CONTACT AUTHOR: nabilanavab@gmail.com