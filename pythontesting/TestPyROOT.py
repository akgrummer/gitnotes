#!/usr/bin/env python2
"""
#############################################################
# Program showing how to use interactive windows and MINUIT #
#############################################################
"""


import sys
from random   import seed, random
from time     import sleep
from argparse import ArgumentParser

from ROOT import gROOT, gStyle, gPad, gApplication, TGaxis, TCanvas, TF1, TGMainFrame, TPyDispatcher, TRootEmbeddedCanvas, TGLayoutHints, TGHorizontalFrame, TGTextButton, TGClient, kLHintsExpandX, kLHintsExpandY


class myGui(TGMainFrame):
    def __init__(self, parent, width, height):
        seed(0)
        
        self.draw = TPyDispatcher(self.drawHisto)
        self.out  = TPyDispatcher(self.getOut)

        TGMainFrame.__init__(self, parent, width, height)

        self.Canvas = TRootEmbeddedCanvas('Canvas', self, 800, 500)
        self.AddFrame(self.Canvas, TGLayoutHints(kLHintsExpandX | kLHintsExpandY))
        self.ButtonsFrame = TGHorizontalFrame(self, 200, 40)

        # Draw button
        self.DrawButton = TGTextButton(self.ButtonsFrame, '&Draw', 10)
        self.DrawButton.Connect('Clicked()', 'TPyDispatcher', self.draw, 'Dispatch()')
        self.ButtonsFrame.AddFrame(self.DrawButton, TGLayoutHints())

        # Exit button
        self.DrawButton = TGTextButton(self.ButtonsFrame, '&Exit', 10)
        self.DrawButton.Connect('Clicked()', 'TPyDispatcher', self.out, 'Dispatch()')
        self.ButtonsFrame.AddFrame(self.DrawButton, TGLayoutHints())

        self.AddFrame(self.ButtonsFrame, TGLayoutHints())

        self.SetWindowName('My Windows')
        self.MapSubwindows()
        self.Resize(self.GetDefaultSize())
        self.MapWindow()
        
        self.myHisto = 0
        
    def __del__(self):
        self.Cleanup()
        
    def getOut(self):
#        self.__del__()
        gApplication.Terminate(0)

    def drawHisto(self):
        if self.myHisto == 0:
            return
        self.Canvas.GetCanvas().cd()
        self.myHisto.SetLineColor(int(10 * random()))
        self.myHisto.Draw()
        gPad.Update()


def ArgParser(argv):
    ###################
    # Argument parser #
    ###################
    parser = ArgumentParser()
    parser.add_argument('-i', '--input',    dest = 'input',     help = 'input file',  default = ''        )
    parser.add_argument('-o', '--output',   dest = 'output',    help = 'otuput file', default = ''        )
    parser.add_argument('-w', '--whatever', dest = 'whaterver', help = 'whatever',    action='store_false')

    options = parser.parse_args()
    if not options.input:
        parser.error('No input parameter given')
    else:
        print('I\'m reading the intput option: ', options.input.split()[0])

    if not options.output:
        parser.error('No output parameter given')
    else:
        print('I\'m reading the output option: ', options.output.split()[0])

    return options


def SetStyle():
    gROOT.SetStyle('Plain')
    gROOT.ForceStyle()
    gStyle.SetTextFont(42)
    
    gStyle.SetOptTitle(0)
    gStyle.SetOptFit(1112)
    gStyle.SetOptStat(1110)
    
    gStyle.SetPadRightMargin(0.08)
    gStyle.SetPadTopMargin(0.11)
    gStyle.SetPadBottomMargin(0.12)
    
    gStyle.SetTitleFont(42,'x')
    gStyle.SetTitleFont(42,'y')
    gStyle.SetTitleFont(42,'z')
    
    gStyle.SetTitleOffset(1.05,'x')
    gStyle.SetTitleOffset(0.95,'y')
    
    gStyle.SetTitleSize(0.05,'x')
    gStyle.SetTitleSize(0.05,'y')
    gStyle.SetTitleSize(0.05,'z')
    
    gStyle.SetLabelFont(42,'x')
    gStyle.SetLabelFont(42,'y')
    gStyle.SetLabelFont(42,'z')
    
    gStyle.SetLabelSize(0.05,'x')
    gStyle.SetLabelSize(0.05,'y')
    gStyle.SetLabelSize(0.05,'z')
    
    TGaxis.SetMaxDigits(3)
    gStyle.SetStatY(0.9)


################
# Main program #
################
def main(argv = None):
    """
    #################################
    # Command line argument parsing #
    #################################
    """
    if argv is None:
        argv = sys.argv
    else:
        print('=== Some arguments are needed, for help run: python TestPyROOT.py --help')
        quit(0)
    cmd = ArgParser(argv)


    """
    ############
    # Graphycs #
    ############
    """
    gROOT.Reset()
    SetStyle()


    # Dynamic window
    myWindow = myGui(TGClient.Instance().GetRoot(),800,500)
    myWindow.myHisto = TF1('funMyWindow', 'abs(sin(x)/x)', 0, 10)
    myWindow.drawHisto()


    it = 0
    while (True):
        print("It: ", it)
        it += 1
        sleep(0.1)
    

    # Static window
    """
    myCanv = TCanvas('myCanv', 'Example with Formula', 10, 10, 800, 500)
    funCanv = TF1( 'funCanv', 'abs(sin(x)/x)', 0, 10)
    myCanv.SetGridx()
    myCanv.SetGridy()
    funCanv.Draw()
    myCanv.Update()
    """
    
    
    """
    ############################
    # Wait for keyborad stroke #
    ############################
    """
    raw_input('\n---press enter---')


if __name__ == '__main__':
    sys.exit(main())
