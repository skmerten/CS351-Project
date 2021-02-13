import matplotlib.pyplot as plt
import numpy as np

from random import random

def draw_bar_graph(progLang: np.ndarray,
                   frequencyArr: np.ndarray):
    '''
    Draws the bar graph visual, note that it does NOT display a figure. You can
       add the "show()" method to a desired line for display.
    '''
    if len(progLang) is not len(frequencyArr):
        raise Exception()

    for p, f in zip(progLang, frequencyArr):
        rgb = [random(), random(), random()]
        plt.bar(p, f, color=rgb)


def draw_pie_charts(progLang: np.ndarray,
                    frequencyArr: np.ndarray):
    '''
    Draws the pie chart visual, note that it does NOT display a figure. You can
       add the "show()" method to a desired line for display.
    '''
    patches,_ = plt.pie(frequencyArr, startangle=90, shadow=True, radius=1.3)
    porcent = 100*frequencyArr/frequencyArr.sum()
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(progLang, porcent)]

    plt.legend(patches, labels, loc='center',fontsize=8,
               bbox_to_anchor=(0.15, 0.,0.65, -0.5))


def show_summary(progLang: np.ndarray,
                 frequencyArr: np.ndarray):
    '''
    Draws and displays visuals, within the same figure
    '''
    plt.subplot(1,2,1)
    draw_bar_graph(progLang, frequencyArr)
    plt.subplot(1,2,2)
    draw_pie_charts(progLang, frequencyArr)
    plt.show()

show_summary(["Java", "C++", "A", "B", "C"], np.array([230, 55, 1,2,3]))
