import matplotlib.pyplot as plt
import numpy as np
import csv

from random import random

### Unused bar graph display due to time restrictions

# def draw_bar_graph(companies: np.ndarray,
#                    frequencyArr: np.ndarray):
#     '''
#     Draws the bar graph visual, note that it does NOT display a figure. You can
#        add the "show()" method to a desired line for display.
#     '''
#     if len(companies) is not len(frequencyArr):
#         raise Exception()
#
#     for p, f in zip(companies, frequencyArr):
#         rgb = [random(), random(), random()]
#         plt.bar(p, f, color=rgb)


def draw_companies_pie_and_legend(companies: np.ndarray,
                                  frequencyArr: np.ndarray):
    '''
    Draws the pie chart visual, note that it does NOT display a figure. You can
       add the "show()" method to a desired line for display.
    '''
    fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))
    fig.canvas.set_window_title('Summary Statistics on Scraped Data')

    patches,_,autotexts = plt.pie(frequencyArr,
                        startangle=90,
                        shadow=False,
                        radius=1.3,
                        autopct=lambda pct: slice_display(pct, frequencyArr))

    #percent = 100*frequencyArr/frequencyArr.sum()
    #labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(companies, percent)]

    # Draw legend with colors and companies in mind
    plt.legend(patches,
               companies,
               loc='center left',
               fontsize=8,
               bbox_to_anchor=(1.1, 0, 0.5, 1))
    ax.set_title("Sample of the Number of Software-Related Job Openings by Company\n"\
                "On Monster.com\n")


def slice_display(pct, allVals):
    '''
    Used in the pie chart to print out the percentage and # of jobs that are
       available.
    '''
    absolute = int(pct/100.*np.sum(allVals))
    return "{:.1f}%\n({:d} jobs)".format(pct, absolute)


def show_summary(companies: np.ndarray,
                 frequencyArr: np.ndarray):
    '''
    Draws and displays visuals, within the same figure
    '''
    draw_companies_pie_and_legend(companies, frequencyArr)
    plt.show()


def main():
    companyDict = {}
    with open('Scrapper_Data.csv', newline = '') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        for row in dataReader:
            if row[1] not in companyDict.keys():
                companyDict[row[1]] = 1
            else:
                companyDict[row[1]] += 1
    # Removes companies with just one job posting
    for company in list(companyDict.keys()):
        if companyDict[company] == 1:
            companyDict.pop(company)

    show_summary(companyDict.keys(), np.array(list(companyDict.values())) )

if __name__ == "__main__":
    main()
