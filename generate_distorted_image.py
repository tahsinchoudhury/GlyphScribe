import click
from glyphscribe import GlyphScribe, get_available_scripts

@click.command()
@click.option('--text', help='Text to be generated in the image')
@click.option('--script', default='bangla', help=f'Script: {get_available_scripts()}')
@click.option('--font_size', default=48, help='Font size for the text')
@click.option('--font_path', default="", help='Path to font file (empty for random)')
@click.option('--font_dir', default="fonts", help='Base font directory')
@click.option('--background_path', default="", help='Path to background image (empty for random)')
@click.option('--angle', default=0, help='Skew angle in degrees')
@click.option('--bars', default=True, type=click.BOOL, help='Add bars')
@click.option('--add_random_text', default=True, type=click.BOOL, help='Add random text')
@click.option('--add_boxes', default=True, type=click.BOOL, help='Add boxes')
@click.option('--add_curves', default=False, type=click.BOOL, help='Apply curves')
@click.option('--apply_data_augmentation', default=True, type=click.BOOL, help='Apply augmentation')
@click.option('--white_background', default=True, type=click.BOOL, help='Use white background')
@click.option('--output_path', default="generated_image.png", help='Output path')
def generate_text_image(text, script, font_size, font_path, font_dir, background_path,
                        angle, bars, add_random_text, add_boxes, add_curves,
                        apply_data_augmentation, white_background, output_path):
    print(f"Script: {script}")
    print(f"Text: {text}")
    scribe = GlyphScribe(base_fonts_dir=font_dir, script=script)
    return scribe.generate(text, font_size, font_path, background_path, angle, bars,
                           add_random_text, add_boxes, add_curves,
                           apply_data_augmentation, white_background, output_path)

if __name__ == '__main__':
    generate_text_image()