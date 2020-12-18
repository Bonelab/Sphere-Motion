import os
import datetime
import shutil

# Directory structure
date = str(datetime.date.today())
base_directory = os.path.abspath(os.path.join('..', '..'))
figure_directory = os.path.join(base_directory, 'Figures')
this_directory = os.path.abspath('.')
output_directory = os.path.join(this_directory, date)
output_figures_directory = os.path.join(output_directory, 'Figures')

# Figure files
figure_files = [
    'W.pdf',
    'advection.pdf',
    'loss.pdf',
    'mean.pdf',
    'solution_1.pdf',
    'solution_2.pdf',
    'solution_3.pdf',
    'model.py',
]

# LaTeX Files
latex_files = [
    'sphere.tex',
    'sphere.bib',
    'IEEEtran.cls',
    'sphere.bbl',
]

def create_output_directory():
    # Create output directory
    if os.path.isdir(output_directory):
        os.sys.exit('Output directory {} already exists. Exiting...'.format(output_directory))
    os.mkdir(output_directory)

    # Create output figures directory
    os.mkdir(output_figures_directory)

def copy_latex_files():
    for filename in latex_files:
        src = os.path.join(base_directory, filename)
        dst = os.path.join(output_directory, filename)
        shutil.copyfile(src, dst)

def copy_figures():
    for filename in figure_files:
        src = os.path.join(figure_directory, filename)
        dst = os.path.join(output_figures_directory, filename)
        shutil.copyfile(src, dst)

def main():
    create_output_directory()
    copy_latex_files()
    copy_figures()

if __name__ == '__main__':
    main()
