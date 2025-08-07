from pypdf import PdfReader, PdfWriter
from argparse import ArgumentParser
from os.path import splitext

def add_watermark(target_files, wtrm_file, in_place=False):
    f = None

    try:
        for f in target_files:
            with open(f, 'rb'):
                pass
        with open(wtrm_file, 'rb') as f:
            pass
    except IOError as e:
         raise ValueError(f"Exception occured when opening file: \"{f}\" - {e}")

    wtrm = PdfReader(wtrm_file).pages[0]

    for f in target_files:
        writer = PdfWriter(clone_from=f)
        for page in writer.pages:
            page.merge_page(wtrm, over=False)

        writer.write(f if in_place else splitext(f)[0] + '-wtrm.pdf')

if __name__ == '__main__':
    parser = ArgumentParser(description='Goes over pdf files and marks with a provided watermark')
    parser.add_argument('pdf_files', nargs='+', type=str, help='Paths of pdf files to watermark')
    parser.add_argument('-w', '--watermark', dest='watermark_file', required=True, type=str, help='Path to the watermark pdf file')
    parser.add_argument('--in-place', action='store_true', dest='in_place', help='Overwrite original files')

    args = parser.parse_args()
    try:
        add_watermark(args.pdf_files, args.watermark_file, args.in_place)
    except ValueError as e:
        print(f"Error: {e}")