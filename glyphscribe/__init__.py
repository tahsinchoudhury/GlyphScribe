"""
GlyphScribe: A module for generating distorted text images with various effects.
Supports all major Indic scripts.
"""
from .glyph_scribe import GlyphScribe
from .augmentation import data_transformer
from .indic_config import (
    INDIC_SCRIPTS,
    get_characters_for_script,
    get_available_scripts,
    get_test_texts,
)

__all__ = ['GlyphScribe', 'data_transformer', 'INDIC_SCRIPTS',
           'get_characters_for_script', 'get_available_scripts', 'get_test_texts']
__version__ = '2.0.0'