import os
import fitz
from pdf2image import convert_from_path
from tqdm import tqdm


def pdf_to_image(pdf_file, output_folder=None, image_format='png', dpi=600):
    if output_folder is None:
        output_folder = os.path.splitext(pdf_file)[0]
    os.makedirs(output_folder, exist_ok=True)

    # extract pdf pages and convert to image
    pdf = fitz.open(pdf_file)
    for i, page in tqdm(enumerate(pdf), total=len(pdf), desc='Converting PDF to image'):
        pixel_map = page.get_pixmap(dpi=dpi, alpha=False)
        pixel_map.save(os.path.join(output_folder, '{}.{}'.format(str(i), image_format)))
    pdf.close()


def pdf2pil(pdf_file, dpi=600):
    return convert_from_path(pdf_file, dpi=dpi)
