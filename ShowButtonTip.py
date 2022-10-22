import tkinter as tk
import tkinter.messagebox
import time
from SelfDefinedConst import buttonConst
# from Interface import initAFADBCmdGui

# -*- coding: UTF-8 -*-

class ShowButtonTip:

    def __init__(self,widget,buttonIndex,timeout=buttonConst.DEFAULT_BUTTONTIP_TIME_DELAY):
        self.widget = widget
        self.buttonIndex = buttonIndex
        self.timeout =  timeout
        self.buttonTipWidow = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind("<Enter>",self.enter)
        self.widget.bind("<Leave>",self.leave)
        # self.widget.bind("<ButtonPress>",self.leave)

    def enter(self,event = None):
        self.x = event.x
        self.y = event.y
        self.buttonSchedule()

    def leave(self,event = None):
        self.buttonUnschedule()
        self.hideButtonTip()

    def buttonSchedule(self):
        self.buttonUnschedule()
        self.id = self.widget.after(self.timeout,self.showButtonTip)

    def buttonUnschedule(self):
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = None

    # def cursorHandler(self,event):
    #     self.curCursorPosition_x = event.x
    #     self.curCursorPostion_y = event.y

    def showButtonTip(self):
        if self.buttonTipWidow:
            return

        x = self.widget.winfo_rootx()  + self.x + buttonConst.DEFAULT_BUTTONTIP_OFFSET_X
        y = self.widget.winfo_rooty()  + self.y + buttonConst.DEFAULT_BUTTONTIP_OFFSET_Y

        self.buttonTipWidow = tk.Toplevel(self.widget)

        try:
            self.buttonTipWidow.wm_overrideredirect(True)
        except:
            print("* Error performing wm_overrideredirect *")

        self.buttonTipWidow.wm_geometry("+%d+%d"% (x,y))
        self.buttonTipWidow.wm_attributes("-topmost",1)

        text = self.showButtonFunctionInfo(self.buttonIndex)

        buttonTipLabel = tk.Label(self.buttonTipWidow,text = text,justify=tk.LEFT,background=buttonConst.BUTTONTIP_BACKGROUND_COLOR,relief=tk.SOLID,borderwidth=1)
        if buttonConst.BUTTONTIP_FONT is not None:
            buttonTipLabel.config(font= buttonConst.BUTTONTIP_FONT)
        buttonTipLabel.pack()

    def hideButtonTip(self):
        if self.buttonTipWidow:
            self.buttonTipWidow.destroy()
        self.buttonTipWidow = None

    def showButtonFunctionInfo(self,buttonIndex):
        if buttonIndex ==buttonConst.SAVE_PATH_BUTTON:
            messages="功能：选择文件需要保存的路径"
        elif buttonIndex ==buttonConst.PULL_RAW_BUTTON:
            messages="功能：从手机中导出RAW图 默认路径：/data/vendor/camera_dump"
        elif buttonIndex == buttonConst.PULL_PICTURES_BUTTON:
            messages="功能：从手机中导出图片 默认位置:/sdcard/DCIM/Camera"
        elif buttonIndex == buttonConst.PULL_LOG_BUTTON:
            messages="功能：从手机中导出LOG 默认位置:/data/debuglogger/mobilelog"
        elif buttonIndex == buttonConst.PULL_MIND_PATH_BUTTON:
            messages="功能：导出手机内存(自定义手机内存路径)中数据,与Set Nvram Path对应"
        elif buttonIndex == buttonConst.EN_DUMP_BUTTON:
            messages="功能：开启Dump Raw文件功能"
        elif buttonIndex == buttonConst.CLEAR_DUMP_RAW_BUTTON:
            messages="功能：清除手机中Dump的Raw文件"
        elif buttonIndex == buttonConst.SET_NVRAM_PATH_PULLING_DATA_BUTTON:
            messages="功能：设置导出数据的路径(手机内存路径),与Pull Fixed Nvran's对应"
        elif buttonIndex == buttonConst.CLEAR_NVRAM_LOGS_BUTTON:
            messages="功能：清除手机中的log 默认:/data/debuglogger"
        elif buttonIndex ==buttonConst.CLEAR_NVRAM_BUTTON:
            messages="功能：手机连接过CCT以后,push so进手机不生效,需要清除Nvram"
        elif buttonIndex ==buttonConst.SWITCH_CAMERA_BUTTON:
            messages="功能：开启多颗模组之间切换功能"
        elif buttonIndex ==buttonConst.CAM_INFO_BUTTON:
            messages="功能：读取模组信息"
        elif buttonIndex ==buttonConst.CLEAR_IMAGE_BUTTON:
            messages="功能：清除手机中图片"
        elif buttonIndex ==buttonConst.AF_LOG_EN_BUTTON:
            messages="功能：开启AF LOG"
        elif buttonIndex ==buttonConst.AF_LOGCAT_BUTTON:
            messages="功能：抓取AF LOG"
        elif buttonIndex ==buttonConst.FULLSCAN_DISABLE_BUTTON:
            messages="功能：关闭AF的FullSweep功能"
        elif buttonIndex ==buttonConst.FULLSCAN_EN_BUTTON:
            messages="功能：开启AF的FullSweep功能"
        elif buttonIndex == buttonConst.AF_LOG_WITH_WATERMARK_EN_BUTTON:
            messages="功能：开启AF Log并显示水印"
        elif buttonIndex ==buttonConst.HW_STATISTIC_EN_BUTTON:
            messages="功能：开启AF的HW Statistic功能"
        elif buttonIndex ==buttonConst.PDAF_LOG_EN_BUTTON:
            messages="功能：开启PDAF的LOG功能"
        elif buttonIndex == buttonConst.AF_PARAMETER_EFFECTIVE_PATH_BUTTON:
            messages="开启fullsweep=3，绘制fv曲线，观察两个峰值"+chr(13)+\
            "也就是两个peak点之间的差距，是否小于10以内"+chr(13)+\
            "注意：做完这一步之后请点击AF-ADB-Cmd主页中的AF Fullsweep Disable按钮"
        elif buttonIndex == buttonConst.AF_PERFORMANCE_PRECHECK_ENABLE_BUTTON:
            messages="功能：抓取显示AF Performance的log,使能"
        elif buttonIndex == buttonConst.AF_PDCALI_PRECHECK_GEN_10STEP_BUTTON:
            messages="功能：根据填入的OTP Infinity和OTP Macro数据,生成PD calibration所需的10个step"
        elif buttonIndex == buttonConst.AF_PDCALI_SELECT_SINGLE_LOG_FILE_BUTTON:
            messages="功能：选择要分析的log文件,单个log文件"
        elif buttonIndex == buttonConst.AF_PDCALI_SELECT_LOGS_FOLDER_BUTTON:
            messages="功能：选择要分析的log文件所在的目录,可以分析多个log文件。"+chr(13)+\
            "因性能原因,最多可解析5个文件。"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_OTP_DRVIER_CHECK_BUTTON:
            messages="功能：从log中直接提取出OTP数据"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_ACCGYRO_DRIVER_CHECK_BUTTON:
            messages="功能：从log中直接提取出跟Acce和Gyro相关的数据"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_PD_DRIVER_CHECK_BUTTON:
            messages="功能：从log中直接提取出跟PD Driver相关的数据"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_PARAMETER_CODE_PATH_BUTTON:
            messages="功能：从log中提取出AF参数在代码中的路径"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_PERFORMANCE_CONFIRM_BUTTON:
            messages="功能：从log中提取出与Actuator Hysteresis相关的参数"
        elif buttonIndex == buttonConst.AF_LOG_EXTRACT_PDCALI_CHECK_BUTTON:
            messages="功能：从log中提取出与PD Calibration Check相关的参数"
        elif buttonIndex == buttonConst.AF_OTP_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="功能：AF OTP CHECK"+chr(13)+\
                    "方法："+chr(13)+"1.点击AF OPT DUMP Enable按钮"+chr(13)+\
                    "2.进入相机,随便拍一张照片在手机里"+chr(13)+\
                    "3.点击AF OPT DUMP Disable"
        elif buttonIndex == buttonConst.AF_OTP_INFO_PULL_BUTTON:
            messages="将手机otp信息导出到OTP_Info文件夹中"
        elif buttonIndex == buttonConst.AF_ACC_GYRO_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="关闭otp dump"
        elif buttonIndex == buttonConst.AF_PD_DRIVER_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="功能：PDAF驱动检查"+chr(13)+\
                    "方法："+chr(13)+"1.支架固定手机，距离高对比图15-30cm"+chr(13)+\
                    "2.点击按钮打开log"+chr(13)+\
                    "3.进入相机拍照"+chr(13)+\
                    "4.切换到video模式并录像"+chr(13)+\
                    "5.停止录像并停止log抓取"+chr(13)+\
                    "检验方法和标准："+chr(13)+\
                    "打开AF_log,搜索关键字PDAF"
        elif buttonIndex == buttonConst.AF_FV_STABLE_TIME_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="功能：FV稳定时间检查"+chr(13)+\
                    "方法："+chr(13)+"1.支架固定手机，距离高对比图25cm,光源亮度设置为300lux"+chr(13)+\
                    "2.点击按钮打开log,并手动进入手机工模开启log"+chr(13)+\
                    "3.进入相机拍照,并等待5分钟待模组温度稳定"+chr(13)+\
                    "4.点击屏幕中心，然后拍照"+chr(13)+\
                    "5.导出图片,CCT工具->AF Calibration->Golden Check->Check Stability"+chr(13)+\
                    "6.Browse选择图片,点击check"+chr(13)+\
                    "检验方法和标准："+chr(13)+\
                    "1.查看Check Result为pass还是Fail"+chr(13)+\
                    "2.若为fail需要细查：滚动鼠标放大图片,每一个lens位置,"+chr(13)+\
                    "包含10个FV值,必须保持第2个到第10个非常接近,若第2个"+chr(13)+\
                    "到第10个差异大,需要模组厂介入分析"
        elif buttonIndex == buttonConst.AF_OTP_LINEARITY_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="功能：AF OTP和线性检测"+chr(13)+\
                    "方法："+chr(13)+"1.支架固定手机,光源亮度设置为300lux"+chr(13)+\
                    "2.按照OTP远焦距离,对着高对比图拍FullScan"+chr(13)+\
                    "3.按照OTP微距距离,对着高对比图拍FullScan"+chr(13)+\
                    "4.按照超微距距离(OTP微距距离-1cm),对着高对比图拍FullScan"+chr(13)+\
                    "5.在实际远焦距离拍FullScan(如拍远处建筑物)"+chr(13)+\
                    "6.导出图片,CCT工具->AF Calibration->Golden Check->Check Linearity"+chr(13)+\
                    "7.Browse选择对应的4张图片"+chr(13)+\
                    "检验方法和标准："+chr(13)+\
                    "线性检测标准:看四张曲线图是否平滑,若不平滑,需要请模组厂确认"+chr(13)+\
                    "OTP检测标准:点击check,若Check Result为pass则表示OK"+chr(13)+\
                    "若OTP检测fail,需要模组厂改进质量,需要模组厂提供200颗模组的"+chr(13)+\
                    "检测报告,来检测OTP的一致性"
        elif buttonIndex == buttonConst.AF_PD_CALI_CHECK_ENABLE_DATA_COLLECT_BUTTON:
            messages="功能：PD调试检测"+chr(13)+\
                    "使用方法："+chr(13)+\
                    "1.支架固定手机,需要保证当前环境拍出来的照片ISO<200"+chr(13)+\
                    "2.对着棱形图案20cm"+chr(13)+\
                    "3.将OTP Infinity和OTP Macro数据填入相应位置"+chr(13)+\
                    "4.执行Gen,会生成10个Step数据(Idx0-Idx9)"+chr(13)+\
                    "5.连上手机，点击Move Lens,会自动执行10个step，在手机中生成相应的log"+chr(13)+\
                    "6.导出log"+chr(13)+\
                    "7.在AF log Extract区域选择log路径"+chr(13)+\
                    "8.点击PD Calibration Check,会自动解析出相应的log"+chr(13)+\
                    "9.将log中数据填入:AF_Basic_Flow_.xlsx-> PD Calibration Check表格内相应位置"+chr(13)+\
                    "10.表格会自动检查PD线性度是否满足需求"
        elif buttonIndex == buttonConst.AF_PDCALI_PRECK_MOVE_LENS_BUTTON:
            messages="功能：点击,指令推动lens走完10个Step,"
        elif buttonIndex == buttonConst.AF_PD_CALI_DISABLE_MANUAL_MOVE_LENS_BUTTON:
            messages="功能：disable 手动推动lens"
        elif buttonIndex == buttonConst.AF_TABLE_DO_FULL_SCAN_BUTTON:
            messages="功能：基础调试2--AF Table调试"+chr(13)+\
                    "使用方法："+chr(13)+\
                    "1.支架固定手机"+chr(13)+\
                    "2.设置环境亮度为300lux,对着高对比图ISO12233,按照如下距离拍FullSweep"+chr(13)+\
                    "golden模组:7、10、14、20、30、40、50、60、120、500cm"+chr(13)+\
                    "分别抓取各个距离下fullsweep的log并以距离重命名log"
        elif buttonIndex == buttonConst.AF_LOGANALYSIS_OPEN_WITH_TEXTANALYSISTOOL:
            messages="功能:用TextAnalysisTool.NET工具打开log" +chr(13)+\
                     "Tip:AF关键词可以加载当前目录下AF_Keywords_filter" +chr(13)+\
                     "    文件夹下的tat文件"+chr(13)+\
                     "AF Keywords也可自行创建，文件中仅供参考"
        return  messages

    def buttonBindInfo(self,buttonName,IdxButton):
        time.sleep(2)
        buttonName.bind("<Enter>",func=lambda buttonIndex: self.showButtonFunctionInfo(buttonIndex,IdxButton))


