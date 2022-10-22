import math
import os
import tkinter as tk
from tkinter.filedialog import  (askdirectory,askopenfilename,askopenfile,asksaveasfilename)
import time
import win32api
from os.path import abspath
import re
import pandas as pd
import matplotlib
from  matplotlib import pyplot as plt
import numpy as np
from matplotlib import lines
import _thread


class AFModuleFunc:

    def __init__(self):
        self.pdCalOTPInfinityEntry = tk.Entry()
        self.pdCalOTPMacroEntry = tk.Entry()
        self.ManualAFPositionEntry = tk.Entry()

        self.pdCalOTPStepIdx0Var = tk.StringVar()
        self.pdCalOTPStepIdx1Var = tk.StringVar()
        self.pdCalOTPStepIdx2Var = tk.StringVar()
        self.pdCalOTPStepIdx3Var = tk.StringVar()
        self.pdCalOTPStepIdx4Var = tk.StringVar()
        self.pdCalOTPStepIdx5Var = tk.StringVar()
        self.pdCalOTPStepIdx6Var = tk.StringVar()
        self.pdCalOTPStepIdx7Var = tk.StringVar()
        self.pdCalOTPStepIdx8Var = tk.StringVar()
        self.pdCalOTPStepIdx9Var = tk.StringVar()


        self.selectPullPath = ""
        self.pullFrameSavePath = tk.StringVar()
        self.savePathEntry = tk.Entry()
        self.Iso100ISPGainEntry = tk.Entry()
        self.Iso100SensorGainEntry = tk.Entry()
        self.Iso100ShutterEntry = tk.Entry()
        self.MaxSensorGainEntry = tk.Entry()
        self.HWThrCapModeVar=tk.IntVar()
        self.AFExtractLogFileName =""
        self.AFExtractSelectedLogFileName = tk.StringVar()
        self.AFExtractSelectedLogFileName2 = tk.StringVar()
        self.AFExtractSelectedLogFileName3 = tk.StringVar()
        self.AFLogExtractSelectFileButton = tk.Button()
        self.AFLogExtractlogSelectFileEntry = tk.Entry()
        self.AFLogExtractlogSelectFileEntry1 = tk.Entry()
        self.AFLogExtractlogSelectFileEntry2 = tk.Entry()
        self.AFLogExtractlogSelectFileEntry3 = tk.Entry()
        self.AFLogExtSelLogFolderEntry = tk.Entry()
        self.AFLogFileSelEntry = tk.Entry()
        self.AFLogFolderSelEntry=tk.Entry()
        self.AFExtLogsFolderPath = ""
        self.AFExtLogsFolderShowPath = tk.StringVar()
        self.AFExtLogsFolderShowPath2 = tk.StringVar()
        self.AFLogFolderSelPath = ""
        self.AFLogFolderSelShowPath = tk.StringVar()
        self.AFLogAnaFileName = ""
        self.AFLogAnaSelectedLogFileName = tk.StringVar()
        self.AFHWThrISOInfo = tk.StringVar()
        self.AFSetNvramPathExtry = tk.Entry()
        self.AFPullMtkLogFuncButton = tk.Button()
        self.AFPullImagesButton = tk.Button()
        self.AFPullRAWButton = tk.Button()
        self.AFPullFixNvramPathButton = tk.Button()

        #AF log filter keyword
        self.AFLogFiltKeyWord1 = tk.IntVar()
        self.AFLogFiltKeyWord2 = tk.IntVar()
        self.AFLogFiltKeyWord3 = tk.IntVar()
        self.AFLogFiltKeyWord4 = tk.IntVar()
        self.AFLogFiltKeyWord5 = tk.IntVar()
        self.AFLogFiltKeyWord6 = tk.IntVar()
        self.AFLogFiltKeyWord7 = tk.IntVar()
        self.AFLogFiltKeyWord8 = tk.IntVar()
        self.AFLogFiltKeyWord9 = tk.IntVar()
        self.AFLogFiltKeyWord10 = tk.IntVar()
        self.AFLogFiltKeyWord11 = tk.IntVar()
        self.AFLogFiltKeyWord12 = tk.IntVar()
        self.AFLogFiltKeyWord13 = tk.IntVar()
        self.AFLogFiltKeyWord14 = tk.IntVar()
        self.AFLogFiltKeyWord15 = tk.IntVar()
        self.AFLogFiltKeyWord16 = tk.IntVar()
        self.AFLogFiltKeyWord17 = tk.IntVar()
        self.AFLogFiltKeyWord18 = tk.IntVar()
        self.AFLogFiltKeyWord19 = tk.IntVar()
        self.AFLogFiltKeyWord20 = tk.IntVar()
        self.AFLogFiltKeyWord21 = tk.IntVar()
        self.AFLogFiltKeyWord22 = tk.IntVar()
        self.AFLogFiltKeyWord23 = tk.IntVar()
        self.AFLogFiltKeyWord24 = tk.IntVar()
        self.AFLogFiltKeyWord25 = tk.IntVar()
        self.AFLogFilterContents =""
        self.AFLogFilterKeyWordsColor={}
        self.AFLOGAnalysisWinMain = None



    def AFLogEnable(self):
        result = os.system('Open3A.bat')

    def AFLogcat(self):
        result = os.system('Logcat.bat')

    def AFLogcatSAG(self):
        result = os.system('Logcat_SAG.bat')

    def AFLogcattableset(self):
        result = os.system('Logcat_tableset.bat')

    def AFLogEnableWithWaterMark(self):
        result = os.system("adb root")
        result = os.system("adb remount")
        result = os.system("adb shell setprop persist.sys.log.ctrl yes")
        result = os.system("adb shell setprop persist.log.ratelimit 0")
        result = os.system("adb shell pkill camera*")

        result = os.system("adb shell setenforce 0")
        result = os.system("adb shell setprop vendor.debug.camera.dbginfo 1")
        result = os.system("adb shell setprop vendor.debug.pd.vpu.enable 1")
        result = os.system("adb shell setprop debug.af.log.enable 1")
        result = os.system("adb shell setprop debug.af.enable 1")
        result = os.system("adb shell setprop vendor.debug.af.log.enable 1")
        result = os.system("adb shell setprop vendor.debug.af.enable 1")
        result = os.system("adb shell setprop vendor.debug.af.log.enable 2")
        result = os.system("adb shell setprop vendor.debug.af_mgr.enable 1")
        result = os.system("adb shell setprop vendor.debug.pd.enable 1")
        result = os.system("adb shell setprop persist.vendor.mtk.camera.log_level 3")
        result = os.system("adb shell setprop vendor.debug.pd.vpu.log.enable 1")
        result = os.system("adb shell setprop vendor.debug.camera.af.draw.lens 1")
        result = os.system("adb shell setprop debug.cam.drawid 1")
        result = os.system("adb shell setprop vendor.debug.hal3a.taskmgr 1")
        result = os.system("adb shell setprop vendor.debug.hal3a.task 1")
        result = os.system("adb shell setprop vendor.debug.hal3av3.log 3")
        result = os.system("adb shell setprop vendor.debug.thread_raw.log 1")
        result = os.system("adb shell setprop vendor.debug.resultpool.log 63")
        result = os.system("adb shell setprop vendor.debug.pdo_mgr.enable 1")
        result = os.system("adb shell setprop vendor.debug.afo_mgr.enable 1")
        result = os.system("adb shell setprop vendor.debug.sync3A.log 1")
        result = os.system("adb shell setprop vendor.debug.sync3AWrapper.log 1")
        result = os.system("adb shell setprop debug.cam.draw.ctrl 'ISOmagicDAC'")
        # result = os.system("adb shell setprop vivo.vaf.mask 1")
        result = os.system("adb shell setprop persist.log.ratelimit 0")
        result = os.system("adb shell setprop persist.camera.log.onlymainlog yes")
        result = os.system("adb shell setprop persist.sys.camera.log yes")
        result = os.system("adb shell logcat -G 25M")
        result = os.system("adb shell sync")
        result = os.system("adb shell sync")
        result = os.system("adb shell sync")
        result = os.system("adb shell pkill camera*")

    def AFFullScanEnable(self):
        result = os.system("adb root")
        result = os.system("adb remount")
        result = os.system("adb shell setprop vendor.debug.camera.af.fullsweep 1")
        result = os.system("adb shell sync")
        result = os.system("adb shell pkill camera*")
        result = os.system("adb shell sync")

    def AFFullScanDisable(self):
        result = os.system("adb root")
        result = os.system("adb remount")
        result = os.system("adb shell setprop vendor.debug.camera.af.fullsweep 0")
        result = os.system("adb shell sync")
        result = os.system("adb shell pkill camera*")
        result = os.system("adb shell sync")
       
    def AFOTPDriverCheckEn(self):
         result = os.system("OTP_dump_enable.bat")

    def Pullotpinfo(self):
        result = os.system("OTP_pull.bat")

    def ACC_GyroDriverCheckEn(self):
        result = os.system("OTP_dump_disable.bat")

    def PDDriverCheckEn(self):
        self.AFLogEnable()

    def FVStableTimeNvramPathCheckEn(self):
        result = os.system("adb root")
        result = os.system("adb remount")
        result = os.system("adb shell setprop vendor.debug.camera.af.fullsweep 3")
        result = os.system("adb shell sync")
        result = os.system("adb shell pkill camera*")
        result = os.system("adb shell sync")


    def AFPerformanceCheckEn(self):
        self.AFLogEnable()

    def AFLogKeyWordHightLight_pattern(self,widget,pattern,tag='highlight',options={"background":"yellow"},regexp=True):
        widget.tag_delete(tag)
        widget.tag_config(tag,**options)
        start = widget.index("1.0")
        stop = widget.index("end")
        print("start:%s,stop:%s"%(start,stop))
        count = tk.IntVar() #get the length of match
        while  True:
            index = widget.search(pattern,start,stop,count=count)
            print("index:%s"%index)
            if not index:
                break
            length = count.get()
            if length == 0:
                break

            widget.tag_add(tag,index,"%s+%sc"%(index,length))
            start = "%s+%sc" %(index,length)

    def AFLogKeyWordHightLight(self,keywords,wintext):
        for keyword,color in keywords.items():
            startIndex = "1.0"
            while True:
                startIndex = wintext.search(keyword,startIndex,"end")
                if startIndex:
                    endIndex = wintext.index("%s+%dc"%(startIndex,(len(keyword))))
                    wintext.tag_add(keyword,startIndex,endIndex)
                    wintext.tag_config(keyword,background=color)
                    startIndex = endIndex
                else:
                    break

    def AFLogAnalysisShow(self,keywords,content):
        print("keyword:%s"%keywords)
        ShowLogWin = tk.Tk()
        ShowLogWin.title("Show Logs")
        ShowLogWin.geometry("1000x600")
        # ShowLogWin.resizable(0,0)

        winMainFrame = tk.Frame(ShowLogWin)
        winMainFrame.pack(side=tk.LEFT,fill=tk.Y)

        winYScroll = tk.Scrollbar(winMainFrame)
        winYScroll.pack(side=tk.RIGHT,fill=tk.Y)
        winXScroll = tk.Scrollbar(winMainFrame,orient=tk.HORIZONTAL)
        winXScroll.pack(side=tk.BOTTOM,fill=tk.X)

        winText = tk.Text(winMainFrame,wrap=tk.NONE, width=800, height=600,xscrollcommand=winXScroll.set,yscrollcommand=winYScroll.set)

        winXScroll.config(command=winText.xview)
        winYScroll.config(command=winText.yview)

        winText.pack(expand=tk.YES,side=tk.TOP, fill=tk.Y)
        winText.insert('insert', content)
        self.AFLogKeyWordHightLight(keywords, winText)
        ShowLogWin.mainloop()

    def AFLOGAnalysisWinMainUpdate(self):
        self.AFLOGAnalysisWinMain.destroy()
        self.AFLOGAnalysisWinMain = None
        self.AFLogFiltKeyWord1.set(0)
        self.AFLogFiltKeyWord2.set(0)
        self.AFLogFiltKeyWord3.set(0)
        self.AFLogFiltKeyWord4.set(0)
        self.AFLogFiltKeyWord5.set(0)
        self.AFLogFiltKeyWord6.set(0)
        self.AFLogFiltKeyWord7.set(0)
        self.AFLogFiltKeyWord8.set(0)
        self.AFLogFiltKeyWord9.set(0)
        self.AFLogFiltKeyWord10.set(0)
        self.AFLogFiltKeyWord11.set(0)
        self.AFLogFiltKeyWord12.set(0)
        self.AFLogFiltKeyWord13.set(0)
        self.AFLogFiltKeyWord14.set(0)
        self.AFLogFiltKeyWord15.set(0)
        self.AFLogFiltKeyWord16.set(0)
        self.AFLogFiltKeyWord17.set(0)
        self.AFLogFiltKeyWord18.set(0)
        self.AFLogFiltKeyWord19.set(0)
        self.AFLogFiltKeyWord20.set(0)
        self.AFLogFiltKeyWord21.set(0)
        self.AFLogFiltKeyWord22.set(0)
        self.AFLogFiltKeyWord23.set(0)
        self.AFLogFiltKeyWord24.set(0)
        self.AFLogFiltKeyWord25.set(0)
        self.AFLogFilterContents= ""

    def AFLOGAnalysisWinMainShow(self,keywordsColor,content):
        if self.AFLOGAnalysisWinMain != None:
            self.AFLOGAnalysisWinMain.destroy()

        self.AFLOGAnalysisWinMain =tk.Tk()
        self.AFLOGAnalysisWinMain.title("Show Logs")
        self.AFLOGAnalysisWinMain.geometry("1000x600")
        # ShowLogWin.resizable(0,0)

        winMainFrame = tk.Frame(self.AFLOGAnalysisWinMain)
        winMainFrame.pack(side=tk.LEFT, fill=tk.Y)

        winYScroll = tk.Scrollbar(winMainFrame)
        winYScroll.pack(side=tk.RIGHT, fill=tk.Y)
        winXScroll = tk.Scrollbar(winMainFrame, orient=tk.HORIZONTAL)
        winXScroll.pack(side=tk.BOTTOM, fill=tk.X)

        winText = tk.Text(winMainFrame, wrap=tk.NONE, width=800, height=600, xscrollcommand=winXScroll.set,
                          yscrollcommand=winYScroll.set)

        winXScroll.config(command=winText.xview)
        winYScroll.config(command=winText.yview)

        winText.pack(expand=tk.YES, side=tk.TOP, fill=tk.Y)
        winText.insert('insert', content)
        self.AFLogKeyWordHightLight(keywordsColor, winText)
        self.AFLOGAnalysisWinMain.protocol('WM_DELETE_WINDOW', self.AFLOGAnalysisWinMainUpdate)
        self.AFLOGAnalysisWinMain.mainloop()


    def PDCalibrationCheck(self):
        self.AFLogEnable()
        result=os.system("PDlib_info.bat")

    def MoveLensByManual(self):
        #move lens
        result=os.system("adb root")
        result=os.system("adb remount")
        result=os.system("adb shell setprop vendor.debug.camera.af.manual 2")
        result=os.system("adb shell pkill camera*")
        moveLensPos = self.ManualAFPositionEntry.get()
        print("moveLensPos:%s"%str(moveLensPos))
        result=os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + str(moveLensPos))

    def PDCalOTPStepGen(self):
        print("self.pdCalOTPInfinityEntry.get()--%s"%str(self.pdCalOTPInfinityEntry.get()))
        otpInfinityData = self.pdCalOTPInfinityEntry.get()
        otpMacroData = self.pdCalOTPMacroEntry.get()
        if otpInfinityData == '' or otpMacroData == '' :
            tk.messagebox.showinfo("信息", "请输入OTP数据")
            return
        else:
            otpInfinityData = int(str(otpInfinityData))
            otpMacroData = int(str(otpMacroData))

        otpStepData = math.ceil((otpMacroData - otpInfinityData)/9)
        print("otpStepData:%s"%str(otpStepData))
        idx0Data = otpInfinityData
        idx1Data = idx0Data + otpStepData
        idx2Data = idx1Data + otpStepData
        idx3Data = idx2Data + otpStepData
        idx4Data = idx3Data + otpStepData
        idx5Data = idx4Data + otpStepData
        idx6Data = idx5Data + otpStepData
        idx7Data = idx6Data + otpStepData
        idx8Data = idx7Data + otpStepData
        idx9Data = idx8Data + otpStepData
        self.pdCalOTPStepIdx0Var.set(idx0Data)
        self.pdCalOTPStepIdx1Var.set(idx1Data)
        self.pdCalOTPStepIdx2Var.set(idx2Data)
        self.pdCalOTPStepIdx3Var.set(idx3Data)
        self.pdCalOTPStepIdx4Var.set(idx4Data)
        self.pdCalOTPStepIdx5Var.set(idx5Data)
        self.pdCalOTPStepIdx6Var.set(idx6Data)
        self.pdCalOTPStepIdx7Var.set(idx7Data)
        self.pdCalOTPStepIdx8Var.set(idx8Data)
        self.pdCalOTPStepIdx9Var.set(idx9Data)

    def PDCalCmdMoveLens(self):
        result=os.system("adb shell setprop vendor.debug.camera.af.manual 2")
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos "+self.pdCalOTPStepIdx0Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx1Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx2Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx3Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos" + self.pdCalOTPStepIdx4Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx5Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx6Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx7Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx8Var)
        time.sleep(1)
        result = os.system("adb shell setprop vendor.debug.camera.af.ctrl.lenspos " + self.pdCalOTPStepIdx9Var)
        time.sleep(1)
        
    def DisableManualFunc(self):
        result=os.system("adb root")
        result=os.system("adb remount")
        result=os.system("adb shell setprop vendor.debug.camera.af.manual 0")
        result=os.system("adb shell pkill camera*")

    def TiltCheck(self):
        self.AFFullScanEnable()


    def AFTableEnableFullScan(self):
        self.AFFullScanEnable()

    def AFPullSelectPath(self):
        self.selectPullPath = askdirectory()
        self.pullFrameSavePath.set(self.selectPullPath)

    def AFADBCmdSetNvramPathButFunc(self):
        self.AFPullMtkLogFuncButton.config(state=tk.DISABLED)
        self.AFPullImagesButton.config(state=tk.DISABLED)
        self.AFPullRAWButton.config(state=tk.DISABLED)
        self.AFSetNvramPathExtry.config(state=tk.NORMAL)
        self.AFPullFixNvramPathButton.config(state=tk.NORMAL)
        print("len of set Nvram Path:%s "%len(self.AFSetNvramPathExtry.get()))


    def AFADBCmdPullFixNvramButFunc(self):
        destPath = self.pullFrameSavePath.get()
        sourcePath = self.AFSetNvramPathExtry.get()
        print("destPath:%s"%destPath)
        print("sourcePath-%s:"%sourcePath)
        if len(destPath) == 0:
            tk.messagebox.showinfo("信息", "请选择pull路径")
            return
        # if len(sourcePath) == 0 :
        #
        if len(self.AFSetNvramPathExtry.get()) == 0:
            tk.messagebox.showinfo("信息", "请设置需要pull的手机内存路径")
            self.AFPullMtkLogFuncButton.config(state=tk.NORMAL)
            self.AFPullImagesButton.config(state=tk.NORMAL)
            self.AFPullRAWButton.config(state=tk.NORMAL)
            self.AFSetNvramPathExtry.config(state=tk.DISABLED)
            self.AFPullFixNvramPathButton.config(state=tk.DISABLED)
            return

        result = os.system("adb pull " + sourcePath+" "+ destPath)


    def AFPullMTKLogFunc(self):
        self.selectPullPath = self.pullFrameSavePath.get()
        if (len(self.selectPullPath) == 0):
            tk.messagebox.showinfo("信息", "请选择pull路径")
            return
        result = os.system("adb pull /data/debuglogger/mobilelog " + self.selectPullPath)

    def AFPullImagesFunc(self):
        self.selectPullPath=self.pullFrameSavePath.get()
        if(len(self.selectPullPath)==0):
            tk.messagebox.showinfo("信息","请选择pull路径")
            return
        result=os.system("adb pull /sdcard/DCIM/Camera "+self.selectPullPath)

    def AFADBCmdClearImageFunc(self):
        information = tk.messagebox.askyesno("确认删除","需要删除手机中所有图片吗？")
        print("r:%s"%information)
        if information == True :
            result=os.system("adb root")
            result=os.system("adb remount")
            result=os.system("adb shell rm -rf /sdcard/DCIM/")
        else:
            return

    def AFADBCmdClearRawFunc(self):
        information = tk.messagebox.askyesno("确认删除", "确认删除手机中所有RAW图吗？")
        if information == True:
            result = os.system("adb shell rm -rf /data/vendor/camera_dump")
            result = os.system("adb shell mkdir /data/vendor/camera_dump/ -p")
        else:
            return

    def AFADBCmdClearLogFunc(self):
        information = tk.messagebox.askyesno("确认删除", "确认删除手机中所有LOG吗？")
        if information == True:
            result = os.system("adb shell rm -rf /data/debuglogger")
        else:
            return

    def AFPullRawFunc(self):
        self.selectPullPath = self.pullFrameSavePath.get()
        if (len(self.selectPullPath) == 0):
            tk.messagebox.showinfo("信息", "请选择pull路径")
            return
        result = os.system("adb pull /data/vendor/camera_dump " + self.selectPullPath)

    def AFExtractLogFileSelectFunc(self):
        self.AFLogExtSelLogFolderEntry.delete(0, tk.END)
        self.AFLogExtSelLogFolderEntry.config(state=tk.DISABLED)
        self.AFLogExtractlogSelectFileEntry.config(state=tk.NORMAL)
        self.AFErtactLogFileName=askopenfilename()
        self.AFExtractSelectedLogFileName.set(self.AFErtactLogFileName)
    
    def AFExtractLogFileSelectFunc1(self):
        self.AFLogExtSelLogFolderEntry.delete(0, tk.END)
        self.AFLogExtSelLogFolderEntry.config(state=tk.DISABLED)
        self.AFLogExtractlogSelectFileEntry1.config(state=tk.NORMAL)
        self.AFErtactLogFileName=askopenfilename()
        self.AFExtractSelectedLogFileName.set(self.AFErtactLogFileName)

    def AFExtractLogFileSelectFunc2(self):
        self.AFLogExtSelLogFolderEntry.delete(0, tk.END)
        self.AFLogExtSelLogFolderEntry.config(state=tk.DISABLED)
        self.AFLogExtractlogSelectFileEntry2.config(state=tk.NORMAL)
        self.AFErtactLogFileName=askopenfilename()
        self.AFExtractSelectedLogFileName2.set(self.AFErtactLogFileName)

    def AFExtractLogFileSelectFunc3(self):
        self.AFLogExtSelLogFolderEntry.delete(0, tk.END)
        self.AFLogExtSelLogFolderEntry.config(state=tk.DISABLED)
        self.AFLogExtractlogSelectFileEntry3.config(state=tk.NORMAL)
        self.AFDrawFvFileName=askopenfilename()
        self.AFExtractSelectedLogFileName3.set(self.AFDrawFvFileName)

    def Draw_FV(self):
        Logpath = self.AFDrawFvFileName
        t = open(Logpath,'r',encoding='utf-8')
        file_name = asksaveasfilename(title=u'Save txt',filetypes=[("文本文件",".txt")])
        t1 = open(file_name,'w',encoding='utf-8')
        lines = t.readlines()
        for line in lines:
            if 'CAF_SCAN_Fullsweep_far_to_near' in line:      
                # print(type(line))
                text1=re.findall(r'Focusval.*?H1',line)
                text2=str(text1).replace(",","")
                # text3=str(text2).replace(".000000","")
                text=str(text2).replace("H1","")
                # print(text)
                t1.write(text+'\n')
        data=open(file_name)
        df1 = pd.DataFrame(data,columns=["NAME"])
        # df = pd.DataFrame(data,columns=["NAME1","VALUE1","NAME2","VALUE2"])
        df2= df1['NAME'].str.split(expand=True)
        # print(df2)
        csv_name = asksaveasfilename(title=u'Save as csv',filetypes=[("数据文件",".csv")])
        df3 = df2.to_csv(csv_name,index=False)
        df = pd.read_csv(csv_name)
        # print(df)
        xdata=df.iloc[:,3].tolist()
        # print(xdata)
        # quit()
        ydata=df.iloc[:,1].tolist()
        # print(ydata)
        # ym=max(ydata)
        # print(ym)
        ydata_maxindex=ydata.index(max(ydata))
        # print(ydata_maxindex)
        xdata_max=df.iloc[ydata_maxindex,3]
        print('max_pos :',xdata_max)
        ydata_max=max(ydata)
        print('max_fv :',ydata_max)
        show_max='['+str(xdata_max)+' '+str(ydata_max)+']'
        plt.plot(xdata_max,ydata_max,'ko')
        plt.annotate(show_max,xy=(xdata_max,ydata_max),xytext=(xdata_max,ydata_max))
        plt.plot(xdata,ydata)
        plt.xlabel('Lens position')
        plt.ylabel('Focus Value')
        im_path = asksaveasfilename(title=u'Save Picture',filetypes=[("图片文件",".jpg")])
        plt.savefig(str(im_path)+'.jpg')
        # i=random.randint(1,10)
        # plt.savefig('./Img/fv-{}.jpg'.format(i))
        plt.show()
        # p = _thread(target=Draw_FV,daemon=True) 
        # p.join()
        # p.stop()

    def AFextLogsFolderSelectFunc(self):
        self.AFLogExtractlogSelectFileEntry.delete(0, tk.END)
        self.AFLogExtractlogSelectFileEntry.config(state=tk.DISABLED)
        self.AFLogExtSelLogFolderEntry.config(state=tk.NORMAL)
        self.AFExtLogsFolderPath = askdirectory()
        self.AFExtLogsFolderShowPath.set(self.AFExtLogsFolderPath)

    def AFextLogsFolderSelectFunc1(self):
        self.AFLogExtractlogSelectFileEntry.delete(0, tk.END)
        self.AFLogExtractlogSelectFileEntry.config(state=tk.DISABLED)
        self.AFLogExtSelLogFolderEntry.config(state=tk.NORMAL)
        self.AFExtLogsFolderPath = askdirectory()
        self.AFExtLogsFolderShowPath.set(self.AFExtLogsFolderPath)

    def AFextLogsFolderSelectFunc2(self):
        self.AFLogExtractlogSelectFileEntry.delete(0, tk.END)
        self.AFLogExtractlogSelectFileEntry.config(state=tk.DISABLED)
        self.AFLogExtSelLogFolderEntry.config(state=tk.NORMAL)
        self.AFExtLogsFolderPath = askdirectory()
        self.AFExtLogsFolderShowPath2.set(self.AFExtLogsFolderPath)

    # def AFAnaLogFileOpenWay2(self):
    #     path1 = (self.AFLogAnaFileName)
    #     print(type(path1))
    #     print(len(path1))
    #     # path=str(path1)
    #     # path2 =[abspath(path1)]
    #     # path = re.sub(r"[\([{})\]]", "", path2)
    #     # print(path1)
    #     # quit()
    #     win32api.ShellExecute(0, 'open', 'TextAnalysisTool.NET.exe', path1, '' , 1)
        
    def AFAnaLogFileSelectFunc(self):
        self.AFLogFolderSelEntry.delete(0, tk.END)
        self.AFLogFileSelEntry.config(state=tk.NORMAL)
        self.AFLogFolderSelEntry.config(state=tk.DISABLED)
        self.AFLogAnaFileName = askopenfilename()
        self.AFLogAnaSelectedLogFileName.set(self.AFLogAnaFileName)
        # return AFLogAnaFileName
    
    # 调用textanalysistool打开文件
    def AFAnaLogFileOpenWay2(self):
        Logpath = self.AFLogAnaFileName
        win32api.ShellExecute(0, 'open','.\TextAnalysisTool.NET\TextAnalysisTool.NET.exe',Logpath, '' , 1)

    # 调用Notepad++打开文件
    def AFAnaLogFileOpenWay1(self):
        Logpath = self.AFLogAnaFileName
        Toolpath = '.\\Notepad++\\Notepad++.exe'
        win32api.ShellExecute(0, 'open', Toolpath, Logpath, '' , 1)
    
    def AFLogFolderSelFunc(self):
        self.AFLogFileSelEntry.delete(0, tk.END)
        self.AFLogFileSelEntry.config(state=tk.DISABLED)
        self.AFLogFolderSelEntry.config(state=tk.NORMAL)
        self.AFLogFolderSelPath =askdirectory()
        self.AFLogFolderSelShowPath.set(self.AFLogFolderSelPath)


    def AFLogExtPDDriverCheck(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if (("pdaf".lower() in line.lower())):
                        #print("the content of line is %s" % line)
                        logcontent = logcontent + line
        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if (("pdaf".lower() in line.lower())):
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"pdaf": "pink",
                    "PD enable":"yellow"}
        self.AFLogAnalysisShow(keyColor, logcontent)

    def AFSAGCompKeywords(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry2.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName2.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if "af_util_calculate_lens_sag_comp".lower() in line.lower() or \
                        "af_map_output_params".lower() in line.lower() or \
                        "af_util_get_lens_focus_distance".lower() in line.lower() or \
                        "lens pos".lower() in line.lower():
                        #print("the content of line is %s" % line)
                        logcontent = logcontent + line

        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if "af_util_calculate_lens_sag_comp".lower() in line.lower() or \
                                "af_map_output_params".lower() in line.lower() or \
                                "af_util_get_lens_focus_distance".lower() in line.lower() or \
                                "lens pos".lower() in line.lower():
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"af_util_calculate_lens_sag_comp": "green",
                    "af_map_output_params": "pink",
                    "af_util_get_lens_focus_distance":"yellow",
                    "lens pos":"pink"}
        self.AFLogAnalysisShow(keyColor, logcontent)
    
    def AFTableKeywords(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry1.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if (("af_fullsweep_srch_far_to_near".lower() in line.lower())):
                            #print("the content of line is %s" % line)
                            logcontent = logcontent + line
        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if (("af_fullsweep_srch_far_to_near".lower() in line.lower())):
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"af_fullsweep_srch_far_to_near": "pink",
                        "Final_lens_pos":"yellow"}
        self.AFLogAnalysisShow(keyColor, logcontent)  


    def AFLogExtNvPathCheck(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if (("updateNVRAM".lower() in line.lower())):
                        #print("the content of line is %s" % line)
                        logcontent = logcontent + line
        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if (("updateNVRAM".lower() in line.lower())):
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"updateNVRAM": "green",
                    "Path":"red"}
        self.AFLogAnalysisShow(keyColor, logcontent)

    def AFLogExtAFPerformanceComfirm(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if ("af_fullsweep_srch_far_to_near".lower() in line.lower()) or \
                    ("af_fullsweep_check_for_max_fv".lower() in line.lower()):
                        #print("the content of line is %s" % line)
                        logcontent = logcontent + line
        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if ("af_fullsweep_srch_far_to_near".lower() in line.lower()) or \
                                    ("af_fullsweep_check_for_max_fv".lower() in line.lower()):
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"af_fullsweep_srch_far_to_near": "blue",
                    "af_fullsweep_check_for_max_fv":"red"}
        self.AFLogAnalysisShow(keyColor, logcontent)

    def AFLogExtPDCaliCheck(self):
        logcontent = ""
        if len(self.AFLogExtractlogSelectFileEntry.get()) != 0:
            self.AFExtractLogFileName = self.AFExtractSelectedLogFileName.get()
            if len(self.AFExtractLogFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFExtractLogFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if "pdlib".lower() in line.lower() or \
                        "PDLibProcess".lower() in line.lower() or \
                        "af_pdaf_proc_pd_single".lower() in line.lower() or \
                        "defocus".lower() in line.lower():
                        #print("the content of line is %s" % line)
                        logcontent = logcontent + line

        elif len(self.AFLogExtSelLogFolderEntry.get()) != 0:
            print("folder path:%s" % self.AFExtLogsFolderPath)
            for root, dirs, files in os.walk(self.AFExtLogsFolderPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line in lines:
                            if "pdlib".lower() in line.lower() or \
                                "PDLibProcess".lower() in line.lower() or \
                                "af_pdaf_proc_pd_single".lower() in line.lower() or \
                                "defocus".lower() in line.lower():
                                logcontent = logcontent + line

            print("logcontent:%s" % logcontent)

        keyColor = {"pdlib": "green",
                    "PDLibProcess": "red",
                    "af_pdaf_proc_pd_single":"blue",
                    "defocus":"pink"}
        self.AFLogAnalysisShow(keyColor, logcontent)

    def AFLogAnaCheckedFunc(self):

        if len(self.AFLogFileSelEntry.get()) != 0:
            self.AFLogAnaFileName = self.AFLogAnaSelectedLogFileName.get()
            if len(self.AFLogAnaFileName) == 0:
                tk.messagebox.showinfo("信息", "请选择Log文件")
                return

            with open(self.AFLogAnaFileName, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if self.AFLogFiltKeyWord1.get() == 1:
                        if "af_value_monitor".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_value_monitor':'#FFCOCB'})                       
                    if self.AFLogFiltKeyWord2.get() == 1:
                        if "af_pdaf_monitor".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_pdaf_monitor': '#DC143C'})
                    if self.AFLogFiltKeyWord3.get() == 1:
                        if "af_process".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_process': '#FF0000'})
                    if self.AFLogFiltKeyWord4.get() == 1:
                        if "af_single_hj".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_single_hj': '#DB7093'})
                    if self.AFLogFiltKeyWord5.get() == 1:
                        if "curve_fitting".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'curve_fitting': '#FF69B4'})
                    if self.AFLogFiltKeyWord6.get() == 1:
                        if "Setting focus mode to".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'Setting focus mode to': '#FF1493'})
                    if self.AFLogFiltKeyWord7.get() == 1:
                        if "af_pdaf_get_fine_range".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_pdaf_get_fine_range': '#C71585'})
                    if self.AFLogFiltKeyWord8.get() == 1:
                        if "finescan".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'finescan': '#DA70D6'})
                    if self.AFLogFiltKeyWord9.get() == 1:
                        if "pre_scan_algo".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'pre_scan_algo': '#D8BFD8'})
                    if self.AFLogFiltKeyWord10.get() == 1:
                        if "af_caf_search".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_caf_search': '#DDA0DD'})
                    if self.AFLogFiltKeyWord11.get() == 1:
                        if "af_pdaf_proc_pd_single".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_pdaf_proc_pd_single': '#EE82EE'})
                    if self.AFLogFiltKeyWord12.get() == 1:
                        if "af_haf_fine_search".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_haf_fine_search': '#FF00FF'})
                    if self.AFLogFiltKeyWord13.get() == 1:
                        if "is_trig_refocus".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'is_trig_refocus': '#8B008B'})
                    if self.AFLogFiltKeyWord14.get() == 1:
                        if "change ratio".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'change ratio': '#800080'})
                    if self.AFLogFiltKeyWord15.get() == 1:
                        if "flat".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'flat': '#BA55D3'})
                    if self.AFLogFiltKeyWord16.get() == 1:
                        if "needed_rev_scan_at_fail".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'needed_rev_scan_at_fail': '#9400D3'})
                    if self.AFLogFiltKeyWord17.get() == 1:
                        if "Converge done".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'Converge done': '#9932CC'})
                    if self.AFLogFiltKeyWord18.get() == 1:
                        if "ALGO Complete".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'ALGO Complete': '#4B0082'})
                    if self.AFLogFiltKeyWord19.get() == 1:
                        if "spotlight".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'spotlight': '#8A2BE2'})
                    if self.AFLogFiltKeyWord20.get() == 1:
                        if "min_max".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'min_max': '#9370DB'})
                    if self.AFLogFiltKeyWord21.get() == 1:
                        if "going to final position".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'going to final position': '#7B68EE'})
                    if self.AFLogFiltKeyWord22.get() == 1:
                        if "af_generate_sad".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_generate_sad': '#6A5ACD'})
                    if self.AFLogFiltKeyWord23.get() == 1:
                        if "af_logic_drive".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'af_logic_drive': '#483D8B'})
                    if self.AFLogFiltKeyWord24.get() == 1:
                        if "PublishPDLibOutput".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'PublishPDLibOutput': '#E6E6FA'})
                    if self.AFLogFiltKeyWord25.get() == 1:
                        if "pdlib".lower() in line.lower():
                            self.AFLogFilterContents = self.AFLogFilterContents + line
                            self.AFLogFilterKeyWordsColor.update({'pdlib': '#0000FF'})
        elif len(self.AFLogFolderSelEntry.get()) != 0:
            filesNum =0
            for root, dirs, files in os.walk(self.AFLogFolderSelPath):
                print("files:%s" % files)
                for file in files:
                    print("file:%s" % file)
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            filesNum = filesNum + 1
                            if filesNum >=5:
                                break
                            lines = f.readlines()
                            for line in lines:
                                if self.AFLogFiltKeyWord1.get() == 1:
                                    if "af_value_monitor".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_value_monitor':'#FFCOCB'})                       
                                if self.AFLogFiltKeyWord2.get() == 1:
                                    if "af_pdaf_monitor".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_monitor': '#DC143C'})
                                if self.AFLogFiltKeyWord3.get() == 1:
                                    if "af_process".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_process': '#FF0000'})
                                if self.AFLogFiltKeyWord4.get() == 1:
                                    if "af_single_hj".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_single_hj': '#DB7093'})
                                if self.AFLogFiltKeyWord5.get() == 1:
                                    if "curve_fitting".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'curve_fitting': '#FF69B4'})
                                if self.AFLogFiltKeyWord6.get() == 1:
                                    if "Setting focus mode to".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'Setting focus mode to': '#FF1493'})
                                if self.AFLogFiltKeyWord7.get() == 1:
                                    if "af_pdaf_get_fine_range".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_get_fine_range': '#C71585'})
                                if self.AFLogFiltKeyWord8.get() == 1:
                                    if "finescan".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'finescan': '#DA70D6'})
                                if self.AFLogFiltKeyWord9.get() == 1:
                                    if "pre_scan_algo".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'pre_scan_algo': '#D8BFD8'})
                                if self.AFLogFiltKeyWord10.get() == 1:
                                    if "af_caf_search".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_caf_search': '#DDA0DD'})
                                if self.AFLogFiltKeyWord11.get() == 1:
                                    if "af_pdaf_proc_pd_single".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_proc_pd_single': '#EE82EE'})
                                if self.AFLogFiltKeyWord12.get() == 1:
                                    if "af_haf_fine_search".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_haf_fine_search': '#FF00FF'})
                                if self.AFLogFiltKeyWord13.get() == 1:
                                    if "is_trig_refocus".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'is_trig_refocus': '#8B008B'})
                                if self.AFLogFiltKeyWord14.get() == 1:
                                    if "change ratio".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'change ratio': '#800080'})
                                if self.AFLogFiltKeyWord15.get() == 1:
                                    if "flat".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'flat': '#BA55D3'})
                                if self.AFLogFiltKeyWord16.get() == 1:
                                    if "needed_rev_scan_at_fail".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'needed_rev_scan_at_fail': '#9400D3'})
                                if self.AFLogFiltKeyWord17.get() == 1:
                                    if "Converge done".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'Converge done': '#9932CC'})
                                if self.AFLogFiltKeyWord18.get() == 1:
                                    if "ALGO Complete".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'ALGO Complete': '#4B0082'})
                                if self.AFLogFiltKeyWord19.get() == 1:
                                    if "spotlight".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'spotlight': '#8A2BE2'})
                                if self.AFLogFiltKeyWord20.get() == 1:
                                    if "min_max".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'min_max': '#9370DB'})
                                if self.AFLogFiltKeyWord21.get() == 1:
                                    if "going to final position".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'going to final position': '#7B68EE'})
                                if self.AFLogFiltKeyWord22.get() == 1:
                                    if "af_generate_sad".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_generate_sad': '#6A5ACD'})
                                if self.AFLogFiltKeyWord23.get() == 1:
                                    if "af_logic_drive".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_logic_drive': '#483D8B'})
                                if self.AFLogFiltKeyWord24.get() == 1:
                                    if "PublishPDLibOutput".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'PublishPDLibOutput': '#E6E6FA'})
                                if self.AFLogFiltKeyWord25.get() == 1:
                                    if "pdlib".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'pdlib': '#0000FF'})
                    except UnicodeDecodeError:
                        with open(os.path.join(root, file)) as f:
                            lines = f.readlines()
                            for line in lines:
                                if self.AFLogFiltKeyWord1.get() == 1:
                                    if "af_value_monitor".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_value_monitor':'#FFCOCB'})                       
                                if self.AFLogFiltKeyWord2.get() == 1:
                                    if "af_pdaf_monitor".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_monitor': '#DC143C'})
                                if self.AFLogFiltKeyWord3.get() == 1:
                                    if "af_process".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_process': '#FF0000'})
                                if self.AFLogFiltKeyWord4.get() == 1:
                                    if "af_single_hj".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_single_hj': '#DB7093'})
                                if self.AFLogFiltKeyWord5.get() == 1:
                                    if "curve_fitting".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'curve_fitting': '#FF69B4'})
                                if self.AFLogFiltKeyWord6.get() == 1:
                                    if "Setting focus mode to".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'Setting focus mode to': '#FF1493'})
                                if self.AFLogFiltKeyWord7.get() == 1:
                                    if "af_pdaf_get_fine_range".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_get_fine_range': '#C71585'})
                                if self.AFLogFiltKeyWord8.get() == 1:
                                    if "finescan".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'finescan': '#DA70D6'})
                                if self.AFLogFiltKeyWord9.get() == 1:
                                    if "pre_scan_algo".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'pre_scan_algo': '#D8BFD8'})
                                if self.AFLogFiltKeyWord10.get() == 1:
                                    if "af_caf_search".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_caf_search': '#DDA0DD'})
                                if self.AFLogFiltKeyWord11.get() == 1:
                                    if "af_pdaf_proc_pd_single".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_pdaf_proc_pd_single': '#EE82EE'})
                                if self.AFLogFiltKeyWord12.get() == 1:
                                    if "af_haf_fine_search".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_haf_fine_search': '#FF00FF'})
                                if self.AFLogFiltKeyWord13.get() == 1:
                                    if "is_trig_refocus".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'is_trig_refocus': '#8B008B'})
                                if self.AFLogFiltKeyWord14.get() == 1:
                                    if "change ratio".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'change ratio': '#800080'})
                                if self.AFLogFiltKeyWord15.get() == 1:
                                    if "flat".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'flat': '#BA55D3'})
                                if self.AFLogFiltKeyWord16.get() == 1:
                                    if "needed_rev_scan_at_fail".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'needed_rev_scan_at_fail': '#9400D3'})
                                if self.AFLogFiltKeyWord17.get() == 1:
                                    if "Converge done".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'Converge done': '#9932CC'})
                                if self.AFLogFiltKeyWord18.get() == 1:
                                    if "ALGO Complete".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'ALGO Complete': '#4B0082'})
                                if self.AFLogFiltKeyWord19.get() == 1:
                                    if "spotlight".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'spotlight': '#8A2BE2'})
                                if self.AFLogFiltKeyWord20.get() == 1:
                                    if "min_max".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'min_max': '#9370DB'})
                                if self.AFLogFiltKeyWord21.get() == 1:
                                    if "going to final position".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'going to final position': '#7B68EE'})
                                if self.AFLogFiltKeyWord22.get() == 1:
                                    if "af_generate_sad".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_generate_sad': '#6A5ACD'})
                                if self.AFLogFiltKeyWord23.get() == 1:
                                    if "af_logic_drive".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'af_logic_drive': '#483D8B'})
                                if self.AFLogFiltKeyWord24.get() == 1:
                                    if "PublishPDLibOutput".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'PublishPDLibOutput': '#E6E6FA'})
                                if self.AFLogFiltKeyWord25.get() == 1:
                                    if "pdlib".lower() in line.lower():
                                        self.AFLogFilterContents = self.AFLogFilterContents + line
                                        self.AFLogFilterKeyWordsColor.update({'pdlib': '#0000FF'})

        self.AFLOGAnalysisWinMainShow(self.AFLogFilterKeyWordsColor, self.AFLogFilterContents)




