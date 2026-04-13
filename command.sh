#!/bin/bash

# ============================================
# Bangla (legacy structure — bangla_fonts/hw/)
# ============================================
python3 generate_distorted_image.py \
    --text "কোচবিহারের প্রথম রেলপথ ছিল যখন কোচবিহার রাজ্য রেলপথ ১৯০১ সালে" \
    --script bangla \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 5 \
    --bars True \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background False \
    --output_path "out/bangla_generated.png"

# ============================================
# Hindi (Devanagari)
# ============================================
python3 generate_distorted_image.py \
    --text "भारत मेरा देश है और हिंदी मेरी भाषा" \
    --script devanagari \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 3 \
    --bars True \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background False \
    --output_path "out/hindi_generated.png"

# ============================================
# Tamil
# ============================================
python3 generate_distorted_image.py \
    --text "தமிழ் எங்கள் மொழி" \
    --script tamil \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/tamil_generated.png"

# ============================================
# Telugu
# ============================================
python3 generate_distorted_image.py \
    --text "తెలుగు మా భాష" \
    --script telugu \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/telugu_generated.png"

# ============================================
# Kannada
# ============================================
python3 generate_distorted_image.py \
    --text "ಕನ್ನಡ ನಮ್ಮ ಭಾಷೆ" \
    --script kannada \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/kannada_generated.png"

# ============================================
# Malayalam
# ============================================
python3 generate_distorted_image.py \
    --text "മലയാളം നമ്മുടെ ഭാഷ" \
    --script malayalam \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/malayalam_generated.png"

# ============================================
# Gujarati
# ============================================
python3 generate_distorted_image.py \
    --text "ગુજરાતી અમારી ભાષા છે" \
    --script gujarati \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/gujarati_generated.png"

# ============================================
# Odia
# ============================================
python3 generate_distorted_image.py \
    --text "ଓଡ଼ିଆ ଆମ ଭାଷା" \
    --script odia \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/odia_generated.png"

# ============================================
# Gurmukhi (Punjabi)
# ============================================
python3 generate_distorted_image.py \
    --text "ਪੰਜਾਬੀ ਸਾਡੀ ਮਾਂ ਬੋਲੀ" \
    --script gurmukhi \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/gurmukhi_generated.png"

# ============================================
# Sinhala
# ============================================
python3 generate_distorted_image.py \
    --text "සිංහල අපේ භාෂාව" \
    --script sinhala \
    --font_size 48 \
    --font_path "" \
    --background_path "" \
    --angle 0 \
    --bars False \
    --add_random_text False \
    --add_boxes False \
    --add_curves False \
    --apply_data_augmentation True \
    --white_background True \
    --output_path "out/sinhala_generated.png"