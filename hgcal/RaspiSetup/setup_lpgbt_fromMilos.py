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

    def __init__(self, device="/dev/i2c-23", address=0x70, mode=Mode.V2_WAGON, protocol="I2C", xml="file://connections.xml",uhaldevice="zcu"):
        self.iic=iic.iic(protocol)
        self.iic.connect(device,address,xml,uhaldevice)
        self.verbose=True
        self.DLLhack=True
        self.lpgbts=['A','B','C']
        self.__mode=mode

    def setup_core(self):
        if self.verbose: print("Setup core (%s)"%self.__mode)

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

        if self.__mode==Mode.V2_WAGON:
            self.iic.write_lpgbt(0x36,0x80) # 0x80 to invert transmitter with VTRX+
        elif self.__mode==Mode.FMCV1_TESTER:
            self.iic.write_lpgbt(0x36,0x00) # 0x00 to no invert transmitter with SFP board
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

    def setup_core_trig(self, doreset, ids=["B","C"]):
        if not ('B' in self.lpgbts) and not ('C' in self.lpgbts):
            return

        if self.verbose: print("Setup core for trig lpgbt")

        # reset line high, common for both lpGBT
        self.iic.write_lpgbt(0x052,0x80)
        if doreset:
            print("Doing a reset")
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
            

            invert_output=False
            if self.__mode==Mode.FMCV1_TESTER and lpgbt_id=="C": invert_output=True
            if self.__mode==Mode.V2_WAGON and lpgbt_id=="B": invert_output=True

            if (invert_output):
                self.iic.write_lpgbt_trig(lpgbt_id,0x36,0x80) # 0x80 to invert input
            else:
                self.iic.write_lpgbt_trig(lpgbt_id,0x36,0x00) # 0x80 to invert input
            self.iic.write_lpgbt_trig(lpgbt_id,0x37,0x00)
            self.iic.write_lpgbt_trig(lpgbt_id,0x38,0x00)

            #uplink
            #self.iic.write_lpgbt_trig(lpgbt_id,0x39,32)
            self.iic.write_lpgbt_trig(lpgbt_id,0x39,(0<<7)|96) # No pre-emphasis, larger drive current -- might be needed
            #self.iic.write_lpgbt(0x3A,0)

            #enable lookpack from Equalizer
            self.iic.write_lpgbt_trig(lpgbt_id,0x118,0x00)
            self.iic.write_lpgbt_trig(lpgbt_id,0x119,0x00)

            self.iic.write_lpgbt_trig(lpgbt_id,0x11d,0x00)

    def setup_gpio(self):
        print("Setup gpio")
        # outputs for the two SCA resets
        self.iic.write_lpgbt(0x53,(1<<5)|(1<<2))
        # SCA reset to high
        self.iic.write_lpgbt(0x55,(1<<5)|(1<<2))

    def finish_setup(self):
        if "A" in self.lpgbts:
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
        #self.iic.write_lpgbt(0x70,((0x3)<<3)|(3)) # This is setting the same register as below...
        #self.iic.write_lpgbt(0x71,0)
        self.iic.write_lpgbt(0x6c+(2*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(2*2)+1,0)

        if mode==Mode.V2_WAGON:
            for iclk in [19,20,22,23,24,25]:
                # 320 MHz, 3 mA drive, no inversion for now
                self.iic.write_lpgbt(0x6c+(iclk*2),(1<<6)|(5<<3)|(4))
                self.iic.write_lpgbt(0x6c+(iclk*2)+1,0)
            # SCA clocks
            for iclk in [2,3,28]:
                # 40 MHz, 3 mA drive, no inversion for now
                self.iic.write_lpgbt(0x6c+(iclk*2),(0<<6)|(7<<3)|(1))
                self.iic.write_lpgbt(0x6c+(iclk*2)+1,0)

        # clock to lpgbt "B" ECLK0
        self.iic.write_lpgbt(0x6c+(0*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(0*2)+1,0)
        # clock to lpgbt "C" ECLK6
        self.iic.write_lpgbt(0x6c+(6*2),((0x3)<<3)|(1))
        self.iic.write_lpgbt(0x6c+(6*2)+1,0)

    def eingsetup(self,lpgbt,group,mode):
        enables=0x1 # just first elink typically
        speed=3 # default is 1.28 Gbps, 1=320 Mbps, 2=640 Mbps
        align=2 # fixed phase(0), continous tracking (2), seeded tracking (3)
        if mode==Mode.FMCV1_TESTER:
            align=0 # fixed phase for tester
        if mode==Mode.V2_WAGON:
            if group==0:
                # EC-like inputs on egroup 0
                enables=0x3
                speed = 1
                #align=0
        return (enables<<4)|(speed<<2)|(align)
        
    def einsetup(self,lpgbt,group,chan,mode,phases):
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
            if lpgbt=='A' and group in [1,2,4,6]:
                polarity=1

        if lpgbt=='B' and group in [0]:
            polarity=1

#        print(lpgbt,group,chan,mode,polarity,term,phase)
        return (phase<<4)|(polarity<<3)|(bias<<2)|(term<<1)|((eq>>1)&1)
    
    def setup_inputs(self,mode=Mode.DEFAULT,phases=None):
        if mode==Mode.DEFAULT: mode=self.__mode
        if self.verbose: print("Setup inputs (%s)"%(mode.name))

        if "A" in self.lpgbts and mode==Mode.V2_WAGON:
            # EC input mode
            self.iic.write_lpgbt(0xcb,0x2)
            self.iic.write_lpgbt(0xe8,(1<<4)|0x0|0x2|0x1)


        for lpgbt in self.lpgbts:
            for group in range(0,7):
                self.iic.write_lpgbt(0xc4+group,self.eingsetup(lpgbt,group,mode),lpgbt)

            # setup the input parameters
            for group in range(0,7):
                for chan in range(0,4):
                    reg=0xcc+(group*4)+chan
                    regval=self.einsetup(lpgbt,group,chan,mode,phases)
                    self.iic.write_lpgbt(reg,regval,lpgbt)
    

    invert_gc_fmcv1=[1,1,1,1, 1,1,0,0, 1,0,0,0, 0,0,0,0]
    #invert_gc_v2wagon=[1,1,1,1, 1,1,0,0, 0,0,1,1, 1,1,1,1] # Old
    # [[G0][G1][G2][G3]] where G = [C0,C1,C2,C3] for every G.
    # G-eGroup, C-ePort/channel
    invert_gc_v2wagon=[1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,0,0] # New

    def eoutsetup(self,mode,group,chan):
        if mode==Mode.DEFAULT: mode=self.__mode
        pre_mode=0       # 0,1 = disabled, 2=self-timed, 3=clock-timed
        pre_strength=0   # valid = 0-7
        pre_width=0      # valid = 0-7
        drive=7          # valid = 0-7
        invert_gc = self.invert_gc_v2wagon
        if mode == Mode.FMCV1_TESTER:
            invert_gc = self.invert_gc_fmcv1
        invert=invert_gc[group*4+chan]
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

        if mode==Mode.V2_WAGON:
            self.iic.write_lpgbt(0xa7,0xFD) # 320 Mbps for groups 3:1, 80 Mbps for group 0
            self.iic.write_lpgbt(0xa8,0x1E) # mirror for groups 3:1, enable EC
            self.iic.write_lpgbt(0xa9,0x31) # enable ch 0, ch 1 in group 1,0
            self.iic.write_lpgbt(0xaa,0x93) # enable ch 3,0 in group 3, ch 0,1 in group 2

            self.iic.write_lpgbt(0xab,(0<<5)|(0<<3)|(7)) # EC TX strength


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
        if "A" in self.lpgbts:
            self.iic.write_lpgbt(0x118,0x05)
            self.finish_setup()
            time.sleep(1)
            self.iic.write_lpgbt(0x118,0x00)
            self.finish_setup()

        if "B" in self.lpgbts:
            self.iic.write_lpgbt_trig('B',0x118,0x05)
            self.finish_setup()
            time.sleep(1)
            self.iic.write_lpgbt_trig('B',0x118,0x00)
            self.finish_setup()

        if "C" in self.lpgbts:
            self.iic.write_lpgbt_trig('C',0x118,0x05)
            self.finish_setup()
            time.sleep(1)
            self.iic.write_lpgbt_trig('C',0x118,0x00)
            self.finish_setup()

    def sca_reset(self):
        if self.verbose: print("Run the SCA Reset")
        self.iic.write_lpgbt(0x55,0)
        self.iic.write_lpgbt(0x55,(1<<5)|(1<<2))

    def zero(self):
        if self.verbose: print("Setting all fuseable registers to zero")
        for reg in range(0,0xf0):
            self.iic.write_lpgbt(reg,0)


if __name__ == "__main__":
    import argparse

    parser=argparse.ArgumentParser(description="lpGBT setup controls")
    parser.add_argument('--linktrick',action='store_true',help='Run the uplink trick of turning on/off the 5 GHz raw clock')
    parser.add_argument('--lpgbt',default=None,type=str,help='Lpgbt to target')
    parser.add_argument('--phase',default=None,type=int,help='Phase to set for inputs')
    parser.add_argument('--reset',action='store_true',help='Reset the Trigger lpgbts')
    parser.add_argument('--daqonly',action='store_true',help='Only the DAQ lpgbt')
    parser.add_argument('--zero',action='store_true',help='Zero all registers')
    parser.add_argument('--scareset',action='store_true',help='Reset the SCAs')
    parser.add_argument('--gpiosetup',action='store_true',help='Setup the gpios controlling the SCA resets')
    parser.add_argument('--protocol',default='I2C',choices=["I2C","IC"],help='Communication protocol')
    parser.add_argument('--dev',default='/dev/i2c-23',help="I2C device to use")
    parser.add_argument('--trigsetup',action='store_true',help='Configure the trigger lpgbts, assumes a working daq lpgbt (intended for use with IC path)')

    modes=[]
    for modetype in Mode:
        modes.append(modetype.name)

    parser.add_argument('--mode',type=str,choices=modes,default="DEFAULT",help='Setup mode')

    args=parser.parse_args()
    mode=Mode.V2_WAGON

    if args.mode!="DEFAULT":
        mode=Mode[args.mode]

    lpgbt=SetupLPGBT(mode=mode,protocol=args.protocol,device=args.dev)
    
    if args.daqonly:
        lpgbt.lpgbts=['A']
        
    if args.lpgbt:
        lpgbt.lpgbts=[args.lpgbt]
        
    if (args.linktrick):
        lpgbt.run_link_tricks()
        quit()

    if args.gpiosetup:
        lpgbt.setup_gpio()
        quit()

    if (args.scareset):
        lpgbt.sca_reset()
        quit()

    if (args.zero):
        lpgbt.zero()
        quit()

    if args.trigsetup:
        lpgbt.lpgbts=['B','C']
        lpgbt.setup_core_trig(args.reset)
        lpgbt.setup_inputs(mode,args.phase)
        lpgbt.finish_setup()
    else:
        lpgbt.setup_core()
        lpgbt.setup_clocks()
        lpgbt.setup_core_trig(args.reset)
        lpgbt.setup_inputs(mode,args.phase)
        lpgbt.setup_outputs()
        if mode==Mode.V2_WAGON:
            lpgbt.setup_gpio()
        lpgbt.finish_setup()
