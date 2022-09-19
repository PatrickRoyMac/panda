import tempfile
import glob
import argparse
from os.path import join, basename
from shutil import copyfile
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode

def panda(input_folder, output_folder):
    for file in glob.glob(join(input_folder, '*.pdf')):
        # convert pdf file to png
        # scan the image
        file_name = basename(file)
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(file, output_folder=path)
            for image in images_from_path:
                decoded = decode(image)
                for d in decoded:
                    print(file_name, d.type, d.data.decode("utf-8"))
                    new_filename=(d.data.decode("utf-8"))
                    new_name = '{}.pdf'.format(new_filename)
                    copyfile(file, join(output_folder, new_name))
                    
def get_args():
    parser = argparse.ArgumentParser(description='Scan pdfs and rename them according to '
                                                 'data in barcodes they contain.'
                                                 '\nTested on python 3.6.'
                                                 '\nRequirements: pip install pdf2image pyzbar pdf2image')
    parser.add_argument('-i', '--input_folder', required=True, help='Where all pdf files take place.')
    parser.add_argument('-o', '--output_folder', required=True, help='Where to copy new renamed pdf files.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    # python panda.py -i 'C:\Users\patpa\Documents\Coding\panda\pdfs' -o 'C:\Users\patpa\Documents\Coding\panda\output'
    args = get_args()
    panda(args.input_folder, args.output_folder)