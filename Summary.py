import matplotlib.pyplot as plt
import numpy as np
import csv

from random import random
'''
def draw_bar_graph(progLang: np.ndarray,
                   frequencyArr: np.ndarray):
    
    Draws the bar graph visual, note that it does NOT display a figure. You can
       add the "show()" method to a desired line for display.
    
    if len(progLang) is not len(frequencyArr):
        raise Exception()

    for p, f in zip(progLang, frequencyArr):
        rgb = [random(), random(), random()]
        plt.bar(p, f, color=rgb)
'''



def draw_pie_charts(progLang: np.ndarray,
                    frequencyArr: np.ndarray):
    '''
    Draws the pie chart visual, note that it does NOT display a figure. You can
       add the "show()" method to a desired line for display.
    '''
    patches,_ = plt.pie(frequencyArr, startangle=90, shadow=True, radius=1.3)
    porcent = 100*frequencyArr/frequencyArr.sum()
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(progLang, porcent)]
    return patches, labels
    
def draw_pie_chart_legend(patches, labels):
    plt.legend(patches, labels, loc='center',fontsize=8,
        bbox_to_anchor=(0.15, 0.,0.65, -0.5))



def show_summary(progLang: np.ndarray,
                 frequencyArr: np.ndarray):
    '''
    Draws and displays visuals, within the same figure
    '''
    plt.subplot(1,2,1)
    patches, labels = draw_pie_charts(progLang, frequencyArr)
    plt.subplot(1,2,2)
    draw_pie_chart_legend(patches, labels)
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
    for company in list(companyDict.keys()):
        if companyDict[company] == 1:
            companyDict.pop(company)

    show_summary(list(companyDict.keys()), np.array(list(companyDict.values())))

if __name__ == "__main__":
    main()