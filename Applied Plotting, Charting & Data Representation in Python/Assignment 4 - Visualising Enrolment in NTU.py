%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import matplotlib.gridspec as gridspec



df = pd.read_csv("ntu data.csv")
programmes = df["Programme"].tolist()
df= df.set_index("Programme")
old_cols = df.columns.tolist()
new_cols = [old_col[:4] for old_col in old_cols]
df.columns = pd.to_datetime(new_cols).year
Engineering = ['Aerospace Engineering','Aerospace Engineering and Economics*', 'Business & Computer Engineering*', 'BioEngineering','BioEngineering and Economics*','Chemical & Biomolecular Engineering'
              ,'Computer Engineering','Computer Engineering & Economics*','Electrical & Electronic Engineering',
              'Electrical & Electronic Engineering and Economics*','Engineering','Information Engineering & Media',
              'Information Engineering & Media and Economics*','Materials Engineering','Materials Engineering and Economics*',
              'Mechanical Engineering','Mechanical Engineering and Economics*','Renaissance Engineering']
Science = ['Business & Computing','Biomedical Sciences^', 'Biomedical Sciences and BioBusiness^', 'Biological Sciences',
           'Biological Sciences and Psychology^','Data Science and Artificial Intelligence','Computer Science',
          'Computer Science and Economics*','Environmental Earth Systems Science',
          'Environmental Earth Systems Science and Public Policy & Global Affairs^','Mathematics & Economics^',
          'Mathematical and Computer Sciences^','Mathematical Sciences','Mathematical Sciences and Economics^',
          'Physics & Applied Physics','Sport Science & Management']
Business = ['Accountancy', 'Accountancy and Business*', 'Business & Computer Engineering*', 'Business & Computing', 'Biomedical Sciences and BioBusiness^','Business' ]
Arts = ['Art Design & Media','Aerospace Engineering and Economics*','BioEngineering and Economics*',
        'Biological Sciences and Psychology^','Chinese','Communication Studies','Computer Engineering & Economics*',
       'Computer Science and Economics*','Economics','Economics and Media Analytics^','Economics and Psychology^',
       'Economics and Public Policy & Global Affairs^','Electrical & Electronic Engineering and Economics*',
       'History','English','English Literature and Art History^','Environmental Earth Systems Science and Public Policy & Global Affairs^',
       'Information Engineering & Media','Information Engineering & Media and Economics*','Linguistics & Multilingual Studies',
       'Mathematics & Economics^','Maritime Studies','Mathematical Sciences and Economics^','Materials Engineering and Economics*',
       'Mechanical Engineering and Economics*','Philosophy','Psychology','Psychology and Linguistics & Multilingual Studies^',
       'Psychology and Media Analytics^','Public Policy and Global Affairs','Sociology']
Education =['Arts(Ed)', 'Science(Ed)', 'Education']
Medicine = ['Medicine']
##getting programme totals
df.loc["Engineering Total"] = df.loc[Engineering].sum(axis = 0)
df.loc["Science Total"] = df.loc[Science].sum(axis = 0)
df.loc["Business Total"] = df.loc[Business].sum(axis = 0)
df.loc["Arts Total"] = df.loc[Arts].sum(axis = 0)
df.loc["Education Total"] = df.loc[Education].sum(axis = 0)
df.loc["Medicine Total"] = df.loc[Medicine].sum(axis = 0)
engineering_df = df.loc[Engineering + ["Engineering Total"]]
## keeping relevant data for analysis
df = df.iloc[-6:-1]
df.loc["Adjusted Total"] = df.sum(axis = 0)
#df_scaled = df.apply(lambda column: column/column.max(), axis = 0)
df= df.transpose()
#df_scaled = df_scaled.transpose()
to_drop = []
for i in range(len(engineering_df)-1):
    if engineering_df.iloc[i].name in engineering_df.iloc[i+1].name and engineering_df.iloc[i].name != "Engineering":
        engineering_df.iloc[i] = engineering_df.iloc[i] + engineering_df.iloc[i+1]
        to_drop.append(engineering_df.iloc[i+1].name)
to_drop.append("Business & Computer Engineering*")
engineering_df.loc["Computer Engineering"] += engineering_df.loc["Business & Computer Engineering*"]
engineering_df.drop(to_drop, inplace=True)
engineering_df = engineering_df.transpose()
#plt.figure(figsize=(10,10))
#gspec = gridspec.GridSpec(2, 2)
#enrolment_totals = plt.subplot(gspec[0, 0:])
#enrolment_engine = plt.subplot(gspec[1, 0:])
#enrolment_totals.plot(df.index,df)
#enrolment_engine.plot(engineering_df.index,engineering_df)
fig, axes = plt.subplots(nrows=2, ncols=1)
fig.set_size_inches(10, 10)
fig.subplots_adjust(right=0.64)
enrolment_totals = df.plot.line(ax = axes[0])
enrolment_totals.legend(loc='best', bbox_to_anchor=(1.0, 0.5))
enrolment_totals.set_title("Undergraduate Enrolment in NTU with Year (All Faculties)",  weight = "bold")
#for xtick in plt.gca().get_xticklabels():
#        xtick.set_visible(False)
enrolment_engine = engineering_df.plot.line(ax = axes[1])
enrolment_engine.legend(loc='best', bbox_to_anchor=(1.0, 0.5))
enrolment_engine.set_title("Undergraduate Enrolment in NTU with Year (Engineering Faculty)",  weight = "bold")
#df_scaled.plot.line(ax = axes[0,1])
fig.text(0.4, 0.04, 'Year', ha='center', va='center', fontsize = 16, weight = "bold")
fig.text(0.04, 0.5, 'Number of Undergraduates', ha='center', va='center', rotation='vertical', fontsize = 16, weight = "bold")
for axis in axes:
    axis.set_xticks(df.index)
#plt.gcf().axes[0].get_lines()[4].set_color("r")