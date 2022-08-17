# -*- coding: utf-8 -*-
# @Author: Anyes Taffard
# @Date:   2022-07-11 13:35:29
# @Last Modified by:   Anyes Taffard
# @Last Modified time: 2022-07-22 09:45:23
import time 
import ROOT
import os
import math


from sampletools import get_samples
from sampletools import get_rootfiles
from sampletools import get_trees

from plotstyletools import set_plot_style
from plotstyletools import set_sample_style 

from variabletools import get_variables
from regiontools import get_regionSelections

from plotstyletools import createCanvas
from plotstyletools import createHistogramPad
from plotstyletools import createRatioPad

from histogramtools import get_sample_stack
from histogramtools import fill_sample_stack

from histogramtools import postprocess_stack

from drawingtools import drawXandYlabels
from drawingtools import getYlabel
from drawingtools import drawRatioPlot

from plotstyletools import get_plotlabel_atlas
from plotstyletools import get_plotlabel_centreofmassenergy
from plotstyletools import get_plotlabel_regioninformation
from plotstyletools import get_plotlabel_topleft
from plotstyletools import get_plotlabel_topright

def get_parser():
    """
    get_parser handles all parser information

    Any new command line options should be added here.

    Returns:
        args (argparse.ArgumentParser): returns all runtime options. 
    """
    import argparse
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--output', '-o', type=str, default="rootpyoutput", \
                        help='Provide a location for output of Plots')
    parser.add_argument('--region', '-r', type=str, default ="preselection", \
                        help='Specify which Region you wish to run over'  )



    args = parser.parse_args()
    return args


def main():
    """
    main We retreive the samples, the rootfiles, the trees and the variables.
    For each variable, we retreive the number of bins, the minimum x and maximum x 
    range, the x label and the y label for that vairbale 
    We create a TCanvas, and two TPads. 
    We then create a stack which will contain all histograms for all our samples 
    For each sample we wish to plot, we create a label (unique for ROOT purposes)
    We then define a selection to apply to the data and monte carlo. 
    We then draw this output into a histogram we call temphist 
    we then process this stack 
    We order the stack, we then plot the backgrounds, the error bands, and the data 
    We draw the labels, overlaying lines in the ratio plot, and the legends 
    Finally we plot information such as ATLAS internal. 

    Then we save it in some directory 

    #      NOTE: this function is not complete. and you can add functionality 
    # to output plots into subfolders, so that you don't override them. 
    I recommend using the --region argument to do this. 

    Returns: None 
    """
    
    set_plot_style()

    t0 = time.time()
    args = get_parser()
    samples = get_samples()
    rootfiles = get_rootfiles(samples)
    trees = get_trees(rootfiles)
    variables = get_variables()
    #n=0
    for variable in variables:
        print(variable)

        name      = variables[variable]['name']
        units     = variables[variable]['units']
        nbins     = int(variables[variable]['nbins'])
        xmin      = float(variables[variable]['xmin'])
        xmax      = float(variables[variable]['xmax'])
        xlabel    = variables[variable]['latex']
        ylabel    = getYlabel(units,nbins,xmin,xmax)

        canvas    = createCanvas(variable)
        histpad   = createHistogramPad(variable)
        ratiopad  = createRatioPad(variable)

        histpad.cd()

        stack     = get_sample_stack(samples)
        stack     = fill_sample_stack(variable,trees,stack,samples,nbins,xmin,xmax)
        #stack     = process_sample_stack(stack)

        processedstacks, breakdowns = postprocess_stack(stack)
        backgrounds         = processedstacks['background']
        data                = processedstacks['data']
        signals             = processedstacks['signal']
        

        backgrounds = create_under_and_overflow_bins(backgrounds,nbins)
        backgrounds = sort_backgrounds_by_integral(backgrounds)

        histpad.cd()

        # get the errorband, totalbackground and data 
        errorband = get_errorband(backgrounds)
        total_background = get_totalbackground(backgrounds)
        total_data = get_totaldata(data)

        # change your style for the errorband, totalbackground and data 
        errorband = style_errorband(errorband)
        total_background = style_totalbackground(total_background)
        total_data = style_totaldata(total_data)

        yminimum,ymaximum = 1e-1,1e8
        #yminimum, ymaximum = plotlabels.RegionYrange(Region)
        backgrounds.SetMinimum(yminimum)
        backgrounds.SetMaximum(ymaximum)

        backgrounds.Draw("HIST")
        errorband.Draw("E2P SAME")
        total_background.Draw("HIST SAME")
        total_data.Draw("SAME EP")

        drawXandYlabels(backgrounds,data,xlabel,ylabel,histpad,ratiopad)
        ylabel = getYlabel(units,nbins,xmin,xmax)
        total_background.GetYaxis().SetTitle(ylabel)
        #for signal in signals:
        #    signal.Draw("Hist SAME X0")

        ratiopad.cd()

        ratioplot,average = drawRatioPlot(data,backgrounds)

        ratioplot_agreementline = get_ratioplot_agreementline(xmin,xmax)
        ratioplot_averageline = get_ratioplot_averageline(xmin,xmax,average)

        ratioplot.Draw("SAME")
        ratioplot_agreementline.Draw("SAME")
        ratioplot_averageline.Draw("SAME")

        #ratioplot.GetYaxis().SetTitle("Data/SM")
        ratioplot.GetYaxis().CenterTitle()
        #ratioplot.GetXaxis().SetTitle(xlabel)
        histpad.cd()

        data_and_sm_legend = create_data_sm_legend(breakdowns)
        background_and_signal_legend = create_background_and_signal_legend(breakdowns)#, n)
        #n=1

        data_and_sm_legend.Draw("SAME")
        background_and_signal_legend.Draw("SAME")

        plotlabel_com = get_plotlabel_centreofmassenergy()
        plotlabel_atlas = get_plotlabel_atlas("Internal")
        plotlabel_topright = get_plotlabel_topright("#lower[0.4]{Rel21:Data1516}")
        plotlabel_regioninformation = get_plotlabel_regioninformation()
        #plotlabel_topleft = plotlabel_topleft("No under or overflow included")

        plotlabel_com.Draw("SAME")
        plotlabel_atlas.Draw("SAME")       
        plotlabel_topright.Draw("SAME")
        plotlabel_regioninformation.Draw("SAME")
        #plotlabel_topleft.Draw("SAME")

        canvas.cd()

        #filenamevariable = variable.replace("/","_").replace("_1000","")
        filenamevariable = name

        if not os.path.exists(args.output):
            os.makedirs(args.output)
        canvas.Print(args.output + "/"+ filenamevariable+ "_" + args.region + ".pdf")


    return None 




def get_errorband(backgrounds):
    import ROOT 
    errorband = backgrounds.GetStack().Last().Clone()
    return errorband

def style_errorband(errorband):
    import ROOT 
    errorband.SetMarkerSize(0)
    errorband.SetLineColor(ROOT.kBlack)
    errorband.SetFillStyle(3344)
    errorband.SetFillColor(ROOT.kBlack)
    return errorband



def get_totalbackground(backgrounds):
    import ROOT
    total_background = backgrounds.GetStack().Last().Clone()
    return total_background

def style_totalbackground(total_background):
    import ROOT
    total_background.SetFillStyle(0)
    total_background.SetLineColor(ROOT.kBlack)
    total_background.SetLineWidth(2)
    total_background.SetMarkerSize(0)
    total_background.GetYaxis().SetTitleOffset(2)
    total_background.GetYaxis().SetTitleSize(30) 
    return total_background



def get_totaldata(data):
    import ROOT
    tempdata = data.GetStack().Last().Clone()
    return tempdata

def style_totaldata(total_data):
    import ROOT
    total_data.SetMarkerStyle(20)
    total_data.SetMarkerSize(1)
    total_data.SetLineColor(ROOT.kBlack)
    total_data.SetLineWidth(2)
    return total_data

def create_under_and_overflow_bins(backgrounds,nbins):

    for hist in backgrounds:
        hist.SetBinContent(1,hist.GetBinContent(0)+hist.GetBinContent(1))
        hist.SetBinContent(nbins,hist.GetBinContent(nbins)+hist.GetBinContent(nbins+1))
    return backgrounds

def sort_backgrounds_by_integral(backgrounds):


    info = []
    for hist in backgrounds:

        info.append([hist.Clone(),hist.Integral() ])
        return backgrounds
    backgrounds = ROOT.THStack()


    for histogram,entries in sorted(info, key=lambda tup: tup[1]):
        backgrounds.Add(histogram)

        return backgrounds



    return backgrounds


        




def create_data_sm_legend(breakdowns):
    
    args = get_parser()

    data_and_sm_legend = ROOT.TLegend(0.55, 0.75, 0.7, 0.9)#xmin,ymin,xmax,ymax)
    data_and_sm_legend.SetLineColor(0)

    backgroundbreakdown = breakdowns['background']
    backgroundhistogram = backgroundbreakdown['total']['histogram']
    backgroundyield     = backgroundbreakdown['total']['yield']
    backgrounderror     = backgroundbreakdown['total']['error']

#       if plotData and (not BLINDED): 
    databreakdown       = breakdowns['data']
    datahistogram       = databreakdown['Data']['histogram']
    datayield           = databreakdown['Data']['yield']
    dataerror           = databreakdown['Data']['error']

    #datahistogram.SetMarkerStyle(20)
    #datahistogram.SetMarkerSize(1) 
    #datahistogram.SetLineWidth(2)

    backgroundhistogram.SetLineColor(1)
    backgroundhistogram.SetLineWidth(2)
    backgroundhistogram.SetFillStyle(3344)
    backgroundhistogram.SetFillColor(16)

    if (args.region.lower().startswith("blind") or args.region.lower().startswith("sr")):
        data_and_sm_legend.AddEntry(datahistogram,"Data [BLINDED]","E1P")
    else: 
        data_and_sm_legend.AddEntry(datahistogram, \
            "Data [" + str(round(datayield,0)) +"]","E1P")

    data_and_sm_legend.AddEntry(backgroundhistogram, \
        "SM   [" + str(round(float(backgroundyield),1)) + "]","LF")
    return data_and_sm_legend



def create_background_and_signal_legend(breakdowns):#, n):
    args = get_parser()
    backgroundbreakdown = breakdowns['background']
    signalbreakdown     = breakdowns['signal']

    bkg_and_sig_legend = ROOT.TLegend(0.72,0.5,0.9,0.9)
    #totalyield,totalerror = backgroundbreakdown['total']['yield'], backgroundbreakdown['total']['error']

    backgroundbreakdown = breakdowns['background']
    backgroundhistogram = backgroundbreakdown['total']['histogram']
    backgroundyield     = backgroundbreakdown['total']['yield']
    backgrounderror     = backgroundbreakdown['total']['error']
    
    #    if plotData and (not BLINDED):
    databreakdown       = breakdowns['data']
    datahistogram       = databreakdown['Data']['histogram']
    datayield           = databreakdown['Data']['yield']

    dataerror           = databreakdown['Data']['error']
    #total_backyne = [0,0]
    #total_datayne = [0,0]
    for background in backgroundbreakdown:                                  #Try in this area
        if background == "total":continue
    
        histogram      = backgroundbreakdown[background]['histogram']
        backgroundyield = backgroundbreakdown[background]['yield']
        backgrounderror = backgroundbreakdown[background]['error']
        information = ""

        if (backgroundyield < 0.0):
            colorwrapper = "#color[16]{"
        else:
            colorwrapper = "#color[1]{"

        information += " [" + colorwrapper + str(round(backgroundyield,1)) + "}]"
        bkg_and_sig_legend.AddEntry(histogram,background + information ,"F")


       # if n == 0:
        #    file1 = open("histoinfo.txt", "a")
   #         rv = "{0}: Background: {1}, With a Yield of: {2}{3}{4}".format(args.region, background, str(round(backgroundyield,1))," +/- ", str(round(backgrounderror,1)))
    #        file1.write(rv)
     #       file1.write('\n')
      #      total_backyne[0] += backgroundyield
       #     total_backyne[1] += backgrounderror
       # if n == -1:
        #    file2 = open("errortest.txt", "a")
         #   rv = "{0}: Background: {1}, With an error of: {2}{3}".format(args.region, background, str(dataerror), '\n')
          #  file2.write(rv)



  #  if n == 0:
   #     file1 = open("histoinfo.txt", "a")
    #    rv = "Total Yield: {0} +/- {1}{2}Total data: {3} +/- {4}{2}Data/MC: {5} +/- {6}".format( str(round(total_backyne[0],1)), str(round(total_backyne[1],1)), '\n', datayield, dataerror, str(round(datayield/total_backyne[0],1)), str(round((total_backyne[1]/total_backyne[0]+dataerror/datayield)*datayield/total_backyne[0],1)))
     #   file1.write(rv)
      #  file1.write('\n')


    for signal in signalbreakdown:
        histogram   = signalbreakdown[signal]['histogram']
        signalyield = signalbreakdown[signal]['yield']
#        signalerror = signalbreakdown[signal]['error']

        signallatex = signal
        bkg_and_sig_legend.AddEntry(signalbreakdown[signal]['histogram'],
                        signallatex + " (" + str(round(signalyield,1)) +")","L")

    return bkg_and_sig_legend

def get_ratioplot_agreementline(xmin,xmax):
    import ROOT
    line = ROOT.TLine(float(xmin)+1e-2*float(xmax),1.,float(xmax)-1e-2*float(xmax),1.);
    line.SetLineWidth(3);
    line.SetLineColor(ROOT.kRed)
    line.SetLineStyle(ROOT.kDashed)
    return line

def get_ratioplot_averageline(xmin,xmax,average):
    line2 = ROOT.TLine(float(xmin),average,float(xmax),average)
    line2.SetLineStyle(2)
    line2.SetLineWidth(3)
    line2.SetLineColor(ROOT.kBlue)
    return line2

if __name__ == "__main__":
    main() 


