# !/usr/bin/python3

# IMPORT MODULE
from tkinter import *
from tkinter import messagebox
import time
from time import sleep, gmtime, strftime
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import serial
from functools import partial
import math
from fractions import Fraction
from threading import *
import os
from tkinter import ttk
import awesometkinter as atk
import tkinter.font as font
import openpyxl
import subprocess
import shutil
import RPi.GPIO as GPIO
from ftplib import FTP
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Protection
from openpyxl.styles.borders import Border, Side
from openpyxl.drawing.image import Image as Img
from datetime import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import re
import dns.resolver
import socket
import awesometkinter as atk
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ds1307
import sys
import threading
######################### GLOBAL VARIABLES ############################
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

RESULT_IMAGE_WIDTH = 1024
RESULT_IMAGE_HEIGHT = 768

VOLTAGE_MIN_VALUE = 12
VOLTAGE_MAX_VALUE = 60
MINUTE_MIN_VALUE = 00
MINUTE_MAX_VALUE = 99
SECOND_MIN_VALUE = 00
SECOND_MAX_VALUE = 59


MAX_VOLTAGE_VALUE = 120
DEIVIDE_VOLTAGE_VALUE = 4.68


voltage0_set = 80
m0_set = 0
s0_set = 15
# m0_raw = m0_set
# s0_raw = s0_set


# RELAY_PIN = 20
# BLUE_LIGHT_PIN = 21
# POWER_LED_PIN = 16
POWER_LED_PIN = 13
RELAY_PIN = 26
BLUE_LIGHT_PIN = 19
BUZZER_PIN = 6
RUN_LED_PIN = 16
SENSOR_PIN = 20

############################ GUI DEFINE ###############################
BANDFINDER_CONTROL_BGD_COLOR = "grey30"
APP_BGD_COLOR = "white smoke"
MAIN_TITLE_BGD_COLOR = "#011e24"
MAIN_TITLE_TXT_COLOR = "#00eaff"
MAIN_TITLE_TXT_FONT = ('Arial', 17, 'bold')
MAIN_MENU_BUTTON_BGD_COLOR = "grey50"
MAIN_MENU_BUTTON_TXT_COLOR = "black"
MAIN_MENU_BUTTON_TXT_FONT = ('Arial', 11, 'bold')
MAIN_MENU_BUTTON_ACTIVE_BGD_COLOR = "grey85"
MAIN_FUNCTION_FRAME_BGD_COLOR = "grey85"
EXIT_BUTTON_BGD_COLOR = "#FF4B4B"
MAIN_MENU_LABELFRAME_BGD_COLOR = "grey85"
MAIN_MENU_LABELFRAME_TXT_COLOR = "black"
MAIN_MENU_LABELFRAME_TXT_FONT = ('Arial', 11, 'bold')
MAIN_MENU_LABELFRAME_BORDER_COLOR = "#00eaff"
RUN_BUTTON_BGD_COLOR = "#011e24"
RUN_BUTTON_TXT_COLOR = "#00eaff"
RUN_BUTTON_TXT_FONT = ('Arial', 12, 'bold')
BANDFINDER_FRAME_BGD_COLOR = "grey85"
BANDFINDER_BUTTON_BGD_COLOR = "grey80"
BANDFINDER_BUTTON_TXT_COLOR = "black"
BANDFINDER_BUTTON_TXT_FONT = ('Arial', 10)
FIRSTBAND_COLOR = 'dodger blue'
LASTBAND_COLOR = 'red'
RESULTBAND_COLOR = '#00ba13'

ACCOUNT_ACTIVE_LABEL_TXT_COLOR = "#099c18"
ACCOUNT_INACTIVE_LABEL_TXT_COLOR = "black"
LOGIN_LABEL_BGD_COLOR = "grey85"
LOGIN_LABEL_TXT_FONT = ('Arial', 12, 'bold')
USERPASS_LABEL_BGD_COLOR = "grey85"
USERPASS_LABEL_TXT_COLOR = "black"
USERPASS_LABEL_TXT_FONT = ('Arial', 13)
LOGIN_BUTTON_BGD_COLOR = "#011e24"
LOGIN_BUTTON_TXT_COLOR = "white"
LOGIN_BUTTON_TXT_FONT = ('Arial', 12, 'bold')
LANGUAGE_SAVE_BUTTON_BGD_COLOR = "#011e24"
LANGUAGE_SAVE_BUTTON_TXT_COLOR = "white"
LANGUAGE_SAVE_BUTTON_TXT_FONT = ('Arial', 12, 'bold')
LANGUAGE_COMBOBOX_TXT_FONT = ('Arial', 13)

FOLDERNAMING_FRAME_BGD_COLOR = 'grey70'
FOLDERNAMING_FRAME_TXT_COLOR = 'black'
FOLDERNAME_LABEL_TXT_COLOR = 'black' 
FOLDERNAME_LABEL_TXT_FONT= ('Arial', 15, 'bold')
FOLDERNAME_BUTTON_BGD_COLOR = "#011e24"
FOLDERNAME_BUTTON_TXT_COLOR = 'white'
FOLDERNAME_BUTTON_TXT_FONT = ('Arial', 12, 'bold')

BUTTON_FRAME_BGD_COLOR = "grey75"
SWITCHPAGE_BUTTON_BGD_COLOR = "#011e24"
SWITCHPAGE_BUTTON_TXT_COLOR = "white"
SWITCHPAGE_BUTTON_TXT_FONT = ('Arial', 12, 'bold')

NUMBEROFWELLS_LABEL_TXT_COLOR = 'black'
NUMBEROFWELLS_LABEL_TXT_FONT = ('Arial', 12)
NUMBEROFWELLS_COMBOBOX_TXT_FONT = ('Arial', 12)
WELLTABLE_LABEL_BGD_COLOR = "#011e24"
WELLTABLE_LABEL_TXT_COLOR = "white"
WELLTABLE_LABEL_TXT_FONT = ('Arial', 12)

SETTINGPARA_LABELFRAME_BGD_COLOR = 'white'
SETTINGPARA_LABELFRAME_TXT_COLOR = 'white'
SETTINGPARA_LABELFRAME_TXT_FONT = ('Arial', 12)
SETTINGPARA_ENTRY_TXT_COLOR = "#fd0558"
SETTINGPARA_ENTRY_TXT_FONT = ('Arial', 25, 'bold')

AUTOMAIL_LABEL_TXT_FONT = ('Arial', 12)
AUTOMAIL_ENTRY_TXT_FONT = ('Arial', 12)

AUTOMAILON_BUTTON_BGD_COLOR = "lawn green"
AUTOMAILOFF_BUTTON_BGD_COLOR =  "#FF4B4B"
AUTOMAIL_BUTTON_BGD_COLOR = "grey80"

RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR = "grey80"
RUNSTAGE_LABELFRAME_ACTIVE_BGD_COLOR =  "#91ff00"
RUNSTAGE_LABELFRAME_TXT_COLOR = "#011e24"
RUNSTAGE_LABELFRAME_TXT_FONT = ('Arial', 12, 'bold')
TIMELEFT_LABELFRAME_TXT_FONT = ('Arial', 10)

STAGE_CONTENT_TXT_COLOR = "#0075FC"
STAGE_CONTENT_TXT_FONT = ('Arial', 15)

SENSE_LABEL_TXT_FONT =  ('Arial', 13)
SENSEVALUE_LABEL_BGD_COLOR = "grey25"
SENSEVALUE_LABEL_TXT_FONT = ('Arial', 15)
SENSEVALUE_LABEL_TXT_COLOR = "#0075FC"

CAPTURE_BUTTON_BGD_COLOR = "#011e24"
CAPTURE_BUTTON_TXT_COLOR = "white"
STOP_BUTTON_BGD_COLOR =  "#FF4B4B"
STOP_BUTTON_TXT_COLOR = "black"
CAMMODE_BUTTON_ACTIVE_BGD_COLOR = "#00eaff"
CAMMODE_BUTTON_INACTIVE_BGD_COLOR = "grey65"
CAMMODE_BUTTON_TXT_COLOR = "black"
CAMMODE_BUTTON_TXT_FONT = ('Arial', 11)


############################### Language #################################
MainScreen_Language = {
	"SingleStage Button": ["Single Stage", "Đơn bước"],
	"MultiStage Button": ["Multi Stage", "Đa bước"],
	"Run Button": ["RUN", "CHẠY"],
	"BandFinder Button": ["BAND FINDER", "XÁC ĐỊNH BAND"],
	"Connect Button": ["CONNECT", "KẾT NỐI"],
	"Language Button": ["LANGUAGE", "NGÔN NGỮ"],
	"Exit Button": ["EXIT", "THOÁT"],
	"Run LabelFrame": ["RUN", "CHẠY"],
	"BandFinder LabelFrame": ["BAND FINDER", "XÁC ĐỊNH BAND"],
	"Connect LabelFrame": ["CONNECT", "KẾT NỐI"],
	"Language LabelFrame": ["LANGUAGE", "NGÔN NGỮ"],
	"Open Button": ["Open", "Mở"],
	"Save Button": ["Save", "Lưu"],
	"Check Button": ["Check", "Kiểm tra"],
	"FirstBand Label": ["First band", "Band đầu tiên"],
	"LastBand Label": ["Last band", "Band cuối cùng"],
	"BandSize Label": ["Result band", "Band kết quả"],

	"AccountInactive Label": ["LOGIN", "ĐĂNG NHẬP"],
	"AccountActive Label": ["YOU ARE ALREADY LOGGED IN ✔", "BẠN ĐÃ ĐĂNG NHẬP ✔"],
	"Password Label": ["Password", "Mật khẩu"],
	"Email Label": ["Email", "Email"],
	"HidePass Checkbutton": ["Hide charaters", "Ẩn ký tự"],
	"Login Button": ["Login", "Đăng nhập"],
	"Logout Button": ["Logout", "Đăng xuất"],
	"Save Button": ["Save", "Lưu"],

	"SingleStageFolder LabelFrame": ["[Single Stage]", "[Đơn bước]"],
	"MultiStageFolder LabelFrame": ["[Multi Stage]", "[Đa bước]"],
	"FolderName Label": ["Folder name", "Tên thư mục"],
	"Next Button": ["Next", "Kế tiếp"],
	"Cancel Button": ["Cancel", "Hủy"],
	"Electrophoresis Button": ["Electrophoresis", "Điện di"],

	##### Messagebox #####
	"Exit Confirm": ["Do you want to close the app ?","Bạn có muốn đóng ứng dụng ?"],
	"FirstBand Entry Empty": ["Please enter First band value", "Xin nhập giá trị Band đầu tiên"],
	"LastBand Entry Empty": ["Please enter Last band value", "Xin nhập giá trị Band cuối cùng"],
	"ResultBand Entry Empty": ["Please enter Result band value", "Xin nhập giá trị Band kết quả"],
	"Band Out Value": ["Band size must be between first and last band value.", "Giá trị band phải ở giữa band đầu tiên và cuối cùng."],
	"Save Done": ["Saved.", "Đã lưu."],
	"Login Successful": ["Login Successful", "Đăng nhập thành công"],
	"Login Unsuccessful": ["An error occurred during login, please try again", "Đã có lỗi xảy ra trong quá trình đăng nhập, xin thử lại"],
	"Logout Ask": ["Are you sure you want to Logout ?", "Bạn muốn đăng xuất ?"],
	"FolderName Entry Empty": ["Please enter the folder name", "Xin nhập tên thư mục"],
	"FolderName Exists": ["This folder already exists, do you want to overwrite it ?", "Thư mục đã tồn tại, bạn có muốn ghi đè ?"],
	"Email Empty": ["Please enter the email", "Xin hãy nhập email"],
	"Password Empty": ["Please enter the password", "Xin hãy nhập mật khẩu"],
	"Email Error": ["Email syntax error", "Lỗi cú pháp email"],
	"Email Incorrect": ["Your email address was incorrect\rPlease try again !", "Email của bạn không đúng\rXin thử lại !"],
	"Password Incorrect": ["Your password was incorrect\rPlease try again !", "Mật khẩu của bạn không đúng\rXin thử lại !"],
	"Language Restart": ["The application needs to be restarted to fully apply the new language. Do you want to restart now ?",
						"Ứng dụng cần khởi động lại để chuyển đổi hoàn toàn sang ngôn ngữ mới. Bạn có muốn khởi động lại ngay ?"]
}

SampleNamingScreen_Language = {
	"Setting Label": ["SETTING", "CÀI ĐẶT"],
	"Next Button": ["Next", "Kế tiếp"],
	"Back Button": ["Back", "Trở lại"],
	"NumberOfWells Label": ["Number of wells", "Số lượng giếng"],
	"WellNumber Label": ["No.", "Stt"],
	"WellName Label": ["Well Name", "Tên giếng"],
	##### Messagebox #####

	"WellName Error": ["Well name must be less than 12 characters.\n[Well ", "Tên giếng phải ít hơn 12 ký tự. \n[Giếng "]
}

Setting_Language = {
	"Setting Label": ["SETTING", "CÀI ĐẶT"],
	"Back Button": ["Back", "Trở lại"],
	"Run Button": ["Run", "Chạy"],
	"Stage LabelFrame": ["Stage", "Giai đoạn"],
	"VoltageSetting LabelFrame": ["Voltage (DC)", "Điện áp (DC)"],
	"TimerSetting LabelFrame": ["Timer (min : sec)", "Thời gian (phút : giây)"],
	"AutoMail LabelFrame": ["Automatic email sending", "Tự động gửi mail"],
	"AutoMailOn Button": ["ON", "Bật"],
	"AutoMailOff Button": ["OFF", "Tắt"],
	"AutoMailRecipient Label": ["Recipient :", "Người nhận :"],
	"Save Button": ["Save", "Lưu"],
	##### Messagebox #####
	"Save Setting": ["Do you want to save the settings ?", "Bạn có muốn lưu cài đặt ?"],
	"Voltage Empty": ["Please enter all voltage values", "Xin nhập đầy đủ giá trị điện áp"],
	"Timer Empty": ["Please enter all timer values", "Xin nhập đầy đủ giá trị thời gian"],
	"Saved": ["Saved", "Đã lưu"],
	"Email Empty": ["Please enter the recipient email", "Xin nhập email người nhận"],
	"Voltage Overflow Value": ["Voltage must be between " + str(VOLTAGE_MIN_VALUE) + " and " + str(VOLTAGE_MAX_VALUE) + " VDC",
								"Điện áp phải ở giữa " + str(VOLTAGE_MIN_VALUE) + " và " + str(VOLTAGE_MAX_VALUE) + " VDC"],
	"Minute Overflow Value": ["Minutes must be between " + str(MINUTE_MIN_VALUE) + " and " + str(MINUTE_MAX_VALUE),
								"Số phút phải ở giữa " + str(MINUTE_MIN_VALUE) + " và " + str(MINUTE_MAX_VALUE)],
	"Second Overflow Value": ["Seconds must be between " + str(SECOND_MIN_VALUE) + " and " + str(SECOND_MAX_VALUE),
								"Số giây phải ở giữa " + str(SECOND_MIN_VALUE) + " và " + str(SECOND_MAX_VALUE)],
}

Run_Language = {
	"Run Label": ["ELECTROPHORESIS", "ĐIỆN DI"],
	"Stage LabelFrame": ["STAGE", "Giai đoạn"],
	"TimeLeft LabelFrame": ["Time left", "Thời gian còn lại"],
	"VoltageSense Label": ["Voltage:", "Điện áp:"],
	"CurrentSense Label": ["Current:", "Dòng điện:"],
	"Capture Button": ["Capture", "Chụp"],
	"Stop Button": ["STOP", "Dừng"],
	"Finish Button": ["FINISH", "Kết thúc"],
	"ViewResult Button": ["View Result", "Xem kết quả"],
	"CamMode1 Button": ["Mode 1", "Mode 1"],
	"CamMode2 Button": ["Mode 2", "Mode 2"],
	"Processing Label": ["Processing\r...", "Đang xử lý\r..."],
	"Complete Label": ["COMPLETE", "HOÀN THÀNH"],
	##### Messagebox #####

	"Stop Running": ["Do you want to stop electrophoresis ?", "Bạn có muốn dừng điện di ?"],
	"Picture Saved": ["The picture have been saved", "Ảnh đã đc lưu"],
}
############################### Check file ##################################
working_dir = '/home/pi/VE100'
parent_dir = '/home/pi'
result_dir = '/home/pi/Desktop/VE100 Result'

# language.txt 
if not os.path.exists(working_dir + "/language.txt"):
	fw = open(working_dir + "/language.txt",'w')
	fw.writelines(["0\n"])
	fw.close()
fr = open(working_dir + "/language.txt","r")
language = int(fr.readline())
fr.close()

# parameters1.txt
if not os.path.exists(working_dir + '/parameters1.txt'):
	fw_para1 = open(working_dir + '/parameters1.txt', 'x')
	fw_para1.writelines('36\n')
	fw_para1.writelines('1000\n')
	fw_para1.writelines('5\n')
	fw_para1.writelines('0\n')
	fw_para1.close()

fr_para1 = open(working_dir + '/parameters1.txt', "r")
voltage_set = int(fr_para1.readline())
timer_set = int(fr_para1.readline().strip('\n'))
auto_capture_timer_set = int(fr_para1.readline().strip('\n'))
automail1_is_on = int(fr_para1.readline().strip('\n'))
fr_para1.close()

m_set = round(timer_set/100)
s_set = timer_set - (m_set*100)

# parameters2.txt
if not os.path.exists(working_dir + '/parameters2.txt'):
	fw_para2 = open(working_dir + '/parameters2.txt', 'x')
	fw_para2.writelines('20\n')
	fw_para2.writelines('0500\n')
	fw_para2.writelines('25\n')
	fw_para2.writelines('1000\n')
	fw_para2.writelines('30\n')
	fw_para2.writelines('1500\n')
	fw_para2.writelines('0\n')
	fw_para2.close()

fr_para2 = open(working_dir + '/parameters2.txt',"r")
voltage1_set = int(fr_para2.readline())
timer1_set = int(fr_para2.readline().strip('\n'))
voltage2_set = int(fr_para2.readline().strip('\n'))
timer2_set = int(fr_para2.readline().strip('\n'))
voltage3_set = int(fr_para2.readline().strip('\n'))
timer3_set = int(fr_para2.readline().strip('\n'))
automail2_is_on = int(fr_para2.readline().strip('\n'))
fr_para2.close()

m1_set = timer1_set//100
s1_set = timer1_set - (m1_set*100)
m2_set = timer2_set//100
s2_set = timer2_set - (m2_set*100)
m3_set = timer3_set//100
s3_set = timer3_set - (m3_set*100)

# account.txt
if not os.path.exists('/home/pi/VE100/.account.txt'):
	fw = open("/home/pi/VE100/.account.txt", "x")
	fw.writelines('0\n')
	fw.close()
	account_active = 0
else:
	fr_account = open("/home/pi/VE100/.account.txt","r")
	account_active = int(fr_account.readline())
	email_address = fr_account.readline().strip('\n')
	email_password = fr_account.readline().strip('\n')

# resolution.txt
# if not os.path.exists(working_dir + "/resolution.txt"):
# 	fw = open(working_dir + "/resolution.txt",'w')
# 	fw.writelines(["1024\n", "600\n"])
# 	fw.close()
# fr = open(working_dir + "/resolution.txt","r")
# resolution_width = fr.readline().strip('\n')
# resolution_height = fr.readline().strip('\n')

# bandcrop.txt
if not os.path.exists('/home/pi/VE100/bandoffset.txt'):
	fw_crop = open('/home/pi/VE100/bandoffset.txt', 'x')
	fw_crop.writelines('100\n')
	fw_crop.close()
	band_offset = 100
else:
	fr_crop = open('/home/pi/VE100/bandoffset.txt')
	band_offset = int(fr_crop.readline())

# .oldemail.txt
if not os.path.exists('/home/pi/VE100/.oldemail.txt'):
	fw_email = open('/home/pi/VE100/.oldemail.txt', 'x')
	fw_email.writelines('@gmail.com\n')
	fw_email.close()
	autofill_email = "@gmail.com"
else:
	fr_email = open('/home/pi/VE100/.oldemail.txt')
	autofill_email = fr_email.readline().strip('\n')

# coordinates.txt
if not os.path.exists('/home/pi/VE100/coordinates.txt'):
	fw_coordinate = open('/home/pi/VE100/coordinates.txt', 'x')
	fw_coordinate.writelines('96\n') # toa do x 18 gieng
	fw_coordinate.writelines('90\n') # toa do x 26 gieng
	fw_coordinate.writelines('84\n') # toa do x 34 gieng
	fw_coordinate.writelines('230\n') # toa do y chung
	fw_coordinate.writelines('49\n') # khoang cach cac gieng 18
	fw_coordinate.writelines('67\n') # khoang giua 18
	fw_coordinate.writelines('32\n') # khoang cach cac gieng 26
	fw_coordinate.writelines('77\n') # khoang giua 26
	fw_coordinate.writelines('20\n') # khoang cach cac gieng 34
	fw_coordinate.writelines('77\n') # khoang giua 34
	fw_coordinate.writelines('15\n') # font size 18
	fw_coordinate.writelines('15\n') # font size 26
	fw_coordinate.writelines('12\n') # font size 34
	fw_coordinate.close()

	x_coordinate_18 = 96
	x_coordinate_26 = 90
	x_coordinate_34 = 84
	y_coordinate = 230
	well_distance_18 = 49
	pace_18 = 67
	well_distance_26 = 32
	pace_26 = 77
	well_distance_34 = 20
	pace_34 = 77
	font_size_18 = 15
	font_size_26 = 15
	font_size_34 = 12
	
else:
	fr_coordinate = open('/home/pi/VE100/coordinates.txt')
	x_coordinate_18 = int(fr_coordinate.readline())
	x_coordinate_26 = int(fr_coordinate.readline().strip('\n'))
	x_coordinate_34 = int(fr_coordinate.readline().strip('\n'))
	y_coordinate = int(fr_coordinate.readline().strip('\n'))
	well_distance_18 = int(fr_coordinate.readline().strip('\n'))
	pace_18 = int(fr_coordinate.readline().strip('\n'))
	well_distance_26 = int(fr_coordinate.readline().strip('\n'))
	pace_26 = int(fr_coordinate.readline().strip('\n'))
	well_distance_34 = int(fr_coordinate.readline().strip('\n'))
	pace_34 = int(fr_coordinate.readline().strip('\n'))
	font_size_18 = int(fr_coordinate.readline().strip('\n'))
	font_size_26 = int(fr_coordinate.readline().strip('\n'))
	font_size_34 = int(fr_coordinate.readline().strip('\n'))

# .config.txt
if not os.path.exists('/home/pi/VE100/.config.txt'):
	fw_voltage = open('/home/pi/VE100/.config.txt', 'x')
	fw_voltage.writelines('4.68\n')
	fw_voltage.close()
else:
	fr_voltage = open('/home/pi/VE100/.config.txt')
	DEIVIDE_VOLTAGE_VALUE = float(fr_voltage.readline())
	fr_voltage.close()


# ADS1115 - START
i2c = busio.I2C(3, 2)
ads = ADS.ADS1115(i2c)
# ADS1115 - END

# DS1307
i2c_2 = board.I2C()
rtc = adafruit_ds1307.DS1307(i2c_2)

# CAMERA - START
camera = PiCamera(framerate = 1, sensor_mode = 3)
camera.resolution = (1024,768)
camera.rotation = 0
# camera.brightness = 53
# camera.contrast = 5
def camera_capture(output):
	global camera
	camera.iso = 200
	camera.shutter_speed = 5000000
	camera.exposure_mode = 'sports'
	camera.capture(output)
	# ~ edit_img = cv2.imread(output) 
	# ~ alpha = 1.5 # Contrast
	# ~ beta = 10 # Brightness
	# ~ adjusted = cv2.convertScaleAbs(edit_img, alpha=alpha, beta=beta)
	# ~ cv2.imwrite(output, adjusted)
def camera_preview(window_position):
	camera.iso = 200
	camera.shutter_speed = 5000000
	camera.exposure_mode = 'sports'
	camera.start_preview(alpha=255, fullscreen=False, window=window_position)
# CAMERA - END

class MyCamera: 
	def __init__(self, parent_frame):
		self.parent_frame = parent_frame

		self.camera_label = Label(self.parent_frame)
		self.camera_label.grid(row=0, column=0, sticky="nsew")
		self.camera_label['bg'] = "black"
		self.camera_label['text'] = Run_Language["Processing Label"][language]
		self.camera_label['fg'] = 'white'
		self.camera_label['font'] = ("Arial", 13)

		self.camera = None
		self.rawCapture = None
		self.running = False
		self.thread = None
		self.latest_frame = None 
	
	def start_preview(self, framerate=1):
		if(self.running):
			return
		
		self.camera = PiCamera()
		self.camera.iso = 200
		self.camera.shutter_speed = 5000000
		self.camera.sensor_mode = 3
		self.camera.framerate = framerate
		# self.camera.exposure_mode = 'sport'
		self.camera.resolution = (1024,768)
		self.camera.rotation = 0
		sleep(1)  # Cho camera thời gian khởi động
		
		self.rawCapture = PiRGBArray(self.camera, size=(1024,768))
		self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)

		self.running = True
		self.thread = threading.Thread(target=self.camera_loop, daemon=True)
		self.thread.start()
		
		self.update_frame()

	def stop_preview(self, finish=0):
		self.running = False

		# Đợi thread thoát hẳn (an toàn)
		if self.thread and self.thread.is_alive():
			self.thread.join(timeout=1)

		if self.camera:
			self.camera.close()
			self.camera = None

		self.camera_label.config(image='')
		self.latest_frame = None

		self.finish = finish
		if(finish):
			self.camera_label['text'] = 'COMPLETED'
			self.camera_label['font'] = ('Arial',20, 'bold')
			self.camera_label['fg'] = 'lawn green'


	def camera_loop(self):
		for frame in self.stream:
			if not self.running:
				break
			image = frame.array
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			self.latest_frame = Image.fromarray(image)
			self.rawCapture.truncate(0)

	def update_frame(self):
		if not self.running:
			return
		
		if self.latest_frame:
			imgtk = ImageTk.PhotoImage(image=self.latest_frame)
			self.camera_label.imgtk = imgtk
			self.camera_label.config(image=imgtk)
		self.camera_label.after(50, self.update_frame)

	def capture_image(self, filepath=None):
		# Nếu đang preview → dùng latest_frame
		if self.latest_frame:
			img = self.latest_frame
		else:
			# Tạo camera tạm thời
			with PiCamera() as cam:
				cam.resolution = (1024,768)
				raw = PiRGBArray(cam)
				sleep(0.5)
				cam.capture(raw, format="bgr")
				image = raw.array
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
				img = Image.fromarray(image)

		# Tạo tên file nếu không có
		if not filepath:
			now = datetime.now().strftime("%Y%m%d_%H%M%S")
			filepath = f"capture_{now}.png"

		img.save(filepath)
		return filepath
	
	def set_framerate(self, framerate):
		was_running = self.running

		if self.running:
			self.stop_preview()  # Ngưng preview và đóng camera


		  # ❗ Đóng stream generator cũ để tránh lỗi KeyError
		if self.stream:
			try:
				self.stream.close()
			except Exception as e:
				print(f"Lỗi khi đóng stream: {e}")
			self.stream = None

		# Tạo lại camera với framerate mới
		self.camera = PiCamera()
		self.camera.iso = 200
		self.camera.shutter_speed = 5000000
		self.camera.sensor_mode = 3
		self.camera.framerate = framerate
		# camera.exposure_mode = 'sport'
		self.camera.resolution = (1024,768)
		self.camera.rotation = 0
		sleep(1)

		# Tạo lại stream
		self.rawCapture = PiRGBArray(self.camera, size=(1024,768))
		self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)

		if was_running:
			self.running = True
			self.thread = threading.Thread(target=self.camera_loop, daemon=True)
			self.thread.start()
			self.update_frame()


# UART - START
ser = serial.Serial(
	port = '/dev/serial0',
	baudrate = 38400,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

def uart_send(vol, state):
	send_data = '\rVOLTAGE ' + str(vol) + '\r'
	ser.write(send_data.encode())
	sleep(0.1)
	send_data = '\rCURRENT 10\r'
	ser.write(send_data.encode())
	sleep(0.1)
#     send_data = '\rECHO 1'
#     ser.write(send_data.encode())
#     sleep(0.1)
	send_data = '\rCOMMIT\r'
	ser.write(send_data.encode())
	sleep(0.1)
	send_data = '\rOUTPUT ' + str(state) + '\r'
	ser.write(send_data.encode())
	sleep(0.1)
# UART - END

# EMAIL - START
def sendmail(recipient, subject, content, zip_file, folder_name_set):
	global email_password, email_address
	print("email_address: ", email_address)
	print("email_password: ", email_password)

	emailData = MIMEMultipart()
	emailData['Subject'] = subject
	emailData['To'] = recipient
	emailData['From'] = email_address

	emailData.attach(MIMEText(content))

#     imageData = MIMEImage(open(image, 'rb').read(), 'jpg')
#     imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
#     emailData.attach(imageData)

	with open(zip_file,'rb') as file:
		emailData.attach(MIMEApplication(file.read(), Name= folder_name_set + '.zip'))

	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.ehlo()

	#session.login(mail_address, password)
	session.login(email_address, email_password)

	session.sendmail(email_address, recipient.split(','), emailData.as_string())
	session.quit
# EMAIL - END

# GPIO - START
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BLUE_LIGHT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(POWER_LED_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RUN_LED_PIN, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SENSOR_PIN, GPIO.IN)
# GPIO - END


class TrialExpiredFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.base_window = master

		# ~ self.title_frame = Frame(self, bg = TITILE_FRAME_BGD_COLOR)
		# ~ self.title_frame.pack(ipadx=0, ipady=5, fill=X)
		self.work_frame = Frame(self, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame.pack(expand=TRUE)
		self.work_frame.pack_propagate(0)
		# ~ self.button_frame = Frame(self, bg = MAIN_MENU_BUTTON_FRAME_BGD_COLOR)
		# ~ self.button_frame.pack(fill=X, expand=TRUE)
		
		# In title frame
		# ~ self.title_label = Label(self.title_frame,
								# ~ text = "...",
								# ~ font = TITLE_TXT_FONT,
								# ~ bg = TITILE_FRAME_BGD_COLOR,
								# ~ fg = TITILE_FRAME_TXT_COLOR)
		# ~ self.title_label.pack(padx=0, pady=0, ipady=10, ipadx=30)
		
		# In work frame
		print("self.base_window.trial_days: ", self.base_window.trial_days)
		self.expire_info1_label = Label(self.work_frame,
								text = "Your " + str(self.base_window.trial_days) + "-day trial has expired",
								font = ('Courier',15),
								bg = LABEL_FRAME_BGD_COLOR,
								fg = 'red')
		self.expire_info1_label.grid(row=0, column=0, pady=30, sticky=EW)
		
		self.expire_info2_label = Label(self.work_frame,
								text = " Please enter the activation code to continue using the application",
								font = TITLE_TXT_FONT,
								bg = LABEL_FRAME_BGD_COLOR,
								fg = 'grey35')
		self.expire_info2_label.grid(row=2, column=0, pady=10, padx=30, sticky=W)
	
		self.active_code_entry = Entry(self.work_frame, width=30, font=('Courier',14))
		self.active_code_entry.grid(row=3, column=0, pady=10, padx=30, sticky=EW)
		
		self.activate_button = Button(self.work_frame,
								text = "Activate",
								font = SWITCH_PAGE_BUTTON_FONT,
								# width = SWITCH_PAGE_BUTTON_WIDTH,
								# height = SWITCH_PAGE_BUTTON_HEIGHT,
								bg = SWITCH_PAGE_BUTTON_BGD_COLOR,
								fg = SWITCH_PAGE_BUTTON_TXT_COLOR,
								borderwidth = 0,
								command = self.activate_clicked)
		self.activate_button.grid(row=4, column=0, ipady=10, pady=30, padx=150, sticky=EW)
	
	def activate_clicked(self):
		self.active_code_enter = self.active_code_entry.get()
		if(self.active_code_enter != ''):
			if(self.active_code_enter == trial_30days_extend_code):
				if(active_code != trial_30days_extend_code):
					fw = open(working_dir + "/active_code.txt",'w')	
					fw.writelines(self.active_code_enter + '\n')
					messagebox.showinfo("","Your trial package has been extended to 30 days.")
					self.base_window.forget_page()
					self.base_window.page_num = self.base_window.frame_list.index(self.base_window.main_menu)
					self.base_window.switch_page()
					self.base_window.system_check_light()
				else:
					messagebox.showerror("","Your code is invalid, please try again.")
			elif(self.active_code_enter == trial_full_active_code):
				fw = open(working_dir + "/active_code.txt",'w')	
				fw.writelines(self.active_code_enter + '\n')
				messagebox.showinfo("","Successful activation.")
				self.base_window.forget_page()
				self.base_window.page_num = self.base_window.frame_list.index(self.base_window.main_menu)
				self.base_window.switch_page()
				self.base_window.system_check_light()
			else:
				messagebox.showerror("","Your code is invalid, please try again.")
		else:
			messagebox.showwarning("","Please enter activation code.")

class ScrollableFrame(Frame):
	def __init__(self, container, *args, **kwargs):
		super().__init__(container, *args, **kwargs)
		# canvas = Canvas(self, bg = 'white', height=400, width=996)
		canvas = Canvas(self, bg = 'white')
		scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
		self.scrollable_frame = Frame(canvas, bg = 'white')
		self.scrollable_frame.columnconfigure(1, weight=1)

		self.scrollable_frame.bind(
			"<Configure>",
			lambda e: canvas.configure(
				scrollregion=canvas.bbox("all")
			)
		)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.grid_propagate(False)

		# canvas.create_window((0, 0), window=self.scrollable_frame)
		canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", tags="frame")
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.grid(row=0, column=0, sticky="nsew")
		canvas.rowconfigure(0, weight=1)
		canvas.columnconfigure(0, weight=1)
		scrollbar.grid(row=0, column=1, sticky="nsew")
		canvas.yview_moveto(0)

		def _on_canvas_configure(event):
			canvas.itemconfig("frame", width=event.width)

		canvas.bind("<Configure>", _on_canvas_configure)


class MultiRun_Screen(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.base_window = master
		
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		self.isense_value = 0 
		self.vsense_value = 0
		self.cam_mode = 1
		self.system_is_running = 1
		self.camera_framerate = 1

		self.preview_x = 0
		self.preview_y = 0
		self.preview_width = 0
		self.preview_height = 0

		self.stage0_is_running = 1
		self.stage1_is_running = 0
		self.stage2_is_running = 0
		self.stage3_is_running = 0

		# Base frame create
		self.base_frame = Frame(self,bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.base_frame.grid(row=0, column=0, sticky='nsew')
		self.base_frame.rowconfigure(0, weight=1)
		self.base_frame.rowconfigure(1, weight=11)
		# self.base_frame.rowconfigure(2, weight=1)
		self.base_frame.columnconfigure(0, weight=1)

		self.title_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.title_frame.grid(row=0, column=0, sticky='nsew')
		self.title_frame.rowconfigure(0, weight=1)
		self.title_frame.columnconfigure(0, weight=1)
		self.title_frame.grid_propagate(False)

		self.work_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame.grid(row=1, column=0, sticky='nsew')
		self.work_frame.columnconfigure(0, weight=1)
		self.work_frame.columnconfigure(1, weight=5)
		self.work_frame.rowconfigure(0, weight=1)
		self.work_frame.grid_propagate(False)

		# In Title frame
		self.title_label = Label(self.title_frame,
								text = Run_Language['Run Label'][language],
								font = MAIN_TITLE_TXT_FONT,
								bg = MAIN_TITLE_BGD_COLOR,
								fg = MAIN_TITLE_TXT_COLOR)
		self.title_label.grid(row=0, column=0, sticky="snew")

		# In Work frame
		self.work_frame_1 = Frame(self.work_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame_1.grid(row=0, column=0, sticky='nsew')
		self.work_frame_1.columnconfigure(0, weight=1)
		self.work_frame_1.rowconfigure(0, weight=1)
		self.work_frame_1.rowconfigure(1, weight=1)
		self.work_frame_1.rowconfigure(2, weight=1)
		self.work_frame_1.rowconfigure(3, weight=1)
		self.work_frame_1.grid_propagate(False)

		self.work_frame_2 = Frame(self.work_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame_2.grid(row=0, column=1, sticky='nsew')
		self.work_frame_2.columnconfigure(0, weight=1)
		self.work_frame_2.rowconfigure(0, weight=8)
		self.work_frame_2.rowconfigure(1, weight=1)
		self.work_frame_2.grid_propagate(False)

		# In work frame 1
		self.stage0_labelframe = LabelFrame(self.work_frame_1, 
										bg = RUNSTAGE_LABELFRAME_ACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["Stage LabelFrame"][language] + " 0",
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage0_labelframe.grid(row=0, column=0, sticky='nsew')
		self.stage0_labelframe.rowconfigure(0, weight=1)
		self.stage0_labelframe.rowconfigure(1, weight=1)
		self.stage0_labelframe.columnconfigure(0, weight=1)
		self.stage0_labelframe.pack_propagate(0)		

		self.stage1_labelframe = LabelFrame(self.work_frame_1, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["Stage LabelFrame"][language] + " 1",
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage1_labelframe.grid(row=1, column=0, sticky='nsew')
		self.stage1_labelframe.rowconfigure(0, weight=1)
		self.stage1_labelframe.rowconfigure(1, weight=1)
		self.stage1_labelframe.columnconfigure(0, weight=1)
		self.stage1_labelframe.pack_propagate(0)

		self.stage2_labelframe = LabelFrame(self.work_frame_1, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["Stage LabelFrame"][language] + " 2",
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage2_labelframe.grid(row=2, column=0, sticky='nsew')
		self.stage2_labelframe.rowconfigure(0, weight=1)
		self.stage2_labelframe.rowconfigure(1, weight=1)
		self.stage2_labelframe.columnconfigure(0, weight=1)
		self.stage2_labelframe.pack_propagate(0)

		self.stage3_labelframe = LabelFrame(self.work_frame_1, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["Stage LabelFrame"][language] + " 3",
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage3_labelframe.grid(row=3, column=0, sticky='nsew')
		self.stage3_labelframe.rowconfigure(0, weight=1)
		self.stage3_labelframe.rowconfigure(1, weight=1)
		self.stage3_labelframe.columnconfigure(0, weight=1)
		self.stage3_labelframe.pack_propagate(0)


		self.stage0_labelframe_1 = LabelFrame(self.stage0_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage0_labelframe_1.grid(row=0, column=0, padx=5, sticky='nsew')
		self.stage0_labelframe_1.rowconfigure(0, weight=1)
		self.stage0_labelframe_1.columnconfigure(0, weight=1)
		self.stage0_labelframe_1.pack_propagate(0)

		self.stage0_labelframe_2 = LabelFrame(self.stage0_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["TimeLeft LabelFrame"][language],
										font = TIMELEFT_LABELFRAME_TXT_FONT)
		self.stage0_labelframe_2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
		self.stage0_labelframe_2.rowconfigure(0, weight=1)
		self.stage0_labelframe_2.columnconfigure(0, weight=1)
		self.stage0_labelframe_2.columnconfigure(1, weight=1)
		self.stage0_labelframe_2.columnconfigure(2, weight=1)
		self.stage0_labelframe_2.pack_propagate(0)

		self.stage1_labelframe_1 = LabelFrame(self.stage1_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage1_labelframe_1.grid(row=0, column=0, padx=5, sticky='nsew')
		self.stage1_labelframe_1.rowconfigure(0, weight=1)
		self.stage1_labelframe_1.columnconfigure(0, weight=1)
		self.stage1_labelframe_1.pack_propagate(0)

		self.stage1_labelframe_2 = LabelFrame(self.stage1_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["TimeLeft LabelFrame"][language],
										font = TIMELEFT_LABELFRAME_TXT_FONT)
		self.stage1_labelframe_2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
		self.stage1_labelframe_2.rowconfigure(0, weight=1)
		self.stage1_labelframe_2.columnconfigure(0, weight=1)
		self.stage1_labelframe_2.columnconfigure(1, weight=1)
		self.stage1_labelframe_2.columnconfigure(2, weight=1)
		self.stage1_labelframe_2.pack_propagate(0)

		self.stage2_labelframe_1 = LabelFrame(self.stage2_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage2_labelframe_1.grid(row=0, column=0, padx=5, sticky='nsew')
		self.stage2_labelframe_1.rowconfigure(0, weight=1)
		self.stage2_labelframe_1.columnconfigure(0, weight=1)
		self.stage2_labelframe_1.pack_propagate(0)

		self.stage2_labelframe_2 = LabelFrame(self.stage2_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["TimeLeft LabelFrame"][language],
										font = TIMELEFT_LABELFRAME_TXT_FONT)
		self.stage2_labelframe_2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
		self.stage2_labelframe_2.rowconfigure(0, weight=1)
		self.stage2_labelframe_2.columnconfigure(0, weight=1)
		self.stage2_labelframe_2.columnconfigure(1, weight=1)
		self.stage2_labelframe_2.columnconfigure(2, weight=1)
		self.stage2_labelframe_2.pack_propagate(0)

		self.stage3_labelframe_1 = LabelFrame(self.stage3_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										font = RUNSTAGE_LABELFRAME_TXT_FONT)
		self.stage3_labelframe_1.grid(row=0, column=0, padx=5, sticky='nsew')
		self.stage3_labelframe_1.rowconfigure(0, weight=1)
		self.stage3_labelframe_1.columnconfigure(0, weight=1)
		self.stage3_labelframe_1.pack_propagate(0)

		self.stage3_labelframe_2 = LabelFrame(self.stage3_labelframe, 
										bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
										fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
										text = Run_Language["TimeLeft LabelFrame"][language],
										font = TIMELEFT_LABELFRAME_TXT_FONT)
		self.stage3_labelframe_2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
		self.stage3_labelframe_2.rowconfigure(0, weight=1)
		self.stage3_labelframe_2.columnconfigure(0, weight=1)
		self.stage3_labelframe_2.columnconfigure(1, weight=1)
		self.stage3_labelframe_2.columnconfigure(2, weight=1)
		self.stage3_labelframe_2.pack_propagate(0)


		# In work frame 2
		self.preview_frame = Frame(self.work_frame_2, bg = 'black')
		self.preview_frame.grid(row=0, column=0, sticky="nsew")
		self.preview_frame.columnconfigure(0, weight=10)
		self.preview_frame.columnconfigure(1, weight=1)
		self.preview_frame.rowconfigure(0, weight=1)
		self.preview_frame.grid_propagate(False)

		self.preview_labelframe = LabelFrame(self.preview_frame, 
									bg='black', 
									fg='red', 
									text = "◉ Camera View", 
									font=("Arial", 12,'bold'))
		self.preview_labelframe.grid(row=0, column=0, sticky="nsew")
		self.preview_labelframe.columnconfigure(0, weight=1)
		self.preview_labelframe.rowconfigure(0, weight=1)
		self.preview_labelframe.grid_propagate(False)

		# self.camera_frame = Frame(self.preview_labelframe, bg = "black")
		# self.camera_frame.grid(row=0, column=0, sticky="nsew")
 		# # Camera Init
		# self.camera = MyCamera(self.camera_frame)

		# t_progressbar = atk.RadialProgressbar(self.preview_labelframe, fg='cyan', text_fg='black', text_bg = 'black')
		# t_progressbar.grid(row=0, column=0, sticky="nsew")
		# t_progressbar.start()
		self.tprocess_label = Label(self.preview_labelframe, bg='black', fg='white smoke', text='Processing\r...', font=("Arial",13,'bold'))
		self.tprocess_label.grid(row=0, column=0, sticky="nsew")

		self.cammode_frame = Frame(self.preview_frame, bg = 'black')
		self.cammode_frame.grid(row=0, column=1, sticky="nsew")
		self.cammode_frame.columnconfigure(0, weight=1)
		self.cammode_frame.rowconfigure(0, weight=1)
		self.cammode_frame.rowconfigure(1, weight=1)
		self.cammode_frame.grid_propagate(False)

		self.cammode1_button = Button(self.cammode_frame,
								text = Run_Language["CamMode1 Button"][language],
								font = CAMMODE_BUTTON_TXT_FONT,
								bg = CAMMODE_BUTTON_ACTIVE_BGD_COLOR,
								fg = CAMMODE_BUTTON_TXT_COLOR,
								borderwidth = 0,
								command = self.mode1_clicked)
		self.cammode1_button.grid(row=0, column=0, sticky="nsew")

		self.cammode2_button = Button(self.cammode_frame,
								text = Run_Language["CamMode2 Button"][language],
								font = CAMMODE_BUTTON_TXT_FONT,
								bg = CAMMODE_BUTTON_INACTIVE_BGD_COLOR,
								fg = CAMMODE_BUTTON_TXT_COLOR,
								borderwidth = 0,
								command = self.mode2_clicked)
		self.cammode2_button.grid(row=1, column=0, sticky="nsew")


		self.control_frame = Frame(self.work_frame_2, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.control_frame.grid(row=1, column=0, sticky='nsew')
		self.control_frame.columnconfigure(0, weight=1)
		self.control_frame.columnconfigure(1, weight=1)
		self.control_frame.columnconfigure(2, weight=1)
		self.control_frame.rowconfigure(0, weight=1)
		self.control_frame.grid_propagate(False)

		self.control_frame_1 = LabelFrame(self.control_frame, bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.control_frame_1.grid(row=0, column=0, pady=1, sticky="nsew")
		self.control_frame_1.columnconfigure(0, weight=1)
		self.control_frame_1.columnconfigure(1, weight=1)
		self.control_frame_1.rowconfigure(0, weight=1)
		self.control_frame_1.rowconfigure(1, weight=1)
		self.control_frame_1.grid_propagate(False)

		self.control_frame_2 = Frame(self.control_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.control_frame_2.grid(row=0, column=1, pady=1, sticky="nsew")
		self.control_frame_2.columnconfigure(0, weight=1)
		self.control_frame_2.rowconfigure(0, weight=1)
		self.control_frame_2.grid_propagate(False)

		self.control_frame_3 = Frame(self.control_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.control_frame_3.grid(row=0, column=2, pady=1, sticky="nsew")
		self.control_frame_3.columnconfigure(0, weight=1)
		self.control_frame_3.rowconfigure(0, weight=1)
		self.control_frame_3.grid_propagate(False)

		

		self.vsense_label = Label(self.control_frame_1,
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
								text = Run_Language["VoltageSense Label"][language],
								# anchor = 'e',
								fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
								font = SENSE_LABEL_TXT_FONT)
		self.vsense_label.grid(row=0, column=0, sticky= "nsew")
		self.isense_label = Label(self.control_frame_1,
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR,
								# ~ text = Run_Language["CurrentSense Label"][language],
								text = '',
								# anchor = 'e',
								fg = RUNSTAGE_LABELFRAME_TXT_COLOR,
								font = SENSE_LABEL_TXT_FONT)
		self.isense_label.grid(row=1, column=0, sticky= "nsew")

		self.vsenseValue_label = Label(self.control_frame_1,
								bg = SENSEVALUE_LABEL_BGD_COLOR,
								text = str(self.vsense_value) + ' V',
								# anchor = 'w',
								fg = SENSEVALUE_LABEL_TXT_COLOR,
								font = SENSEVALUE_LABEL_TXT_FONT)
		self.vsenseValue_label.grid(row=0, column=1, sticky= "nsew")
		self.isenseValue_label = Label(self.control_frame_1,
								bg = SENSEVALUE_LABEL_BGD_COLOR,
								# ~ text =  str(self.isense_value) + ' A',
								text =  '',
								# anchor = 'w',
								fg = SENSEVALUE_LABEL_TXT_COLOR,
								font = SENSEVALUE_LABEL_TXT_FONT)
		self.isenseValue_label.grid(row=1, column=1, sticky= "nsew")

		self.capture_button = Button(self.control_frame_2,
								text = Run_Language["Capture Button"][language],
								font = SWITCHPAGE_BUTTON_TXT_FONT,
								bg = CAPTURE_BUTTON_BGD_COLOR,
								fg = CAPTURE_BUTTON_TXT_COLOR,
								borderwidth = 3,
								command = self.capture_clicked)
		self.capture_button.grid(row=0, column=0, sticky="nsew")

		self.stop_button = Button(self.control_frame_3,
								text = Run_Language["Stop Button"][language],
								font = SWITCHPAGE_BUTTON_TXT_FONT,
								bg = STOP_BUTTON_BGD_COLOR,
								fg = STOP_BUTTON_TXT_COLOR,
								borderwidth = 3,
								command = self.stop_clicked)
		self.stop_button.grid(row=0, column=0, sticky="nsew")

	def stage0_counter(self):
		self.system_is_running = 1

		self.s0_curent = self.s0_curent - 1
		if(self.s0_curent < 0):
			self.m0_curent = self.m0_curent - 1 
			self.s0_curent = 59
		self.s0_label.config(text = str('%02d'%self.s0_curent)) # update second label
		self.m0_label.config(text = str('%02d'%self.m0_curent)) # update minute label

		# read Voltage & Current feedback here
		self.readFeebackValue()

		send_data = '\rSTATUS\r'
		ser.write(send_data.encode())

		if(self.m0_curent != -1):
			self.s0_solve = self.s0_label.after(1000, self.stage0_counter)
		else: 
			self.m0_label.config(text = '00')
			self.s0_label.config(text = '00')
			try: 
				self.s0_label.after_cancel(self.s1_solve)
			except: 
				pass

			if(m0_set!=0 or s0_set!=0):
				try:
					camera_capture(self.base_window.main_menu.result_path + 'stage0_result.png')
				except Exception as e:
					error = messagebox.showerror("ERR 03", str(e), icon = "error")
					if(error=='ok'):
						pass

			# Xet xem co run voltage 1 khong 
			if(int(self.base_window.multi_setting.voltage1_set) > 0):
				GPIO.output(RELAY_PIN, GPIO.HIGH)
				GPIO.output(RUN_LED_PIN, GPIO.HIGH)
				uart_send(self.base_window.multi_setting.voltage1_set, 1)
			else:
				uart_send(0, 0)
				GPIO.output(RELAY_PIN, GPIO.LOW)
				GPIO.output(RUN_LED_PIN, GPIO.LOW)

				for i in range(0,3):
					GPIO.output(BUZZER_PIN, GPIO.HIGH)
					sleep(0.7)
					GPIO.output(BUZZER_PIN, GPIO.LOW)
					sleep(0.7)

			self.stage0_is_running = 0
			self.stage1_is_running = 1

			self.stage1_counter()



	def stage1_counter(self):
		self.stage0_labelframe['bg'] = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR
		self.stage1_labelframe['bg'] = RUNSTAGE_LABELFRAME_ACTIVE_BGD_COLOR

		self.s1_curent = self.s1_curent - 1
		if(self.s1_curent < 0):
			self.m1_curent = self.m1_curent - 1 
			self.s1_curent = 59
		self.s1_label.config(text = str('%02d'%self.s1_curent)) # update second label
		self.m1_label.config(text = str('%02d'%self.m1_curent)) # update minute label

		# read Voltage & Current feedback here
		self.readFeebackValue()

		send_data = '\rSTATUS\r'
		ser.write(send_data.encode())

		if(self.m1_curent != -1):
			self.s1_solve = self.s1_label.after(1000, self.stage1_counter)
		else: 
			self.m1_label.config(text = '00')
			self.s1_label.config(text = '00')
			try: 
				self.s1_label.after_cancel(self.s1_solve)
			except: 
				pass

			if(self.base_window.multi_setting.m1_set!=0 or self.base_window.multi_setting.s1_set!=0):
				try:
					camera_capture(self.base_window.main_menu.result_path + 'stage1_result.png')
				except Exception as e:
					error = messagebox.showerror("ERR 03", str(e), icon = "error")
					if(error=='ok'):
						pass

			# Xet xem co run voltage 2 khong 
			if(int(self.base_window.multi_setting.voltage2_set) > 0):
				GPIO.output(RELAY_PIN, GPIO.HIGH)
				GPIO.output(RUN_LED_PIN, GPIO.HIGH)
				uart_send(self.base_window.multi_setting.voltage2_set, 1)
			else:
				uart_send(0, 0)
				GPIO.output(RELAY_PIN, GPIO.LOW)
				GPIO.output(RUN_LED_PIN, GPIO.LOW)

				for i in range(0,3):
					GPIO.output(BUZZER_PIN, GPIO.HIGH)
					sleep(0.7)
					GPIO.output(BUZZER_PIN, GPIO.LOW)
					sleep(0.7)

			self.stage1_is_running = 0
			self.stage2_is_running = 1

			self.stage2_counter()
	
	def stage2_counter(self):
		self.stage1_labelframe['bg'] = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR
		self.stage2_labelframe['bg'] = RUNSTAGE_LABELFRAME_ACTIVE_BGD_COLOR

		self.s2_curent = self.s2_curent - 1
		if(self.s2_curent < 0):
			self.m2_curent = self.m2_curent - 1 
			self.s2_curent = 59
		self.s2_label.config(text = str('%02d'%self.s2_curent)) # update second label
		self.m2_label.config(text = str('%02d'%self.m2_curent)) # update minute label

		# read Voltage & Current feedback here
		self.readFeebackValue()

		send_data = '\rSTATUS\r'
		ser.write(send_data.encode())

		if(self.m2_curent != -1):
			self.s2_solve = self.s2_label.after(1000, self.stage2_counter)
		else: 
			self.m2_label.config(text = '00')
			self.s2_label.config(text = '00')
			try: 
				self.s2_label.after_cancel(self.s2_solve)
			except: 
				pass

			if(self.base_window.multi_setting.m2_set!=0 or self.base_window.multi_setting.s2_set!=0):
				try:
					camera_capture(self.base_window.main_menu.result_path + 'stage2_result.png')
				except Exception as e:
					error = messagebox.showerror("ERR 03", str(e), icon = "error")
					if(error=='ok'):
						pass

			# Xet xem co run voltage 3 khong 
			if(int(self.base_window.multi_setting.voltage3_set) > 0):
				GPIO.output(RELAY_PIN, GPIO.HIGH)
				GPIO.output(RUN_LED_PIN, GPIO.HIGH)
				uart_send(self.base_window.multi_setting.voltage3_set, 1)
			else:
				uart_send(0, 0)
				GPIO.output(RELAY_PIN, GPIO.LOW)
				GPIO.output(RUN_LED_PIN, GPIO.LOW)

				for i in range(0,3):
					GPIO.output(BUZZER_PIN, GPIO.HIGH)
					sleep(0.7)
					GPIO.output(BUZZER_PIN, GPIO.LOW)
					sleep(0.7)

			self.stage2_is_running = 0
			self.stage3_is_running = 1

			self.stage3_counter()
	
	def stage3_counter(self):
		self.stage2_labelframe['bg'] = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR
		self.stage3_labelframe['bg'] = RUNSTAGE_LABELFRAME_ACTIVE_BGD_COLOR

		self.s3_curent = self.s3_curent - 1
		if(self.s3_curent < 0):
			self.m3_curent = self.m3_curent - 1 
			self.s3_curent = 59
		self.s3_label.config(text = str('%02d'%self.s3_curent)) # update second label
		self.m3_label.config(text = str('%02d'%self.m3_curent)) # update minute label

		# read Voltage & Current feedback here
		self.readFeebackValue()

		send_data = '\rSTATUS\r'
		ser.write(send_data.encode())

		if(self.m3_curent != -1):
			self.s3_solve = self.s3_label.after(1000, self.stage3_counter)
		else:
			self.vsenseValue_label.config(text = "0 V")
			# ~ self.isenseValue_label.config(text = "0 A")
			self.isenseValue_label.config(text = "")

			GPIO.output(RELAY_PIN, GPIO.LOW)
			GPIO.output(POWER_LED_PIN, GPIO.LOW)
			uart_send(0,0)

			self.m3_label.config(text = '00')
			self.s3_label.config(text = '00')

			try:
				self.s3_label.after_cancel(self.s3_solve)
			except:
				pass

			try: 
				camera_capture(self.base_window.main_menu.result_path + 'stage3_result.png')

				# Create Image with sample name 
				original_img = Image.open(self.base_window.main_menu.result_path + 'stage3_result.png')
				process_img = ImageDraw.Draw(original_img)
				shape = [(1024, 768), (0,550)]
				process_img.rectangle(shape, fill="lightgray", outline="lightgray")
				img_font_1_18 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_18)
				img_font_1_26 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_26)
				img_font_1_34 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_34)
				img_font_2 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 23)
				img_font_3 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 17)

				if(self.base_window.sample_naming.number_of_wells == 18):
					x_coordinate = x_coordinate_18
					for i in range(0,9):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_18, fill=(0,255,0))
						x_coordinate += well_distance_18

					x_coordinate = x_coordinate - well_distance_18 + pace_18
					for i in range(9,18):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_18, fill=(0,255,0))
						x_coordinate += well_distance_18

					r1 = 568
					r2 = 568
					r3 = 568
					r4 = 568
					r5 = 568
					for i in range(0,18):
						if(i<6):
							process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r1 += 32
						elif(i<12):
							process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r2 += 32
						else:
							process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r3 += 32
				
				elif(self.base_window.sample_naming.number_of_wells == 26):
					x_coordinate = x_coordinate_26
					for i in range(0,13):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_26, fill=(0,255,0))
						x_coordinate += well_distance_26

					x_coordinate = x_coordinate - well_distance_26 + pace_26
					for i in range(13,26):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_26, fill=(0,255,0))
						x_coordinate += well_distance_26

					r1 = 568
					r2 = 568
					r3 = 568
					r4 = 568
					r5 = 568
					for i in range(0,26):
						if(i<6):
							process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r1 += 32
						elif(i<12):
							process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r2 += 32
						elif(i<18):
							process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r3 += 32
						elif(i<24):
							process_img.text((632,r4), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r4 += 32
						else:
							process_img.text((832,r5), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
							r5 += 32

				elif(self.base_window.sample_naming.number_of_wells == 34):
					x_coordinate = x_coordinate_34
					for i in range(0,17):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_34, fill=(0,255,0))
						x_coordinate += well_distance_34

					x_coordinate = x_coordinate - well_distance_34 + pace_34
					for i in range(17,34):
						process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_34, fill=(0,255,0))
						x_coordinate += well_distance_34

					r1 = 568
					r2 = 568
					r3 = 568
					r4 = 568
					r5 = 568
					for i in range(0,34):
						if(i<7):
							process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
							r1 += 28
						elif(i<14):
							process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
							r2 += 28
						elif(i<21):
							process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
							r3 += 28
						elif(i<28):
							process_img.text((632,r4), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
							r4 += 28
						else:
							process_img.text((832,r5), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
							r5 += 28

				original_img.save(self.base_window.main_menu.result_path + 'edit_img.png','png')

			except Exception as e:
				error = messagebox.showerror("ERR 03", str(e), icon = "error")
				if(error=='ok'):
					pass 

			self.stage3_labelframe['bg'] = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR


			#Button Change 
			self.capture_button['text'] = Run_Language["ViewResult Button"][language]
			self.stop_button['text'] = Run_Language["Finish Button"][language]
			self.stop_button['bg'] = "dodger blue"
			# self.cammode1_button['state'] = "disable"

			self.stage3_is_running = 0
			self.stage0_is_running = 1

			# Close camera
			try:
				camera.stop_preview()
			except:
				pass

			# Turn off all 
			GPIO.output(BLUE_LIGHT_PIN, GPIO.LOW)
			GPIO.output(RELAY_PIN, GPIO.LOW)
			GPIO.output(RUN_LED_PIN, GPIO.LOW)

			# Automail here 
			self.automail_check()

			# Complete Inform
			self.tprocess_label = Label(self.preview_labelframe, bg='black', fg='white smoke', text='Processing\r...', font=("Arial",13,'bold'))
			self.tprocess_label.grid(row=0, column=0, sticky="nsew")
			self.tprocess_label['text'] = 'COMPLETED'
			self.tprocess_label['font'] = ('Arial',20, 'bold')
			self.tprocess_label['fg'] = 'lawn green'

			self.system_is_running = 0

			# Buzzer 
			for i in range(0,3):
				GPIO.output(BUZZER_PIN, GPIO.HIGH)
				sleep(0.7)
				GPIO.output(BUZZER_PIN, GPIO.LOW)
				sleep(0.7)


	def readFeebackValue(self):
		v_adc = AnalogIn(ads, ADS.P2)
		v_refVoltage = v_adc.voltage
		v_realVoltage = round(v_refVoltage * MAX_VOLTAGE_VALUE / DEIVIDE_VOLTAGE_VALUE)
		self.vsenseValue_label.config(text = str(v_realVoltage) + ' V')

		# i_adc =  AnalogIn(ads, ADS.P1)
		# i_refVoltage = i_adc.voltage
	
	def automail_check(self):
		if(account_active and automail2_is_on):
			shutil.make_archive(self.base_window.main_menu.result_path, format='zip', root_dir = self.base_window.main_menu.result_path)
			try:
				sendmail(self.base_window.multi_setting.recipient_email, 
							self.base_window.main_menu.folderName_set , 
							'This is an email from VE100 device.',
							self.base_window.main_menu.result_path_0 + '/' + self.base_window.main_menu.folderName_set + '.zip',
							self.base_window.main_menu.folderName_set)
			except Exception as e:
				try:
					camera.stop_preview()
				except:
					pass
				error = messagebox.showerror("ERR 02", str(e), icon = "error")
				if(error=='ok'):
					pass

	def capture_clicked(self):
		if(self.capture_button['text'] == "Capture"):
			if(self.stage0_is_running):
				s_cap = s0_set - self.s0_curent
				if(s_cap<0):
					s_cap = 60 + s_cap
					m_cap = m0_set - self.m0_curent - 1
				else:
					m_cap = m0_set - self.m0_curent
				if(m_cap<0):
					m_cap=0

				output_result = str('stage0_' + '%02d'%m_cap) + ':' + str('%02d'%s_cap) +'.png'

			elif(self.stage1_is_running):
				s_cap = self.base_window.multi_setting.s1_set - self.s1_curent
				if(s_cap<0):
					s_cap = 60 + s_cap
					m_cap = self.base_window.multi_setting.m1_set - self.m1_curent - 1
				else:
					m_cap = self.base_window.multi_setting.m1_set - self.m1_curent
				if(m_cap<0):
					m_cap=0

				output_result = str('stage1_' + '%02d'%m_cap) + ':' + str('%02d'%s_cap) +'.png'

			elif(self.stage2_is_running):
				s_cap = self.base_window.multi_setting.s2_set - self.s2_curent
				if(s_cap<0):
					s_cap = 60 + s_cap
					m_cap = self.base_window.multi_setting.m2_set - self.m2_curent - 1
				else:
					m_cap = self.base_window.multi_setting.m2_set - self.m2_curent
				if(m_cap<0):
					m_cap=0

				output_result = str('stage2_' + '%02d'%m_cap) + ':' + str('%02d'%s_cap) +'.png'

			elif(self.stage3_is_running):
				s_cap = self.base_window.multi_setting.s3_set - self.s3_curent
				if(s_cap<0):
					s_cap = 60 + s_cap
					m_cap = self.base_window.multi_setting.m3_set - self.m3_curent - 1
				else:
					m_cap = self.base_window.multi_setting.m3_set - self.m3_curent
				if(m_cap<0):
					m_cap=0

				output_result = str('stage3_' + '%02d'%m_cap) + ':' + str('%02d'%s_cap) +'.png'

			try:
				camera_capture(self.base_window.main_menu.result_path + output_result)
				camera.stop_preview()
				msgbox = messagebox.showinfo('', Run_Language["Picture Saved"][language])
				# if(msgbox=='ok'):
				camera_preview((self.preview_x, self.preview_y, self.preview_width, self.preview_height))

			except Exception as e:
				error = messagebox.showerror("ERR 03",str(e), icon = "error")
				if(error=='ok'):
					pass

		else:
			result_file = filedialog.askopenfilename(initialdir = self.base_window.main_menu.result_path, filetypes=[('png file','*.png')])
			if result_file is not None:
				if(result_file[len(result_file)-3:]=='png'):
					try:
						self.tprocess_label.destroy()
					except:
						pass

					previewframe_width = self.preview_labelframe.winfo_width()
					previewframe_height = self.preview_labelframe.winfo_height()
					preview_img_percent  = round(previewframe_width*100/RESULT_IMAGE_WIDTH)

					preview_img = Image.open(result_file)
					img_original_width, img_original_height = preview_img.size
					img_scale_width = int(img_original_width * preview_img_percent / 100)
					img_scale_height = int(img_original_height * preview_img_percent / 100)
					scale_img = preview_img.resize((img_scale_width, img_scale_height))
					
					img_height_shift = round((img_scale_height - previewframe_height)/2) # fix chieu cao cua anh sau khi scale voi chieu cao cua canvas
					crop_area = (0, img_height_shift, img_scale_width, img_height_shift + previewframe_height)
					crop_img = scale_img.crop(crop_area)
					display_img = ImageTk.PhotoImage(crop_img)

					try:
						display_label.destroy()
					except:
						pass
					display_label =  Label(self.preview_labelframe, image=display_img)
					display_label.image = display_img
					display_label.grid(row=0, column=0, sticky="nsew")

				else:
					pass



	def stop_clicked(self):
		try:
			camera.stop_preview()
		except:
			pass
		msgbox = messagebox.askquestion('', Run_Language["Stop Running"][language], icon = 'question')
		if(msgbox=='yes'):
			uart_send(0,0)
			GPIO.output(RUN_LED_PIN, GPIO.LOW)
			GPIO.output(RELAY_PIN, GPIO.LOW)

			if(self.stop_button['text'] == 'STOP'):
				try:
					tprocess_label(self.base_window.main_menu.result_path + 'final_result.png')

					# Create Image with sample name 
					original_img = Image.open(self.base_window.main_menu.result_path + 'final_result.png')
					process_img = ImageDraw.Draw(original_img)
					shape = [(1024, 768), (0,550)]
					process_img.rectangle(shape, fill="lightgray", outline="lightgray")
					img_font_1_18 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_18)
					img_font_1_26 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_26)
					img_font_1_34 = ImageFont.truetype("/home/pi/VE100/arial.ttf", font_size_34)
					img_font_2 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 23)
					img_font_3 = ImageFont.truetype("/home/pi/VE100/arial.ttf", 17)

					if(self.base_window.sample_naming.number_of_wells == 18):
						x_coordinate = x_coordinate_18
						for i in range(0,9):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_18, fill=(0,255,0))
							x_coordinate += well_distance_18

						x_coordinate = x_coordinate - well_distance_18 + pace_18
						for i in range(9,18):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_18, fill=(0,255,0))
							x_coordinate += well_distance_18

						r1 = 568
						r2 = 568
						r3 = 568
						r4 = 568
						r5 = 568
						for i in range(0,18):
							if(i<6):
								process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r1 += 32
							elif(i<12):
								process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r2 += 32
							else:
								process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r3 += 32
					
					elif(self.base_window.sample_naming.number_of_wells == 26):
						x_coordinate = x_coordinate_26
						for i in range(0,13):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_26, fill=(0,255,0))
							x_coordinate += well_distance_26

						x_coordinate = x_coordinate - well_distance_26 + pace_26
						for i in range(13,26):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_26, fill=(0,255,0))
							x_coordinate += well_distance_26

						r1 = 568
						r2 = 568
						r3 = 568
						r4 = 568
						r5 = 568
						for i in range(0,26):
							if(i<6):
								process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r1 += 32
							elif(i<12):
								process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r2 += 32
							elif(i<18):
								process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r3 += 32
							elif(i<24):
								process_img.text((632,r4), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r4 += 32
							else:
								process_img.text((832,r5), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_2, fill=(0,0,0))
								r5 += 32

					elif(self.base_window.sample_naming.number_of_wells == 34):
						x_coordinate = x_coordinate_34
						for i in range(0,17):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_34, fill=(0,255,0))
							x_coordinate += well_distance_34

						x_coordinate = x_coordinate - well_distance_34 + pace_34
						for i in range(17,34):
							process_img.text((x_coordinate, y_coordinate), str(i+1), font=img_font_1_34, fill=(0,255,0))
							x_coordinate += well_distance_34

						r1 = 568
						r2 = 568
						r3 = 568
						r4 = 568
						r5 = 568
						for i in range(0,34):
							if(i<7):
								process_img.text((32,r1), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
								r1 += 28
							elif(i<14):
								process_img.text((232,r2), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
								r2 += 28
							elif(i<21):
								process_img.text((432,r3), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
								r3 += 28
							elif(i<28):
								process_img.text((632,r4), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
								r4 += 28
							else:
								process_img.text((832,r5), str(i+1) + '. ' + str(self.base_window.sample_naming.wellname_list[i]), font=img_font_3, fill=(0,0,0))
								r5 += 28

					original_img.save(self.base_window.main_menu.result_path + 'edit_img.png','png')
				except Exception as e:
					error = messagebox.showerror("ERR 03", str(e), icon = "error")
					if(error=='ok'):
						pass
				
			GPIO.output(BLUE_LIGHT_PIN, GPIO.LOW)

			try:
				self.s0_label.after_cancel(self.s0_solve)
			except:
				pass
			try:
				self.s1_label.after_cancel(self.s1_solve)
			except:
				pass
			try:
				self.s2_label.after_cancel(self.s2_solve)
			except:
				pass
			try:
				self.s3_label.after_cancel(self.s3_solve)
			except:
				pass
			
			if(self.stop_button['text'] == 'STOP'):
				self.automail_check()
			
			self.system_is_running = 0

			self.base_window.switch_page(self.base_window.main_menu)
			self.base_window.reset()
								
				
		else:
			if(self.system_is_running == 1):
				GPIO.output(RUN_LED_PIN, GPIO.HIGH)
				GPIO.output(BLUE_LIGHT_PIN, GPIO.HIGH)
				GPIO.output(RELAY_PIN, GPIO.HIGH)
				camera_preview((self.preview_x, self.preview_y, self.preview_width, self.preview_height))

	
	def mode1_clicked(self):
		if(self.system_is_running):
			global camera
			self.cam_mode = 1
			self.cammode1_button['bg'] = CAMMODE_BUTTON_ACTIVE_BGD_COLOR
			self.cammode2_button['bg'] = CAMMODE_BUTTON_INACTIVE_BGD_COLOR

			# self.camera_framerate = 1

			try:
				camera.stop_preview()
			except:
				pass
			camera.framerate = 1
			camera.exposure_mode = 'sports'
			sleep(1)
			camera_preview((self.preview_x, self.preview_y, self.preview_width, self.preview_height))

			# try:
			# 	self.camera.stop_preview()
			# except:
			# 	pass
			# self.camera.start_preview(self.camera_framerate)
			# self.camera.set_framerate(self.camera_framerate)


	def mode2_clicked(self):
		if(self.system_is_running):
			global camera
			self.cam_mode = 1
			self.cammode1_button['bg'] = CAMMODE_BUTTON_INACTIVE_BGD_COLOR
			self.cammode2_button['bg'] = CAMMODE_BUTTON_ACTIVE_BGD_COLOR

			# self.camera_framerate = 3

			try:
				camera.stop_preview()
			except:
				pass
			camera.framerate = 3
			camera.exposure_mode = 'sports'
			sleep(1)
			camera_preview((self.preview_x, self.preview_y, self.preview_width, self.preview_height))

			# try:
			# 	self.camera.stop_preview()
			# except:
			# 	pass
			# self.camera.start_preview(self.camera_framerate)
			# self.camera.set_framerate(self.camera_framerate)
	
	def runStage_change(self):
		pass 
	

	def update_frame(self):
		self.m0_curent = m0_set
		self.s0_curent = s0_set
		self.m1_curent = self.base_window.multi_setting.m1_set
		self.s1_curent = self.base_window.multi_setting.s1_set
		self.m2_curent = self.base_window.multi_setting.m2_set
		self.s2_curent = self.base_window.multi_setting.s2_set
		self.m3_curent = self.base_window.multi_setting.m3_set
		self.s3_curent = self.base_window.multi_setting.s3_set

		###### CONTENT IN STAGE 0 ######
		self.settingValue0_label = Label(self.stage0_labelframe_1, 
								fg = STAGE_CONTENT_TXT_COLOR, 
								text = str(voltage0_set) + 'V - ' + str(m0_set) + ':' + str(s0_set), 
								font = STAGE_CONTENT_TXT_FONT, 
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.settingValue0_label.grid(row=0, column=0, sticky="nsew")

		self.m0_label = Label(self.stage0_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str(m0_set),
						font = STAGE_CONTENT_TXT_FONT, 
						anchor='e',
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.m0_label.grid(row=0, column=0, sticky="nsew")
		self.twodot0_label = Label(self.stage0_labelframe_2, 
							fg = STAGE_CONTENT_TXT_COLOR, 
							text = ':', 
							font = STAGE_CONTENT_TXT_FONT, 
							bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.twodot0_label.grid(row=0, column=1, sticky="nsew")
		self.s0_label = Label(self.stage0_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str(s0_set), 
						anchor='w',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.s0_label.grid(row=0, column=2, sticky="nsew")


		###### CONTENT IN STAGE 1 ######
		self.settingValue1_label = Label(self.stage1_labelframe_1, 
								fg = STAGE_CONTENT_TXT_COLOR, 
								text = str(self.base_window.multi_setting.voltage1_set) + 'V - ' + str('%02d'%self.base_window.multi_setting.m1_set) + ':' + str('%02d'%self.base_window.multi_setting.s1_set), 
								font = STAGE_CONTENT_TXT_FONT, 
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.settingValue1_label.grid(row=0, column=0, sticky="nsew")

		self.m1_label = Label(self.stage1_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.m1_set),
						anchor = 'e',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.m1_label.grid(row=0, column=0, sticky="nsew")
		self.twodot1_label = Label(self.stage1_labelframe_2, 
							fg = STAGE_CONTENT_TXT_COLOR, 
							text = ':', 
							font = STAGE_CONTENT_TXT_FONT, 
							bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.twodot1_label.grid(row=0, column=1, sticky="nsew")
		self.s1_label = Label(self.stage1_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.s1_set), 
						anchor = 'w',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.s1_label.grid(row=0, column=2, sticky="nsew")

		###### CONTENT IN STAGE 2 ######
		self.settingValue2_label = Label(self.stage2_labelframe_1, 
								fg = STAGE_CONTENT_TXT_COLOR, 
								text = str(self.base_window.multi_setting.voltage2_set) + 'V - ' + str('%02d'%self.base_window.multi_setting.m2_set) + ':' + str('%02d'%self.base_window.multi_setting.s2_set), 
								font = STAGE_CONTENT_TXT_FONT, 
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.settingValue2_label.grid(row=0, column=0, sticky="nsew")

		self.m2_label = Label(self.stage2_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.m2_set),
						anchor = 'e',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.m2_label.grid(row=0, column=0, sticky="nsew")
		self.twodot2_label = Label(self.stage2_labelframe_2, 
							fg = STAGE_CONTENT_TXT_COLOR, 
							text = ':', 
							font = STAGE_CONTENT_TXT_FONT, 
							bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.twodot2_label.grid(row=0, column=1, sticky="nsew")
		self.s2_label = Label(self.stage2_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.s2_set), 
						anchor = 'w',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.s2_label.grid(row=0, column=2, sticky="nsew")

		###### CONTENT IN STAGE 3 ######
		self.settingValue3_label = Label(self.stage3_labelframe_1, 
								fg = STAGE_CONTENT_TXT_COLOR, 
								text = str(self.base_window.multi_setting.voltage3_set) + 'V - ' + str('%02d'%self.base_window.multi_setting.m3_set) + ':' + str('%02d'%self.base_window.multi_setting.s3_set), 
								font = STAGE_CONTENT_TXT_FONT, 
								bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.settingValue3_label.grid(row=0, column=0, sticky="nsew")

		self.m3_label = Label(self.stage3_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.m2_set),
						anchor = 'e',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.m3_label.grid(row=0, column=0, sticky="nsew")
		self.twodot3_label = Label(self.stage3_labelframe_2, 
							fg = STAGE_CONTENT_TXT_COLOR, 
							text = ':', 
							font = STAGE_CONTENT_TXT_FONT, 
							bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.twodot3_label.grid(row=0, column=1, sticky="nsew")
		self.s3_label = Label(self.stage3_labelframe_2, 
						fg = STAGE_CONTENT_TXT_COLOR, 
						text = str('%.02d'%self.base_window.multi_setting.s3_set), 
						anchor = 'w',
						font = STAGE_CONTENT_TXT_FONT, 
						bg = RUNSTAGE_LABELFRAME_INACTIVE_BGD_COLOR)
		self.s3_label.grid(row=0, column=2, sticky="nsew")



		# if(self.cam_mode == 1):
		# 	self.mode1_clicked()
		# else:
		# 	self.mode2_clicked()

		self.tprocess_label.update_idletasks()

		self.preview_x = self.tprocess_label.winfo_rootx()
		self.preview_y = self.tprocess_label.winfo_rooty()
		self.preview_width = self.tprocess_label.winfo_width()
		self.preview_height = self.tprocess_label.winfo_height()

		print("preview_x: ", self.preview_x)
		print("preview_y: ", self.preview_y)
		print("preview_width: ", self.preview_width)
		print("preview_height: ", self.preview_height)
		camera_preview((self.preview_x, self.preview_y, self.preview_width, self.preview_height))

		
		# self.camera.start_preview()

		if(voltage0_set != 0):
			uart_send(voltage0_set, 1)
			self.stage0_counter()
		else:
			uart_send(self.voltage1_set, 1)
			self.stage1_counter()



class MultiSetting_Screen(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.base_window = master
		
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		self.voltage1_set = 0
		self.voltage2_set = 0
		self.voltage3_set = 0
		self.m1_set = 0
		self.m2_set = 0
		self.m3_set = 0
		self.s1_set = 0
		self.s2_set = 0
		self.s3_set = 0

		# Base frame create
		self.base_frame = Frame(self,bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.base_frame.grid(row=0, column=0, sticky='nsew')
		self.base_frame.rowconfigure(0, weight=1)
		self.base_frame.rowconfigure(1, weight=10)
		self.base_frame.rowconfigure(2, weight=1)
		self.base_frame.columnconfigure(0, weight=1)

		self.title_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.title_frame.grid(row=0, column=0, sticky='nsew')
		self.title_frame.rowconfigure(0, weight=1)
		self.title_frame.columnconfigure(0, weight=1)
		self.title_frame.grid_propagate(False)

		self.work_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame.grid(row=1, column=0, sticky='nsew')
		self.work_frame.rowconfigure(0, weight=5)
		self.work_frame.rowconfigure(1, weight=1)
		self.work_frame.columnconfigure(0, weight=1)
		self.work_frame.grid_propagate(False)

		self.button_frame = Frame(self.base_frame, bg = BUTTON_FRAME_BGD_COLOR)
		self.button_frame.grid(row=2, column=0, sticky='nsew')
		self.button_frame.rowconfigure(0, weight=1)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.columnconfigure(1, weight=1)
		self.button_frame.columnconfigure(2, weight=1)
		self.button_frame.columnconfigure(3, weight=1)
		self.button_frame.columnconfigure(4, weight=1)
		self.button_frame.columnconfigure(5, weight=1)
		self.button_frame.columnconfigure(6, weight=1)
		self.button_frame.grid_propagate(False)

		# In Title frame
		self.title_label = Label(self.title_frame,
								text = Setting_Language['Setting Label'][language],
								font = MAIN_TITLE_TXT_FONT,
								bg = MAIN_TITLE_BGD_COLOR,
								fg = MAIN_TITLE_TXT_COLOR)
		self.title_label.grid(row=0, column=0, sticky="snew")
		
		# In work frame 
		self.work_frame_1 = Frame(self.work_frame, bg = BUTTON_FRAME_BGD_COLOR)
		self.work_frame_1.grid(row=0, column=0, sticky="snew")
		self.work_frame_1.columnconfigure(0, weight=1)
		self.work_frame_1.columnconfigure(1, weight=1)
		self.work_frame_1.columnconfigure(2, weight=1)
		self.work_frame_1.rowconfigure(0, weight=1)
		self.work_frame_1.pack_propagate(0)
		self.work_frame_2 = Frame(self.work_frame, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.work_frame_2.grid(row=1, column=0, sticky="snew")
		self.work_frame_2.columnconfigure(0, weight=1)
		self.work_frame_2.rowconfigure(0, weight=1)
		self.work_frame_2.pack_propagate(0)


		self.stage1_labelframe = LabelFrame(self.work_frame_1, 
										bg = BUTTON_FRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = Setting_Language["Stage LabelFrame"][language] + " 1",
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.stage1_labelframe.grid(row=0, column=0, sticky='nsew')
		self.stage1_labelframe.rowconfigure(0, weight=1)
		self.stage1_labelframe.rowconfigure(1, weight=1)
		self.stage1_labelframe.columnconfigure(0, weight=1)
		self.stage1_labelframe.pack_propagate(0)
		self.stage2_labelframe = LabelFrame(self.work_frame_1, 
										bg = BUTTON_FRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = Setting_Language["Stage LabelFrame"][language] + " 2",
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.stage2_labelframe.grid(row=0, column=1, padx=5, sticky='nsew')
		self.stage2_labelframe.rowconfigure(0, weight=1)
		self.stage2_labelframe.rowconfigure(1, weight=1)
		self.stage2_labelframe.columnconfigure(0, weight=1)
		self.stage2_labelframe.pack_propagate(0)
		self.stage3_labelframe = LabelFrame(self.work_frame_1, 
										bg = BUTTON_FRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = Setting_Language["Stage LabelFrame"][language] + " 3",
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.stage3_labelframe.grid(row=0, column=2, sticky='nsew')
		self.stage3_labelframe.rowconfigure(0, weight=1)
		self.stage3_labelframe.rowconfigure(1, weight=1)
		self.stage3_labelframe.columnconfigure(0, weight=1)
		self.stage3_labelframe.pack_propagate(0)

		self.stage1_labelframe_1= LabelFrame(self.stage1_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["VoltageSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage1_labelframe_1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
		self.stage1_labelframe_1.rowconfigure(0, weight=1)
		self.stage1_labelframe_1.columnconfigure(0, weight=1)
		self.stage1_labelframe_1.pack_propagate(0)

		self.stage1_labelframe_2= LabelFrame(self.stage1_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["TimerSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage1_labelframe_2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
		self.stage1_labelframe_2.rowconfigure(0, weight=1)
		self.stage1_labelframe_2.columnconfigure(0, weight=1)
		self.stage1_labelframe_2.columnconfigure(1, weight=1)
		self.stage1_labelframe_2.columnconfigure(2, weight=1)
		self.stage1_labelframe_2.pack_propagate(0)

		self.stage2_labelframe_1= LabelFrame(self.stage2_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["VoltageSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage2_labelframe_1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
		self.stage2_labelframe_1.rowconfigure(0, weight=1)
		self.stage2_labelframe_1.columnconfigure(0, weight=1)
		self.stage2_labelframe_1.pack_propagate(0)

		self.stage2_labelframe_2= LabelFrame(self.stage2_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["TimerSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage2_labelframe_2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
		self.stage2_labelframe_2.rowconfigure(0, weight=1)
		self.stage2_labelframe_2.columnconfigure(0, weight=1)
		self.stage2_labelframe_2.columnconfigure(1, weight=1)
		self.stage2_labelframe_2.columnconfigure(2, weight=1)
		self.stage2_labelframe_2.pack_propagate(0)

		self.stage3_labelframe_1= LabelFrame(self.stage3_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["VoltageSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage3_labelframe_1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
		self.stage3_labelframe_1.rowconfigure(0, weight=1)
		self.stage3_labelframe_1.columnconfigure(0, weight=1)
		self.stage3_labelframe_1.pack_propagate(0)
		
		self.stage3_labelframe_2= LabelFrame(self.stage3_labelframe, 
										bg = MAIN_TITLE_BGD_COLOR,
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR,
										text = Setting_Language["TimerSetting LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = SETTINGPARA_LABELFRAME_TXT_FONT)
		self.stage3_labelframe_2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
		self.stage3_labelframe_2.rowconfigure(0, weight=1)
		self.stage3_labelframe_2.columnconfigure(0, weight=1)
		self.stage3_labelframe_2.columnconfigure(1, weight=1)
		self.stage3_labelframe_2.columnconfigure(2, weight=1)
		self.stage3_labelframe_2.pack_propagate(0)

		##### In stage1_labelframe_1 #####
		self.voltage1_entry = Entry(self.stage1_labelframe_1, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							justify = 'center',
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
							width = 3)
		self.voltage1_entry.grid(row=0, column=0, sticky='nsew')
		self.voltage1_entry.insert(0, voltage1_set)

		self.m1_entry = Entry(self.stage1_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.m1_entry.grid(row=0, column=0, sticky='nsew')
		self.m1_entry.insert(0, str('%02d'%m1_set))

		self.twodot_label_1 = Label(self.stage1_labelframe_2, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							text =':')
		self.twodot_label_1.grid(row=0, column=1, sticky='nsew')

		self.s1_entry = Entry(self.stage1_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.s1_entry.grid(row=0, column=2, sticky='nsew')
		self.s1_entry.insert(0, str('%02d'%s1_set))

		##### In stage1_labelframe_2 #####
		self.voltage2_entry = Entry(self.stage2_labelframe_1, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							justify = 'center',
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
							width = 3)
		self.voltage2_entry.grid(row=0, column=0, sticky='nsew')
		self.voltage2_entry.insert(0, voltage2_set)

		self.m2_entry = Entry(self.stage2_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.m2_entry.grid(row=0, column=0, sticky='nsew')
		self.m2_entry.insert(0, str('%02d'%m2_set))

		self.twodot_label_2 = Label(self.stage2_labelframe_2, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							text =':')
		self.twodot_label_2.grid(row=0, column=1, sticky='nsew')

		self.s2_entry = Entry(self.stage2_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.s2_entry.grid(row=0, column=2, sticky='nsew')
		self.s2_entry.insert(0, str('%02d'%s2_set))

		##### In stage1_labelframe_3 #####
		self.voltage3_entry = Entry(self.stage3_labelframe_1, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							justify = 'center',
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
							width = 3)
		self.voltage3_entry.grid(row=0, column=0, sticky='nsew')
		self.voltage3_entry.insert(0, voltage3_set)

		self.m3_entry = Entry(self.stage3_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.m3_entry.grid(row=0, column=0, sticky='nsew')
		self.m3_entry.insert(0, str('%02d'%m2_set))

		self.twodot_label_3 = Label(self.stage3_labelframe_2, 
							fg = SETTINGPARA_ENTRY_TXT_COLOR, 
							bg = SETTINGPARA_LABELFRAME_BGD_COLOR, 
							font = SETTINGPARA_ENTRY_TXT_FONT,
							text =':')
		self.twodot_label_3.grid(row=0, column=1, sticky='nsew')

		self.s3_entry = Entry(self.stage3_labelframe_2, 
						fg = SETTINGPARA_ENTRY_TXT_COLOR, 
						font = SETTINGPARA_ENTRY_TXT_FONT,
						bg = SETTINGPARA_LABELFRAME_BGD_COLOR,
						justify = 'center',
						width = 3)
		self.s3_entry.grid(row=0, column=2, sticky='nsew')
		self.s3_entry.insert(0, str('%02d'%s3_set))

		# In work_frame_2
		self.automail_labelframe = LabelFrame(self.work_frame_2, 
										bg = MAIN_TITLE_BGD_COLOR, 
										fg = SETTINGPARA_LABELFRAME_TXT_COLOR, 
										font = MAIN_MENU_LABELFRAME_TXT_FONT,
										text = Setting_Language["AutoMail LabelFrame"][language])
		self.automail_labelframe.grid(row=0, column=0, sticky="nsew")
		self.automail_labelframe.columnconfigure(0, weight=2)
		self.automail_labelframe.columnconfigure(1, weight=10)
		self.automail_labelframe.rowconfigure(0, weight=1)

		self.automail_button_frame =  Frame(self.automail_labelframe, bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.automail_button_frame.grid(row=0, column=0, sticky='nsew')
		self.automail_button_frame.columnconfigure(0, weight=1)
		self.automail_button_frame.columnconfigure(1, weight=1)
		self.automail_button_frame.rowconfigure(0, weight=1)
		self.automail_on_button = Button(self.automail_button_frame,
								bd = 0,
								text =  Setting_Language["AutoMailOn Button"][language], 
								command = self.automail_on_click)
		self.automail_on_button.grid(row=0, column=0, sticky="nsew")
		self.automail_off_button = Button(self.automail_button_frame, 
									bd = 0,
									text = Setting_Language["AutoMailOff Button"][language], 
									command = self.automail_off_click)
		self.automail_off_button.grid(row=0, column=1, sticky="nsew")

		self.automail_recipient_frame =  Frame(self.automail_labelframe, bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.automail_recipient_frame.grid(row=0, column=1, sticky='nsew')
		self.automail_recipient_frame.columnconfigure(0, weight=1)
		self.automail_recipient_frame.columnconfigure(1, weight=1)
		self.automail_recipient_frame.columnconfigure(2, weight=5)
		self.automail_recipient_frame.rowconfigure(0, weight=1)

		self.recipient_label = Label(self.automail_recipient_frame, 
							bg = MAIN_FUNCTION_FRAME_BGD_COLOR, 
							text = Setting_Language["AutoMailRecipient Label"][language], 
							font = AUTOMAIL_LABEL_TXT_FONT)
		self.recipient_label.grid(row=0, column=1, sticky="we")
		self.recipient_entry = Entry(self.automail_recipient_frame, 
							justify = 'left',
							font = AUTOMAIL_ENTRY_TXT_FONT)
		self.recipient_entry.grid(row=0, column=2, sticky="nsew")
		

		# ~ if(account_active):
			# ~ self.automail_on_button['state'] = "normal"
			# ~ self.automail_off_button['state'] = "normal"
			# ~ if(automail2_is_on):
				# ~ self.automail_on_button['bg'] = AUTOMAILON_BUTTON_BGD_COLOR
				# ~ self.automail_off_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
				# ~ self.recipient_entry['state'] = "normal"
				# ~ self.recipient_entry.insert(0, autofill_email)
			# ~ else:
				# ~ self.automail_off_button['bg'] = AUTOMAILOFF_BUTTON_BGD_COLOR
				# ~ self.automail_on_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
		# ~ else: 
			# ~ self.recipient_entry['state'] = "disabled"
			# ~ self.automail_on_button['state'] = "disabled"
			# ~ self.automail_off_button['state'] = "disabled"

		# In Button frame
		self.run_button = Button(self.button_frame, 
								text = Setting_Language["Run Button"][language], 
								font = SWITCHPAGE_BUTTON_TXT_FONT, 
								fg = SWITCHPAGE_BUTTON_TXT_COLOR, 
								bg = SWITCHPAGE_BUTTON_BGD_COLOR, 
								command = self.run_clicked)
		self.run_button.grid(row=0, column=6, padx=2, pady=2, sticky="nsew")
		self.back_button = Button(self.button_frame, 
								text = Setting_Language["Back Button"][language], 
								font = SWITCHPAGE_BUTTON_TXT_FONT, 
								fg = SWITCHPAGE_BUTTON_TXT_COLOR, 
								bg = SWITCHPAGE_BUTTON_BGD_COLOR, 
								command = self.back_clicked)
		self.back_button.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
		self.save_button = Button(self.button_frame, 
								text = Setting_Language["Save Button"][language], 
								font = SWITCHPAGE_BUTTON_TXT_FONT, 
								fg = SWITCHPAGE_BUTTON_TXT_COLOR, 
								bg = SWITCHPAGE_BUTTON_BGD_COLOR, 
								command = self.save_clicked)
		self.save_button.grid(row=0, column=3, padx=2, pady=2, sticky="nsew")

	def update_frame(self):
		if(account_active):
			self.automail_on_button['state'] = "normal"
			self.automail_off_button['state'] = "normal"
			if(automail2_is_on):
				self.automail_on_button['bg'] = AUTOMAILON_BUTTON_BGD_COLOR
				self.automail_off_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
				self.recipient_entry['state'] = "normal"
				self.recipient_entry.insert(0, autofill_email)
			else:
				self.automail_off_button['bg'] = AUTOMAILOFF_BUTTON_BGD_COLOR
				self.automail_on_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
		else: 
			self.recipient_entry['state'] = "disabled"
			self.automail_on_button['state'] = "disabled"
			self.automail_off_button['state'] = "disabled"
			
	def automail_on_click(self):
		global automail2_is_on
		automail2_is_on = 1
		self.automail_on_button['bg'] = AUTOMAILON_BUTTON_BGD_COLOR
		self.automail_off_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
		self.recipient_entry['state'] = "normal"
		if(self.recipient_entry.get()==''):
			self.recipient_entry.insert(0, autofill_email)

	def automail_off_click(self):
		global automail2_is_on
		automail2_is_on = 0
		self.automail_on_button['bg'] = AUTOMAIL_BUTTON_BGD_COLOR
		self.automail_off_button['bg'] = AUTOMAILOFF_BUTTON_BGD_COLOR
		self.recipient_entry.delete(0,END)
		self.recipient_entry['state'] = 'disable'
	
	def save_clicked(self):
		msg = messagebox.askquestion("", Setting_Language["Save Setting"][language])
		if(msg=='yes'):
			if(self.voltage1_entry.get()=='' or self.voltage2_entry.get()=='' or self.voltage3_entry.get()==''):
				messagebox.showwarning("", Setting_Language["Voltage Empty"][language])
			elif(self.m1_entry.get()=='' or self.m2_entry.get()=='' or self.m3_entry.get()=='' or
					self.s1_entry.get()=='' or self.s2_entry.get()=='' or self.s3_entry.get()==''):
				messagebox.showwarning("", Setting_Language["Timer Empty"][language])
			else:
				self.voltage1_set = self.voltage1_entry.get()
				self.voltage2_set = self.voltage2_entry.get()
				self.voltage3_set = self.voltage3_entry.get()
				self.m1_set = int(self.m1_entry.get())
				self.m2_set = int(self.m2_entry.get())
				self.m3_set = int(self.m3_entry.get())
				self.s1_set = int(self.s1_entry.get())
				self.s2_set = int(self.s2_entry.get())
				self.s3_set = int(self.s3_entry.get())

				fw = open('/home/pi/VE100/parameters2.txt','w')
				fw.writelines(str(self.voltage1_set) + '\n')
				fw.writelines(str('%02d'%self.m1_set) + str('%02d'%self.s1_set) + '\n')
				fw.writelines(str(self.voltage2_set) + '\n')
				fw.writelines(str('%02d'%self.m2_set) + str('%02d'%self.s2_set) + '\n')
				fw.writelines(str(self.voltage3_set) + '\n')
				fw.writelines(str('%02d'%self.m3_set) + str('%02d'%self.s3_set) + '\n')
				fw.writelines(str(automail2_is_on) + '\n')
				fw.close()
				messagebox.showinfo("", Setting_Language["Saved"][language])

	def back_clicked(self):
		self.base_window.switch_page(self.base_window.multi_setting)

		self.base_window.frame_list.remove(self.base_window.multi_setting)
		del self.base_window.multi_setting
		self.base_window.multi_setting = MultiSetting_Screen(self.base_window)
		self.base_window.frame_list.append(self.self.base_window.multi_setting)

	def run_clicked(self):
		if(self.voltage1_entry.get()=='' or self.voltage2_entry.get()=='' or self.voltage3_entry.get()==''):
			messagebox.showwarning("", Setting_Language["Voltage Empty"][language])
		elif(self.m1_entry.get()=='' or self.m2_entry.get()=='' or self.m3_entry.get()=='' or 
			self.s1_entry.get()=='' or self.s2_entry.get()=='' or self.s3_entry.get()==''):
			messagebox.showwarning("", Setting_Language["Timer Empty"][language])
		elif((self.voltage1_entry.get().isnumeric())==0 or (self.voltage2_entry.get().isnumeric())==0 or (self.voltage3_entry.get().isnumeric())==0):
			messagebox.showwarning("", Setting_Language["Voltage Overflow Value"][language])
		elif((self.m1_entry.get().isnumeric())==0 or (self.m2_entry.get().isnumeric())==0 or (self.m3_entry.get().isnumeric())==0):
			messagebox.showwarning("", Setting_Language["Minute Overflow Value"][language])
		elif((self.s1_entry.get().isnumeric())==0 or (self.s2_entry.get().isnumeric())==0 or (self.s3_entry.get().isnumeric())==0):
			messagebox.showwarning("", Setting_Language["Second Overflow Value"][language])
		elif(int(self.voltage1_entry.get()) < VOLTAGE_MIN_VALUE or int(self.voltage1_entry.get()) > VOLTAGE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Voltage Overflow Value"][language])
		elif(int(self.voltage2_entry.get()) < VOLTAGE_MIN_VALUE or int(self.voltage2_entry.get()) > VOLTAGE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Voltage Overflow Value"][language])
		elif(int(self.voltage3_entry.get()) < VOLTAGE_MIN_VALUE or int(self.voltage3_entry.get()) > VOLTAGE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Voltage Overflow Value"][language])
		elif(int(self.m1_entry.get()) < MINUTE_MIN_VALUE or int(self.m1_entry.get()) > MINUTE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Minute Overflow Value"][language])
		elif(int(self.m2_entry.get()) < MINUTE_MIN_VALUE or int(self.m2_entry.get()) > MINUTE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Minute Overflow Value"][language])
		elif(int(self.m3_entry.get()) < MINUTE_MIN_VALUE or int(self.m3_entry.get()) > MINUTE_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Minute Overflow Value"][language])
		elif(int(self.s1_entry.get()) < SECOND_MIN_VALUE or int(self.s1_entry.get()) > SECOND_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Second Overflow Value"][language])
		elif(int(self.s2_entry.get()) < SECOND_MIN_VALUE or int(self.s2_entry.get()) > SECOND_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Second Overflow Value"][language])
		elif(int(self.s3_entry.get()) < SECOND_MIN_VALUE or int(self.s3_entry.get()) > SECOND_MAX_VALUE):
			messagebox.showwarning("", Setting_Language["Second Overflow Value"][language])
		elif((self.recipient_entry.get()=='' or self.recipient_entry.get()=='@gmail.com') and automail2_is_on):
			messagebox.showwarning("", Setting_Language["Email Empty"][language])
		else:
			subprocess.call(["scrot", self.base_window.main_menu.result_path + 'parameters.jpg'])

			global autofill_email 
			if(automail2_is_on):
				self.recipient_email = self.recipient_entry.get()
				fw = open('/home/pi/VE100/.oldemail.txt', 'w')
				fw.writelines(self.recipient_email + '\n')
				fw.close()
				autofill_email = self.recipient_email

			self.voltage1_set = self.voltage1_entry.get()
			self.voltage2_set = self.voltage2_entry.get()
			self.voltage3_set = self.voltage3_entry.get()
			self.m1_set = int(self.m1_entry.get())
			self.m2_set = int(self.m2_entry.get())
			self.m3_set = int(self.m3_entry.get())
			self.s1_set = int(self.s1_entry.get())
			self.s2_set = int(self.s2_entry.get())
			self.s3_set = int(self.s3_entry.get())

			print("voltage1_set = ", voltage1_set)
			print("voltage2_set = ", voltage2_set)
			print("voltage3_set = ", voltage3_set)

			sleep(2)
			self.base_window.switch_page(self.base_window.multi_run)
			self.base_window.multi_run.update_frame()
		

class SampleNaming_Screen(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.base_window = master
		
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# Base frame create
		self.base_frame = Frame(self,bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.base_frame.grid(row=0, column=0, sticky='nsew')
		self.base_frame.rowconfigure(0, weight=1)
		self.base_frame.rowconfigure(1, weight=10)
		self.base_frame.rowconfigure(2, weight=1)
		self.base_frame.columnconfigure(0, weight=1)

		self.title_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.title_frame.grid(row=0, column=0, sticky='nsew')
		self.title_frame.rowconfigure(0, weight=1)
		self.title_frame.columnconfigure(0, weight=1)
		self.title_frame.grid_propagate(False)

		self.work_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame.grid(row=1, column=0, sticky='nsew')
		self.work_frame.rowconfigure(0, weight=1)
		self.work_frame.rowconfigure(1, weight=20)
		self.work_frame.columnconfigure(0, weight=1)
		self.work_frame.grid_propagate(False)

		self.button_frame = Frame(self.base_frame, bg = BUTTON_FRAME_BGD_COLOR)
		self.button_frame.grid(row=2, column=0, sticky='nsew')
		self.button_frame.rowconfigure(0, weight=1)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.columnconfigure(1, weight=5)
		self.button_frame.columnconfigure(2, weight=1)
		self.button_frame.grid_propagate(False)

		# In Title frame
		self.title_label = Label(self.title_frame,
								text = SampleNamingScreen_Language['Setting Label'][language],
								font = MAIN_TITLE_TXT_FONT,
								bg = MAIN_TITLE_BGD_COLOR,
								fg = MAIN_TITLE_TXT_COLOR)
		self.title_label.grid(row=0, column=0, sticky="snew")

		#In work frame 
		self.work_frame_1 = Frame(self.work_frame, bg = BUTTON_FRAME_BGD_COLOR)
		self.work_frame_1.grid(row=0, column=0, sticky="snew")
		self.work_frame_1.columnconfigure(0, weight=1)
		self.work_frame_1.columnconfigure(1, weight=1)
		self.work_frame_1.columnconfigure(2, weight=12)
		self.work_frame_1.rowconfigure(0, weight=1)
		self.work_frame_1.pack_propagate(0)
		self.work_frame_2 = Frame(self.work_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame_2.grid(row=1, column=0, sticky="snew")
		self.work_frame_2.columnconfigure(0, weight=1)
		self.work_frame_2.rowconfigure(0, weight=1)
		self.work_frame_2.pack_propagate(0)

		self.numberofwells_label =  Label(self.work_frame_1,
								text = SampleNamingScreen_Language['NumberOfWells Label'][language],
								bg = BUTTON_FRAME_BGD_COLOR,
								fg = NUMBEROFWELLS_LABEL_TXT_COLOR,
								font = NUMBEROFWELLS_LABEL_TXT_FONT)
		self.numberofwells_label.grid(row=0, column=0, sticky='snew')

		numberofwells_list = ['18 wells', '26 wells', '34 wells']
		self.numberofwells_combobox= ttk.Combobox(self.work_frame_1, 
								state = "readonly",
								width = 10, 
								font = LANGUAGE_COMBOBOX_TXT_FONT,
								value = numberofwells_list)
		self.numberofwells_combobox.grid(row=0, column=1, sticky='w')
		self.numberofwells_combobox.current(1)
		self.numberofwells_combobox.bind("<<ComboboxSelected>>", self.numberofwell_select)



		# In button frame
		self.next_button = Button(self.button_frame, 
								text = SampleNamingScreen_Language["Next Button"][language], 
								font = SWITCHPAGE_BUTTON_TXT_FONT, 
								fg = SWITCHPAGE_BUTTON_TXT_COLOR, 
								bg = SWITCHPAGE_BUTTON_BGD_COLOR, 
								command = self.next_clicked)
		self.next_button.grid(row=0, column=2, padx=2, pady=2, sticky="nsew")
		self.back_button = Button(self.button_frame, 
								text = SampleNamingScreen_Language["Back Button"][language], 
								font = SWITCHPAGE_BUTTON_TXT_FONT, 
								fg = SWITCHPAGE_BUTTON_TXT_COLOR, 
								bg = SWITCHPAGE_BUTTON_BGD_COLOR, 
								command = self.back_clicked)
		self.back_button.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

		self.frame_create_26wells()
	
	def frame_create_18wells(self):
		try: 
			self.wells_34_frame.destroy()
		except:
			pass
		try: 
			self.wells_18_frame.destroy()
		except:
			pass
		try: 
			self.wells_26_frame.destroy()
		except:
			pass

		self.wells_18_frame = Frame(self.work_frame_2, bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.wells_18_frame.grid(row=0, column=0, sticky="nsew")
		self.wells_18_frame.rowconfigure(0, weight=1)
		self.wells_18_frame.columnconfigure(0, weight=1)

		self.wells_18_scrollableframe = ScrollableFrame(self.wells_18_frame)
		self.wells_18_scrollableframe.grid(row=0, column=0, sticky="nsew")
		
		self.wells_18_scrollableframe.rowconfigure(0, weight=1)
		self.wells_18_scrollableframe.columnconfigure(0, weight=1)
		self.wells_18_scrollableframe.pack_propagate(0)
	
		self.number0_button_list_18 = Button(self.wells_18_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellNumber Label"][language],
						borderwidth = 0)
		self.number0_button_list_18.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)

		self.well0_entry_list_18 = Button(self.wells_18_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellName Label"][language],
						width=50,
						borderwidth = 0)
		self.well0_entry_list_18.grid(row=0, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_18 = list(range(18))
		self.number_button_list_18 = list(range(18))
		n=0
		for i in range(0,18):
			self.number_button_list_18[i] = Button(self.wells_18_scrollableframe.scrollable_frame,
							bg = WELLTABLE_LABEL_BGD_COLOR, 
							fg = WELLTABLE_LABEL_TXT_COLOR,
							font = WELLTABLE_LABEL_TXT_FONT,
							text= str(i+1),
							borderwidth = 0)
			self.number_button_list_18[i].grid(row=i+1, column=0, sticky='nsew', padx=1, pady=1)

			self.well_entry_list_18[i] = Entry(self.wells_18_scrollableframe.scrollable_frame,
									justify = 'left',
									width=50,
									font = WELLTABLE_LABEL_TXT_FONT)
			self.well_entry_list_18[i].grid(row=i+1, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_18[0].focus_set()
		self.well_entry_list_18[0].bind("<Return>",lambda funct:self.well_entry_list_18[1].focus_set())
		self.well_entry_list_18[1].bind("<Return>",lambda funct:self.well_entry_list_18[2].focus_set())
		self.well_entry_list_18[2].bind("<Return>",lambda funct:self.well_entry_list_18[3].focus_set())
		self.well_entry_list_18[3].bind("<Return>",lambda funct:self.well_entry_list_18[4].focus_set())
		self.well_entry_list_18[4].bind("<Return>",lambda funct:self.well_entry_list_18[5].focus_set())
		self.well_entry_list_18[5].bind("<Return>",lambda funct:self.well_entry_list_18[6].focus_set())
		self.well_entry_list_18[6].bind("<Return>",lambda funct:self.well_entry_list_18[7].focus_set())
		self.well_entry_list_18[7].bind("<Return>",lambda funct:self.well_entry_list_18[8].focus_set())
		self.well_entry_list_18[8].bind("<Return>",lambda funct:self.well_entry_list_18[9].focus_set())
		self.well_entry_list_18[9].bind("<Return>",lambda funct:self.well_entry_list_18[10].focus_set())
		self.well_entry_list_18[10].bind("<Return>",lambda funct:self.well_entry_list_18[11].focus_set())
		self.well_entry_list_18[11].bind("<Return>",lambda funct:self.well_entry_list_18[12].focus_set())
		self.well_entry_list_18[12].bind("<Return>",lambda funct:self.well_entry_list_18[13].focus_set())
		self.well_entry_list_18[13].bind("<Return>",lambda funct:self.well_entry_list_18[14].focus_set())
		self.well_entry_list_18[14].bind("<Return>",lambda funct:self.well_entry_list_18[15].focus_set())
		self.well_entry_list_18[15].bind("<Return>",lambda funct:self.well_entry_list_18[16].focus_set())
		self.well_entry_list_18[16].bind("<Return>",lambda funct:self.well_entry_list_18[17].focus_set())
		self.well_entry_list_18[17].bind("<Return>",lambda funct:self.well_entry_list_18[0].focus_set())

	def frame_create_26wells(self):
		try: 
			self.wells_34_frame.destroy()
		except:
			pass
		try: 
			self.wells_18_frame.destroy()
		except:
			pass
		try: 
			self.wells_26_frame.destroy()
		except:
			pass

		self.wells_26_frame = Frame(self.work_frame_2, bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.wells_26_frame.grid(row=0, column=0, sticky="nsew")
		self.wells_26_frame.rowconfigure(0, weight=1)
		self.wells_26_frame.columnconfigure(0, weight=1)

		self.wells_26_scrollableframe = ScrollableFrame(self.wells_26_frame)
		self.wells_26_scrollableframe.grid(row=0, column=0, sticky="nsew")
		
		self.wells_26_scrollableframe.rowconfigure(0, weight=1)
		self.wells_26_scrollableframe.columnconfigure(0, weight=1)
		self.wells_26_scrollableframe.pack_propagate(0)
	
		self.number0_button_list_26 = Button(self.wells_26_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellNumber Label"][language],
						borderwidth = 0)
		self.number0_button_list_26.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)

		self.well0_entry_list_26 = Button(self.wells_26_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellName Label"][language],
						width=50,
						borderwidth = 0)
		self.well0_entry_list_26.grid(row=0, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_26 = list(range(26))
		self.number_button_list_26 = list(range(26))
		n=0
		for i in range(0,26):
			self.number_button_list_26[i] = Button(self.wells_26_scrollableframe.scrollable_frame,
							bg = WELLTABLE_LABEL_BGD_COLOR, 
							fg = WELLTABLE_LABEL_TXT_COLOR,
							font = WELLTABLE_LABEL_TXT_FONT,
							text= str(i+1),
							borderwidth = 0)
			self.number_button_list_26[i].grid(row=i+1, column=0, sticky='nsew', padx=1, pady=1)

			self.well_entry_list_26[i] = Entry(self.wells_26_scrollableframe.scrollable_frame,
									justify = 'left',
									width=50,
									font = WELLTABLE_LABEL_TXT_FONT)
			self.well_entry_list_26[i].grid(row=i+1, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_26[0].focus_set()
		self.well_entry_list_26[0].bind("<Return>",lambda funct:self.well_entry_list_26[1].focus_set())
		self.well_entry_list_26[1].bind("<Return>",lambda funct:self.well_entry_list_26[2].focus_set())
		self.well_entry_list_26[2].bind("<Return>",lambda funct:self.well_entry_list_26[3].focus_set())
		self.well_entry_list_26[3].bind("<Return>",lambda funct:self.well_entry_list_26[4].focus_set())
		self.well_entry_list_26[4].bind("<Return>",lambda funct:self.well_entry_list_26[5].focus_set())
		self.well_entry_list_26[5].bind("<Return>",lambda funct:self.well_entry_list_26[6].focus_set())
		self.well_entry_list_26[6].bind("<Return>",lambda funct:self.well_entry_list_26[7].focus_set())
		self.well_entry_list_26[7].bind("<Return>",lambda funct:self.well_entry_list_26[8].focus_set())
		self.well_entry_list_26[8].bind("<Return>",lambda funct:self.well_entry_list_26[9].focus_set())
		self.well_entry_list_26[9].bind("<Return>",lambda funct:self.well_entry_list_26[10].focus_set())
		self.well_entry_list_26[10].bind("<Return>",lambda funct:self.well_entry_list_26[11].focus_set())
		self.well_entry_list_26[11].bind("<Return>",lambda funct:self.well_entry_list_26[12].focus_set())
		self.well_entry_list_26[12].bind("<Return>",lambda funct:self.well_entry_list_26[13].focus_set())
		self.well_entry_list_26[13].bind("<Return>",lambda funct:self.well_entry_list_26[14].focus_set())
		self.well_entry_list_26[14].bind("<Return>",lambda funct:self.well_entry_list_26[15].focus_set())
		self.well_entry_list_26[15].bind("<Return>",lambda funct:self.well_entry_list_26[16].focus_set())
		self.well_entry_list_26[16].bind("<Return>",lambda funct:self.well_entry_list_26[17].focus_set())
		self.well_entry_list_26[17].bind("<Return>",lambda funct:self.well_entry_list_26[18].focus_set())
		self.well_entry_list_26[18].bind("<Return>",lambda funct:self.well_entry_list_26[19].focus_set())
		self.well_entry_list_26[19].bind("<Return>",lambda funct:self.well_entry_list_26[20].focus_set())
		self.well_entry_list_26[20].bind("<Return>",lambda funct:self.well_entry_list_26[21].focus_set())
		self.well_entry_list_26[21].bind("<Return>",lambda funct:self.well_entry_list_26[22].focus_set())
		self.well_entry_list_26[22].bind("<Return>",lambda funct:self.well_entry_list_26[23].focus_set())
		self.well_entry_list_26[23].bind("<Return>",lambda funct:self.well_entry_list_26[24].focus_set())
		self.well_entry_list_26[24].bind("<Return>",lambda funct:self.well_entry_list_26[25].focus_set())
		self.well_entry_list_26[25].bind("<Return>",lambda funct:self.well_entry_list_26[0].focus_set())

	def frame_create_34wells(self):
		try: 
			self.wells_34_frame.destroy()
		except:
			pass
		try: 
			self.wells_18_frame.destroy()
		except:
			pass
		try: 
			self.wells_26_frame.destroy()
		except:
			pass

		self.wells_34_frame = Frame(self.work_frame_2, bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.wells_34_frame.grid(row=0, column=0, sticky="nsew")
		self.wells_34_frame.rowconfigure(0, weight=1)
		self.wells_34_frame.columnconfigure(0, weight=1)

		self.wells_34_scrollableframe = ScrollableFrame(self.wells_34_frame)
		self.wells_34_scrollableframe.grid(row=0, column=0, sticky="nsew")
		
		self.wells_34_scrollableframe.rowconfigure(0, weight=1)
		self.wells_34_scrollableframe.columnconfigure(0, weight=1)
		self.wells_34_scrollableframe.pack_propagate(0)
	
		self.number0_button_list_34 = Button(self.wells_34_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellNumber Label"][language],
						borderwidth = 0)
		self.number0_button_list_34.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)

		self.well0_entry_list_34 = Button(self.wells_34_scrollableframe.scrollable_frame,
						bg = WELLTABLE_LABEL_BGD_COLOR,
						fg = WELLTABLE_LABEL_TXT_COLOR,
						font = WELLTABLE_LABEL_TXT_FONT,
						text= SampleNamingScreen_Language["WellName Label"][language],
						width=50,
						borderwidth = 0)
		self.well0_entry_list_34.grid(row=0, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_34 = list(range(34))
		self.number_button_list_34 = list(range(34))
		n=0
		for i in range(0,34):
			self.number_button_list_34[i] = Button(self.wells_34_scrollableframe.scrollable_frame,
							bg = WELLTABLE_LABEL_BGD_COLOR, 
							fg = WELLTABLE_LABEL_TXT_COLOR,
							font = WELLTABLE_LABEL_TXT_FONT,
							text= str(i+1),
							borderwidth = 0)
			self.number_button_list_34[i].grid(row=i+1, column=0, sticky='nsew', padx=1, pady=1)

			self.well_entry_list_34[i] = Entry(self.wells_34_scrollableframe.scrollable_frame,
									justify = 'left',
									width=50,
									font = WELLTABLE_LABEL_TXT_FONT)
			self.well_entry_list_34[i].grid(row=i+1, column=1, sticky='nsew', padx=1, pady=1)

		self.well_entry_list_34[0].focus_set()
		self.well_entry_list_34[0].bind("<Return>",lambda funct:self.well_entry_list_34[1].focus_set())
		self.well_entry_list_34[1].bind("<Return>",lambda funct:self.well_entry_list_34[2].focus_set())
		self.well_entry_list_34[2].bind("<Return>",lambda funct:self.well_entry_list_34[3].focus_set())
		self.well_entry_list_34[3].bind("<Return>",lambda funct:self.well_entry_list_34[4].focus_set())
		self.well_entry_list_34[4].bind("<Return>",lambda funct:self.well_entry_list_34[5].focus_set())
		self.well_entry_list_34[5].bind("<Return>",lambda funct:self.well_entry_list_34[6].focus_set())
		self.well_entry_list_34[6].bind("<Return>",lambda funct:self.well_entry_list_34[7].focus_set())
		self.well_entry_list_34[7].bind("<Return>",lambda funct:self.well_entry_list_34[8].focus_set())
		self.well_entry_list_34[8].bind("<Return>",lambda funct:self.well_entry_list_34[9].focus_set())
		self.well_entry_list_34[9].bind("<Return>",lambda funct:self.well_entry_list_34[10].focus_set())
		self.well_entry_list_34[10].bind("<Return>",lambda funct:self.well_entry_list_34[11].focus_set())
		self.well_entry_list_34[11].bind("<Return>",lambda funct:self.well_entry_list_34[12].focus_set())
		self.well_entry_list_34[12].bind("<Return>",lambda funct:self.well_entry_list_34[13].focus_set())
		self.well_entry_list_34[13].bind("<Return>",lambda funct:self.well_entry_list_34[14].focus_set())
		self.well_entry_list_34[14].bind("<Return>",lambda funct:self.well_entry_list_34[15].focus_set())
		self.well_entry_list_34[15].bind("<Return>",lambda funct:self.well_entry_list_34[16].focus_set())
		self.well_entry_list_34[16].bind("<Return>",lambda funct:self.well_entry_list_34[17].focus_set())
		self.well_entry_list_34[17].bind("<Return>",lambda funct:self.well_entry_list_34[18].focus_set())
		self.well_entry_list_34[18].bind("<Return>",lambda funct:self.well_entry_list_34[19].focus_set())
		self.well_entry_list_34[19].bind("<Return>",lambda funct:self.well_entry_list_34[20].focus_set())
		self.well_entry_list_34[20].bind("<Return>",lambda funct:self.well_entry_list_34[21].focus_set())
		self.well_entry_list_34[21].bind("<Return>",lambda funct:self.well_entry_list_34[22].focus_set())
		self.well_entry_list_34[22].bind("<Return>",lambda funct:self.well_entry_list_34[23].focus_set())
		self.well_entry_list_34[23].bind("<Return>",lambda funct:self.well_entry_list_34[24].focus_set())
		self.well_entry_list_34[24].bind("<Return>",lambda funct:self.well_entry_list_34[25].focus_set())
		self.well_entry_list_34[25].bind("<Return>",lambda funct:self.well_entry_list_34[26].focus_set())
		self.well_entry_list_34[26].bind("<Return>",lambda funct:self.well_entry_list_34[27].focus_set())
		self.well_entry_list_34[27].bind("<Return>",lambda funct:self.well_entry_list_34[28].focus_set())
		self.well_entry_list_34[28].bind("<Return>",lambda funct:self.well_entry_list_34[29].focus_set())
		self.well_entry_list_34[29].bind("<Return>",lambda funct:self.well_entry_list_34[30].focus_set())
		self.well_entry_list_34[30].bind("<Return>",lambda funct:self.well_entry_list_34[31].focus_set())
		self.well_entry_list_34[31].bind("<Return>",lambda funct:self.well_entry_list_34[32].focus_set())
		self.well_entry_list_34[32].bind("<Return>",lambda funct:self.well_entry_list_34[33].focus_set())
		self.well_entry_list_34[33].bind("<Return>",lambda funct:self.well_entry_list_34[0].focus_set())

	def numberofwell_select(self, eventObject):
		if(self.numberofwells_combobox.current() == 0):
			self.frame_create_18wells()
		elif(self.numberofwells_combobox.current() == 1):
			self.frame_create_26wells()
		else:
			self.frame_create_34wells()

	def next_clicked(self):
		err = 0
		if(self.numberofwells_combobox.current() == 0):
			self.number_of_wells = 18
			self.wellname_list = list(range(18))
			for i in range(0, 18):
				if(len(self.well_entry_list_18[i].get().strip()) > 12):
					err = 1
					messagebox.showwarning("", SampleNamingScreen_Language["WellName Error"][language] + str(i+1) + ']')
					break
				else:
					self.wellname_list[i] = self.well_entry_list_18[i].get().strip()
		elif(self.numberofwells_combobox.current() == 1):
			self.number_of_wells = 26
			self.wellname_list = list(range(26))
			for i in range(0, 26):
				if(len(self.well_entry_list_26[i].get().strip()) > 12):
					err = 1
					messagebox.showwarning("", SampleNamingScreen_Language["WellName Error"][language] + str(i+1) + ']')
					break
				else:
					self.wellname_list[i] = self.well_entry_list_26[i].get().strip()
		else:
			self.number_of_wells = 34
			self.wellname_list = list(range(34))
			for i in range(0, 34):
				if(len(self.well_entry_list_34[i].get().strip()) > 12):
					err = 1
					messagebox.showwarning("", SampleNamingScreen_Language["WellName Error"][language] + str(i+1) + ']')
					break
				else:
					self.wellname_list[i] = self.well_entry_list_34[i].get().strip()
		
		if(err == 0):
			self.base_window.switch_page(self.base_window.multi_setting)
			self.base_window.multi_setting.update_frame()


	def back_clicked(self):
		self.base_window.switch_page(self.base_window.main_menu)

		self.base_window.frame_list.remove(self.base_window.sample_naming)
		del self.base_window.sample_naming
		self.base_window.sample_naming = SampleNaming_Screen(self.base_window)
		self.base_window.frame_list.append(self.base_window.sample_naming)

		# python = sys.executable
		# os.execl(python, python, *sys.argv)

class MainMenu(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.base_window = master
		
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# Base frame create
		self.base_frame = Frame(self,bg=MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.base_frame.grid(row=0, column=0, sticky='nsew')
		self.base_frame.rowconfigure(0, weight=1)
		self.base_frame.rowconfigure(1, weight=10)
		self.base_frame.rowconfigure(2, weight=1)
		self.base_frame.columnconfigure(0, weight=1)

		self.title_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.title_frame.grid(row=0, column=0, sticky='nsew')
		self.title_frame.rowconfigure(0, weight=1)
		self.title_frame.columnconfigure(0, weight=1)
		self.title_frame.grid_propagate(False)

		self.work_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.work_frame.grid(row=1, column=0, sticky='nsew')
		self.work_frame.rowconfigure(0, weight=1)
		self.work_frame.columnconfigure(0, weight=1)
		self.work_frame.grid_propagate(False)

		self.button_frame = Frame(self.base_frame, bg = MAIN_FUNCTION_FRAME_BGD_COLOR)
		self.button_frame.grid(row=2, column=0, sticky='nsew')
		self.button_frame.rowconfigure(0, weight=1)
		self.button_frame.columnconfigure(0, weight=2)
		self.button_frame.columnconfigure(1, weight=2)
		self.button_frame.columnconfigure(2, weight=2)
		self.button_frame.columnconfigure(3, weight=2)
		self.button_frame.columnconfigure(4, weight=1)
		self.button_frame.grid_propagate(False)

		self.title_label = Label(self.title_frame,
								text = "VE100",
								font = MAIN_TITLE_TXT_FONT,
								bg = MAIN_TITLE_BGD_COLOR,
								fg = MAIN_TITLE_TXT_COLOR)
		self.title_label.grid(row=0, column=0, sticky="snew")

		self.run_button = Button(self.button_frame,
									text = MainScreen_Language["Run Button"][language],
									font = MAIN_MENU_BUTTON_TXT_FONT,
									bg = MAIN_MENU_BUTTON_BGD_COLOR,
									fg = MAIN_MENU_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.run_clicked)
		self.run_button.grid(row=0, column=0, sticky='nsew')

		self.bandFinder_button = Button(self.button_frame,
									text = MainScreen_Language["BandFinder Button"][language],
									font = MAIN_MENU_BUTTON_TXT_FONT,
									bg = MAIN_MENU_BUTTON_BGD_COLOR,
									fg = MAIN_MENU_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.bandFinder_clicked)
		self.bandFinder_button.grid(row=0, column=1, sticky='nsew')

		self.connect_button = Button(self.button_frame,
									text = MainScreen_Language["Connect Button"][language],
									font = MAIN_MENU_BUTTON_TXT_FONT,
									bg = MAIN_MENU_BUTTON_BGD_COLOR,
									fg = MAIN_MENU_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.connect_clicked)
		self.connect_button.grid(row=0, column=2, sticky='nsew')

		self.language_button = Button(self.button_frame,
									text = MainScreen_Language["Language Button"][language],
									font = MAIN_MENU_BUTTON_TXT_FONT,
									bg = MAIN_MENU_BUTTON_BGD_COLOR,
									fg = MAIN_MENU_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.language_clicked)
		self.language_button.grid(row=0, column=3, sticky='nsew')
		
		self.exit_button = Button(self.button_frame,
									text = MainScreen_Language["Exit Button"][language],
									font = MAIN_MENU_BUTTON_TXT_FONT,
									bg = EXIT_BUTTON_BGD_COLOR,
									fg = MAIN_MENU_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.exit_clicked)
		self.exit_button.grid(row=0, column=4, sticky='nsew')

		
		############################ CONNECT GUI ###############################
		# self.connect_labelframe = LabelFrame(self.work_frame, 
		# 							   	bg = MAIN_FUNCTION_FRAME_BGD_COLOR,
		# 					  			text = 'Connect',
		# 								font = TITLE_TXT_FONT)
		############################ CONNECT GUI ###############################

		self.run_clicked()

	def singleStage_clicked(self):
		self.stage_chosen = 0
		self.folderNaming_screen()

	def multiStage_clicked(self):
		self.stage_chosen = 1
		self.folderNaming_screen()
	
	def folderNaming_screen(self):
		self.stageNaming_labelframe = LabelFrame(self.run_labelframe,
												bg = FOLDERNAMING_FRAME_BGD_COLOR,
												fg = FOLDERNAMING_FRAME_TXT_COLOR)
		if(self.stage_chosen == 0):
			self.stageNaming_labelframe['text'] = MainScreen_Language['SingleStageFolder LabelFrame'][language]
		else:
			self.stageNaming_labelframe['text'] = MainScreen_Language['MultiStageFolder LabelFrame'][language]
		self.stageNaming_labelframe.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.stageNaming_labelframe.rowconfigure(0, weight=1)
		self.stageNaming_labelframe.rowconfigure(1, weight=1)
		self.stageNaming_labelframe.columnconfigure(0, weight=1)

		
		self.stageNaming_frame_1 = Frame(self.stageNaming_labelframe, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_1.grid(row=0, column=0, sticky="nsew")
		self.stageNaming_frame_1.columnconfigure(0, weight=2)
		self.stageNaming_frame_1.columnconfigure(1, weight=3)
		self.stageNaming_frame_1.columnconfigure(2, weight=2)
		self.stageNaming_frame_1.rowconfigure(0, weight=1)
		self.stageNaming_frame_1.grid_propagate(False)

		self.stageNaming_frame_2 = Frame(self.stageNaming_labelframe, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_2.grid(row=1, column=0, sticky="nsew")
		self.stageNaming_frame_2.columnconfigure(0, weight=2)
		self.stageNaming_frame_2.columnconfigure(1, weight=3)
		self.stageNaming_frame_2.columnconfigure(2, weight=2)
		self.stageNaming_frame_2.rowconfigure(0, weight=1)
		self.stageNaming_frame_2.grid_propagate(False)
		
		self.stageNaming_frame_1_1 = Frame(self.stageNaming_frame_1, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_1_1.grid(row=0, column=0, sticky="nsew")
		self.stageNaming_frame_1_2 = Frame(self.stageNaming_frame_1, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_1_2.grid(row=0, column=1, sticky="nsew")
		self.stageNaming_frame_1_2.rowconfigure(0, weight=1)
		self.stageNaming_frame_1_2.rowconfigure(1, weight=1)
		self.stageNaming_frame_1_2.columnconfigure(0, weight=1)
		self.stageNaming_frame_1_3 = Frame(self.stageNaming_frame_1, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_1_3.grid(row=0, column=2, sticky="nsew")
		
		self.stageNaming_frame_2_1 = Frame(self.stageNaming_frame_2, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_2_1.grid(row=0, column=0, sticky="nsew")
		self.stageNaming_frame_2_2 = Frame(self.stageNaming_frame_2, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_2_2.grid(row=0, column=1, sticky="nsew")
		self.stageNaming_frame_2_2.columnconfigure(0, weight=1)
		self.stageNaming_frame_2_2.columnconfigure(1, weight=1)
		self.stageNaming_frame_2_2.rowconfigure(0, weight=1)
		self.stageNaming_frame_2_3 = Frame(self.stageNaming_frame_2, bg = FOLDERNAMING_FRAME_BGD_COLOR)
		self.stageNaming_frame_2_3.grid(row=0, column=2, sticky="nsew")

		self.folderName_label =  Label(self.stageNaming_frame_1_2,
								text = MainScreen_Language['FolderName Label'][language],
								bg = FOLDERNAMING_FRAME_BGD_COLOR,
								fg = FOLDERNAME_LABEL_TXT_COLOR,
								font = FOLDERNAME_LABEL_TXT_FONT)
		self.folderName_label.grid(row=0, column=0, sticky='s')
		self.folderName_entry =  Entry(self.stageNaming_frame_1_2, justify='right', font=('Arial',15))
		self.folderName_entry.grid(row=1, column=0, padx=100, sticky='we')

		self.next_button = Button(self.stageNaming_frame_2_2,
									text = MainScreen_Language["Next Button"][language],
									font = FOLDERNAME_BUTTON_TXT_FONT,
									bg = FOLDERNAME_BUTTON_BGD_COLOR,
									fg = FOLDERNAME_BUTTON_TXT_COLOR,
									borderwidth = 0,
									width = 12, 
									height = 3,
									command = self.next_clicked)
		self.next_button.grid(row=0, column=0, sticky='n')

		self.cancel_button = Button(self.stageNaming_frame_2_2,
									text = MainScreen_Language["Cancel Button"][language],
									font = FOLDERNAME_BUTTON_TXT_FONT,
									bg = FOLDERNAME_BUTTON_BGD_COLOR,
									fg = FOLDERNAME_BUTTON_TXT_COLOR,
									width = 12, 
									height = 3,
									borderwidth = 0,
									command = self.cancel_clicked)
		self.cancel_button.grid(row=0, column=1, sticky='n')

	def next_clicked(self):
		self.folderName_set = self.folderName_entry.get()
		if(self.folderName_set != ''):
			create_time = strftime("%y-%m-%d")
			if not os.path.exists(result_dir + '/' + create_time):
				self.result_path_0 = os.path.join(result_dir + '/', create_time)
				os.mkdir(self.result_path_0)
			else:
				self.result_path_0 =  result_dir + '/' + create_time

			if(os.path.exists(self.result_path_0 + "/" + self.folderName_set)):
				msg = messagebox.askquestion("", MainScreen_Language['FolderName Exists'][language])
				if(msg == 'yes'):
					self.result_path = os.path.join(self.result_path_0, self.folderName_set +'/')
					shutil.rmtree(self.result_path)
					os.mkdir(self.result_path)
			else:
				self.result_path = os.path.join(self.result_path_0,  self.folderName_set +'/')
				os.mkdir(self.result_path)

			#### chuyen sang naming screen ####
			self.stageNaming_labelframe.destroy()
			self.base_window.switch_page(self.base_window.sample_naming)

		else: 
			messagebox.showwarning("", MainScreen_Language['FolderName Entry Empty'][language])

	def cancel_clicked(self):
		self.stageNaming_labelframe.destroy()

	def run_clicked(self):
		try: 
			self.run_labelframe.destroy()
		except:
			pass
		try: 
			self.bandFinder_labelframe.destroy()
		except:
			pass 
		try: 
			self.connect_labelframe.destroy()
		except:
			pass
		try: 
			self.language_labelframe.destroy()
		except:
			pass
		
		self.run_button['bg'] = MAIN_MENU_BUTTON_ACTIVE_BGD_COLOR
		self.bandFinder_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.connect_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.language_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		############################## RUN GUI #################################
		self.run_labelframe = LabelFrame(self.work_frame, 
										bg = MAIN_MENU_LABELFRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = MainScreen_Language["Run LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.run_labelframe.grid(row=0, column=0, sticky='nsew')

		self.run_labelframe.columnconfigure(0, weight=1)  # Cột 0 giãn đều
		self.run_labelframe.columnconfigure(1, weight=1)  # Cột 1 giãn đều
		self.run_labelframe.columnconfigure(2, weight=1)
		self.run_labelframe.columnconfigure(3, weight=1)
		self.run_labelframe.columnconfigure(4, weight=1)
		self.run_labelframe.rowconfigure(0, weight=1)

		# self.singleStage_button = Button(self.run_labelframe,
		# 							text = MainScreen_Language["SingleStage Button"][language],
		# 							font = RUN_BUTTON_TXT_FONT,
		# 							bg = RUN_BUTTON_BGD_COLOR,
		# 							fg = RUN_BUTTON_TXT_COLOR,
		# 							borderwidth = 0,
		# 							command = self.singleStage_clicked)
		# self.singleStage_button.grid(row=0, column=1, ipadx=50, ipady=35)
		# self.singleStage_button.columnconfigure(0, weight=1)
		# self.singleStage_button.rowconfigure(0, weight=1)

		self.multiStage_button = Button(self.run_labelframe,
									text = MainScreen_Language["Electrophoresis Button"][language],
									font = RUN_BUTTON_TXT_FONT,
									bg = RUN_BUTTON_BGD_COLOR,
									fg = RUN_BUTTON_TXT_COLOR,
									borderwidth = 0,
									command = self.multiStage_clicked)
		self.multiStage_button.grid(row=0, column=2, ipadx=50, ipady=35)
		self.multiStage_button.columnconfigure(0, weight=1)
		self.multiStage_button.rowconfigure(0, weight=1)
		############################## RUN GUI #################################


	def bandFinder_clicked(self):
		try: 
			self.bandFinder_labelframe.destroy()
		except:
			pass 
		try: 
			self.run_labelframe.destroy()
		except:
			pass 
		try: 
			self.connect_labelframe.destroy()
		except:
			pass
		try: 
			self.language_labelframe.destroy()
		except:
			pass

		self.run_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.bandFinder_button['bg'] = MAIN_MENU_BUTTON_ACTIVE_BGD_COLOR
		self.connect_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.language_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		
		self.line1_value = DoubleVar()
		self.line2_value = DoubleVar()
		self.bandline_value = DoubleVar()

		self.line1 = None
		self.line2 = None 
		self.bandline = None
		########################## BAND FINDER GUI #############################
		#--------- Band Finder Frame ----------#
		self.bandFinder_labelframe = LabelFrame(self.work_frame, 
										bg = MAIN_MENU_LABELFRAME_BGD_COLOR,
										text = MainScreen_Language["BandFinder LabelFrame"][language],
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.bandFinder_labelframe.grid(row=0, column=0, sticky='nsew')
		self.bandFinder_labelframe.rowconfigure(0, weight=7)  # Frame 1
		self.bandFinder_labelframe.rowconfigure(1, weight=1)  # Frame 2
		self.bandFinder_labelframe.columnconfigure(0, weight=1)
		
		#--------- Frame chua Canvas & Slider ----------#
		self.BF_frame_1 = Frame(self.bandFinder_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.BF_frame_1.grid(row=0, column=0, sticky="nsew")
		self.BF_frame_1.columnconfigure(0, weight=15)
		self.BF_frame_1.columnconfigure(1, weight=1)
		self.BF_frame_1.rowconfigure(0, weight=1)
		self.BF_frame_1.grid_propagate(False)

		#--------- Frame chua cac Control Button ----------#
		self.BF_frame_2 = Frame(self.bandFinder_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.BF_frame_2.grid(row=1, column=0, sticky="nsew")
		self.BF_frame_2.columnconfigure(0, weight=1)
		self.BF_frame_2.columnconfigure(1, weight=2)
		self.BF_frame_2.columnconfigure(2, weight=2)
		self.BF_frame_2.columnconfigure(3, weight=1)
		self.BF_frame_2.rowconfigure(0, weight=1)
		self.BF_frame_2.grid_propagate(False)

		#--------- Frame chua Canvas ----------#
		self.BF_frame_1_1 = Frame(self.BF_frame_1, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_1_1.grid(row=0, column=0, sticky="nsew")
		self.BF_frame_1_1.rowconfigure(0, weight=1)
		self.BF_frame_1_1.columnconfigure(0, weight=1)
		self.BF_frame_1_1.grid_propagate(False)
		
		self.image_canvas = Canvas(self.BF_frame_1_1, bg='grey10')
		self.image_canvas.grid(row=0, column=0, pady=13, sticky="nsew")
		
		#--------- Frame chua cac Slider ----------#
		self.BF_frame_1_2 = Frame(self.BF_frame_1, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_1_2.grid(row=0, column=1, sticky="nsew")
		self.BF_frame_1_2.rowconfigure(0, weight=1)
		self.BF_frame_1_2.columnconfigure(0, weight=1)
		self.BF_frame_1_2.columnconfigure(1, weight=1)
		self.BF_frame_1_2.columnconfigure(2, weight=1)
		self.BF_frame_1_2.grid_propagate(False)

		self.lowerBand_slidebar = Scale(self.BF_frame_1_2, 
								variable = self.line1_value, 
								bg = FIRSTBAND_COLOR, 
								orient = VERTICAL, 
								showvalue=False,
								state = 'disabled',
								command = self.LowerLine_Drawing)
		self.lowerBand_slidebar.grid(row=0, column=0, sticky='snew')
		self.higherBand_slidebar = Scale(self.BF_frame_1_2, 
								variable = self.line2_value, 
								bg = LASTBAND_COLOR, 
								orient = VERTICAL, 
								showvalue=False,
								state = 'disabled',
								command = self.HigherLine_Drawing)
		self.higherBand_slidebar.grid(row=0, column=1, sticky='snew')
		self.resultBand_slidebar = Scale(self.BF_frame_1_2, 
								variable = self.bandline_value, 
								bg = RESULTBAND_COLOR, 
								orient = VERTICAL, 
								showvalue=False,
								state='disabled',
								command = self.ResultLine_Drawing)
		self.resultBand_slidebar.grid(row=0, column=2, sticky='snew')

		


		#--------- Frame Control Button 1 ----------#
		self.BF_frame_2_1 = LabelFrame(self.BF_frame_2, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_2_1.grid(row=0, column=0, ipadx=2, ipady=2, sticky="nsew")
		self.BF_frame_2_1.rowconfigure(0, weight=1)
		self.BF_frame_2_1.columnconfigure(0, weight=1)
		self.BF_frame_2_1.grid_propagate(False)

		self.bandopen_button = Button(self.BF_frame_2_1, 
								text = MainScreen_Language["Open Button"][language], 
								font = ('Arial', 13), 
								fg = BANDFINDER_BUTTON_TXT_COLOR, 
								bg = BANDFINDER_BUTTON_BGD_COLOR, 
								borderwidth=2,
								command = self.bandopen_clicked)
		self.bandopen_button.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

		#--------- Frame Control Button 2 ----------#
		self.BF_frame_2_2 = LabelFrame(self.BF_frame_2, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_2_2.grid(row=0, column=1, ipadx=2, ipady=2, sticky="nsew")
		self.BF_frame_2_2.rowconfigure(0, weight=1)
		self.BF_frame_2_2.columnconfigure(0, weight=1)
		self.BF_frame_2_2.rowconfigure(1, weight=1)
		self.BF_frame_2_2.columnconfigure(1, weight=1)
		self.BF_frame_2_2.grid_propagate(False)

		self.firstband_label = Label(self.BF_frame_2_2, 
							text = MainScreen_Language["FirstBand Label"][language], 
							bg = BANDFINDER_FRAME_BGD_COLOR,
							fg = FIRSTBAND_COLOR, 
							font = ('Arial', 12))
		self.firstband_label.grid(row=0, column=0, padx=2, pady=2, sticky="nsew") 
		self.lastband_label = Label(self.BF_frame_2_2, 
							text = MainScreen_Language["LastBand Label"][language], 
							bg = BANDFINDER_FRAME_BGD_COLOR,
							fg = LASTBAND_COLOR, 
							font = ('Arial', 12))
		self.lastband_label.grid(row=1, column=0, padx=2, pady=2, sticky="nsew") 

		self.firstband_entry = Entry(self.BF_frame_2_2, 
								justify='right',
								# width=10, 
								font=('Arial',12))
		self.firstband_entry.grid(row=0, column=1, pady=2, padx=2, sticky="nsew")
		self.firstband_entry.insert(0, 2000)
		self.lastband_entry = Entry(self.BF_frame_2_2, 
							justify='right', 
							#   width=10, 
							font=('Arial',12))
		self.lastband_entry.grid(row=1, column=1, pady=2, padx=2, sticky="nsew")
		self.lastband_entry.insert(0, 100)
		
		#--------- Frame Control Button 3 ----------#
		self.BF_frame_2_3 = LabelFrame(self.BF_frame_2, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_2_3.grid(row=0, column=2, ipadx=2, ipady=2, sticky="nsew")
		self.BF_frame_2_3.columnconfigure(0, weight=1)
		self.BF_frame_2_3.columnconfigure(1, weight=2)
		self.BF_frame_2_3.rowconfigure(0, weight=1)
		self.BF_frame_2_3.rowconfigure(1, weight=1)
		self.BF_frame_2_3.grid_propagate(False)

		self.bandsize_label = Label(self.BF_frame_2_3, 
							text = MainScreen_Language["BandSize Label"][language], 
							bg = BANDFINDER_FRAME_BGD_COLOR,
							fg = RESULTBAND_COLOR, 
							anchor='w',
							font = ('Arial', 12))
		self.bandsize_label.grid(row=0, column=0, padx=2, pady=2, sticky="we")

		self.bandsize_entry = Entry(self.BF_frame_2_3, 
							justify='right', 
							#   width=10, 
							font=('Arial',12))
		self.bandsize_entry.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

		self.bandcheck_button = Button(self.BF_frame_2_3, 
								text = MainScreen_Language["Check Button"][language], 
								font = ('Arial', 13), 
								fg = BANDFINDER_BUTTON_TXT_COLOR, 
								bg = BANDFINDER_BUTTON_BGD_COLOR, 
								borderwidth=2,
								state = 'disabled',
								command = self.bandcheck_clicked)
		self.bandcheck_button.grid(row=0, column=1, rowspan=2, padx=2, pady=2, sticky="nsew")

		#--------- Frame Control Button 4 ----------#
		self.BF_frame_2_4 = LabelFrame(self.BF_frame_2, bg = BANDFINDER_FRAME_BGD_COLOR)
		self.BF_frame_2_4.grid(row=0, column=3, ipadx=2, ipady=2, sticky="nsew")
		self.BF_frame_2_4.rowconfigure(0, weight=1)
		self.BF_frame_2_4.columnconfigure(0, weight=1)
		self.BF_frame_2_4.grid_propagate(False)

		self.bandsave_button = Button(self.BF_frame_2_4, 
								text = MainScreen_Language["Save Button"][language], 
								font = ('Arial', 13), 
								fg = BANDFINDER_BUTTON_TXT_COLOR, 
								bg = BANDFINDER_BUTTON_BGD_COLOR, 
								borderwidth=2,
								state = 'disabled',
								command = self.bandsave_clicked)
		self.bandsave_button.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

		########################## BAND FINDER GUI #############################

	def connect_clicked(self):
		try: 
			self.run_labelframe.destroy()
		except:
			pass
		try: 
			self.bandFinder_labelframe.destroy()
		except:
			pass 
		try: 
			self.connect_labelframe.destroy()
		except:
			pass
		try: 
			self.language_labelframe.destroy()
		except:
			pass
		
		self.run_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.bandFinder_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.connect_button['bg'] = MAIN_MENU_BUTTON_ACTIVE_BGD_COLOR
		self.language_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR

		############################## CONNECT GUI #################################
		self.connect_labelframe = LabelFrame(self.work_frame, 
										bg = MAIN_MENU_LABELFRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = MainScreen_Language["Connect LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.connect_labelframe.grid(row=0, column=0, sticky='nsew')
		self.connect_labelframe.rowconfigure(0, weight=1)
		self.connect_labelframe.rowconfigure(1, weight=1)
		self.connect_labelframe.rowconfigure(2, weight=1)
		self.connect_labelframe.columnconfigure(0, weight=1)
		
		self.connect_frame_1 = Frame(self.connect_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR) 			# Chua label trang thai account
		self.connect_frame_1.grid(row=0, column=0, sticky='nsew')
		self.connect_frame_1.rowconfigure(0, weight=1)
		self.connect_frame_1.columnconfigure(0, weight=1)
		self.connect_frame_1.grid_propagate(False)
		
		self.connect_frame_2 = Frame(self.connect_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)		# Chua label va entry dang nhap
		self.connect_frame_2.grid(row=1, column=0, sticky='nsew')
		self.connect_frame_2.columnconfigure(0, weight=1)
		self.connect_frame_2.columnconfigure(1, weight=2)
		self.connect_frame_2.columnconfigure(2, weight=1)
		self.connect_frame_2.rowconfigure(0, weight=1)
		self.connect_frame_2.grid_propagate(False)

		self.connect_frame_3 = Frame(self.connect_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)			# Chua button login
		self.connect_frame_3.grid(row=2, column=0, sticky='nsew')
		self.connect_frame_3.columnconfigure(0, weight=1)
		self.connect_frame_3.rowconfigure(0, weight=1)
		self.connect_frame_3.grid_propagate(False)

		##### connect_frame_1 #####
		self.login_label = Label(self.connect_frame_1, 
						bg = MAIN_MENU_LABELFRAME_BGD_COLOR,
						font = LOGIN_LABEL_TXT_FONT)
		self.login_label.grid(row=0, column=0, sticky='nsew')


		##### connect_frame_2 #####
		self.connect_frame_2_1 = Frame(self.connect_frame_2, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.connect_frame_2_1.grid(row=0, column=0, sticky='nsew')
		self.connect_frame_2_1.grid_propagate(False)

		self.connect_frame_2_2 = Frame(self.connect_frame_2, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.connect_frame_2_2.grid(row=0, column=1, sticky='nsew')
		self.connect_frame_2_2.rowconfigure(0, weight=2)
		self.connect_frame_2_2.rowconfigure(1, weight=2)
		self.connect_frame_2_2.rowconfigure(2, weight=1)
		self.connect_frame_2_2.columnconfigure(0, weight=1)
		self.connect_frame_2_2.columnconfigure(1, weight=2)
		self.connect_frame_2_2.grid_propagate(False)

		self.connect_frame_2_3 = Frame(self.connect_frame_2, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)
		self.connect_frame_2_3.grid(row=0, column=2, sticky='nsew')
		self.connect_frame_2_3.grid_propagate(False)

		self.email_label = Label(self.connect_frame_2_2,
							text = MainScreen_Language["Email Label"][language],
							bg = USERPASS_LABEL_BGD_COLOR,
							fg = USERPASS_LABEL_TXT_COLOR,
							font = USERPASS_LABEL_TXT_FONT)
		self.email_label.grid(row=0, column=0, padx=10, sticky = 'e')

		self.password_label = Label(self.connect_frame_2_2,
							text = MainScreen_Language["Password Label"][language],
							bg = USERPASS_LABEL_BGD_COLOR,
							fg = USERPASS_LABEL_TXT_COLOR,
							font = USERPASS_LABEL_TXT_FONT)
		self.password_label.grid(row=1, column=0, padx=10, sticky='e')

		self.email_entry =  Entry(self.connect_frame_2_2, justify='right', font=('Arial',15))
		self.email_entry.grid(row=0, column=1, padx=10, sticky='we')
		self.password_entry =  Entry(self.connect_frame_2_2, justify='right', font=('Arial',15))
		self.password_entry.grid(row=1, column=1, padx=10, sticky='we')

		self.hide_state = IntVar()
		self.hidepass_checkbutton = Checkbutton(self.connect_frame_2_2, 
										variable = self.hide_state, 
										bg = USERPASS_LABEL_BGD_COLOR, 
										text = MainScreen_Language["HidePass Checkbutton"][language],
										onvalue = 1, offvalue = 0, 
										command= self.hide_charaters)
		self.hidepass_checkbutton.select()
		

		##### connect_frame_3 #####
		self.login_button = Button(self.connect_frame_3,
							bg = LOGIN_BUTTON_BGD_COLOR, 
							fg = LOGIN_BUTTON_TXT_COLOR,
							font = LOGIN_BUTTON_TXT_FONT,
							bd = 0, 
							command = self.login_clicked)
		self.login_button.grid(row=0, column=0, ipadx=30, ipady=15, pady=5, sticky='n')

		if(account_active):
			self.login_label['text'] = MainScreen_Language["AccountActive Label"][language]
			self.login_label['fg'] = ACCOUNT_ACTIVE_LABEL_TXT_COLOR
			self.login_button['text'] = MainScreen_Language["Logout Button"][language]

			self.email_entry.insert(0, email_address)
			self.email_entry['state'] = "disable"
			self.password_entry.insert(0, email_password)
			self.password_entry['state'] = "disable"

			self.hidepass_checkbutton.select()
			self.hide_charaters()
			# self.hidepass_checkbutton.grid_forget()
		else:
			self.login_label['text'] = MainScreen_Language["AccountInactive Label"][language]
			self.login_label['fg'] = ACCOUNT_INACTIVE_LABEL_TXT_COLOR
			self.login_button['text'] = MainScreen_Language["Login Button"][language]

			self.email_entry['state'] = "normal"
			self.password_entry['state'] = "normal"

			self.hidepass_checkbutton.grid(row=2, column=1, sticky='e', padx=8)
		
		self.hide_charaters()


	def language_clicked(self):
		try: 
			self.run_labelframe.destroy()
		except:
			pass
		try: 
			self.bandFinder_labelframe.destroy()
		except:
			pass 
		try: 
			self.connect_labelframe.destroy()
		except:
			pass
		try: 
			self.language_labelframe.destroy()
		except:
			pass
		
		self.run_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.bandFinder_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.connect_button['bg'] = MAIN_MENU_BUTTON_BGD_COLOR
		self.language_button['bg'] = MAIN_MENU_BUTTON_ACTIVE_BGD_COLOR

		############################## LANGUAGE GUI #################################
		self.language_labelframe = LabelFrame(self.work_frame, 
										bg = MAIN_MENU_LABELFRAME_BGD_COLOR,
										fg = MAIN_MENU_LABELFRAME_TXT_COLOR,
										text = MainScreen_Language["Language LabelFrame"][language],
										highlightbackground = MAIN_MENU_LABELFRAME_BORDER_COLOR,
										font = MAIN_MENU_LABELFRAME_TXT_FONT)
		self.language_labelframe.grid(row=0, column=0, sticky='nsew')
		self.language_labelframe.rowconfigure(0, weight=1)
		self.language_labelframe.rowconfigure(1, weight=1)
		self.language_labelframe.columnconfigure(0, weight=1)

		self.connect_frame_1 = Frame(self.language_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR) 			# Chua label trang thai account
		self.connect_frame_1.grid(row=0, column=0, sticky='nsew')
		self.connect_frame_1.rowconfigure(0, weight=1)
		self.connect_frame_1.columnconfigure(0, weight=1)
		self.connect_frame_1.grid_propagate(False)
		
		self.connect_frame_2 = Frame(self.language_labelframe, bg = MAIN_MENU_LABELFRAME_BGD_COLOR)		# Chua label va entry dang nhap
		self.connect_frame_2.grid(row=1, column=0, sticky='nsew')
		self.connect_frame_2.columnconfigure(0, weight=1)
		self.connect_frame_2.rowconfigure(0, weight=1)
		self.connect_frame_2.grid_propagate(False)

		language_list = ['English', 'Tiếng Việt']
		self.language_combobox= ttk.Combobox(self.connect_frame_1, 
								state = "readonly",
								width = 20, 
								font = LANGUAGE_COMBOBOX_TXT_FONT,
								value = language_list)
		self.language_combobox.grid(row=0, column=0, sticky='s', pady=40)
		self.language_combobox.current(language)

		self.save_button = Button(self.connect_frame_2,
							text = MainScreen_Language['Save Button'][language],
							bg = LANGUAGE_SAVE_BUTTON_BGD_COLOR, 
							fg = LANGUAGE_SAVE_BUTTON_TXT_COLOR,
							font = LANGUAGE_SAVE_BUTTON_TXT_FONT,
							bd = 0, 
							command = self.save_clicked)
		self.save_button.grid(row=0, column=0, ipadx=30, ipady=15, sticky='n', pady=40)
		
	def hide_charaters(self):
		if(self.hide_state.get()==0):
			self.password_entry['show']=""
		else:
			self.password_entry['show']="◼"

	def exit_clicked(self):
		msg = messagebox.askquestion("", MainScreen_Language["Exit Confirm"][language])
		if(msg == "yes"):
			os._exit(0)
			self.base_window.destroy()
	
	def LowerLine_Drawing(self, value=None):
		try:
			self.image_canvas.delete(self.line1)
			self.image_canvas.delete(self.bandline)
		except:
			pass

		self.bandsave_button['state'] = 'disabled'
		self.resultBand_slidebar['state'] = 'disabled'

		self.line1 = self.image_canvas.create_line(1, 
											self.line1_value.get(), 
											self.image_canvas.winfo_width(),  
											self.line1_value.get(), 
											fill=FIRSTBAND_COLOR, 
											width=1)
	def HigherLine_Drawing(self, value=None):
		try:
			self.image_canvas.delete(self.line2)
			self.image_canvas.delete(self.bandline)
		except:
			pass

		self.bandsave_button['state'] = 'disabled'
		self.resultBand_slidebar['state'] = 'disabled'

		self.line2 = self.image_canvas.create_line(1, self.line2_value.get(), 
											self.image_canvas.winfo_width(),  
											self.line2_value.get(), 
											fill=LASTBAND_COLOR, 
											width=1)
	
	def ResultLine_Drawing(self, value=None):
		try:
			self.image_canvas.delete(self.bandline)
		except:
			pass
		
		self.band_distance = self.bandline_value.get()

		if(self.band_distance > self.line2_value.get()):
			self.resultBand_slidebar.set(self.line2_value.get())
		if(self.band_distance < self.line1_value.get()):
			self.resultBand_slidebar.set(self.line1_value.get())

		tmp_value = (self.band_distance - self.b_value)/self.a_value
		self.resultband_value = round(pow(10, tmp_value))

		if(self.resultband_value > int(self.firstband_entry.get())):
			self.resultband_value = 2000
		if(self.resultband_value < int(self.lastband_entry.get())):
			self.resultband_value = 100
		
		if(self.bandcheck_is_clicked == 0):
			self.bandsize_entry.delete(0, END)
			self.bandsize_entry.insert(0, self.resultband_value)
		else:
			self.bandcheck_is_clicked = 0

		self.bandline = self.image_canvas.create_line(1, 
													self.bandline_value.get(), 
													self.image_canvas.winfo_width(),  
													self.bandline_value.get(), 
													fill=RESULTBAND_COLOR, 
													width=1)


		
	def bandopen_clicked(self):
		self.openfile_name =  filedialog.askopenfilename(initialdir=result_dir, filetypes=[('png file','*png')])
		if self.openfile_name is not None:
			# lấy kích thước canvas so với kích thước ảnh để tính tỉ lệ scale
			self.image_canvas_width = self.image_canvas.winfo_width()
			self.image_canvas_height = self.image_canvas.winfo_height()
			self.canvas_image_percent = round(self.image_canvas_width*100/RESULT_IMAGE_WIDTH) # % dung de fix chieu rong cua anh goc voi chieu rong cua canvas

			self.band_img = Image.open(self.openfile_name)
			self.img_original_width, self.img_original_height = self.band_img.size
			self.img_scale_width = int(self.img_original_width * self.canvas_image_percent / 100)
			self.img_scale_height = int(self.img_original_height * self.canvas_image_percent / 100)
			self.scale_img = self.band_img.resize((self.img_scale_width, self.img_scale_height))

			# img_height_shift = round((img_scale_height - self.image_canvas_height)/2) # fix chieu cao cua anh sau khi scale voi chieu cao cua canvas
			# crop_area = (0, img_height_shift, img_scale_width, img_height_shift + self.image_canvas_height)
			crop_area = (0, band_offset, self.img_scale_width, band_offset + self.image_canvas_height)
			self.crop_img = self.scale_img.crop(crop_area)
			self.display_img = ImageTk.PhotoImage(self.crop_img)

			self.image_canvas.create_image(0, 0, anchor=NW, image=self.display_img)

			# Update gia tri cho cac slidebar theo chieu cao cua canvas 
			self.lowerBand_slidebar['from_'] = 1
			self.lowerBand_slidebar['to'] = self.image_canvas_height-2
			self.lowerBand_slidebar['length'] = self.BF_frame_1_2.winfo_height()-4,
			self.higherBand_slidebar['from_'] = 1
			self.higherBand_slidebar['to'] = self.image_canvas_height-2
			self.higherBand_slidebar['length'] = self.BF_frame_1_2.winfo_height()-4,
			self.resultBand_slidebar['from_'] = 1
			self.resultBand_slidebar['to'] = self.image_canvas_height-2
			self.resultBand_slidebar['length'] = self.BF_frame_1_2.winfo_height()-4,

			# Mo khoa cac widget lien quan
			self.bandcheck_button['state'] = 'normal'
			self.higherBand_slidebar['state'] = 'normal'
			self.lowerBand_slidebar['state'] = 'normal'

	def bandcheck_clicked(self):
		self.bandcheck_is_clicked = 1
		firstband_value = int(self.firstband_entry.get())
		lastband_value = int(self.lastband_entry.get())

		if(self.firstband_entry.get()==''):
			messagebox.showwarning("", MainScreen_Language['FirstBand Entry Empty'][language])
		elif(self.lastband_entry.get()==''):
			messagebox.showwarning("", MainScreen_Language['LastBand Entry Empty'][language])
		elif(self.bandsize_entry.get()==''):
			messagebox.showwarning("", MainScreen_Language['ResultBand Entry Empty'][language])
		else:
			firstband_value = int(self.firstband_entry.get())
			lastband_value = int(self.lastband_entry.get())
			if(int(self.bandsize_entry.get()) > firstband_value or int(self.bandsize_entry.get()) < lastband_value):
				messagebox.showwarning("", MainScreen_Language['Band Out Value'][language])
			else:
				self.bandsave_button['state'] = 'normal'
				self.resultBand_slidebar['state'] = 'normal'

				resultband_value = int(self.bandsize_entry.get())
				
				self.a_value = round((self.line2_value.get() - self.line1_value.get())/(math.log10(lastband_value) - math.log10(firstband_value)), 2)
				self.b_value = round(self.line1_value.get() - math.log10(firstband_value)*self.a_value, 2)

				self.band_distance = round(math.log10(resultband_value)*self.a_value + self.b_value)
				self.resultBand_slidebar.set(self.band_distance)

				try:
					self.image_canvas.delete(self.bandline)
				except:
					pass
				
				self.bandline = self.image_canvas.create_line(0,  self.band_distance, self.image_canvas.winfo_width(), self.band_distance, fill=RESULTBAND_COLOR, width=1)

				
				
	def bandsave_clicked(self):
		save_dir = filedialog.asksaveasfile(filetypes=[("jpg file", ".jpg")], defaultextension = '.jpg')
		if save_dir is not None:
			dir_name = save_dir.name
			result_img = cv2.imread(self.openfile_name)
			new_band_distance = round((self.band_distance + band_offset) * self.canvas_image_percent/100)
			start_point = (0, new_band_distance)
			end_point = (RESULT_IMAGE_WIDTH,  new_band_distance)
			save_img = cv2.line(result_img, start_point, end_point, (0,255,0), 1)
			save_img = cv2.putText(result_img, self.bandsize_entry.get()+' bp', (RESULT_IMAGE_WIDTH-200,RESULT_IMAGE_HEIGHT-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
			save_name = os.path.splitext(dir_name)[0]
			cv2.imwrite(save_name +'.jpg', save_img)
			msg = messagebox.showinfo("","Saved.")

	def login_clicked(self):
		global account_active, email_password, email_address
		if(self.login_button['text'] == "Login"):
			if(self.email_entry.get()==''):
				messagebox.showwarning("", MainScreen_Language['Email Empty'][language])
			elif(self.password_entry.get()==''):
				messagebox.showwarning("", MainScreen_Language['Password Empty'][language])
			else:
				mail_address = self.email_entry.get()
				password = self.password_entry.get()
				self.hidepass_checkbutton.select()
				self.hide_charaters()

				addressToVerify = mail_address
				match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
				if(match == None):
					messagebox.showwarning("", MainScreen_Language['Email Error'][language])
				else:
					try:
						domain_name = mail_address.split('@')[1]
						records = dns.resolver.resolve(domain_name, 'MX')
						mxRecord = records[0].exchange
						mxRecord = str(mxRecord)

						host = socket.gethostname()

						server = smtplib.SMTP()
						server.set_debuglevel(0)

						server.connect(mxRecord)
						server.helo(host)
						server.mail('me@domain.com')
						code, message = server.rcpt(str(addressToVerify))
						server.quit()

						if(code==250):
							server=smtplib.SMTP('smtp.gmail.com:587')
							server.starttls()
							try:
								server.login(mail_address,password)
								save_file = open("/home/pi/VE100/.account.txt","w")
								save_file.writelines('1' + "\n")
								save_file.writelines(mail_address + "\n")
								save_file.writelines(password + "\n")

								messagebox.showinfo("", MainScreen_Language['Login Successful'][language])

								account_active = 1
								email_address = mail_address
								email_password = password

								self.connect_clicked()
								# self.login_button['text'] = "Logout"
								# self.email_entry['state'] = "disable"
								# self.password_entry['state'] = "disable"

							except:
								messagebox.showerror("", MainScreen_Language['Password Incorrect'][language])
						else:
							messagebox.showerror("", MainScreen_Language['Email Incorrect'][language])
							
					except:
						messagebox.showerror("", MainScreen_Language['Login Unsuccessful'][language])
						pass
					server.quit()
		else:
			msg = messagebox.askquestion("", MainScreen_Language['Logout Ask'][language])
			if(msg=='yes'):
				save_file = open("/home/pi/VE100/.account.txt","w")
				save_file.writelines('0' + "\n")
				save_file.writelines("\n")
				save_file.writelines("\n")
				save_file.close()

				account_active = 0
				email_address = '\n'
				email_password = '\n'

				# self.login_button['text'] = "Login"
				# self.email_entry['state'] = "normal"
				# self.password_entry['state'] = "normal"
				self.connect_clicked()

	def save_clicked(self):
		global language
		if(self.language_combobox.current() == 0): 
			language = 0
			fw = open(working_dir + "/language.txt",'w')
			fw.writelines(["0\n"])
			fw.close()
		else:
			language = 1
			fw = open(working_dir + "/language.txt",'w')
			fw.writelines(["1\n"])
			fw.close()

		msg = messagebox.askquestion("", MainScreen_Language['Language Restart'][language])
		if(msg=='yes'):
			try:
				camera.close()  # Giải phóng camera đúng cách
			except:
				pass  # Nếu camera đã bị đóng rồi
	
			python = sys.executable
			os.execl(python, python, *sys.argv)
		else:
			pass
		

	# def reset(self, class_name, class_instance):
	# 	self.base_window.frame_list.remove(self.base_window.page)
	# 	del self.base_window.page
	# 	self.base_window.page = class_instance
	# 	self.base_window.frame_list.append(self.base_window.page)


class MainWindow(Tk): 
	def __init__(self):
		Tk.__init__(self)

		# Main window settting
		self.title("VE100")
		self.configure(background = APP_BGD_COLOR)
		self.resizable(TRUE, TRUE)
		self.attributes('-fullscreen', TRUE)

		self.page_num = 0 
		self.frame_list = []
		self.trial_days= 0

		self.main_menu = MainMenu(self)
		self.sample_naming = SampleNaming_Screen(self)
		self.multi_setting = MultiSetting_Screen(self)
		self.multi_run = MultiRun_Screen(self)

		self.frame_list.append(self.main_menu)
		self.frame_list.append(self.sample_naming)
		self.frame_list.append(self.multi_setting)
		self.frame_list.append(self.multi_run)

		self.switch_page(self.main_menu)

	def forget_page(self):
		self.frame_list[self.page_num].forget()
	def switch_page(self, page_name):
		self.forget_page()
		self.page_num = self.frame_list.index(page_name)
		self.frame_list[self.page_num].tkraise()
		self.frame_list[self.page_num].grid(row=0, column=0, sticky="nsew")
	def reset(self):
		self.frame_list.remove(self.sample_naming)
		self.frame_list.remove(self.multi_setting)
		self.frame_list.remove(self.multi_run)

		del self.sample_naming
		del self.multi_setting
		del self.multi_run

		self.sample_naming = SampleNaming_Screen(self)
		self.multi_setting = MultiSetting_Screen(self)
		self.multi_run = MultiRun_Screen(self)

		self.frame_list.append(self.sample_naming)
		self.frame_list.append(self.multi_setting)
		self.frame_list.append(self.multi_run)
		
		
################################ MAIN ##################################
if __name__ == "__main__":
	app = MainWindow()
	app.rowconfigure(0, weight=1)
	app.columnconfigure(0, weight=1)
	app.attributes("-topmost", False)
	screen_width = app.winfo_width()
	screen_height = app.winfo_height()
	print("screen_width: ", screen_width)
	print("screen_height: ", screen_height)
	app.mainloop()
