import files
import ege2
from ege2 import poisk

def main():
    files.json_exams('json/exams_new', ege2.regular(poisk, files.htmlpage()))
    d = ege2.sravnenie(files.json_load('json/exams_old'), files.json_load('json/exams_new'))
    ege2.vk_id(d, 'json/students')
    n = files.json_load('json/exams_new')
    files.json_save('json/exams_old', n)

main()
