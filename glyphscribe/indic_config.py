"""
Indic script configurations — Unicode ranges, font sources, and metadata.
"""

INDIC_SCRIPTS = {
    "bangla": {
        "name": "Bangla (Bengali)",
        "unicode_range": (0x0980, 0x09FF),
        "direction": "ltr",
        "test_text": {
            "vowels": "অ আ ই ঈ উ ঊ ঋ এ ঐ ও ঔ",
            "consonants": "ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম",
            "conjuncts": "ক্ষ জ্ঞ ত্র শ্র ক্র প্র",
            "kar_marks": "কা কি কী কু কূ কে কৈ কো কৌ কৃ",
            "numbers": "০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯",
            "sample": "আমার সোনার বাংলা",
        },
        "noto_font": "NotoSansBengali",
    },
    "devanagari": {
        "name": "Devanagari (Hindi, Marathi, Sanskrit, Nepali)",
        "unicode_range": (0x0900, 0x097F),
        "direction": "ltr",
        "test_text": {
            "vowels": "अ आ इ ई उ ऊ ऋ ए ऐ ओ औ",
            "consonants": "क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म",
            "conjuncts": "क्ष त्र ज्ञ श्र क्र प्र",
            "kar_marks": "का कि की कु कू के कै को कौ कृ",
            "numbers": "० १ २ ३ ४ ५ ६ ७ ८ ९",
            "sample": "भारत मेरा देश है",
        },
        "noto_font": "NotoSansDevanagari",
    },
    "tamil": {
        "name": "Tamil",
        "unicode_range": (0x0B80, 0x0BFF),
        "direction": "ltr",
        "test_text": {
            "vowels": "அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ",
            "consonants": "க ங ச ஞ ட ண த ந ப ம ய ர ல வ ழ ள ற ன",
            "numbers": "௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯",
            "sample": "தமிழ் எங்கள் மொழி",
        },
        "noto_font": "NotoSansTamil",
    },
    "telugu": {
        "name": "Telugu",
        "unicode_range": (0x0C00, 0x0C7F),
        "direction": "ltr",
        "test_text": {
            "vowels": "అ ఆ ఇ ఈ ఉ ఊ ఋ ఎ ఏ ఐ ఒ ఓ ఔ",
            "consonants": "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న",
            "numbers": "౦ ౧ ౨ ౩ ౪ ౫ ౬ ౭ ౮ ౯",
            "sample": "తెలుగు మా భాష",
        },
        "noto_font": "NotoSansTelugu",
    },
    "kannada": {
        "name": "Kannada",
        "unicode_range": (0x0C80, 0x0CFF),
        "direction": "ltr",
        "test_text": {
            "vowels": "ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಎ ಏ ಐ ಒ ಓ ಔ",
            "consonants": "ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ",
            "numbers": "೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯",
            "sample": "ಕನ್ನಡ ನಮ್ಮ ಭಾಷೆ",
        },
        "noto_font": "NotoSansKannada",
    },
    "malayalam": {
        "name": "Malayalam",
        "unicode_range": (0x0D00, 0x0D7F),
        "direction": "ltr",
        "test_text": {
            "vowels": "അ ആ ഇ ഈ ഉ ഊ ഋ എ ഏ ഐ ഒ ഓ ഔ",
            "consonants": "ക ഖ ഗ ഘ ങ ച ഛ ജ ഝ ഞ ട ഠ ഡ ഢ ണ ത ഥ ദ ധ ന",
            "numbers": "൦ ൧ ൨ ൩ ൪ ൫ ൬ ൭ ൮ ൯",
            "sample": "മലയാളം നമ്മുടെ ഭാഷ",
        },
        "noto_font": "NotoSansMalayalam",
    },
    "gujarati": {
        "name": "Gujarati",
        "unicode_range": (0x0A80, 0x0AFF),
        "direction": "ltr",
        "test_text": {
            "vowels": "અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ",
            "consonants": "ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન",
            "numbers": "૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮ ૯",
            "sample": "ગુજરાતી અમારી ભાષા",
        },
        "noto_font": "NotoSansGujarati",
    },
    "odia": {
        "name": "Odia (Oriya)",
        "unicode_range": (0x0B00, 0x0B7F),
        "direction": "ltr",
        "test_text": {
            "vowels": "ଅ ଆ ଇ ଈ ଉ ଊ ଋ ଏ ଐ ଓ ଔ",
            "consonants": "କ ଖ ଗ ଘ ଙ ଚ ଛ ଜ ଝ ଞ ଟ ଠ ଡ ଢ ଣ ତ ଥ ଦ ଧ ନ",
            "numbers": "୦ ୧ ୨ ୩ ୪ ୫ ୬ ୭ ୮ ୯",
            "sample": "ଓଡ଼ିଆ ଆମ ଭାଷା",
        },
        "noto_font": "NotoSansOriya",
    },
    "gurmukhi": {
        "name": "Gurmukhi (Punjabi)",
        "unicode_range": (0x0A00, 0x0A7F),
        "direction": "ltr",
        "test_text": {
            "vowels": "ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ",
            "consonants": "ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ",
            "numbers": "੦ ੧ ੨ ੩ ੪ ੫ ੬ ੭ ੮ ੯",
            "sample": "ਪੰਜਾਬੀ ਸਾਡੀ ਮਾਂ ਬੋਲੀ",
        },
        "noto_font": "NotoSansGurmukhi",
    },
    "sinhala": {
        "name": "Sinhala",
        "unicode_range": (0x0D80, 0x0DFF),
        "direction": "ltr",
        "test_text": {
            "vowels": "අ ආ ඇ ඈ ඉ ඊ උ ඌ එ ඒ ඔ ඕ",
            "consonants": "ක ඛ ග ඝ ඞ ච ඡ ජ ඣ ඤ ට ඨ ඩ ඪ ණ ත ථ ද ධ න",
            "numbers": "0 1 2 3 4 5 6 7 8 9",
            "sample": "සිංහල අපේ භාෂාව",
        },
        "noto_font": "NotoSansSinhala",
    },
}

RTL_SCRIPTS = {"arabic", "urdu", "hebrew"}

def get_available_scripts():
    """Return list of all supported script names."""
    return list(INDIC_SCRIPTS.keys())

def get_characters_for_script(script):
    """Get Unicode characters for a given script."""
    if script == "all_indic":
        chars = ""
        for config in INDIC_SCRIPTS.values():
            start, end = config["unicode_range"]
            chars += ''.join([chr(i) for i in range(start, end + 1)])
        return chars

    if script not in INDIC_SCRIPTS:
        raise ValueError(
            f"Unknown script: '{script}'\n"
            f"Available scripts: {get_available_scripts()}"
        )

    start, end = INDIC_SCRIPTS[script]["unicode_range"]
    return ''.join([chr(i) for i in range(start, end + 1)])

def get_test_texts(script):
    """Get test texts for a given script."""
    if script not in INDIC_SCRIPTS:
        raise ValueError(f"Unknown script: '{script}'")
    return INDIC_SCRIPTS[script]["test_text"]

def get_script_direction(script):
    """Get text direction for a script."""
    if script in RTL_SCRIPTS:
        return "rtl"
    return "ltr"