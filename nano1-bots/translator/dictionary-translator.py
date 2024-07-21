from deep_translator import GoogleTranslator


units_labels = {
    'length' : [
        {'value': 'meter', 'label': 'meter', 'flabel': 'متر'}, 
        {'value': 'kilometer', 'label': 'kilometer', 'flabel': 'کیلومنر'}, 
        {'value': 'centimeter', 'label': 'centimeter', 'flabel': 'سانتی متر'}, 
        {'value': 'milimeter', 'label': 'milimeter', 'flabel': 'میلی متر'}, 
        {'value': 'micometer', 'label': 'micometer', 'flabel': 'میکرو متر'}, 
        {'value': 'nanometer', 'label': 'nanometer', 'flabel': 'نانو متر'}, 
        {'value': 'mile', 'label': 'mile', 'flabel': 'مایل'}, 
        {'value': 'yard', 'label': 'yard', 'flabel': 'یارد'}, 
        {'value': 'inch', 'label': 'inch', 'flabel': 'اینچ'}, 
        {'value': 'foot', 'label': 'foot', 'flabel': 'فوت'}
    ],
    'time' : [
        {'value': 'second', 'label': 'second', 'flabel': 'ثانیه'}, 
        {'value': 'milisecond', 'label': 'milisecond', 'flabel': 'میلی ثانیه'}, 
        {'value': 'microsecond', 'label': 'microsecond', 'flabel': 'میکرو ثانیه'}, 
        {'value': 'nanosecond', 'label': 'nanosecond', 'flabel': 'نانو ثانیه'}, 
        {'value': 'minute', 'label': 'minute', 'flabel': 'دقیقه'}, 
        {'value': 'hour', 'label': 'hour', 'flabel': 'ساعت'}, 
        {'value': 'day', 'label': 'day', 'flabel': 'روز'}, 
        {'value': 'week', 'label': 'week', 'flabel': 'هفته'}, 
        {'value': 'month', 'label': 'month', 'flabel': 'ماه'}, 
        {'value': 'year', 'label': 'year', 'flabel': 'سال'}
    ],
    'mass' : [
        {'value': 'gram', 'label': 'gram', 'flabel': 'گرم'}, 
        {'value': 'kilogram', 'label': 'kilogram', 'flabel': 'کیلوگرم'}, 
        {'value': 'milligram', 'label': 'milligram', 'flabel': 'میلی گرم'}, 
        {'value': 'microgram', 'label': 'microgram', 'flabel': 'میکرو گرم'}, 
        {'value': 'ton', 'label': 'ton', 'flabel': 'تن'}, 
        {'value': 'USton', 'label': 'USton', 'flabel': 'تن آمریکا'}, 
        {'value': 'stone', 'label': 'stone', 'flabel': 'سنگ'}, 
        {'value': 'pound', 'label': 'pound', 'flabel': 'پوند'}, 
        {'value': 'ounce', 'label': 'ounce', 'flabel': 'اونس'}
    ],
    'area' : [
        {'value': 'squaremeter', 'label': 'squaremeter', 'flabel': 'مترمربغ'}, 
        {'value': 'squarekilometer', 'label': 'squarekilometer', 'flabel': 'کیلومتر مربع'}, 
        {'value': 'squaremile', 'label': 'squaremile', 'flabel': 'مایل مربع'}, 
        {'value': 'squareyard', 'label': 'squareyard', 'flabel': 'یارد مربع'}, 
        {'value': 'squarefoot', 'label': 'squarefoot', 'flabel': 'فوت مربع'}, 
        {'value': 'squareinch', 'label': 'squareinch', 'flabel': 'اینچ مربع'}, 
        {'value': 'hectare', 'label': 'hectare', 'flabel': 'هکتار'}, 
        {'value': 'acre', 'label': 'acre', 'flabel': 'جریب'}
    ],
    'data-transfer' : [
        {'value': 'BitPerSecond', 'label': 'BitPerSecond', 'flabel': 'بیت بر ثانیه'}, 
        {'value': 'KilobitPerSecond', 'label': 'KilobitPerSecond', 'flabel': 'کیلوبیت بر ثانیه'}, 
        {'value': 'KilobytePerSecond', 'label': 'KilobytePerSecond', 'flabel': 'کیلوبایت بر ثانیه'}, 
        {'value': 'KibibitPerSecond', 'label': 'KibibitPerSecond', 'flabel': 'کیبی بیت بر ثانیه'}, 
        {'value': 'MegabitPerSecond', 'label': 'MegabitPerSecond', 'flabel': 'مگابیت بر ثانیه'}, 
        {'value': 'MegabytePerSecond', 'label': 'MegabytePerSecond', 'flabel': 'مگابایت بر ثانیه'}, 
        {'value': 'MebibitPerSecond', 'label': 'MebibitPerSecond', 'flabel': 'مبی بیت بر ثانیه'}, 
        {'value': 'GigabitPerSecond', 'label': 'GigabitPerSecond', 'flabel': 'گیگابیت بر ثانیه'}, 
        {'value': 'GigabytePerSecond', 'label': 'GigabytePerSecond', 'flabel': 'گیگابایت بر ثانیه'}, 
        {'value': 'GibibitPerSecond', 'label': 'GibibitPerSecond', 'flabel': 'گیبی بیت بر ثانیه'}, 
        {'value': 'TerabitPerSecond', 'label': 'TerabitPerSecond', 'flabel': 'ترابیت بر ثانیه'}, 
        {'value': 'TerabytePerSecond', 'label': 'TerabytePerSecond', 'flabel': 'ترابایت بر ثانیه'}, 
        {'value': 'TebibitPerSecond', 'label': 'TebibitPerSecond', 'flabel': 'تبی بیت بر ثانیه'}
    ],
    'digital-storage' : [
        {'value': 'Byte', 'label': 'Byte', 'flabel': 'بایت'}, 
        {'value': 'Kilobyte', 'label': 'Kilobyte', 'flabel': 'کیلوبایت'}, 
        {'value': 'Kibibyte', 'label': 'Kibibyte', 'flabel': 'کیبی بیت'}, 
        {'value': 'Megabyte', 'label': 'Megabyte', 'flabel': 'مگا بایت'}, 
        {'value': 'Mebibyte', 'label': 'Mebibyte', 'flabel': 'مبی بایت'}, 
        {'value': 'Gigabyte', 'label': 'Gigabyte', 'flabel': 'گیگا بایت'}, 
        {'value': 'Gibibyte', 'label': 'Gibibyte', 'flabel': 'گیبی بایت'}, 
        {'value': 'Terabyte', 'label': 'Terabyte', 'flabel': 'ترا بایت'}, 
        {'value': 'Tebibyte', 'label': 'Tebibyte', 'flabel': 'تبی بایت'}, 
        {'value': 'Bit', 'label': 'Bit', 'flabel': 'بیت'}, 
        {'value': 'Kilobit', 'label': 'Kilobit', 'flabel': 'کیلو بیت'}, 
        {'value': 'Kibibit', 'label': 'Kibibit', 'flabel': 'کیبی بیت'}, 
        {'value': 'Megabit', 'label': 'Megabit', 'flabel': 'مگا بیت'}, 
        {'value': 'Mebibit', 'label': 'Mebibit', 'flabel': 'مبی بیت'}, 
        {'value': 'Gigabit', 'label': 'Gigabit', 'flabel': 'گیگا بیت'}, 
        {'value': 'Gibibit', 'label': 'Gibibit', 'flabel': 'گیبی بیت'}, 
        {'value': 'Terabit', 'label': 'Terabit', 'flabel': 'ترا بیت'}, 
        {'value': 'Tebibit', 'label': 'Tebibit', 'flabel': 'نبی بیت'}, 
        {'value': 'Petabit', 'label': 'Petabit', 'flabel': 'پتا بیت'}, 
        {'value': 'Pebibit', 'label': 'Pebibit', 'flabel': 'پبی بیت'}
    ],
    'energy' : [
        {'value': 'Joule', 'label': 'Joule', 'flabel': 'ژول'}, 
        {'value': 'KiloJoule', 'label': 'KiloJoule', 'flabel': 'کیلوژول'}, 
        {'value': 'GramCalorie', 'label': 'GramCalorie', 'flabel': 'کالری-گرم'}, 
        {'value': 'Kilocalorie', 'label': 'Kilocalorie', 'flabel': 'کیلو کالری'}, 
        {'value': 'WattHour', 'label': 'WattHour', 'flabel': 'وات-ساعت'}, 
        {'value': 'KilowattHour', 'label': 'KilowattHour', 'flabel': 'کیلو وات-ساعت'}, 
        {'value': 'Electronvolt', 'label': 'Electronvolt', 'flabel': 'الکترو-ولت'}, 
        {'value': 'BritishThermalUnit', 'label': 'BritishThermalUnit', 'flabel': 'یکای گرمایی بریتانیا'}, 
        {'value': 'USTherm', 'label': 'USTherm', 'flabel': 'یکای گرمای امریکا'}, 
        {'value': 'FootPound', 'label': 'FootPound', 'flabel': 'فوت-پوند'}
    ],
    'volume' : [
        {'value': 'Liter','label': 'Liter', 'flabel': 'لیتر'}, 
        {'value': 'MiliLiter','label': 'MiliLiter', 'flabel': 'میلی لیتر'}, 
        {'value': 'USLiquidGallon','label': 'USLiquidGallon', 'flabel': 'گالون امریکا'}, 
        {'value': 'USLiquidQuart','label': 'USLiquidQuart', 'flabel': 'کوارت امریکا'}, 
        {'value': 'USLiquidPint','label': 'USLiquidPint', 'flabel': 'پینت امریکا'}, 
        {'value': 'USLegalCup','label': 'USLegalCup', 'flabel': 'فنجان امریکا'}, 
        {'value': 'FluidOunce','label': 'FluidOunce', 'flabel': 'انس سیال'}, 
        {'value': 'USTableSpoon','label': 'USTableSpoon', 'flabel': 'قاشق غذاخوری امریکا'}, 
        {'value': 'SUTeaSpoon','label': 'SUTeaSpoon', 'flabel': 'قاشق چای خوری امریکا'}, 
        {'value': 'QubicMeter','label': 'QubicMeter', 'flabel': 'متر مکعب'}, 
        {'value': 'ImperialGallon','label': 'ImperialGallon', 'flabel': 'گالن امپراطوری'}, 
        {'value': 'ImperialQuart','label': 'ImperialQuart', 'flabel': 'کوارت امپراطوری'}, 
        {'value': 'ImperialPint','label': 'ImperialPint', 'flabel': 'پینت امپراطوری'}, 
        {'value': 'ImperialCup','label': 'ImperialCup', 'flabel': 'فنجان امپراطوری'}, 
        {'value': 'Imp-FluidOunce', 'label': 'Imp-FluidOunce', 'flabel': 'اونس سیال امپراطوری'}, 
        {'value': 'Imp-TableSpoon', 'label': 'Imp-TableSpoon', 'flabel': 'قاشق غذاخوری امپراطوری'}, 
        {'value': 'Imp-TeaSpoon', 'label': 'Imp-TeaSpoon', 'flabel': 'قاشق چای خوری امپراطوری'}, 
        {'value': 'CubicFoot','label': 'CubicFoot', 'flabel': 'فوت مکعب'}, 
        {'value': 'CubicInch','label': 'CubicInch', 'flabel': 'اینچ مکعب'}
    ],
    'speed' : [
        {'value': 'MeterPerSecond', 'label': 'MeterPerSecond', 'flabel': 'متر بر ثانیه'}, 
        {'value': 'KiloMeterPerHour', 'label': 'KiloMeterPerHour', 'flabel': 'کیلومتر بر ساعت'}, 
        {'value': 'FootPerSecond', 'label': 'FootPerSecond', 'flabel': 'فوت بر ثانیه'}, 
        {'value': 'MilePerHour', 'label': 'MilePerHour', 'flabel': 'مایل بر ساعت'}
    ],
    'pressure' : [
        {'value': 'pascal', 'label': 'pascal', 'flabel': 'پاسکال'}, 
        {'value': 'bar', 'label': 'bar', 'flabel': 'بار'}, 
        {'value': 'PoundPerSquareInch', 'label': 'PoundPerSquareInch', 'flabel': 'پوند بر اینچ مربع'}, 
        {'value': 'StandardAtmosphere', 'label': 'StandardAtmosphere', 'flabel': 'اتمسفر استاندارد'}
    ],
}

# Create a translator object
ru_translator = GoogleTranslator(source='auto', target='ru')
de_translator = GoogleTranslator(source='auto', target='de')
ar_translator = GoogleTranslator(source='auto', target='ar')
fr_translator = GoogleTranslator(source='auto', target='fr')



for key in units_labels:
    for item in units_labels[key]:
        de_translated = de_translator.translate(item["value"], lang_tgt="de")
        ru_translated = ru_translator.translate(item["value"], lang_tgt="ru")
        ar_translated = ar_translator.translate(item["value"], lang_tgt="ar")
        fr_translated = fr_translator.translate(item["value"], lang_tgt="fr")
        item["rulabel"] = ru_translated
        item["delabel"] = de_translated
        item["frlabel"] = fr_translated
        item["arlabel"] = ar_translated


print(units_labels)