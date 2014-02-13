__author__ = 'Bakaboykie'

from django.contrib import admin
from Project_WaifuDB.assets.models import Waifu, WaifuAssetClientPicture

class WaifuAdmin(admin.ModelAdmin):
    fields = [
        'picture',
        'name_alphabet',
        'name_nickname',
        'name_kanji',
        'name_hiragana',
        'name_katakana',
        'waifu_birthday',
        'waifu_age',
        'waifu_sign',
        'waifu_job',
        'blood_type',
        'waifu_height',
        'waifu_weight',
        'waifu_bust',
        'waifu_waist',
        'waifu_hip',
        'series_alphabet',
        'series_japanese',
        'waifu_description',
        'date_uploaded'
    ]

    list_display = (
        'admin_image',
        'name_alphabet',
        'name_kanji',
        'name_nickname',
        'waifu_age',
        'waifu_birthday',
        'waifu_height',
        'waifu_weight',
        'waifu_bust',
        'waifu_waist',
        'waifu_hip',
        'series_alphabet',
        'date_uploaded'
    )


class WaifuAssetClientPictureAdmin(admin.ModelAdmin):
    list_display = ('waifu', 'name', 'admin_image')


admin.site.register(Waifu, WaifuAdmin)
admin.site.register(WaifuAssetClientPicture, WaifuAssetClientPictureAdmin)