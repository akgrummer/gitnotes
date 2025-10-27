#!/usr/bin/python

import iic
import time
from enum import Enum

class Mode(Enum):
    V2_WAGON = 0
    FMCV1_TESTER = 10
    DEFAULT = 99 # whatever the default of the class is

class SetupLPGBT:
    """A class to setup the lpGBT in various configurations"""

    def __init__(self, device="/dev/i2c-23", address=0x70, mode=Mode.V2_WAGON):
        self.iic=iic.iic()
        self.iic.connect(device,address)
        self.verbose=True
        self.DLLhack=True
        self.lpgbts=['A','B','C']
        self.__mode=mode

    def setup_core(self):
        if self.verbose: print("Setup core")

        self.iic.write_lpgbt(0xef,0)
        # HACK to disable DLL timeout
        if self.DLLhack: self.iic.write_lpgbt(0xee,0xF0)

        self.iic.write_lpgbt(0x1F,((5)<<4)|(5))
        self.iic.write_lpgbt(0x20,((12)<<4)|(8))
        self.iic.write_lpgbt(0x21,0x38)  # new value from DHM
        self.iic.write_lpgbt(0x22,((4)<<4)|(4))
        self.iic.write_lpgbt(0x23,((5)<<4)|(5))
        self.iic.write_lpgbt(0x24,((5)<<4)|(5))
        self.iic.write_lpgbt(0x25,((5)<<4)|(5))
        self.iic.write_lpgbt(0x26,((5)<<4)|(5))
        self.iic.write_lpgbt(0x27,((5)<<4)|(5))
        self.iic.write_lpgbt(0x28,0x05) # new value from DHM
        self.iic.write_lpgbt(0x29,0x18) # new value from DHM
        self.iic.write_lpgbt(0x2a,0)
        self.iic.write_lpgbt(0x2b,0)
        self.iic.write_lpgbt(0x2c,((8)<<4)|(8))
        self.iic.write_lpgbt(0x2d,0x80|(9))
        self.iic.write_lpgbt(0x2e,((9)<<4)|(9))
        
        self.iic.write_lpgbt(0x33,0x54)
        self.iic.write_lpgbt(0x34,0x54)

        self.iic.write_lpgbt(0x36,0x00) # 0x40 to invert input
        self.iic.write_lpgbt(0x37,0x00)
        self.iic.write_lpgbt(0x38,0x00)

        #uplink
        #self.iic.write_lpgbt(0x39,32)
        self.iic.write_lpgbt(0x39,(0<<7)|96) # No pre-emphasis, larger drive current -- needed for V2B
        self.iic.write_lpgbt(0x3A,0)
    
        #downlink frame aligner setup
        self.iic.write_lpgbt(0x2f,0xA)
        self.iic.write_lpgbt(0x30,0xA)
        self.iic.write_lpgbt(0x31,0xA)
        self.iic.write_lpgbt(0x32,0xA)
        
        self.iic.write_lpgbt(0x118,0x00)
        self.iic.write_lpgbt(0x119,0x00)

        self.iic.write_lpgbt(0x11d,0x00)

    def setup_core_trig(self, ids=["B","C"]):
        if not ('B' in self.lpgbts) and not ('C' in self.lpgbts):
            return

        if self.verbose: print("Setup core for trig lpgbt")

        # reset line high, common for both lpGBT
        self.iic.write_lpgbt(0x052,0x80)
        self.iic.write_lpgbt(0x054,0x00)
        self.iic.write_lpgbt(0x054,0x80)

        # reset the I2C cores
        self.iic.write_lpgbt(0x12c, 0x0)
        self.iic.write_lpgbt(0x12c, 0x7)
        self.iic.write_lpgbt(0x12c, 0x0)

        for lpgbt_id in ids:
            self.iic.write_lpgbt_trig(lpgbt_id,0xef,0)

            self.iic.write_lpgbt_trig(lpgbt_id,0x1F,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x20,((12)<<4)|(8))
            self.iic.write_lpgbt_trig(lpgbt_id,0x21,0x38)  # new value from DHM  
            self.iic.write_lpgbt_trig(lpgbt_id,0x22,((4)<<4)|(4))
            self.iic.write_lpgbt_trig(lpgbt_id,0x23,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x24,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x25,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x26,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x27,((5)<<4)|(5))
            self.iic.write_lpgbt_trig(lpgbt_id,0x28,0x05) # new value from DHM 
            self.iic.write_lpgbt_trig(lpgbt_id,0x29,0x18) # new value from DHM 
            self.iic.write_lpgbt_trig(lpgbt_id,0x2a,0)
            self.iic.write_lpgbt_trig(lpgbt_id,0x2b,0)
            self.iic.write_lpgbt_trig(lpgbt_id,0x2c,((8)<<4)|(8))
            self.iic.write_lpgbt_trig(lpgbt_id,0x2d,0x80|(9))
            self.iic.write_lpgbt_trig(lpgbt_id,0x2e,((9)<<4)|(9))
            
            self.iic.write_lpgbt_trig(lpgbt_id,0x33,0x54)
            self.iic.write_lpgbt_trig(lpgbt_id,0x34,0x54)
            

            if (lpgbt_id=="B"):
                self.iic.write_lpgbt_trig(lpgbt_id,0x36,0x80) # 0x40 to invert input
            else:
                self.iic.write_lpgbt_trig(lpgbt_id,0x36,0x00) # 0x40 to invert input
            self.iic.write_lpgbt_trig(lpgbt_id,0x37,0x00)
            self.iic.write_lpgbt_trig(lpgbt_id,0x38,0x00)

            #uplink
            self.iic.write_lpgbt_trig(lpgbt_id,0x39,32)
            #self.iic.write_lpgbt(0x39,(0<<7)|96) # No pre-emphasis, larger drive current -- might be needed
            #self.iic.write_lpgbt(0x3A,0)

            #enable lookpack from Equalizer
            self.iic.write_lpgbt_trig(lpgbt_id,0x118,0x00)
            self.iic.write_lpgbt_trig(lpgbt_id,0x119,0x00)

            self.iic.write_lpgbt_trig(lpgbt_id,0x11d,0x00)

    def finish_setup(self):
        self.iic.write_lpgbt(0xef,4|2)
        if "B" in self.lpgbts:
            self.iic.write_lpgbt_trig("B",0xef,4|2)
        if "C" in self.lpgbts:
            self.iic.write_lpgbt_trig("C",0xef,4|2)

    def setup_clocks(self,mode=Mode.DEFAULT):
        if mode==Mode.DEFAULT: mode=self.__mode
        if self.verbose: print("Setup clocks (%s)"%(mode.name))
        #clocks
        # CLK 24
        self.iic.write_lpgbt(0x6c+(24*2),((0x3)<<3)|(2))
        self.iic.write_lpgbt(0x6c+(24*2)+1,0)
        # CLK 20
        self.iic.write_lpgbt(0x6c+(20*2),((0x3)<<3)|(4))
        self.iic.write_lpgbt(0x6c+(20*2)+1,0)
        self.iic.write_lpgbt(0x70,((0x3)<<3)|(3))
        self.iic.write_lpgbt(0x71,0)
        self.iic.write_lpgbt(0x6c+(2*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(2*2)+1,0)
        # clock to lpgbt "B" ECLK0
        self.iic.write_lpgbt(0x6c+(0*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(0*2)+1,0)
        # clock to lpgbt "C" ECLK6
        self.iic.write_lpgbt(0x6c+(6*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(6*2)+1,0)

    def eingsetup(self,group,mode):
        enables=0x1 # just first elink typically
        speed=3 # default is 1.28 Gbps, 1=320 Mbps, 2=640 Mbps
        align=2 # fixed phase(0), continous tracking (2), seeded tracking (3)
        if mode==Mode.FMCV1_TESTER:
            align=0 # fixed phase for tester

        return (enables<<4)|(speed<<2)|(align)
        
    def einsetup(self,group,chan,mode,phases):
        phase=0
        if phases:
            if isinstance(phases,int):
                phase=phases
            elif phases and len(phases)==7:
                phase=phases[group]
            elif phases and len(phases)==7:
                phase=phases[group]
        polarity=0
        term=1
        bias=0
        eq=0        

        if mode==Mode.FMCV1_TESTER:
            if group in [1,2,4,5,6]:
                polarity=1

        return (phase<<4)|(polarity<<3)|(bias<<2)|(term<<1)|(eq)
    
    def setup_inputs(self,mode=Mode.DEFAULT,phases=None):
        if mode==Mode.DEFAULT: mode=self.__mode
        if self.verbose: print("Setup inputs (%s)"%(mode.name))

        for group in range(0,7):
            self.iic.write_lpgbt(0xc4+group,self.eingsetup(group,mode))

        # setup the input parameters
        for group in range(0,7):
            for chan in range(0,4):
                reg=0xcc+(group*4)+chan
                regval=self.einsetup(group,chan,mode,phases)
                self.iic.write_lpgbt(reg,regval)
    

    invert_gc=[1,1,1,1, 1,1,0,0, 1,0,0,0, 0,0,0,0]
    def eoutsetup(self,mode,group,chan):
        pre_mode=0       # 0,1 = disabled, 2=self-timed, 3=clock-timed
        pre_strength=0   # valid = 0-7
        pre_width=0      # valid = 0-7
        drive=7          # valid = 0-7
        invert=self.invert_gc[group*4+chan]
        return drive,invert,pre_strength,pre_mode,pre_width
        
    def setup_outputs(self,mode=Mode.DEFAULT):
        if mode==Mode.DEFAULT: mode=self.__mode
        if self.verbose: print("Setup outputs (%s)"%mode.name)

        if mode==Mode.FMCV1_TESTER:
            #elinktx
            self.iic.write_lpgbt(0xa7,0xFF) # 320 Mbps everywhere
            self.iic.write_lpgbt(0xa8,0x0F) # mirror for all groups, disable EC
            self.iic.write_lpgbt(0xa9,0x3F) # enable ch 0, ch 1 in group 1, all of group 0
            self.iic.write_lpgbt(0xaa,0x33) # enable ch 0, ch 1 in groups 2, 3

        for group in range(0,4):
            chncntr=0
            for link in range(0,4):
                (drive, invert, pre_strength, pre_mode, pre_width) = self.eoutsetup(mode,group,link)
                self.iic.write_lpgbt(0xac+group*4+link, drive | (pre_mode<<3) | (pre_strength<<5))
                if (link in [0,2]):
                    chncntr=pre_width|(invert<<3)
                else:
                    chncntr=chncntr|(((pre_width)|(invert<<3))<<4)
                    reg=0xbc+int(link/2)+group*2
                    self.iic.write_lpgbt(reg,chncntr)
                    
    def run_link_tricks(self):
        if self.verbose: print("Run the link trick")
        self.iic.write_lpgbt(0x118,0x05)
        if "B" in self.lpgbts:
            self.iic.write_lpgbt_trig('B',0x118,0x05)
        if "C" in self.lpgbts:
            self.iic.write_lpgbt_trig('C',0x118,0x05)
        self.finish_setup()

        time.sleep(1)
        self.iic.write_lpgbt(0x118,0x00)
        if "B" in self.lpgbts:
            self.iic.write_lpgbt_trig('B',0x118,0x00)
        if "C" in self.lpgbts:
            self.iic.write_lpgbt_trig('C',0x118,0x00)

        self.finish_setup()



if __name__ == "__main__":
    import argparse

    parser=argparse.ArgumentParser(description="lpGBT setup controls")
    parser.add_argument('--linktrick',action='store_true',help='Run the uplink trick of turning on/off the 5 GHz raw clock')
    parser.add_argument('--daqonly',action='store_true',help='Only the DAQ lpgbt')

    modes=[]
    for modetype in Mode:
        modes.append(modetype.name)

    parser.add_argument('--mode',type=str,choices=modes,default="DEFAULT",help='Setup mode')
    parser.add_argument('--mount',type=str,default="/dev/i2c-23",help='Mount dir')

    args=parser.parse_args()
    mode=Mode.V2_WAGON

    if args.mode!="DEFAULT":
        mode=Mode[args.mode]

    lpgbt=SetupLPGBT(device=args.mount, mode=mode)
    

    if args.daqonly:
        lpgbt.lpgbts=['A']
        
    if (args.linktrick):
        lpgbt.run_link_tricks()
        quit()


    lpgbt.setup_core()
    lpgbt.setup_clocks()
    lpgbt.setup_core_trig()
    lpgbt.setup_inputs()
    lpgbt.setup_outputs()
    lpgbt.finish_setup()





