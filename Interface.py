import tkinter as tk
# from tkinter import *
from tkinter import Canvas
from tkinter import ttk
from ShowButtonTip import ShowButtonTip
from SelfDefinedConst import buttonConst
from AFModuleFunc import AFModuleFunc
from PIL import Image,ImageTk
import _thread
# -*- coding: UTF-8 -*-

class  Interface:
    def __init__(self):
        self.MTKTITLE = "Qualcomm_AF Tool"
        self.TOOLWIDTH = 800
        self.TOOLHEIGHT = 550


        self.AFAdbCmdFrame = None
        self.AFPreCheckFrame = None
        self.AFBasicCaliFrame = None
        self.AFLOGAnalysisFrame = None

    def initialGUI(self):
        def changeTag(tag):
            # pass
            self.AFAdbCmdFrame.pack_forget()
            self.AFPreCheckFrame.pack_forget()
            self.AFBasicCaliFrame.pack_forget()
            self.AFLOGAnalysisFrame.pack_forget()
            if tag == 0:
                self.AFAdbCmdFrame.pack(fill = tk.X)
            elif tag == 1:
                self.AFPreCheckFrame.pack(fill = tk.X)
            elif tag == 2:
                self.AFBasicCaliFrame.pack(fill = tk.X)
            elif tag == 3:
                self.AFLOGAnalysisFrame.pack(fill = tk.X)

        def changeType(tag):
            pass

        #implemention the main GUI 执行界面
        def initPagenationGui(pagenationFrame):
            tag = tk.IntVar()
            tagWidth = 25
            tk.Radiobutton(pagenationFrame,text = "AF-ADB-Cmd",command=lambda:changeTag(0),width=tagWidth,variable=tag,value=0,bd=1,indicatoron=0).grid(column=0,row=1)
            tk.Radiobutton(pagenationFrame,text="AF-PreCheck",command=lambda:changeTag(1),width=tagWidth,variable=tag,value=1,bd=1,indicatoron=0).grid(column=1,row=1)
            tk.Radiobutton(pagenationFrame,text="AF-Basic-Calibration",command=lambda:changeTag(2),width=tagWidth,variable=tag,value=2,bd=1,indicatoron=0).grid(column=2,row=1)
            tk.Radiobutton(pagenationFrame,text="AF-LOG-Analysis",command=lambda:changeTag(3),width=tagWidth,variable=tag,value=3,bd=1,indicatoron=0).grid(column=3,row=1)
            # FunctionsRadioButton=tk.Radiobutton(pagenationFrame,text="AF-Basic-Calibration",command=lambda:changeTag(2),width=tagWidth,variable=tag,value=2,bd=1,indicatoron=0)
            # FunctionsRadioButton.grid(column=2,row=1)
            # AFRadioButton=tk.Radiobutton(pagenationFrame,text="AF-LOG-Analysis",command=lambda:changeTag(3),width=tagWidth,variable=tag,value=3,bd=1,indicatoron=0)
            # AFRadioButton.grid(column=3,row=1)

        # the gui of AF-ADB-Cmd
        def initAFADBCmdGui(AFAdbCmdBasicFrame):
            AFAllFunc = AFModuleFunc()
            AFADBFrame = tk.LabelFrame(AFAdbCmdBasicFrame, borderwidth=2, text="AF ADB Command",labelanchor="n")
            AFADBFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH, padx=2, pady=2)

            AFFullScanFrame = tk.Frame(AFADBFrame)
            AFFullScanFrame.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
            # AF FullScan Enable Button
            AFFullScanButton = tk.Button(AFFullScanFrame,text="AF FullSweep Enable",width=20,command=AFAllFunc.AFFullScanEnable)
            AFFullScanButton.pack(side=tk.LEFT,fill=tk.X)
            ShowButtonTip(AFFullScanButton, buttonConst.FULLSCAN_EN_BUTTON)
            # AF FullScan Disable Button
            AFFullScanButton = tk.Button(AFFullScanFrame,text="AF FullSweep Disable",width=20,command=AFAllFunc.AFFullScanDisable)
            AFFullScanButton.pack(side=tk.LEFT,fill=tk.X)
            ShowButtonTip(AFFullScanButton, buttonConst.FULLSCAN_DISABLE_BUTTON)
            #Open AF Log Button
            AFOpenLogButton = tk.Button(AFFullScanFrame, text="Open AF Log",width=20, command=AFAllFunc.AFLogEnable)
            AFOpenLogButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFOpenLogButton, buttonConst.AF_LOG_EN_BUTTON)
            #AF Logcat Button
            AFOpenLogButton = tk.Button(AFFullScanFrame, text="AF Logcat",width=20, command=AFAllFunc.AFLogcat)
            AFOpenLogButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFOpenLogButton, buttonConst.AF_LOGCAT_BUTTON)
            #Show Water Mark button
            AFOpenLogWithWaterMarkButton = tk.Button(AFFullScanFrame, text="Show Water Mark ",width=20, command=AFAllFunc.AFLogEnableWithWaterMark)
            AFOpenLogWithWaterMarkButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFOpenLogWithWaterMarkButton, buttonConst.AF_LOG_WITH_WATERMARK_EN_BUTTON)

            #AF PUll LOG
            AFPullFrame = tk.Frame(AFADBFrame)
            AFPullFrame.pack(side=tk.TOP, fill=tk.X,pady=2)
            AFPullFilesFrame = tk.LabelFrame(AFPullFrame, borderwidth=2, text=None,labelanchor="n")
            AFPullFilesFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH,pady=10)
            AFPullSelectPathFrame = tk.Frame(AFPullFilesFrame)
            AFPullSelectPathFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
            # select pulled path button
            AFPullMtkLogSelectFileButton = tk.Button(AFPullSelectPathFrame, text="Select Pull Path", command=AFAllFunc.AFPullSelectPath)
            AFPullMtkLogSelectFileButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFPullMtkLogSelectFileButton, buttonConst.SAVE_PATH_BUTTON)
            AFAllFunc.savePathEntry = tk.Entry(AFPullSelectPathFrame, width=50, textvariable=AFAllFunc.pullFrameSavePath)
            AFAllFunc.savePathEntry.pack(side=tk.LEFT,padx=2)

            #PULL_LOG_BUTTON
            AFPullButtonsFrame = tk.Frame(AFPullFilesFrame)
            AFPullButtonsFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
            AFAllFunc.AFPullMtkLogFuncButton = tk.Button(AFPullButtonsFrame, text="Pull Logs",width=15,command=AFAllFunc.AFPullMTKLogFunc)
            AFAllFunc.AFPullMtkLogFuncButton.pack(side=tk.LEFT, fill=tk.X) 
            ShowButtonTip(AFAllFunc.AFPullMtkLogFuncButton, buttonConst.PULL_LOG_BUTTON)
            #pull nv's image button
            AFAllFunc.AFPullImagesButton = tk.Button(AFPullButtonsFrame, text="Pull Images",width=15,command=AFAllFunc.AFPullImagesFunc)
            AFAllFunc.AFPullImagesButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFAllFunc.AFPullImagesButton, buttonConst.PULL_PICTURES_BUTTON)
            #pull raw button
            AFAllFunc.AFPullRAWButton = tk.Button(AFPullButtonsFrame, text="Pull Raws", width=15,command=AFAllFunc.AFPullRawFunc)
            AFAllFunc.AFPullRAWButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFAllFunc.AFPullRAWButton, buttonConst.PULL_RAW_BUTTON)
             #clear Cam log button
            AFADBCmdClearLogButton = tk.Button(AFPullFilesFrame, text="Clear Cam Logs", width=15,
                                               command=AFAllFunc.AFADBCmdClearLogFunc)
            AFADBCmdClearLogButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFADBCmdClearLogButton, buttonConst.CLEAR_NVRAM_LOGS_BUTTON)
            #Clear Cam Image Button
            AFADBCmdClearImageButton = tk.Button(AFPullFilesFrame,text="Clear Cam Images",width=15,command=AFAllFunc.AFADBCmdClearImageFunc)
            AFADBCmdClearImageButton.pack(side=tk.LEFT, fill=tk.X)
            ShowButtonTip(AFADBCmdClearImageButton, buttonConst.CLEAR_IMAGE_BUTTON)
            #Clear Cam raw button
            AFADBCmdClearRawButton = tk.Button(AFPullFilesFrame, text="Clear Cam Raws",width=15,command=AFAllFunc.AFADBCmdClearRawFunc)
            AFADBCmdClearRawButton.pack(side=tk.LEFT, fill=tk.X)  
            ShowButtonTip(AFADBCmdClearRawButton, buttonConst.CLEAR_DUMP_RAW_BUTTON)

        #gui of AF-PreCheck
        def initAFPreCheckGui(AFPreCheckbasicFrame):
            AFAllFunc = AFModuleFunc()

            AFPreCheckFrame = tk.LabelFrame(AFPreCheckbasicFrame, borderwidth=2, text="AF PreCheck",labelanchor="n")
            AFPreCheckFrame.pack(expand=tk.YES,side=tk.LEFT, fill=tk.BOTH, padx=2, pady=2)

            AFPreCheckItemFrame = tk.Frame(AFPreCheckFrame)
            AFPreCheckItemFrame.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
            #driver check frame
            driverCheckFrame = tk.LabelFrame(AFPreCheckItemFrame, borderwidth=2, text="Driver Check",labelanchor="n")
            driverCheckFrame.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
            # AF OTP Driver check enable button
            AFOTPDriverCheckFrame = tk.Frame(driverCheckFrame, borderwidth=3)
            AFOTPDriverCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            AFOTPDriverCheckButton = tk.Button(AFOTPDriverCheckFrame, text="AF OTP DUMP Enable",width=33,
                                               command=AFAllFunc.AFOTPDriverCheckEn)
            AFOTPDriverCheckButton.pack(side=tk.TOP, fill=tk.X, padx=2)
            ShowButtonTip(AFOTPDriverCheckButton, buttonConst.AF_OTP_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON)
            AFOTPDriverCheckFrame = tk.Frame(driverCheckFrame, borderwidth=3)
            AFOTPDriverCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            AFOTPDriverCheckButton = tk.Button(AFOTPDriverCheckFrame, text="AF OTP INFO PULL",width=33,
                                               command=AFAllFunc.Pullotpinfo)
            AFOTPDriverCheckButton.pack(side=tk.TOP, fill=tk.X, padx=2)
            ShowButtonTip(AFOTPDriverCheckButton, buttonConst.AF_OTP_INFO_PULL_BUTTON)
            # acce/gyro driver check enable button
            ACC_GyroDriverCheckFrame = tk.Frame(driverCheckFrame, borderwidth=3)
            ACC_GyroDriverCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            ACC_GyroDriverCheckButton = tk.Button(ACC_GyroDriverCheckFrame, text="AF OTP DUMP Disable",width=33,
                                                  command=AFAllFunc.ACC_GyroDriverCheckEn)
            ACC_GyroDriverCheckButton.pack(side=tk.TOP, fill=tk.X, padx=2)
            ShowButtonTip(ACC_GyroDriverCheckButton, buttonConst.AF_ACC_GYRO_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON)
            # pd driver check enable button
            PDDriverCheckFrame = tk.Frame(driverCheckFrame, borderwidth=3)
            PDDriverCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            PDDriverCheckButton = tk.Button(PDDriverCheckFrame, text="PD Driver Check  Enable",width=33,
                                            command=AFAllFunc.PDDriverCheckEn)
            PDDriverCheckButton.pack(side=tk.TOP, fill=tk.X, padx=2)
            ShowButtonTip(PDDriverCheckButton, buttonConst.AF_PD_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON)
            #nvram path enable button
            FVStableTimeCheckFrame = tk.LabelFrame(driverCheckFrame, borderwidth=3,text="Actuator Performance Check",labelanchor="n")
            FVStableTimeCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            # nvram path enable button
            FVStableTimeNvramPathCheckButton = tk.Button(FVStableTimeCheckFrame,text="Actuator Hysteresis Check",width=33,
                                                command=AFAllFunc.FVStableTimeNvramPathCheckEn)
            FVStableTimeNvramPathCheckButton.pack(side=tk.LEFT, fill=tk.X, padx=1)
            ShowButtonTip(FVStableTimeNvramPathCheckButton, buttonConst.AF_PARAMETER_EFFECTIVE_PATH_BUTTON)

            #golden module check frame
            goldenModuleCheckFrame = tk.LabelFrame(AFPreCheckItemFrame,  borderwidth=2,
                                                   text="Golden Module Check", labelanchor="n")
            goldenModuleCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=5)


            golModuCheckRow2Frame = tk.Frame(goldenModuleCheckFrame)
            golModuCheckRow2Frame.pack(side=tk.TOP, fill=tk.X)

            PDCalibrationCheckFrame = tk.Frame(golModuCheckRow2Frame, relief="ridge", borderwidth=3)
            PDCalibrationCheckFrame.pack(side=tk.TOP, fill=tk.X, padx=2, pady=3)
            # pd calibration precheck,begin
            PDCalibrationCheckButton = tk.Button(PDCalibrationCheckFrame, text="PD Calibration Check  Enable",
                                                 command=AFAllFunc.PDCalibrationCheck)
            PDCalibrationCheckButton.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
            ShowButtonTip(PDCalibrationCheckButton, buttonConst.AF_PD_CALI_CHECK_ENABLE_DATA_COLLECT_BUTTON)
            # OTP data
            pdCalOTPFrame = tk.LabelFrame(PDCalibrationCheckFrame,borderwidth=2,text="OTP", labelanchor="n")
            pdCalOTPFrame.pack(side=tk.TOP, fill=tk.X,padx=2)
            pdCalOTPDataFrame = tk.Frame(pdCalOTPFrame)
            pdCalOTPDataFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPInfinityLabel=tk.Label(pdCalOTPDataFrame,text="OTP Infinity:")
            pdCalOTPInfinityLabel.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPInfinityEntry =tk.Entry(pdCalOTPDataFrame,width=5)
            AFAllFunc.pdCalOTPInfinityEntry.pack(side=tk.LEFT,fill=tk.X,padx=1)
            pdCalOTPMacroLable=tk.Label(pdCalOTPDataFrame,text="OTP Macro:")
            pdCalOTPMacroLable.pack(side=tk.LEFT,padx=1)
            AFAllFunc.pdCalOTPMacroEntry = tk.Entry(pdCalOTPDataFrame, width=5)
            AFAllFunc.pdCalOTPMacroEntry.pack(side=tk.LEFT, fill=tk.X,padx=1)
            pdCalOTPStepGenButton=tk.Button(pdCalOTPDataFrame,text="Gen",command=AFAllFunc.PDCalOTPStepGen)
            pdCalOTPStepGenButton.pack(side=tk.LEFT,fill=tk.X,padx=2)
            ShowButtonTip(pdCalOTPStepGenButton, buttonConst.AF_PDCALI_PRECHECK_GEN_10STEP_BUTTON)
            

            ManualAFPositionButton = tk.Button(pdCalOTPDataFrame,text="MF",command=AFAllFunc.MoveLensByManual)
            ManualAFPositionButton.pack(side=tk.RIGHT,fill=tk.X,padx=10)
            AFAllFunc.ManualAFPositionEntry = tk.Entry(pdCalOTPDataFrame, width=8)
            AFAllFunc.ManualAFPositionEntry.pack(side=tk.RIGHT,fill=tk.X,padx=3)

            pdCalOTPSeparator = ttk.Separator(pdCalOTPFrame, orient="horizontal")
            pdCalOTPSeparator.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)

            pdCalOTPStepDataFrame=tk.Frame(pdCalOTPFrame)
            pdCalOTPStepDataFrame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPStepDataLine1Frame =tk.Frame(pdCalOTPStepDataFrame)
            pdCalOTPStepDataLine1Frame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPStep0Label = tk.Label(pdCalOTPStepDataLine1Frame, text="Idx0:")
            pdCalOTPStep0Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx0Entry = tk.Entry(pdCalOTPStepDataLine1Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx0Var)
            AFAllFunc.pdCalOTPStepIdx0Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep1Label = tk.Label(pdCalOTPStepDataLine1Frame, text="Idx1:")
            pdCalOTPStep1Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx1Entry = tk.Entry(pdCalOTPStepDataLine1Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx1Var)
            AFAllFunc.pdCalOTPStepIdx1Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep2Label = tk.Label(pdCalOTPStepDataLine1Frame, text="Idx2:")
            pdCalOTPStep2Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx2Entry = tk.Entry(pdCalOTPStepDataLine1Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx2Var)
            AFAllFunc.pdCalOTPStepIdx2Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)

            pdCalOTPStepDataLine2Frame = tk.Frame(pdCalOTPStepDataFrame)
            pdCalOTPStepDataLine2Frame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPStep3Label = tk.Label(pdCalOTPStepDataLine2Frame, text="Idx3:")
            pdCalOTPStep3Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx3Entry = tk.Entry(pdCalOTPStepDataLine2Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx3Var)
            AFAllFunc.pdCalOTPStepIdx3Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep4Label = tk.Label(pdCalOTPStepDataLine2Frame, text="Idx4:")
            pdCalOTPStep4Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx4Entry = tk.Entry(pdCalOTPStepDataLine2Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx4Var)
            AFAllFunc.pdCalOTPStepIdx4Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep5Label = tk.Label(pdCalOTPStepDataLine2Frame, text="Idx5:")
            pdCalOTPStep5Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx5Entry = tk.Entry(pdCalOTPStepDataLine2Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx5Var)
            AFAllFunc.pdCalOTPStepIdx5Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)

            pdCalOTPStepDataLine3Frame = tk.Frame(pdCalOTPStepDataFrame)
            pdCalOTPStepDataLine3Frame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPStep6Label = tk.Label(pdCalOTPStepDataLine3Frame, text="Idx6:")
            pdCalOTPStep6Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx6Entry = tk.Entry(pdCalOTPStepDataLine3Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx6Var)
            AFAllFunc.pdCalOTPStepIdx6Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep7Label = tk.Label(pdCalOTPStepDataLine3Frame, text="Idx7:")
            pdCalOTPStep7Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx7Entry = tk.Entry(pdCalOTPStepDataLine3Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx7Var)
            AFAllFunc.pdCalOTPStepIdx7Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)
            pdCalOTPStep8Label = tk.Label(pdCalOTPStepDataLine3Frame, text="Idx8:")
            pdCalOTPStep8Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx8Entry = tk.Entry(pdCalOTPStepDataLine3Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx8Var)
            AFAllFunc.pdCalOTPStepIdx8Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)

            pdCalCmdMoveLensButton =tk.Button(pdCalOTPStepDataLine3Frame,text="Manual AF: move lens(idx)",command=AFAllFunc.PDCalCmdMoveLens)
            pdCalCmdMoveLensButton.pack(side=tk.RIGHT, fill=tk.X, padx=10)
            ShowButtonTip(pdCalCmdMoveLensButton, buttonConst.AF_PDCALI_PRECK_MOVE_LENS_BUTTON)

            pdCalOTPStepDataLine4Frame = tk.Frame(pdCalOTPStepDataFrame)
            pdCalOTPStepDataLine4Frame.pack(side=tk.TOP, fill=tk.X, padx=2)
            pdCalOTPStep9Label = tk.Label(pdCalOTPStepDataLine4Frame, text="Idx9:")
            pdCalOTPStep9Label.pack(side=tk.LEFT)
            AFAllFunc.pdCalOTPStepIdx9Entry = tk.Entry(pdCalOTPStepDataLine4Frame, width=5,textvariable=AFAllFunc.pdCalOTPStepIdx9Var)
            AFAllFunc.pdCalOTPStepIdx9Entry.pack(side=tk.LEFT, fill=tk.X, padx=2)

            pdCalCmdMoveLensButton =tk.Button(pdCalOTPStepDataLine4Frame,text="Disable Manual AF", command=AFAllFunc.DisableManualFunc)
            pdCalCmdMoveLensButton.pack(side=tk.RIGHT, fill=tk.X, padx=10)
            # pd calibration precheck,end


            #AF LOG Extract
            AFPreCheckLogOutPutFrame = tk.LabelFrame(AFPreCheckFrame,text="AF Log Extract",labelanchor="n")
            AFPreCheckLogOutPutFrame.pack(side=tk.TOP, fill=tk.X)
            AFLogExtractFileSelectFrame = tk.Frame(AFPreCheckLogOutPutFrame)
            AFLogExtractFileSelectFrame.pack(side=tk.TOP, fill=tk.X)
            #select log file button
            AFLogExtractSelectFileButton = tk.Button(AFLogExtractFileSelectFrame, text="Select Log File",width=16, command=AFAllFunc.AFExtractLogFileSelectFunc)
            AFLogExtractSelectFileButton.pack(side=tk.LEFT, padx=2)
            ShowButtonTip(AFLogExtractSelectFileButton, buttonConst.AF_PDCALI_SELECT_SINGLE_LOG_FILE_BUTTON)
            AFAllFunc.AFLogExtractlogSelectFileEntry = tk.Entry(AFLogExtractFileSelectFrame, width=80, textvariable=AFAllFunc.AFExtractSelectedLogFileName)
            AFAllFunc.AFLogExtractlogSelectFileEntry.pack(side=tk.LEFT, padx=4)
            #select log's folder button
            AFLogExtSelLogFolderFrame = tk.Frame(AFPreCheckLogOutPutFrame)
            AFLogExtSelLogFolderFrame.pack(side=tk.TOP, fill=tk.X)
            AFLogExtSelLogFolderButton = tk.Button(AFLogExtSelLogFolderFrame, text="Select Log's Folder",
                                                     command=AFAllFunc.AFextLogsFolderSelectFunc)
            AFLogExtSelLogFolderButton.pack(side=tk.LEFT, padx=2,pady=3)
            ShowButtonTip(AFLogExtSelLogFolderButton, buttonConst.AF_PDCALI_SELECT_LOGS_FOLDER_BUTTON)
            AFAllFunc.AFLogExtSelLogFolderEntry = tk.Entry(AFLogExtSelLogFolderFrame, width=80,state=tk.DISABLED,
                                                      textvariable=AFAllFunc.AFExtLogsFolderShowPath)
            AFAllFunc.AFLogExtSelLogFolderEntry.pack(side=tk.LEFT, padx=4)

            # #log extract button:AF otp driver check
            AFPreCheckFunsButtonFrame=tk.Frame(AFPreCheckLogOutPutFrame)
            AFPreCheckFunsButtonFrame.pack(side=tk.TOP)

            # log extract button:pd driver check
            AFLogExtPDDriverCheckButton = tk.Button(AFPreCheckFunsButtonFrame, width=30,text="PD Driver Check",command=AFAllFunc.AFLogExtPDDriverCheck)
            AFLogExtPDDriverCheckButton.pack(side=tk.LEFT,padx=2)
            ShowButtonTip(AFLogExtPDDriverCheckButton, buttonConst.AF_LOG_EXTRACT_PD_DRIVER_CHECK_BUTTON)

            # log extract button:af performance confirm
            AFLogExtAFPerformanceButton = tk.Button(AFPreCheckFunsButtonFrame, width=30,text="Actuator Hysteresis Check",
                                                    command=AFAllFunc.AFLogExtAFPerformanceComfirm)
            AFLogExtAFPerformanceButton.pack(side=tk.LEFT,padx=2)
            ShowButtonTip(AFLogExtAFPerformanceButton, buttonConst.AF_LOG_EXTRACT_PERFORMANCE_CONFIRM_BUTTON)

            # log extract button: pd calibration check
            # AFPreCheckFunsButtonRow2Frame = tk.Frame(AFPreCheckLogOutPutFrame)
            # AFPreCheckFunsButtonRow2Frame.pack(side=tk.TOP)
            AFLogExtPDcaliChkButton = tk.Button(AFPreCheckFunsButtonFrame, width=30,text="PD Calibration Check",
                                                     command=AFAllFunc.AFLogExtPDCaliCheck)
            AFLogExtPDcaliChkButton.pack(side=tk.LEFT, padx=2)
            ShowButtonTip(AFLogExtPDcaliChkButton, buttonConst.AF_LOG_EXTRACT_PDCALI_CHECK_BUTTON)


        def initAFBasicCaliGui(AFBasicCaliBaseFrame):
            AFAllFunc = AFModuleFunc()
            #af basic calibration frame
            AFBasicCalibrationFrame = tk.LabelFrame(AFBasicCaliBaseFrame, borderwidth=2,
                                                    text="AF Basic Tuning", labelanchor="n")
            AFBasicCalibrationFrame.pack(expand=tk.YES,side=tk.TOP, fill=tk.BOTH, padx=10)
 

            AFBasicCaliRightFrame = tk.Frame(AFBasicCalibrationFrame,borderwidth=2)
            AFBasicCaliRightFrame.pack(expand=tk.YES,side=tk.TOP,  padx=2)

            AFTableFrame = tk.LabelFrame(AFBasicCaliRightFrame, text="1.Set AF Table",borderwidth=2, labelanchor="n")
            AFTableFrame.pack(side=tk.TOP,  padx=2)
            AFTableButton = tk.Button(AFTableFrame, text="Enable Fullsweep", command=AFAllFunc.AFTableEnableFullScan)
            AFTableButton.pack(side=tk.LEFT, padx=2,pady=2)
            ShowButtonTip(AFTableButton, buttonConst.AF_TABLE_DO_FULL_SCAN_BUTTON)
            AFTableButton2 = tk.Button(AFTableFrame,text="Disable FullSweep ",command=AFAllFunc.AFFullScanDisable)
            AFTableButton2.pack(side=tk.LEFT,fill=tk.X)
            ShowButtonTip(AFTableButton2, buttonConst.FULLSCAN_DISABLE_BUTTON)

            AFLogcatButton = tk.Button(AFTableFrame, text="Logcat", command=AFAllFunc.AFLogcat)
            AFLogcatButton.pack(side=tk.LEFT,padx=2)
            ShowButtonTip(AFLogcatButton, buttonConst.AF_LOGCAT_BUTTON)
            
             #AF LOG Extract
            AFPreCheckLogOutPutFrame = tk.LabelFrame(AFTableFrame,text="AF Log Extract",labelanchor="n")
            AFPreCheckLogOutPutFrame.pack(side=tk.TOP, fill=tk.X)
            AFLogExtractFileSelectFrame = tk.Frame(AFPreCheckLogOutPutFrame)
            AFLogExtractFileSelectFrame.pack(side=tk.TOP, fill=tk.X)
            #select log file button
            AFLogExtractSelectFileButton = tk.Button(AFLogExtractFileSelectFrame, text="Select Log File",width=16, command=AFAllFunc.AFExtractLogFileSelectFunc1)
            AFLogExtractSelectFileButton.pack(side=tk.LEFT, padx=2)
            ShowButtonTip(AFLogExtractSelectFileButton, buttonConst.AF_PDCALI_SELECT_SINGLE_LOG_FILE_BUTTON)
            AFAllFunc.AFLogExtractlogSelectFileEntry1 = tk.Entry(AFLogExtractFileSelectFrame, width=80, textvariable=AFAllFunc.AFExtractSelectedLogFileName)
            AFAllFunc.AFLogExtractlogSelectFileEntry1.pack(side=tk.LEFT, padx=4)
            #select log's folder button
            AFLogExtSelLogFolderFrame = tk.Frame(AFPreCheckLogOutPutFrame)
            AFLogExtSelLogFolderFrame.pack(side=tk.TOP, fill=tk.X)
            AFLogExtSelLogFolderButton = tk.Button(AFLogExtSelLogFolderFrame, text="Select Log's Folder",
                                                     command=AFAllFunc.AFextLogsFolderSelectFunc1)
            AFLogExtSelLogFolderButton.pack(side=tk.LEFT, padx=2,pady=3)
            ShowButtonTip(AFLogExtSelLogFolderButton, buttonConst.AF_PDCALI_SELECT_LOGS_FOLDER_BUTTON)
            AFAllFunc.AFLogExtSelLogFolderEntry = tk.Entry(AFLogExtSelLogFolderFrame, width=80,state=tk.DISABLED,
                                                      textvariable=AFAllFunc.AFExtLogsFolderShowPath)
            AFAllFunc.AFLogExtSelLogFolderEntry.pack(side=tk.LEFT, padx=4)

            AFPreCheckFunsButtonFrame=tk.Frame(AFPreCheckLogOutPutFrame)
            AFPreCheckFunsButtonFrame.pack(side=tk.TOP)
            AFLogExtPDDriverCheckButton = tk.Button(AFPreCheckFunsButtonFrame, width=30,text="Table Configure Keywords",command=AFAllFunc.AFTableKeywords)
            AFLogExtPDDriverCheckButton.pack(side=tk.LEFT,padx=2)
        

            ##AFSAGCompensation(Posture)
            AFPostureCompFrame = tk.LabelFrame(AFBasicCaliRightFrame, borderwidth=2,text="2.AF SAG Compensation", labelanchor="n")
            AFPostureCompFrame.pack(side=tk.TOP, fill=tk.X, pady=5)

            AFPostureCompButton = tk.Button(AFPostureCompFrame, text="Enable Fullsweep", command=AFAllFunc.AFTableEnableFullScan)
            AFPostureCompButton.pack(side=tk.LEFT, fill=tk.X,padx=2,pady=2)
            ShowButtonTip(AFPostureCompButton, buttonConst.AF_POSTURE_COMP_DO_FULLSCAN_BUTTON)

            AFSAGButton = tk.Button(AFPostureCompFrame,text="Disable FullSweep ",command=AFAllFunc.AFFullScanDisable)
            AFSAGButton.pack(side=tk.LEFT,fill=tk.X)
            ShowButtonTip(AFSAGButton, buttonConst.FULLSCAN_DISABLE_BUTTON)

            AFLogcatButton2 = tk.Button(AFPostureCompFrame, text="Logcat", command=AFAllFunc.AFLogcatSAG)
            AFLogcatButton2.pack(side=tk.LEFT,padx=2)
            ShowButtonTip(AFLogcatButton2, buttonConst.AF_LOGCAT_BUTTON)
            
             #AF LOG Extract
            AFPreCheckLogOutPutFrame2 = tk.LabelFrame(AFPostureCompFrame,text="AF Log Extract",labelanchor="n")
            AFPreCheckLogOutPutFrame2.pack(side=tk.TOP, fill=tk.X)
            AFLogExtractFileSelectFrame2 = tk.Frame(AFPreCheckLogOutPutFrame2)
            AFLogExtractFileSelectFrame2.pack(side=tk.TOP, fill=tk.X)
            #select log file button
            AFLogExtractSelectFileButton2 = tk.Button(AFLogExtractFileSelectFrame2, text="Select Log File",width=16, command=AFAllFunc.AFExtractLogFileSelectFunc2)
            AFLogExtractSelectFileButton2.pack(side=tk.LEFT, padx=2)
            ShowButtonTip(AFLogExtractSelectFileButton2, buttonConst.AF_PDCALI_SELECT_SINGLE_LOG_FILE_BUTTON)
            AFAllFunc.AFLogExtractlogSelectFileEntry2 = tk.Entry(AFLogExtractFileSelectFrame2, width=80, textvariable=AFAllFunc.AFExtractSelectedLogFileName2)
            AFAllFunc.AFLogExtractlogSelectFileEntry2.pack(side=tk.LEFT, padx=4)
            #select log's folder button
            AFLogExtSelLogFolderFrame2 = tk.Frame(AFPreCheckLogOutPutFrame2)
            AFLogExtSelLogFolderFrame2.pack(side=tk.TOP, fill=tk.X)
            AFLogExtSelLogFolderButton3 = tk.Button(AFLogExtSelLogFolderFrame2, text="Select Log's Folder",
                                                     command=AFAllFunc.AFextLogsFolderSelectFunc2)
            AFLogExtSelLogFolderButton3.pack(side=tk.LEFT, padx=2,pady=3)
            ShowButtonTip(AFLogExtSelLogFolderButton3, buttonConst.AF_PDCALI_SELECT_LOGS_FOLDER_BUTTON)
            AFAllFunc.AFLogExtSelLogFolderEntry = tk.Entry(AFLogExtSelLogFolderFrame2, width=80,state=tk.DISABLED,
                                                      textvariable=AFAllFunc.AFExtLogsFolderShowPath2)
            AFAllFunc.AFLogExtSelLogFolderEntry.pack(side=tk.LEFT, padx=4)

            AFPreCheckFunsButtonFrame2=tk.Frame(AFPreCheckLogOutPutFrame2)
            AFPreCheckFunsButtonFrame2.pack(side=tk.TOP)
            AFLogExtPDDriverCheckButton2 = tk.Button(AFPreCheckFunsButtonFrame2, width=30,text="SAG Compensation Data",command=AFAllFunc.AFSAGCompKeywords)
            AFLogExtPDDriverCheckButton2.pack(side=tk.LEFT,padx=2)

            #Draw fv curve
            AFfvcurveFrame = tk.LabelFrame(AFBasicCaliRightFrame, borderwidth=2,text="3.Draw FV Curve", labelanchor="n")
            AFfvcurveFrame.pack(side=tk.TOP, fill=tk.X, pady=5)
            #select log file button
            AFLogExtractSelectFileButton3 = tk.Button(AFfvcurveFrame, text="Select Log File",width=16, command=AFAllFunc.AFExtractLogFileSelectFunc3)
            AFLogExtractSelectFileButton3.pack(side=tk.LEFT, padx=2)  
            AFAllFunc.AFLogExtractlogSelectFileEntry3 = tk.Entry(AFfvcurveFrame, width=60, textvariable=AFAllFunc.AFExtractSelectedLogFileName3)
            AFAllFunc.AFLogExtractlogSelectFileEntry3.pack(side=tk.LEFT, padx=4)
            # read log & draw fv curve
            AFreadloganddrawfvButton = tk.Button(AFfvcurveFrame, text="Draw FV",width=10, command=AFAllFunc.Draw_FV)
            AFreadloganddrawfvButton.pack(side=tk.RIGHT, padx=8)

        def initAFLogAnalysisGui(AFLOGAnalysisBasicFrame):
            AFAllFunc = AFModuleFunc()

            # platformOption = tk.StringVar()

            # platformOption.set("平台")
            # platformOptionMenu = tk.OptionMenu(PlatformFrame,platformOption,"SM4250","SM4350","SM6376")
            # platformOptionMenu.pack(side=tk.LEFT)
            # platformOptionMenu.config(state=tk.NORMAL)
            # platformOptionMenu.config(state=tk.DISABLED)
            ##############################################################


            AFLogFileSelectFrame=tk.Frame(AFLOGAnalysisBasicFrame,borderwidth=2)
            AFLogFileSelectFrame.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)

            AFLogLogFile1openway1Button = tk.Button(AFLogFileSelectFrame,text="Open With Notepad++",command=AFAllFunc.AFAnaLogFileOpenWay1)
            AFLogLogFile1openway1Button.pack(side=tk.RIGHT,padx=5)
                                                
            AFLogLogFile1openway2Button = tk.Button(AFLogFileSelectFrame,text="Open With TextanalysisTool",command=AFAllFunc.AFAnaLogFileOpenWay2)
            AFLogLogFile1openway2Button.pack(side=tk.RIGHT,padx=5)
            ShowButtonTip(AFLogLogFile1openway2Button, buttonConst.AF_LOGANALYSIS_OPEN_WITH_TEXTANALYSISTOOL)

            AFLogLogFile1SelectButton = tk.Button(AFLogFileSelectFrame,text="Select AF Log File",width=17,command=AFAllFunc.AFAnaLogFileSelectFunc)
            AFLogLogFile1SelectButton.pack(side=tk.LEFT,padx=5)
            AFAllFunc.AFLogFileSelEntry = tk.Entry(AFLogFileSelectFrame, width=80,
                                                      textvariable=AFAllFunc.AFLogAnaSelectedLogFileName)
            AFAllFunc.AFLogFileSelEntry.pack(side=tk.LEFT, padx=4)

            AFLogSelectFolderFrame=tk.Frame(AFLOGAnalysisBasicFrame,borderwidth=2)
            AFLogSelectFolderFrame.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
            AFLogFolderSelectButton = tk.Button(AFLogSelectFolderFrame, text="Select AF Log Folder",
                                                  command=AFAllFunc.AFLogFolderSelFunc)
            AFLogFolderSelectButton.pack(side=tk.LEFT, padx=5)
            AFAllFunc.AFLogFolderSelEntry = tk.Entry(AFLogSelectFolderFrame, width=80,state=tk.DISABLED,
                                         textvariable=AFAllFunc.AFLogFolderSelShowPath)
            AFAllFunc.AFLogFolderSelEntry.pack(side=tk.LEFT, padx=4)

            AFLogAnaKeyWordFrame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFLogAnaKeyWordFrame.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
            #line1 keyword
            AFlogAnaKeyWordLine1Frame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFlogAnaKeyWordLine1Frame.pack(side=tk.TOP, fill=tk.X)
            AFLogAnaKeyWord1CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine1Frame,text="af_value_monitor",width=20,
                                                         variable=AFAllFunc.AFLogFiltKeyWord1,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord1CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=30)
            AFLogAnaKeyWord3CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine1Frame, text="af_pdaf_monitor",width=15,
                                                         variable=AFAllFunc.AFLogFiltKeyWord2,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord3CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord4CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine1Frame, text="af_process",width=15,
                                                         variable=AFAllFunc.AFLogFiltKeyWord3,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord4CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord5CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine1Frame, text="af_single_hj",width=15,
                                                         variable=AFAllFunc.AFLogFiltKeyWord4,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord5CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord6CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine1Frame, text="curve_fitting",width=15,
                                                         variable=AFAllFunc.AFLogFiltKeyWord5,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord6CheckButton.pack(side=tk.LEFT, fill=tk.X)

            # line2 keyword
            AFlogAnaKeyWordLine2Frame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFlogAnaKeyWordLine2Frame.pack(side=tk.TOP, fill=tk.X)
            AFLogAnaKeyWord7CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine2Frame, text="Setting focus mode to",
                                                         variable=AFAllFunc.AFLogFiltKeyWord6,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord7CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=30)
            AFLogAnaKeyWord8CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine2Frame, text="af_pdaf_get_fine_range",
                                                         variable=AFAllFunc.AFLogFiltKeyWord7,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord8CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=5)
            AFLogAnaKeyWord9CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine2Frame, text="finescan",
                                                         variable=AFAllFunc.AFLogFiltKeyWord8,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord9CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord10CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine2Frame, text="pre_scan_algo", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord9,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord10CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=40)
            AFLogAnaKeyWord11CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine2Frame, text="af_caf_search",
                                                          variable=AFAllFunc.AFLogFiltKeyWord10,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord11CheckButton.pack(side=tk.LEFT, fill=tk.X)

            # line3 keyword
            AFlogAnaKeyWordLine3Frame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFlogAnaKeyWordLine3Frame.pack(side=tk.TOP, fill=tk.X)
            AFLogAnaKeyWord13CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine3Frame, text="af_pdaf_proc_pd_single", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord11,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord13CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=28)
            AFLogAnaKeyWord14CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine3Frame, text="af_haf_fine_search", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord12,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord14CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord15CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine3Frame, text="is_trig_refocus", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord13,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord15CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord16CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine3Frame, text="change ratio", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord14,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord16CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=28)
            AFLogAnaKeyWord18CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine3Frame, text="flat", width=10,padx=10,
                                                          variable=AFAllFunc.AFLogFiltKeyWord15,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord18CheckButton.pack(side=tk.LEFT, fill=tk.X)

            # line4 keyword
            AFlogAnaKeyWordLine4Frame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFlogAnaKeyWordLine4Frame.pack(side=tk.TOP, fill=tk.X)
            AFLogAnaKeyWord19CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine4Frame, text="needed_rev_scan_at_fail", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord16,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord19CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=28)
            AFLogAnaKeyWord20CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine4Frame, text="Converge done", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord17,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord20CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=8)
            AFLogAnaKeyWord22CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine4Frame, text="ALGO Complete",
                                                          variable=AFAllFunc.AFLogFiltKeyWord18,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord22CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord23CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine4Frame, text="spotlight",
                                                          variable=AFAllFunc.AFLogFiltKeyWord19,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord23CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=35)
            AFLogAnaKeyWord24CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine4Frame, text="min_max",
                                                          variable=AFAllFunc.AFLogFiltKeyWord20,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord24CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=3)
            #line5
            AFlogAnaKeyWordLine5Frame = tk.Frame(AFLOGAnalysisBasicFrame, borderwidth=2)
            AFlogAnaKeyWordLine5Frame.pack(side=tk.TOP, fill=tk.X)
            AFLogAnaKeyWord25CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine5Frame, text="going to final position",
                                                          variable=AFAllFunc.AFLogFiltKeyWord21,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord25CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=17)
            AFLogAnaKeyWord2CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine5Frame, text="af_generate_sad", 
                                                         variable=AFAllFunc.AFLogFiltKeyWord22,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord2CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=40)
            AFLogAnaKeyWord12CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine5Frame, text="af_logic_drive", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord23,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord12CheckButton.pack(side=tk.LEFT, fill=tk.X)
            AFLogAnaKeyWord17CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine5Frame, text="PublishPDLibOutput", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord24,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord17CheckButton.pack(side=tk.LEFT, fill=tk.X,padx=30)
            AFLogAnaKeyWord21CheckButton = tk.Checkbutton(AFlogAnaKeyWordLine5Frame, text="pdlib", 
                                                          variable=AFAllFunc.AFLogFiltKeyWord25,onvalue=1,offvalue=0,command=AFAllFunc.AFLogAnaCheckedFunc)
            AFLogAnaKeyWord21CheckButton.pack(side=tk.LEFT, fill=tk.X)

        def enterMainGui(mainWindow):
            pagenationFrame = tk.Frame(mainWindow)
            pagenationFrame.pack(fill=tk.Y,pady=10)
            initPagenationGui(pagenationFrame)

            self.AFAdbCmdFrame = tk.Frame(mainWindow,borderwidth=2)
            self.AFAdbCmdFrame.pack(side=tk.TOP, fill=tk.X)
            self.AFAdbCmdFrame.pack_forget()
            initAFADBCmdGui(self.AFAdbCmdFrame)

            self.AFPreCheckFrame = tk.Frame(mainWindow, borderwidth=2)
            self.AFPreCheckFrame.pack(expand=tk.YES,side=tk.TOP, fill=tk.X)
            self.AFPreCheckFrame.pack_forget()
            initAFPreCheckGui(self.AFPreCheckFrame)

            self.AFBasicCaliFrame = tk.Frame(mainWindow, borderwidth=2)
            self.AFBasicCaliFrame.pack(expand=tk.YES,side=tk.TOP, fill=tk.X)
            self.AFBasicCaliFrame.pack_forget()
            initAFBasicCaliGui(self.AFBasicCaliFrame)

            self.AFLOGAnalysisFrame = tk.LabelFrame(mainWindow,relief="ridge",borderwidth=2,text="AF Basic Log Analysis",labelanchor="n")
            self.AFLOGAnalysisFrame.pack(side=tk.TOP, fill=tk.X)
            self.AFLOGAnalysisFrame.pack_forget()
            initAFLogAnalysisGui(self.AFLOGAnalysisFrame)

        selPlatformWindow = tk.Tk()
        selPlatformWindow.configure(bg='lightgrey')
        selPlatformWindow.title(self.MTKTITLE)

        self.ws = selPlatformWindow.winfo_screenwidth()
        self.hs = selPlatformWindow.winfo_screenheight()
        print("window.winfo_screenwidth():",selPlatformWindow.winfo_screenwidth())
        print("window.winfo_screenheight():",selPlatformWindow.winfo_screenheight())
        x = (self.ws/2) - (self.TOOLWIDTH/2)
        y = (self.hs/2) - (self.TOOLHEIGHT/2)
        print("self.TOOLWIDTH:%d,self.TOOLHEIGHT:%d,x:%d,y:%d" % (self.TOOLWIDTH,self.TOOLHEIGHT,x,y))
        print("self.TOOLWIDTH//2:%d"%(self.TOOLWIDTH//2))
        selPlatformWindow.geometry("%dx%d+%d+%d" % (self.TOOLWIDTH,self.TOOLHEIGHT,x,y))
        selPlatformWindow.resizable(0,0)
        ####### 修改ui
        # selPlatformWindow.resizable(False,False)
        file = Image.open('./Background/QC.jpg')
        file = file.resize((150,80))
        img = ImageTk.PhotoImage(file)
        background = tk.Label(selPlatformWindow, image=img)
        background.image = img
        background.pack(side="bottom",padx=(600,0),pady=(0,10))
        ####### 修改ui

        # platformSelectGUI(selPlatformWindow)

        enterMainGui(selPlatformWindow)

        selPlatformWindow.mainloop()



if __name__ == "__main__":
    window = Interface()
    window.initialGUI()