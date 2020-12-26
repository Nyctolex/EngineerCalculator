import os
import pandas as pd
import labFormat
import lab_calculator

#OUT_FOLDER = r"C:\Users\chris-chen\Documents\TAU\Year B\Semester A\lab\דוחות\חיכוך ואנרגיה\output"
_OUT_FOLDER = r"C:\Users\chris-chen\Documents\TAU\Year B\Semester A\lab\דוחות\צמיגות\output"
_KEYWORDS_FILTER = []
#Filtering wanted folders out of th main plot folder

class folder_scanner():
    def __init__(self, main_folder, keyword_filter = []):
        self.head_folder = main_folder
        self.keyword_filter = keyword_filter
        self.folders_lst = []
        self.load_folders()
        self.plot_files = []
        self.load_plot_files()
        self.df = None

    @staticmethod
    def get_p(lines):
        """
        Get a p_propability value from a plot txt file.
        """
        for line in lines:
            if "probability" in line:
                p = float(line.split(" ")[1].strip("\n"))
                p = lab_calculator.lab_round(p)
                return p

    @staticmethod
    def get_chi(lines):
        """
        Get a chi reduced value from a plot txt file.
        """
        for line in lines:
            if "Chi squared reduced:" in line:
                chi = float(line.split(" ")[3].strip("\n"))
                chi = lab_calculator.lab_round(chi)
                return chi

    @staticmethod
    def get_a(lines, no, er = None):
        """
        Getting a specified a value.
        """
        for line in lines:
            if "a[{0}]".format(no) in line:
                a = float(line.split(" ")[2].strip("\n"))
                if er != None:
                    a = lab_calculator.lab_round(a, er)
                return a

    @staticmethod
    def get_d(lines, no):
        """
        Getting error of specified a value. 
        """
        for line in lines:
            if "a[{0}]".format(no) in line:
                d = float(line.split(" ")[4].strip("\n"))
                d = lab_calculator.lab_round(d)
                return d

    @staticmethod
    def filter_folders(folder_lst ,key_words, inclue=True):
        """
        Include detectes if the keywords-filter should be included or not.
        """
        folder_lst_cpy =  folder_lst.copy()
        filtered_list =  folder_lst.copy()
        for folder_name in folder_lst_cpy:
            for key_word in key_words:
                if ((key_word in folder_name) != inclue):
                    filtered_list.remove(folder_name)
        return filtered_list

    def load_folders(self):
        folders_lst = os.listdir(self.head_folder)
        self.folders_lst = self.filter_folders(folders_lst, self.keyword_filter)
        return folders_lst

    @staticmethod
    def get_txt_name(folder_name):
        """
        Getting only the relevant txt files.
        """
        files = os.listdir(folder_name)
        for file_name in files:
            if "txt" in file_name:
                return file_name

    def load_plot_files(self, txt_file=None):
        plots = []
        for sub_folder in self.folders_lst:
            if ("." not in sub_folder):
                if txt_file == None:
                    path = self.head_folder + "\\" + sub_folder + "\\" + self.get_txt_name(self.head_folder + "\\" + sub_folder)
                else:
                    path = self.head_folder + "\\" + sub_folder + "\\" + txt_file
                with open(path, 'r') as fitting:
                    lines = fitting.readlines()
                    plots.append(lines)
        self.plot_files = plots
        return plots

    def load_p(self, txt_file=None):
        """
        Loading all p-propability values in destination folders.
        """
        p_lst = []
        for plot in self.plot_files:
            p_lst.append(self.get_p(plot))
        return p_lst

    def load_chi(self):
        """
        Loading all chi-reduced values in destination folders.
        """
        chi_lst = []
        for plot in self.plot_files:
            chi_lst.append(self.get_chi(plot))
        return chi_lst

    def load_d(self, no):
        """
        Loading all error values in destination folders.
        """
        d_lst = []
        for plot in self.plot_files:
            d_lst.append(self.get_d(plot, no))
        return d_lst

    def load_a(self, no):
        """
        Loading all a[no] values in destination folders.
        """
        a_lst = []
        for plot in self.plot_files:
            d = self.get_d(plot, no)
            a_lst.append(self.get_a(plot, no, d))
        return a_lst
    
    @staticmethod
    def val_plus_minus_error_string(val, er):
        er = lab_calculator.lab_round(er)
        val = lab_calculator.lab_round(val, er)
        res_format = "{val} +- {er}".format(val=val, er=er)
        return(res_format)

    def plot_to_table(self, no, rel_er_lst=[], file_display=False):
        """
        Copies wanted data to clipboard in a format of a table. no is for the maximum a[number] to calculate. rel_er_lst is a list
        of nubers that the table should yield a relative error for them as well.
        """
        data = {"file": self.folders_lst}

        for n in range(no+1):
            all_a = self.load_a(n).copy()
            all_d = self.load_d(n).copy()
            a_d_title = "a_{num} +- Δa_{num}".format(num=n)
            relative_error_title = "a_({num} relative error)".format(num=n)
            all_a_d = []
            all_relative_errors = []
            for i in range(len(all_a)):
                all_a_d.append(self.val_plus_minus_error_string(all_a[i], all_d[i]))
                if n in rel_er_lst:
                    all_relative_errors.append(str(lab_calculator.relative_error(all_a[i], all_d[i])) + "%")
            data[a_d_title] = all_a_d
            if n in rel_er_lst:
                data[relative_error_title] = all_relative_errors
        data["χ_red^2"] = self.load_chi()
        data["P_probability"] = self.load_p()
        df =pd.DataFrame(data)
        if not file_display:
            data.pop("file")
            df =pd.DataFrame(data)
        self.df = df
        df.to_clipboard(index=False)
        return df
    
    @staticmethod
    def get_max_a_in_plot(plot):
        no = 0
        for line in plot:
            while("a[{0}]".format(no+1) in line):
                no += 1
        return no

if __name__ == "__main__":
    pass