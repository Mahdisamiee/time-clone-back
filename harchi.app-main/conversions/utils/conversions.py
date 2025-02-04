'''
google unit converter
	find all of that


Volume:
	{
		'liter': 1,
		'milliliter': 1000,
		''
	}
	


'''

units_labels = {
    'length': [{'value': 'meter',
   'label': 'meter',
   'flabel': 'متر',
   'rulabel': 'метр',
   'delabel': 'Meter',
   'frlabel': 'mètre',
   'arlabel': 'متر'},
  {'value': 'kilometer',
   'label': 'kilometer',
   'flabel': 'کیلومنر',
   'rulabel': 'километр',
   'delabel': 'Kilometer',
   'frlabel': 'kilomètre',
   'arlabel': 'كيلومتر'},
  {'value': 'centimeter',
   'label': 'centimeter',
   'flabel': 'سانتی متر',
   'rulabel': 'сантиметр',
   'delabel': 'Zentimeter',
   'frlabel': 'centimètre',
   'arlabel': 'سنتيمتر'},
  {'value': 'milimeter',
   'label': 'milimeter',
   'flabel': 'میلی متر',
   'rulabel': 'миллиметры',
   'delabel': 'Millimeter',
   'frlabel': 'millimètres',
   'arlabel': 'ملليمتر'},
  {'value': 'micometer',
   'label': 'micometer',
   'flabel': 'میکرو متر',
   'rulabel': 'микрометр',
   'delabel': 'Mikrometer',
   'frlabel': 'micromètre',
   'arlabel': 'ميكرومتر'},
  {'value': 'nanometer',
   'label': 'nanometer',
   'flabel': 'نانو متر',
   'rulabel': 'нанометр',
   'delabel': 'Nanometer',
   'frlabel': 'nanomètre',
   'arlabel': 'نانومتر'},
  {'value': 'mile',
   'label': 'mile',
   'flabel': 'مایل',
   'rulabel': 'миля',
   'delabel': 'Meile',
   'frlabel': 'mile',
   'arlabel': 'ميل'},
  {'value': 'yard',
   'label': 'yard',
   'flabel': 'یارد',
   'rulabel': 'площадка',
   'delabel': 'Hof',
   'frlabel': 'cour',
   'arlabel': 'حديقة منزل'},
  {'value': 'inch',
   'label': 'inch',
   'flabel': 'اینچ',
   'rulabel': 'дюйм',
   'delabel': 'Zoll',
   'frlabel': 'pouce',
   'arlabel': 'بوصة'},
  {'value': 'foot',
   'label': 'foot',
   'flabel': 'فوت',
   'rulabel': 'ступня',
   'delabel': 'Fuß',
   'frlabel': 'pied',
   'arlabel': 'قدم'}],
 'time': [{'value': 'second',
   'label': 'second',
   'flabel': 'ثانیه',
   'rulabel': 'второй',
   'delabel': 'zweite',
   'frlabel': 'deuxième',
   'arlabel': 'ثانية'},
  {'value': 'milisecond',
   'label': 'milisecond',
   'flabel': 'میلی ثانیه',
   'rulabel': 'миллисекунда',
   'delabel': 'Millisekunde',
   'frlabel': 'milliseconde',
   'arlabel': 'ميلي ثانية'},
  {'value': 'microsecond',
   'label': 'microsecond',
   'flabel': 'میکرو ثانیه',
   'rulabel': 'микросекунда',
   'delabel': 'Mikrosekunde',
   'frlabel': 'microseconde',
   'arlabel': 'ميكروثانية'},
  {'value': 'nanosecond',
   'label': 'nanosecond',
   'flabel': 'نانو ثانیه',
   'rulabel': 'наносекунда',
   'delabel': 'Nanosekunde',
   'frlabel': 'nanoseconde',
   'arlabel': 'نانو ثانية'},
  {'value': 'minute',
   'label': 'minute',
   'flabel': 'دقیقه',
   'rulabel': 'минута',
   'delabel': 'Minute',
   'frlabel': 'minute',
   'arlabel': 'دقيقة'},
  {'value': 'hour',
   'label': 'hour',
   'flabel': 'ساعت',
   'rulabel': 'час',
   'delabel': 'Stunde',
   'frlabel': 'heure',
   'arlabel': 'ساعة'},
  {'value': 'day',
   'label': 'day',
   'flabel': 'روز',
   'rulabel': 'день',
   'delabel': 'Tag',
   'frlabel': 'jour',
   'arlabel': 'يوم'},
  {'value': 'week',
   'label': 'week',
   'flabel': 'هفته',
   'rulabel': 'неделя',
   'delabel': 'Woche',
   'frlabel': 'semaine',
   'arlabel': 'أسبوع'},
  {'value': 'month',
   'label': 'month',
   'flabel': 'ماه',
   'rulabel': 'месяц',
   'delabel': 'Monat',
   'frlabel': 'mois',
   'arlabel': 'شهر'},
  {'value': 'year',
   'label': 'year',
   'flabel': 'سال',
   'rulabel': 'год',
   'delabel': 'Jahr',
   'frlabel': 'année',
   'arlabel': 'سنة'}],
 'mass': [{'value': 'gram',
   'label': 'gram',
   'flabel': 'گرم',
   'rulabel': 'грамм',
   'delabel': 'Gramm',
   'frlabel': 'gramme',
   'arlabel': 'غرام'},
  {'value': 'kilogram',
   'label': 'kilogram',
   'flabel': 'کیلوگرم',
   'rulabel': 'килограмм',
   'delabel': 'Kilogramm',
   'frlabel': 'kilogramme',
   'arlabel': 'كيلوغرام'},
  {'value': 'milligram',
   'label': 'milligram',
   'flabel': 'میلی گرم',
   'rulabel': 'миллиграмм',
   'delabel': 'Milligramm',
   'frlabel': 'milligramme',
   'arlabel': 'مليغرام'},
  {'value': 'microgram',
   'label': 'microgram',
   'flabel': 'میکرو گرم',
   'rulabel': 'микрограмм',
   'delabel': 'Mikrogramm',
   'frlabel': 'microgramme',
   'arlabel': 'ميكروجرام'},
  {'value': 'ton',
   'label': 'ton',
   'flabel': 'تن',
   'rulabel': 'тонна',
   'delabel': 'Tonne',
   'frlabel': 'tonne',
   'arlabel': 'طن'},
  {'value': 'USton',
   'label': 'USton',
   'flabel': 'تن آمریکا',
   'rulabel': 'СШАтон',
   'delabel': 'USton',
   'frlabel': 'États-Uniston',
   'arlabel': 'أوستون'},
  {'value': 'stone',
   'label': 'stone',
   'flabel': 'سنگ',
   'rulabel': 'камень',
   'delabel': 'Stein',
   'frlabel': 'pierre',
   'arlabel': 'حجر'},
  {'value': 'pound',
   'label': 'pound',
   'flabel': 'پوند',
   'rulabel': 'фунт',
   'delabel': 'Pfund',
   'frlabel': 'livre',
   'arlabel': 'جنيه'},
  {'value': 'ounce',
   'label': 'ounce',
   'flabel': 'اونس',
   'rulabel': 'унция',
   'delabel': 'Unze',
   'frlabel': 'once',
   'arlabel': 'أوقية'}],
 'area': [{'value': 'squaremeter',
   'label': 'squaremeter',
   'flabel': 'مترمربغ',
   'rulabel': 'квадратный метр',
   'delabel': 'Quadratmeter',
   'frlabel': 'mètre carré',
   'arlabel': 'متر مربع'},
  {'value': 'squarekilometer',
   'label': 'squarekilometer',
   'flabel': 'کیلومتر مربع',
   'rulabel': 'квадратный километр',
   'delabel': 'Quadratkilometer',
   'frlabel': 'kilomètre carré',
   'arlabel': 'كيلو متر مربع'},
  {'value': 'squaremile',
   'label': 'squaremile',
   'flabel': 'مایل مربع',
   'rulabel': 'квадратная миля',
   'delabel': 'Quadratmeile',
   'frlabel': 'mile carré',
   'arlabel': 'ميل مربع'},
  {'value': 'squareyard',
   'label': 'squareyard',
   'flabel': 'یارد مربع',
   'rulabel': 'квадратный двор',
   'delabel': 'Quadratmeter',
   'frlabel': 'Yard carré',
   'arlabel': 'فناء مربع'},
  {'value': 'squarefoot',
   'label': 'squarefoot',
   'flabel': 'فوت مربع',
   'rulabel': 'квадратный фут',
   'delabel': 'Quadratfuß',
   'frlabel': 'pied carré',
   'arlabel': 'قدم مربع'},
  {'value': 'squareinch',
   'label': 'squareinch',
   'flabel': 'اینچ مربع',
   'rulabel': 'квадратный дюйм',
   'delabel': 'Quadratzoll',
   'frlabel': 'pouce carré',
   'arlabel': 'بوصة مربعة'},
  {'value': 'hectare',
   'label': 'hectare',
   'flabel': 'هکتار',
   'rulabel': 'га',
   'delabel': 'Hektar',
   'frlabel': 'hectare',
   'arlabel': 'هكتار'},
  {'value': 'acre',
   'label': 'acre',
   'flabel': 'جریب',
   'rulabel': 'акр',
   'delabel': 'Acre',
   'frlabel': 'acre',
   'arlabel': 'فدان'}],
 'data-transfer': [{'value': 'BitPerSecond',
   'label': 'BitPerSecond',
   'flabel': 'بیت بر ثانیه',
   'rulabel': 'Битперсекунда',
   'delabel': 'BitProSekunde',
   'frlabel': 'BitParSeconde',
   'arlabel': 'بت في الثانية'},
  {'value': 'KilobitPerSecond',
   'label': 'KilobitPerSecond',
   'flabel': 'کیلوبیت بر ثانیه',
   'rulabel': 'Килобит в секунду',
   'delabel': 'KilobitProSekunde',
   'frlabel': 'Kilobit par seconde',
   'arlabel': 'كيلوبت في الثانية'},
  {'value': 'KilobytePerSecond',
   'label': 'KilobytePerSecond',
   'flabel': 'کیلوبایت بر ثانیه',
   'rulabel': 'Килобайтперсекунда',
   'delabel': 'KilobyteProSekunde',
   'frlabel': 'Kilooctet par seconde',
   'arlabel': 'كيلو بايت في الثانية'},
  {'value': 'KibibitPerSecond',
   'label': 'KibibitPerSecond',
   'flabel': 'کیبی بیت بر ثانیه',
   'rulabel': 'Кибибитперсекунда',
   'delabel': 'KibibitPerSecond',
   'frlabel': 'KibibitParSeconde',
   'arlabel': 'KibibitPerSecond'},
  {'value': 'MegabitPerSecond',
   'label': 'MegabitPerSecond',
   'flabel': 'مگابیت بر ثانیه',
   'rulabel': 'МегабитВСекунду',
   'delabel': 'MegabitProSekunde',
   'frlabel': 'Mégabit par seconde',
   'arlabel': 'ميغابت في الثانية'},
  {'value': 'MegabytePerSecond',
   'label': 'MegabytePerSecond',
   'flabel': 'مگابایت بر ثانیه',
   'rulabel': 'Мегабайт в секунду',
   'delabel': 'MegabyteProSekunde',
   'frlabel': 'MégaoctetParSeconde',
   'arlabel': 'ميغا بايت في الثانية'},
  {'value': 'MebibitPerSecond',
   'label': 'MebibitPerSecond',
   'flabel': 'مبی بیت بر ثانیه',
   'rulabel': 'МебибитПерсекунда',
   'delabel': 'MebibitProSekunde',
   'frlabel': 'MebibitParSeconde',
   'arlabel': 'MebibitPerSecond'},
  {'value': 'GigabitPerSecond',
   'label': 'GigabitPerSecond',
   'flabel': 'گیگابیت بر ثانیه',
   'rulabel': 'Гигабит в секунду',
   'delabel': 'Gigabit pro Sekunde',
   'frlabel': 'GigabitParSeconde',
   'arlabel': 'جيجابت في الثانية'},
  {'value': 'GigabytePerSecond',
   'label': 'GigabytePerSecond',
   'flabel': 'گیگابایت بر ثانیه',
   'rulabel': 'ГигабайтВСекунду',
   'delabel': 'GigabyteProSekunde',
   'frlabel': 'GigaoctetParSeconde',
   'arlabel': 'جيجابايت في الثانية'},
  {'value': 'GibibitPerSecond',
   'label': 'GibibitPerSecond',
   'flabel': 'گیبی بیت بر ثانیه',
   'rulabel': 'ГибибитВСекунду',
   'delabel': 'GibibitProSekunde',
   'frlabel': 'GibibitParSeconde',
   'arlabel': 'جيبيبت في الثانية'},
  {'value': 'TerabitPerSecond',
   'label': 'TerabitPerSecond',
   'flabel': 'ترابیت بر ثانیه',
   'rulabel': 'Терабит в секунду',
   'delabel': 'TerabitProSekunde',
   'frlabel': 'Térabit par seconde',
   'arlabel': 'تيرابت في الثانية'},
  {'value': 'TerabytePerSecond',
   'label': 'TerabytePerSecond',
   'flabel': 'ترابایت بر ثانیه',
   'rulabel': 'Терабайтперсекунда',
   'delabel': 'Terabyte pro Sekunde',
   'frlabel': 'Téraoctet par seconde',
   'arlabel': 'تيرابايت في الثانية'},
  {'value': 'TebibitPerSecond',
   'label': 'TebibitPerSecond',
   'flabel': 'تبی بیت بر ثانیه',
   'rulabel': 'ТебибитВСекунду',
   'delabel': 'TebibitProSekunde',
   'frlabel': 'TébibitParSeconde',
   'arlabel': 'TebibitPerSecond'}],
 'digital-storage': [{'value': 'Byte',
   'label': 'Byte',
   'flabel': 'بایت',
   'rulabel': 'Байт',
   'delabel': 'Byte',
   'frlabel': 'Octet',
   'arlabel': 'بايت'},
  {'value': 'Kilobyte',
   'label': 'Kilobyte',
   'flabel': 'کیلوبایت',
   'rulabel': 'Килобайты',
   'delabel': 'Kilobyte',
   'frlabel': 'Kilooctets',
   'arlabel': 'كيلو بايت'},
  {'value': 'Kibibyte',
   'label': 'Kibibyte',
   'flabel': 'کیبی بیت',
   'rulabel': 'Кибибайт',
   'delabel': 'Kibibyte',
   'frlabel': 'Kibioctet',
   'arlabel': 'كيبيبيايت'},
  {'value': 'Megabyte',
   'label': 'Megabyte',
   'flabel': 'مگا بایت',
   'rulabel': 'Мегабайт',
   'delabel': 'Megabyte',
   'frlabel': 'Mégaoctet',
   'arlabel': 'ميغا بايت'},
  {'value': 'Mebibyte',
   'label': 'Mebibyte',
   'flabel': 'مبی بایت',
   'rulabel': 'Мебибайт',
   'delabel': 'Mebibyte',
   'frlabel': 'Mébioctet',
   'arlabel': 'ميبيبايت'},
  {'value': 'Gigabyte',
   'label': 'Gigabyte',
   'flabel': 'گیگا بایت',
   'rulabel': 'Гигабайт',
   'delabel': 'Gigabyte',
   'frlabel': 'Gigaoctet',
   'arlabel': 'جيجابايت'},
  {'value': 'Gibibyte',
   'label': 'Gibibyte',
   'flabel': 'گیبی بایت',
   'rulabel': 'Gibibyte',
   'delabel': 'Gibibyte',
   'frlabel': 'Gibioctet',
   'arlabel': 'جيبي بايت'},
  {'value': 'Terabyte',
   'label': 'Terabyte',
   'flabel': 'ترا بایت',
   'rulabel': 'Терабайт',
   'delabel': 'Terabyte',
   'frlabel': 'Téraoctet',
   'arlabel': 'تيرابايت'},
  {'value': 'Tebibyte',
   'label': 'Tebibyte',
   'flabel': 'تبی بایت',
   'rulabel': 'Tebibyte',
   'delabel': 'Tebibyte',
   'frlabel': 'Tébioctet',
   'arlabel': 'تيبيبايت'},
  {'value': 'Bit',
   'label': 'Bit',
   'flabel': 'بیت',
   'rulabel': 'Кусочек',
   'delabel': 'Bisschen',
   'frlabel': 'Peu',
   'arlabel': 'قليل'},
  {'value': 'Kilobit',
   'label': 'Kilobit',
   'flabel': 'کیلو بیت',
   'rulabel': 'Килобит',
   'delabel': 'Kilobit',
   'frlabel': 'Kilobit',
   'arlabel': 'كيلوبت'},
  {'value': 'Kibibit',
   'label': 'Kibibit',
   'flabel': 'کیبی بیت',
   'rulabel': 'Кибибит',
   'delabel': 'Kibibit',
   'frlabel': 'Kibibit',
   'arlabel': 'كيبيبيت'},
  {'value': 'Megabit',
   'label': 'Megabit',
   'flabel': 'مگا بیت',
   'rulabel': 'мегабиты',
   'delabel': 'Megabit',
   'frlabel': 'mégabits',
   'arlabel': 'ميغابت'},
  {'value': 'Mebibit',
   'label': 'Mebibit',
   'flabel': 'مبی بیت',
   'rulabel': 'Он выпьет меня',
   'delabel': 'Er wird mich trinken',
   'frlabel': 'Il me boira',
   'arlabel': 'سوف يشربني'},
  {'value': 'Gigabit',
   'label': 'Gigabit',
   'flabel': 'گیگا بیت',
   'rulabel': 'Гигабит',
   'delabel': 'Gigabit',
   'frlabel': 'Gigabits',
   'arlabel': 'جيجابت'},
  {'value': 'Gibibit',
   'label': 'Gibibit',
   'flabel': 'گیبی بیت',
   'rulabel': 'Он пойдет',
   'delabel': 'Er wird gehen',
   'frlabel': 'Il ira',
   'arlabel': 'هو سيذهب'},
  {'value': 'Terabit',
   'label': 'Terabit',
   'flabel': 'ترا بیت',
   'rulabel': 'Это пройдет',
   'delabel': 'Es wird nachlassen',
   'frlabel': "Cela va s'estomper",
   'arlabel': 'سوف يزول'},
  {'value': 'Tebibit',
   'label': 'Tebibit',
   'flabel': 'نبی بیت',
   'rulabel': 'Тебибит',
   'delabel': 'Tebibit',
   'frlabel': 'Tébibit',
   'arlabel': 'تيبيبت'},
  {'value': 'Petabit',
   'label': 'Petabit',
   'flabel': 'پتا بیت',
   'rulabel': 'Он спросит',
   'delabel': 'Er wird fragen',
   'frlabel': 'Il demandera',
   'arlabel': 'سوف يسأل'},
  {'value': 'Pebibit',
   'label': 'Pebibit',
   'flabel': 'پبی بیت',
   'rulabel': 'Он будет пить',
   'delabel': 'Er wird trinken',
   'frlabel': 'Il boira',
   'arlabel': 'سوف يشرب'}],
 'energy': [{'value': 'Joule',
   'label': 'Joule',
   'flabel': 'ژول',
   'rulabel': 'Джоуль',
   'delabel': 'Joule',
   'frlabel': 'Joule',
   'arlabel': 'جول'},
  {'value': 'KiloJoule',
   'label': 'KiloJoule',
   'flabel': 'کیلوژول',
   'rulabel': 'КилоДжоуль',
   'delabel': 'KiloJoule',
   'frlabel': 'KiloJoule',
   'arlabel': 'كيلوجول'},
  {'value': 'GramCalorie',
   'label': 'GramCalorie',
   'flabel': 'کالری-گرم',
   'rulabel': 'Грамм Калорий',
   'delabel': 'GrammKalorien',
   'frlabel': 'Gramcalorie',
   'arlabel': 'جرام كالوري'},
  {'value': 'Kilocalorie',
   'label': 'Kilocalorie',
   'flabel': 'کیلو کالری',
   'rulabel': 'Килокалория',
   'delabel': 'Kilokalorie',
   'frlabel': 'Kilocalorie',
   'arlabel': 'كيلو كالوري'},
  {'value': 'WattHour',
   'label': 'WattHour',
   'flabel': 'وات-ساعت',
   'rulabel': 'Ваттчас',
   'delabel': 'WattStunde',
   'frlabel': 'Wattheure',
   'arlabel': 'وات ساعة'},
  {'value': 'KilowattHour',
   'label': 'KilowattHour',
   'flabel': 'کیلو وات-ساعت',
   'rulabel': 'Киловатт-час',
   'delabel': 'Kilowattstunde',
   'frlabel': 'Kilowatt-heure',
   'arlabel': 'كيلووات في ساعة وحدة كهربائية'},
  {'value': 'Electronvolt',
   'label': 'Electronvolt',
   'flabel': 'الکترو-ولت',
   'rulabel': 'Электронвольт',
   'delabel': 'Elektronenvolt',
   'frlabel': 'Électron-volt',
   'arlabel': 'إلكترون فولت'},
  {'value': 'BritishThermalUnit',
   'label': 'BritishThermalUnit',
   'flabel': 'یکای گرمایی بریتانیا',
   'rulabel': 'BritishThermalUnit',
   'delabel': 'BritischeThermalEinheit',
   'frlabel': 'Unité thermique britannique',
   'arlabel': 'الوحدة الحرارية البريطانية'},
  {'value': 'USTherm',
   'label': 'USTherm',
   'flabel': 'یکای گرمای امریکا',
   'rulabel': 'USTherm',
   'delabel': 'USTherm',
   'frlabel': 'USTherm',
   'arlabel': 'USثيرم'},
  {'value': 'FootPound',
   'label': 'FootPound',
   'flabel': 'فوت-پوند',
   'rulabel': 'ФутПаунд',
   'delabel': 'Fußpfund',
   'frlabel': 'PiedPound',
   'arlabel': 'فوت باوند'}],
 'volume': [{'value': 'Liter',
   'label': 'Liter',
   'flabel': 'لیتر',
   'rulabel': 'Литр',
   'delabel': 'Liter',
   'frlabel': 'Litre',
   'arlabel': 'لتر'},
  {'value': 'MiliLiter',
   'label': 'MiliLiter',
   'flabel': 'میلی لیتر',
   'rulabel': 'Миллилитры',
   'delabel': 'Milliliter',
   'frlabel': 'Millilitres',
   'arlabel': 'ملليلتر'},
  {'value': 'USLiquidGallon',
   'label': 'USLiquidGallon',
   'flabel': 'گالون امریکا',
   'rulabel': 'СШАЖидкостьГаллон',
   'delabel': 'US-Flüssiggallone',
   'frlabel': 'USLiquideGallon',
   'arlabel': 'يو اس ليكويد جالون'},
  {'value': 'USLiquidQuart',
   'label': 'USLiquidQuart',
   'flabel': 'کوارت امریکا',
   'rulabel': 'СШАЖидкостьКварта',
   'delabel': 'USLiquidQuart',
   'frlabel': 'USLiquideQuart',
   'arlabel': 'USLiquidQuart'},
  {'value': 'USLiquidPint',
   'label': 'USLiquidPint',
   'flabel': 'پینت امریکا',
   'rulabel': 'СШАЖидкостьПинта',
   'delabel': 'USLiquidPint',
   'frlabel': 'USLiquidPint',
   'arlabel': 'USLiquidPint'},
  {'value': 'USLegalCup',
   'label': 'USLegalCup',
   'flabel': 'فنجان امریکا',
   'rulabel': 'СШАЮридическийКубок',
   'delabel': 'USLegalCup',
   'frlabel': 'USLegalCup',
   'arlabel': 'USLegalCup'},
  {'value': 'FluidOunce',
   'label': 'FluidOunce',
   'flabel': 'انس سیال',
   'rulabel': 'Жидкая унция',
   'delabel': 'Flüssigunzen',
   'frlabel': 'FluidOnce',
   'arlabel': 'فلويد أونس'},
  {'value': 'USTableSpoon',
   'label': 'USTableSpoon',
   'flabel': 'قاشق غذاخوری امریکا',
   'rulabel': 'USTableЛожка',
   'delabel': 'USTableSpoon',
   'frlabel': 'Cuillère à soupe américaine',
   'arlabel': 'UStableSpoon'},
  {'value': 'SUTeaSpoon',
   'label': 'SUTeaSpoon',
   'flabel': 'قاشق چای خوری امریکا',
   'rulabel': 'SUTЧайЛожка',
   'delabel': 'SUTeaSpoon',
   'frlabel': 'SUTéCuillère',
   'arlabel': 'سوتيسبون'},
  {'value': 'QubicMeter',
   'label': 'QubicMeter',
   'flabel': 'متر مکعب',
   'rulabel': 'QubicMeter',
   'delabel': 'QubicMeter',
   'frlabel': 'QubicMètre',
   'arlabel': 'QubicMeter'},
  {'value': 'ImperialGallon',
   'label': 'ImperialGallon',
   'flabel': 'گالن امپراطوری',
   'rulabel': 'Имперский галлон',
   'delabel': 'ImperialGallon',
   'frlabel': 'Gallon Impérial',
   'arlabel': 'امبريال جالون'},
  {'value': 'ImperialQuart',
   'label': 'ImperialQuart',
   'flabel': 'کوارت امپراطوری',
   'rulabel': 'Имперская кварта',
   'delabel': 'KaiserQuart',
   'frlabel': 'Quart Impérial',
   'arlabel': 'إمبريال كوارت'},
  {'value': 'ImperialPint',
   'label': 'ImperialPint',
   'flabel': 'پینت امپراطوری',
   'rulabel': 'ИмпериалПинта',
   'delabel': 'ImperialPint',
   'frlabel': 'Pinte Impériale',
   'arlabel': 'إمبريال باينت'},
  {'value': 'ImperialCup',
   'label': 'ImperialCup',
   'flabel': 'فنجان امپراطوری',
   'rulabel': 'ИмпериалКубок',
   'delabel': 'KaiserCup',
   'frlabel': 'Coupe Impériale',
   'arlabel': 'كأس امبريال'},
  {'value': 'Imp-FluidOunce',
   'label': 'Imp-FluidOunce',
   'flabel': 'اونس سیال امپراطوری',
   'rulabel': 'Imp-FluidOunce',
   'delabel': 'Imp-FluidUnze',
   'frlabel': 'Imp-FluidOunce',
   'arlabel': 'عفريت فلويد أونس'},
  {'value': 'Imp-TableSpoon',
   'label': 'Imp-TableSpoon',
   'flabel': 'قاشق غذاخوری امپراطوری',
   'rulabel': 'Imp-TableSpoon',
   'delabel': 'Imp-Esslöffel',
   'frlabel': 'Imp-TableSpoon',
   'arlabel': 'عفريت ملعقة كبيرة'},
  {'value': 'Imp-TeaSpoon',
   'label': 'Imp-TeaSpoon',
   'flabel': 'قاشق چای خوری امپراطوری',
   'rulabel': 'Имп-Чайная Ложка',
   'delabel': 'Imp-Teelöffel',
   'frlabel': 'Imp-Cuillère à thé',
   'arlabel': 'عفريت ملعقة صغيرة'},
  {'value': 'CubicFoot',
   'label': 'CubicFoot',
   'flabel': 'فوت مکعب',
   'rulabel': 'Кубический Фут',
   'delabel': 'Kubikfuß',
   'frlabel': 'CubicFoot',
   'arlabel': 'قدم مكعب'},
  {'value': 'CubicInch',
   'label': 'CubicInch',
   'flabel': 'اینچ مکعب',
   'rulabel': 'Кубический дюйм',
   'delabel': 'Kubikzoll',
   'frlabel': 'Pouce cube',
   'arlabel': 'بوصة مكعبة'}],
 'speed': [{'value': 'MeterPerSecond',
   'label': 'MeterPerSecond',
   'flabel': 'متر بر ثانیه',
   'rulabel': 'Метр в секунду',
   'delabel': 'MeterProSekunde',
   'frlabel': 'MètreParSeconde',
   'arlabel': 'متر في الثانية'},
  {'value': 'KiloMeterPerHour',
   'label': 'KiloMeterPerHour',
   'flabel': 'کیلومتر بر ساعت',
   'rulabel': 'Километр в час',
   'delabel': 'KiloMeterProStunde',
   'frlabel': 'Kilomètre par heure',
   'arlabel': 'كيلو متر في الساعة'},
  {'value': 'FootPerSecond',
   'label': 'FootPerSecond',
   'flabel': 'فوت بر ثانیه',
   'rulabel': 'ФутПерСекунд',
   'delabel': 'FußProSekunde',
   'frlabel': 'Pied par seconde',
   'arlabel': 'فوت في الثانية'},
  {'value': 'MilePerHour',
   'label': 'MilePerHour',
   'flabel': 'مایل بر ساعت',
   'rulabel': 'Миля в час',
   'delabel': 'MeileProStunde',
   'frlabel': 'MileParHeure',
   'arlabel': 'MilePerHour'}],
 'pressure': [{'value': 'pascal',
   'label': 'pascal',
   'flabel': 'پاسکال',
   'rulabel': 'паскаль',
   'delabel': 'pascal',
   'frlabel': 'pascal',
   'arlabel': 'باسكال'},
  {'value': 'bar',
   'label': 'bar',
   'flabel': 'بار',
   'rulabel': 'бар',
   'delabel': 'Bar',
   'frlabel': 'bar',
   'arlabel': 'حاجِز'},
  {'value': 'PoundPerSquareInch',
   'label': 'PoundPerSquareInch',
   'flabel': 'پوند بر اینچ مربع',
   'rulabel': 'фунт на квадратный дюйм',
   'delabel': 'Pfund pro Quadratzoll',
   'frlabel': 'Livre par pouce carré',
   'arlabel': 'رطل على البوصة المربعة'},
  {'value': 'StandardAtmosphere',
   'label': 'StandardAtmosphere',
   'flabel': 'اتمسفر استاندارد',
   'rulabel': 'Стандартная атмосфера',
   'delabel': 'Standardatmosphäre',
   'frlabel': 'Ambiance standard',
   'arlabel': 'الغلاف الجوي القياسي'}]
}

units = {
    'length': {
        # 'base': 'meter',
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'milimeter': 1000,
        'micometer': 10**6,
        'nanometer': 10**9,
        'mile': 0.000621371,
        'yard': 1.09361,
        'inch': 39.3701,
        'foot': 3.28084,
    },
    'time': {
        # 'base': 'second',
        'second': 1,
        'milisecond': 1000,
        'microsecond': 10**6,
        'nanosecond': 10**9,
        'minute': 1/60,
        'hour': 0.000277778,
        'day': 1/86400,
        'week': 1/604800,
        'month': 1/(30*24*3600),
        'year': 1/(365*24*3600),
    },
    'mass': {
        # 'base': 'mass',
        'gram': 1,
        'kilogram': 0.001,
        'milligram': 1000,
        'microgram': 10**6,
        'ton': 10**-6,
        'USton': 1/907200,
        'stone': 0.000157473,
        'pound': 0.002204621999999999832,
        'ounce': 0.035273951999999997309,
    },
    'area': {
        # 'base': 'squaremeter',
        'squaremeter': 1,
        'squarekilometer': 10**(-6),
        'squaremile': 0.00352077626,
        'squareyard': 1.1959,
        'squarefoot': 10.7639,
        'squareinch': 1550,
        'hectare': 10**-4,
        'acre': 1/4047,
    },
    'data-transfer': {
        'BitPerSecond': 1,
        'KilobitPerSecond': 0.001,
        'KilobytePerSecond': 0.000125,
        'KibibitPerSecond': 0.000976563, # 1/1024
        'MegabitPerSecond': 1/10**6,
        'MegabytePerSecond': 1 / (8*10**6),
        'MebibitPerSecond': 1/(1.049 * 10**6),
        'GigabitPerSecond': 1/10**9,
        'GigabytePerSecond': 1/(8*10**9),
        'GibibitPerSecond': 1/(1.074*10**9),
        'TerabitPerSecond': 1/(10**12),
        'TerabytePerSecond': 1/(8*10**12),
        'TebibitPerSecond': 1/(1.1*10**12),
    },
    'digital-storage': {
        'Byte': 1,
        'Kilobyte': 1/10**3,
        'Kibibyte': 1/1024,
        'Megabyte': 1/10**6,
        'Mebibyte': 1/(1.049*10**6),
        'Gigabyte': 1/10**9,
        'Gibibyte': 1/(1.074*10**9),
        'Terabyte': 1/10**12,
        'Tebibyte': 1/(1.1*10**12),
        'Bit': 8,
        'Kilobit': 0.008,
        'Kibibit': 1/128,
        'Megabit': 1/125000,
        'Mebibit': 1/131100,
        'Gigabit': 1/(1.25*10**8),
        'Gibibit': 1/(1.342*10**8),
        'Terabit': 1/(1.25*10**11),
        'Tebibit': 1/(1.374*10**11),
        'Petabit': 1/(1.25*10**14),
        'Pebibit': 1/(1.407*10**14),
    },
    'energy':{
        'Joule': 1,
        'KiloJoule': 0.001,
        'GramCalorie': 0.239006,
        'Kilocalorie': 1/4184,
        'WattHour': 1/3600,
        'KilowattHour': 1/(3.6*10**6),
        'Electronvolt': 6.242*10**18,
        'BritishThermalUnit': 1/1055,
        'USTherm': 1/(1.055*10**8),
        'FootPound': 1/1.356,        
    },
    'volume':{
        'Liter': 1,
        'MiliLiter': 1000,
        'USLiquidGallon': 1/3.785,
        'USLiquidQuart': 1.057,
        'USLiquidPint': 2.113,
        'USLegalCup': 4.167,
        'FluidOunce': 33.814,
        'USTableSpoon': 64.628,
        'SUTeaSpoon': 202.884,
        'QubicMeter': 1/1000,
        'ImperialGallon': 1/4.546,
        'ImperialQuart': 1/1.136,
        'ImperialPint': 1.76,
        'ImperialCup': 3.52,
        'Imp-FluidOunce': 35.195,
        'Imp-TableSpoon': 56.312,
        'Imp-TeaSpoon': 168.936,
        'CubicFoot': 1/28.317,
        'CubicInch': 61.024,
    },
    'speed':{
        'MeterPerSecond': 1,
        'KiloMeterPerHour': 3.6,
        'FootPerSecond': 3.28084,
        'MilePerHour': 2.23694,
    },
    'pressure': {
        'pascal': 1,
        'bar' : 1/10**5,
        'PoundPerSquareInch': 1/6895,
        'StandardAtmosphere': 1/101300,
    },
}


def get_generics():
    return list(units.keys())


def get_pu_for_unit(unit):
    return list(units_labels[unit])


def unit_conv(unit, from_unit, to_unit, val):
    '''
        if its not meter convert it to meter then convert it to the next one
        converting to meter => divide by that value
        convert to next => multiply by next
        120inch to yard
            120/39.3701*1.09361 => 3.33yard
    '''
    if unit not in get_generics():
        return 'general topic you have choosed doesnt exist'
    if from_unit not in units[unit].keys() or \
        to_unit not in units[unit].keys():
        return 'units you have choosed for conversion are not supported'
 
    unit_dict = units[unit]
    base_value = float(val)/(unit_dict[from_unit])
    converted_value = base_value*(unit_dict[to_unit])
    
    return converted_value


def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32


def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9


def celsius_to_kelvin(C):
    return C + 273.15


def kelvin_to_celsius(K):
    return K - 273.15


def kelvin_to_fahrenheit(K):
    return (K - 273.15) * 9/5 + 32 


def fahrenheit_to_kelvin(F):
    return (F - 32) * 5/9 + 273.15


temp_conv = {
    'celsius2fahrenheit': celsius_to_fahrenheit,
    'fahrenheit2celsius': fahrenheit_to_celsius,
    'celsius2kelvin': celsius_to_kelvin,
    'kelvin2celsius': kelvin_to_celsius,
    'kelvin2fahrenheit': kelvin_to_fahrenheit,
    'fahrenheit2kelvin': fahrenheit_to_kelvin,
}


def temp_conversion_modes():
    return list(temp_conv.keys())


def temp_conversion(conv_mode, val):
    '''
        - c2f
        - f2c
        - c2k
        - k2c
        - k2f
        - f2k
    '''
    
    if conv_mode in list(temp_conv.keys()):
        return temp_conv[conv_mode](float(val))
    
    return 'the mode you have choiced is not supported'
