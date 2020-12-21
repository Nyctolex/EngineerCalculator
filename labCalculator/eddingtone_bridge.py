import os

OUT_FOLDER = r"C:\Users\chris-chen\Documents\TAU\Year B\Semester A\lab\דוחות\צמיגות\output"
def get_p(lines):
    """
    Get a p_propability value from a plot txt file.
    """
    for line in lines:
        if "probability" in line:
            p = float(line.split(" ")[1].strip("\n"))
            p = labFormat.lab_round(p)
            return p

def get_chi(lines):
    """
    Get a chi reduced value from a plot txt file.
    """
    for line in lines:
        if "Chi squared reduced:" in line:
            chi = float(line.split(" ")[3].strip("\n"))
            chi = labFormat.lab_round(chi)
            return chi

def get_a(lines, no, er = None):
    """
    Getting a specified a value.
    """
    for line in lines:
        if "a[{0}]".format(no) in line:
            a = float(line.split(" ")[2].strip("\n"))
            if er != None:
                a = labFormat.lab_round(a, er)
            return a

def get_d(lines, no):
    """
    Getting error of specified a value. 
    """
    for line in lines:
        if "a[{0}]".format(no) in line:
            d = float(line.split(" ")[4].strip("\n"))
            d = labFormat.lab_round(d)
            return d

def filter_folders(folder_lst ,key_words, inclue=True):
    """
    Include detectes if the keywords-filter should be included or not.
    """
    folder_lst_cpy =  folder_lst.copy()
    for folder_name in folder_lst_cpy:
        for key_word in key_words:
            if ((key_word in folder_name) != inclue):
                folder_lst.remove(folder_name)

def load_folders(head_folder=OUT_FOLDER):
    folders_lst = os.listdir(head_folder)
    filter_folders(folders_lst, KEYWORDS_FILTER)
    return folders_lst

def get_txt_name(folder_name):
    """
    Getting only the relevant txt files.
    """
    files = os.listdir(folder_name)
    for file_name in files:
        if "txt" in file_name:
            return file_name

def load_plot_files(head_folder=OUT_FOLDER, txt_file=None):
    folders_lst = load_folders(head_folder)
    plots = []
    for sub_folder in folders_lst:
        if txt_file == None:
            path = head_folder + "\\" + sub_folder + "\\" + get_txt_name(head_folder + "\\" + sub_folder)
        else:
            path = head_folder + "\\" + sub_folder + "\\" + txt_file
        with open(path, 'r') as fitting:
            lines = fitting.readlines()
            plots.append(lines)
    return plots

def load_p(head_folder=OUT_FOLDER, txt_file=None):
    """
    Loading all p-propability values in destination folders.
    """
    p_lst = []
    plots = load_plot_files(head_folder, txt_file)
    for plot in plots:
        p_lst.append(get_p(plot))
    return p_lst

def load_chi(head_folder=OUT_FOLDER, txt_file=None):
    """
    Loading all chi-reduced values in destination folders.
    """
    chi_lst = []
    plots = load_plot_files(head_folder, txt_file)
    for plot in plots:
        chi_lst.append(get_chi(plot))
    return chi_lst

def load_d(no, head_folder=OUT_FOLDER, txt_file=None):
    """
    Loading all error values in destination folders.
    """
    d_lst = []
    plots = load_plot_files(head_folder, txt_file)
    for plot in plots:
        d_lst.append(get_d(plot, no))
    return d_lst

def load_a(no, head_folder=OUT_FOLDER, txt_file=None):
    """
    Loading all a[no] values in destination folders.
    """
    a_lst = []
    plots = load_plot_files(head_folder, txt_file)
    for plot in plots:
        d = get_d(plot, no)
        a_lst.append(get_a(plot, no, d))
    return a_lst