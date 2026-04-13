import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
import string
import numpy as np
import math
import os
import re
from .augmentation import data_transformer
from .indic_config import (
    INDIC_SCRIPTS, RTL_SCRIPTS,
    get_characters_for_script, get_available_scripts, get_script_direction
)


class GlyphScribe:
    """
    GlyphScribe: A class for generating distorted text images with various effects.
    Supports all major Indic scripts.
    """

    def __init__(self, base_fonts_dir='fonts', background_base_dir='background', script='bangla'):
        """
        Initialize GlyphScribe.

        Args:
            base_fonts_dir (str): Base directory for fonts.
                Structure: fonts/{script}/hw/ and fonts/{script}/printed/
                OR legacy: bangla_fonts/hw/ (auto-detected)
            background_base_dir (str): Base directory for background images
            script (str): Target script. Options:
                'bangla', 'devanagari', 'tamil', 'telugu', 'kannada',
                'malayalam', 'gujarati', 'odia', 'gurmukhi', 'sinhala', 'all_indic'
        """
        self.base_fonts_dir = base_fonts_dir
        self.background_base_dir = background_base_dir
        self.script = script
        self.direction = get_script_direction(script)
        self.all_characters = string.punctuation + " " + get_characters_for_script(script)

        # Validate font directory exists
        self._validate_font_dir()

    def _validate_font_dir(self):
        """Check if font directory structure is valid."""
        if not os.path.exists(self.base_fonts_dir):
            # Try legacy bangla_fonts path
            if os.path.exists("bangla_fonts") and self.script == "bangla":
                self.base_fonts_dir = "bangla_fonts"
                print(f"⚠️ Using legacy font path: bangla_fonts/")
                return
            raise FileNotFoundError(
                f"Font directory not found: {self.base_fonts_dir}\n"
                f"Expected structure:\n"
                f"  {self.base_fonts_dir}/{self.script}/hw/*.ttf\n"
                f"  {self.base_fonts_dir}/{self.script}/printed/*.ttf"
            )

    @staticmethod
    def supported_scripts():
        """Return list of all supported scripts."""
        return get_available_scripts()

    @staticmethod
    def calculate_skew_offset(x, x_pivot, angle):
        """Calculate vertical offset for skewing text."""
        angle = np.radians(angle)
        delta_y = (x_pivot - x) * np.tan(angle)
        return delta_y

    @staticmethod
    def calculate_bent_offset(x, amplitude, frequency):
        """Calculate vertical offset for bent effect using sine wave."""
        return int(amplitude * np.sin(frequency * x))

    @staticmethod
    def extract_words(sentence):
        """Extract words from a sentence, works for any script."""
        words = re.findall(r'\S+\s*', sentence)
        return words

    def _get_font_dir(self, font_type="hw"):
        """
        Resolve font directory path with fallback logic.

        Tries in order:
            1. fonts/{script}/{font_type}/
            2. fonts/{font_type}/
            3. bangla_fonts/{font_type}/  (legacy)
        """
        # Try script-specific path
        path = os.path.join(self.base_fonts_dir, self.script, font_type)
        if os.path.exists(path):
            return path

        # Legacy fallback (existing bangla_fonts/hw/ and bangla_fonts/printed/)
        if self.script in ("bangla", "assamese"):
            path = os.path.join(self.base_fonts_dir, font_type)
            if os.path.exists(path) and os.listdir(path):
                return path

        raise FileNotFoundError(
            f"No font directory found for script='{self.script}', type='{font_type}'\n"
            f"Tried:\n"
            f"  {self.base_fonts_dir}/{self.script}/{font_type}/\n"
            f"  {self.base_fonts_dir}/{font_type}/\n"
            f"  bangla_fonts/{font_type}/"
        )

    def get_random_font_path(self, font_type="hw"):
        """Get a random font path from the fonts directory."""
        font_dir = self._get_font_dir(font_type)
        fonts = [f for f in os.listdir(font_dir) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]

        if not fonts:
            raise FileNotFoundError(f"No font files found in {font_dir}")

        font_name = np.random.choice(fonts)
        return os.path.join(font_dir, font_name)

    def get_all_font_paths(self, font_type="hw"):
        """Get all font paths for current script."""
        font_dir = self._get_font_dir(font_type)
        fonts = [
            os.path.join(font_dir, f)
            for f in os.listdir(font_dir)
            if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))
        ]
        return fonts

    def get_random_background_path(self):
        """Get a random background image path."""
        valid_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        backgrounds = [
            f for f in os.listdir(self.background_base_dir)
            if f.lower().endswith(valid_ext) and not f.startswith('.')
        ]

        if not backgrounds:
            raise FileNotFoundError(f"No background images in {self.background_base_dir}")

        bg_name = np.random.choice(backgrounds)
        return os.path.join(self.background_base_dir, bg_name)

    def add_bars(self, draw, image_size):
        """Add random vertical and horizontal bars to the image."""
        for _ in range(random.randint(3, 6)):
            bar_x = random.randint(0, image_size[0] - 1)
            draw.line([(bar_x, 0), (bar_x, image_size[1])],
                     fill=tuple([np.random.randint(0, 100)] * 3),
                     width=random.randint(1, 3))

        for _ in range(random.randint(1, 3)):
            bar_y = random.randint(0, image_size[1] - 1)
            draw.line([(0, bar_y), (image_size[0], bar_y)],
                     fill=tuple([np.random.randint(0, 100)] * 3),
                     width=random.randint(1, 3))

    def add_random_text_overlay(self, draw, text, font, padding, image_size):
        """Add random text overlay using script-appropriate characters."""
        random_text = ''.join(random.choice(self.all_characters) for _ in range(len(text)))
        bbox = draw.textbbox((0, 0), text, font=font)
        text_height = bbox[3] - bbox[1]
        draw.text(
            (random.randint(-50, 50),
             image_size[1] - random.randint(5, 15) if padding[1] <= padding[3]
             else -text_height + random.randint(5, 15)),
            random_text,
            font=font,
            fill=tuple([np.random.randint(0, 100)] * 3),
        )

    def draw_text_with_boxes(self, draw, text, font, padding, tol, character_width, character_height):
        """Draw text with boxes around each character."""
        color = tuple([np.random.randint(0, 100)] * 3)
        text_color = tuple([np.random.randint(0, 100)] * 3)
        width = random.randint(1, 3)

        for i in range(len(text)):
            draw.line([(padding[0] + i*tol * character_width, padding[1]),
                      (padding[0] + i*tol * character_width, padding[1] + tol * character_width)],
                      fill=color, width=width)
            draw.line([(padding[0] + i*tol * character_width, padding[1] + tol * character_width),
                      (padding[0] + (i+1)*tol * character_width, padding[1] + tol * character_width)],
                      fill=color, width=width)
            draw.line([(padding[0] + (i+1)*tol * character_width, padding[1]),
                      (padding[0] + (i+1)*tol * character_width, padding[1] + tol * character_width)],
                      fill=color, width=width)
            draw.text(
                (padding[0] + i*tol * character_width + ((tol-1) * character_width) // 2 + random.randint(-2,2),
                 padding[1] + tol * character_width - character_height + random.randint(-2,2)),
                text[i],
                font=font,
                fill=text_color,
            )

    def draw_text_with_curves(self, draw, words, font, padding):
        """Draw text with curved effect."""
        x, y = padding[0], padding[1]
        for word in words:
            offset_y = self.calculate_bent_offset(x=x, amplitude=4, frequency=0.02)
            draw.text(
                (x, y + offset_y),
                word,
                font=font,
                fill=tuple([np.random.randint(0, 100)] * 3),
            )
            word_bbox = draw.textbbox((0, 0), word, font=font)
            word_width = word_bbox[2] - word_bbox[0]
            x += word_width

    def draw_text_with_skew(self, draw, words, font, padding, text_width, image_height, angle):
        """Draw text with skew effect."""
        x, y = padding[0], (image_height // 2)
        x_mid = x + (text_width // 2)
        for word in words:
            offset_y = self.calculate_skew_offset(x=x, x_pivot=x_mid, angle=angle)
            draw.text(
                (x, y - offset_y),
                word,
                font=font,
                fill=tuple([np.random.randint(0, 100)] * 3),
            )
            word_bbox = draw.textbbox((0, 0), word, font=font)
            word_width = word_bbox[2] - word_bbox[0]
            x += word_width

    def generate(self, text, font_size=48, font_path="", background_path="", angle=0,
                bars=True, add_random_text=True, add_boxes=True, add_curves=False,
                apply_data_augmentation=True, white_background=True, output_path="generated_image.png"):
        """
        Generate a distorted text image with various effects.
        Works with any supported Indic script.
        """
        image = Image.new("RGB", (2000, 2000), "white")
        draw = ImageDraw.Draw(image)

        # Apply BiDi ONLY for RTL scripts
        if self.direction == "rtl":
            from bidi.algorithm import get_display
            text = get_display(text)

        words = self.extract_words(text)

        if font_path == "":
            font_path = self.get_random_font_path(font_type="hw")

        font = ImageFont.truetype(font_path, size=font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        total_word_width = 0
        for word in words:
            word_bbox = draw.textbbox((0, 0), word, font=font)
            word_width = word_bbox[2] - word_bbox[0]
            total_word_width += word_width

        if add_boxes:
            tol = random.randint(10, 15) / 10
            char_sizes = []
            for c in text:
                cb = draw.textbbox((0, 0), c, font=font)
                char_sizes.append((cb[2] - cb[0], cb[3] - cb[1]))
            character_width, character_height = np.mean(char_sizes, axis=0).astype(int)
            image = Image.new("RGB", (int(tol * character_width * len(text)), character_height), "white")
        else:
            w = text_width
            h = text_height

            if angle != 0 or add_curves:
                w = total_word_width

            angle_rad = math.radians(angle)
            new_w = w
            new_h = h
            if not add_curves:
                new_h = h + int(abs(w * np.tan(angle_rad)))

            image = Image.new("RGB", (new_w, new_h), "white")

        padding = tuple(random.randint(40, 40) for _ in range(4))
        image = ImageOps.expand(image, padding, fill="white")
        image_width, image_height = image.size

        if not white_background:
            if background_path == "":
                background_path = self.get_random_background_path()
            background_image = Image.open(background_path)
            background_image = background_image.resize((image_width, image_height))
            image.paste(background_image)

        draw = ImageDraw.Draw(image)

        if bars:
            self.add_bars(draw, image.size)

        if add_random_text:
            self.add_random_text_overlay(draw, text, font, padding, image.size)

        if add_boxes:
            self.draw_text_with_boxes(draw, text, font, padding, tol, character_width, character_height)
        else:
            if add_curves:
                self.draw_text_with_curves(draw, words, font, padding)
            elif angle != 0:
                self.draw_text_with_skew(draw, words, font, padding, text_width, image_height, angle)
            else:
                draw.text(
                    (padding[0], padding[1]),
                    text,
                    font=font,
                    fill=tuple([np.random.randint(0, 100)] * 3),
                )

        if apply_data_augmentation:
            image = data_transformer(image)

        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        image.save(output_path)
        return