import pandas as pd
import glob
import os

class Reader:

    def readCS(self):

        path = '/Users/keller/PycharmProjects/gradeDistribution/data/'
        allFiles = glob.glob(os.path.join(path, 'cs/*.csv'))
        df_from_each_file = (pd.read_csv(f,  usecols=["course_number_1", "course_title", "faculty", "course_ei",
                                                      "credit_hours", "qca", "number", "As", "Bs", "Cs", "Ds", "Fs",
                                                      "Textbox10"], header=0) for f in allFiles)

        concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
        concatenated_df.columns =["Course ID", "Title", "Professor", "CRN", "Credits", "GPA", "Students", "A%", "B%", "C%", "D%", "F%", "Withdrawals"]



        grouped = concatenated_df.groupby(['Course ID', 'Title', 'Professor'])
        classes_taught = concatenated_df.groupby(['Course ID', 'Title', 'Professor']).size()
        average = grouped[['GPA', 'A%', 'B%', 'C%', 'D%', 'F%']].mean()
        average = average.applymap("{0:.2f}".format)
        average['Withdrawals'] = grouped[['Withdrawals']].sum()
        average['# of Classes'] = classes_taught
        average.to_html('/Users/keller/PycharmProjects/gradeDistribution/templates/cstemplate.html', classes='CS')

    def readAero(self):
        path = '/Users/keller/PycharmProjects/gradeDistribution/data'
        allFiles = glob.glob(os.path.join(path, 'aero/*.csv'))
        df_from_each_file = (pd.read_csv(f, usecols=["course_number_1", "course_title", "faculty", "course_ei",
                                                     "credit_hours", "qca", "number", "As", "Bs", "Cs", "Ds", "Fs",
                                                     "Textbox10"], header=0) for f in allFiles)

        concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
        concatenated_df.columns = ["Course ID", "Title", "Professor", "CRN", "Credits", "GPA", "Students", "A%", "B%",
                                   "C%", "D%", "F%", "Withdrawals"]

        grouped = concatenated_df.groupby(['Course ID', 'Title', 'Professor'])
        classes_taught = concatenated_df.groupby(['Course ID', 'Title', 'Professor']).size()
        average = grouped[['GPA', 'A%', 'B%', 'C%', 'D%', 'F%']].mean()
        average = average.applymap("{0:.2f}".format)
        average['Withdrawals'] = grouped[['Withdrawals']].sum()
        average['# of Classes'] = classes_taught
        average.to_html('/Users/keller/PycharmProjects/gradeDistribution/templates/aerotemplate.html', classes='aero')

    def readECE(self):
        path = '/Users/keller/PycharmProjects/gradeDistribution/data'
        allFiles = glob.glob(os.path.join(path, 'ece/*.csv'))
        df_from_each_file = (pd.read_csv(f, usecols=["course_number_1", "course_title", "faculty", "course_ei",
                                                     "credit_hours", "qca", "number", "As", "Bs", "Cs", "Ds", "Fs",
                                                     "Textbox10"], header=0) for f in allFiles)

        concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
        concatenated_df.columns = ["Course ID", "Title", "Professor", "CRN", "Credits", "GPA", "Students", "A%", "B%",
                                   "C%", "D%", "F%", "Withdrawals"]

        grouped = concatenated_df.groupby(['Course ID', 'Title', 'Professor'])
        classes_taught = concatenated_df.groupby(['Course ID', 'Title', 'Professor']).size()
        average = grouped[['GPA', 'A%', 'B%', 'C%', 'D%', 'F%']].mean()
        average = average.applymap("{0:.2f}".format)
        average['Withdrawals'] = grouped[['Withdrawals']].sum()
        average['# of Classes'] = classes_taught
        average.to_html('/Users/keller/PycharmProjects/gradeDistribution/templates/ecetemplate.html', classes='ECE')

def main():
    x = Reader()
    x.readCS()
    x.readAero()
    x.readECE()

if __name__ == '__main__':
    main()