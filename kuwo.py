import requests
import json
from tkinter import *
from tkinter import messagebox

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
	'Cookie': 'kw_token=BP8XTY9W9TP',
	'csrf': 'BP8XTY9W9TP',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6'
}

class Hide:
    # kw = input('请输入歌曲名称:')
    def get_music(self):
        # e1.get()
        ceshi = {
            'key': e1.get(),
            'pn': 1,
            'rn': '1',
            'httpsStatus': '1',
            'reqId': 'df82d61b91de0a53f72e5e6ec720eedb',
        }
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
        res = requests.get(url,headers=headers,params=ceshi)
        json_list = json.loads(res.text)['data']
        for i in json_list['list']:

            name = i['name']
            artist = i['artist']
            # 文本框
            text.insert(END, '名称:{}'.format(name))
            text.insert(END, '歌手:{}'.format(artist))
            # 文本框滚动
            text.see(END)
            # 更新
            text.update()
    def downloadall(self):
        ceshi = {
            'key': e1.get(),
            'pn': 1,
            'rn': '1',
            'httpsStatus': '1',
            'reqId': 'df82d61b91de0a53f72e5e6ec720eedb',
        }
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
        res = requests.get(url, headers=headers, params=ceshi)
        # 转成字典
        json_list = json.loads(res.text)['data']
        for i in json_list['list']:
            rid = i['rid']
            name = i['name']
            url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1591364466986&httpsStatus=1&reqId=352286c0-a732-11ea-82f8-3d82e3bf3067'.format(rid)
            res2 = requests.get(url)
            music_list = json.loads(res2.text)
            print(music_list['url'])
            music = requests.get(music_list['url']).content
            with open(r'E:\music\{}.mp3'.format(name),'wb') as f:
                try:
                    f.write(music)
                    messagebox.showinfo(message="{}下载成功".format(name))
                    f.close()
                except:
                    pass


hide = Hide()
# hide.get_music()
# 主窗口
root = Tk()
root.title('阿琨音乐下载器')
root.geometry('400x450')
# tktable = Button(root,text='搜索',fg='blue',command=get_music)
# tktable.pack()
Label(root,text='输入歌曲名称:').grid(row=0,column=0)
# Label(root,text='作者').grid(row=1,column=0)
e1 = Entry(root)
e1.grid(row=0,column=1,padx=10,pady=5)
text = Listbox(root,width=35,heigh=20)
# text.bind('<Double-Button-1>',downloadone)
text.grid(row=1,columnspan=2)
Button(root,text='搜索',width=10,command=hide.get_music).grid(row=3,column=0,sticky=W,padx=10,pady=5)
button1 = Button(root,text='退出',width=10,command=root.quit)
button1.grid(row=3,column=1,sticky=E,padx=10,pady=5)
# Button(root,text='单曲下载',width=10)\
#     .grid(row=2,column=0,sticky=E,padx=100,pady=100)
button2 = Button(root,text="单曲下载",width="8",bd=3,command=hide.downloadall).place(relx=0.8,rely=0.4,relheight=0.08)
# button3 = Button(root,text="试听",width="8",bd=3).place(relx=0.8,rely=0.6,relheight=0.08)
# button4 = Button(root,text="单曲下载",width="8",bd=3).place(relx=0.8,rely=0.2,relheight=0.08)
root.mainloop()
