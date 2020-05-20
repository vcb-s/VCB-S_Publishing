import pyperclip

# 工具函数
def line(text=''):
    '''
    automatically starts a new line, indent, and finish with <br>
    YOU NEED THIS FOR ALMOST ALL TEXTS!
    '''
    string = f'\n\t{text}<br>'
    return string

def clean(paste):
    '''
    takes an input string from pyperclip.paste()
    return a string that remove all the empty lines ('\r')
    v2:
    also replace all 'enter' with <br>
    replace all empty lines with <br>
    '''
    line_list = paste.split('\r')
    paste_cleaned = ''.join(line_list)
    line_list = paste_cleaned.split('\n') #v2
    paste_cleaned = '<br>\n\t'.join(line_list)
    return paste_cleaned

def write_to_files(text):
    HTML = open('BGM.html', 'w', encoding = 'utf-8')
    HTML.write(text)
    HTML.close()

    TXT = open('BGM.txt', 'w', encoding = 'utf-8')
    TXT.write(text)
    TXT.close()

# 需要生成的各个部分
def poster():
    string = ''
    string += '<p>'

    poster_url = input('输入宽度800海报的链接，然后回车：').strip()
    string += line(f'<img src="{poster_url}" alt="image">')
    # poster_raw = input('有爱请输入原图链接，没有则直接回车：').strip()
    # if poster_raw:
    #     string += line(f'<a href="{poster_raw}"><img src="{poster_url}"></a>')

    string += line()
    return string

def recruit():
    string = ''

    recruit = input('招新吗？有则输入任意字符然后回车，没有则直接回车：')
    if recruit:
        string += line(f'<strong><span style="color:#c0504d" data-redactor-tag="span">VCB-Studio 2019 秋季招新中，\
有兴趣的同学请访问我们的主页了解相关情况：<b><a href="https://vcb-s.com/archives/11199">\
https://vcb-s.com/archives/11199</a></b></span></strong>')
        print('# 警告：可能需要手动修改招新时间与链接')
        string += line() #indent 保证无招新也不会多一空行
    string += '\n'
    return string

def info(name_long):
    string = ''

    name_ch = input('输入中文番名，然后回车：').strip()
    name_en = input('输入英文番名，然后回车：').strip()
    name_jp = input('输入日文番名，然后回车：').strip()
    print('# 作品性质范例：')
    print('# BDRip')
    print('# S1-3 BDRip')
    print('# BDRip MP4 Ver')
    print('# S1+S2+OVA BDRip Reseed')
    package_type = input('输入作品性质，然后回车：').strip()
    if name_long:
        string += line(f'{name_ch} {package_type}')
        string += line(f'{name_en} {package_type}')
        string += line(f'{name_jp} {package_type}')
    else:
        string += line(f'{name_ch} / {name_en} / {name_jp} {package_type}')

    print('# 格式及大小范例：')
    print('# 10-bit 1080p AVC + FLAC，MKV 格式。约 650 MB 一集。')
    print('# 10-bit 1080p HEVC + FLAC + AAC，MKV 格式。每话约 1.1 GB。')
    print('# 8-bit 720p HEVC + AAC，MP4 格式。每话约 250 MB。')
    format_and_size = input('输入格式及大小，然后回车：').strip()
    string += line(format_and_size)
    subtitle = input('输入内嵌字幕信息，没有则直接回车：').strip()
    if subtitle:
        string += line(subtitle)
    track = input('输入内嵌/外挂音轨信息，没有则直接回车：').strip()
    if track:
        string += line(track)

    string += line()
    return string

def collaboration():
    string = ''

    sub_dict = {'千夏字幕组': 'Airota', '喵萌奶茶屋': 'Nekomoe kissaten',
                '悠哈璃羽字幕社': 'UHA-WINGS', '诸神字幕组': 'Kamigami',
                '天香字幕社': 'T.H.X', '动漫国字幕组': 'DMG',
                '星空字幕组': 'XKsub', '茉语星梦': 'MakariHoshiyume',
                '风之圣殿': 'FZSD', '白恋字幕组': 'Shirokoi',
                '西农YUI': 'YUI-7', '豌豆字幕组': 'BeanSub',
                'SweetSub': 'SweetSub'}
    print('现有字幕组名单:', sub_dict.keys())
    sub_ch1 = input('输入合作字幕组1中文名（无合作直接按回车）：').strip()
    if sub_ch1:
        sub_en1 = sub_dict[sub_ch1]
        sub_ch2 = input('输入合作字幕组2中文名（没有则直接按回车）：').strip()
        if sub_ch2:
            sub_en2 = sub_dict[sub_ch2]
            string += line(f'这个项目与 <strong>{sub_ch1}</strong> 和 <strong>{sub_ch2}</strong> 合作，感谢他们精心制作的字幕。')
            string += line(f'This project is in cooperation with <strong>{sub_en1}</strong> and <strong>{sub_en2}</strong>. Thanks to them for elaborating Chinese subtitles.')
            string += line()
        else:
            string += line(f'这个项目与 <strong>{sub_ch1}</strong> 合作，感谢他们精心制作的字幕。')
            string += line(f'This project is in cooperation with <strong>{sub_en1}</strong>. Thanks to them for elaborating Chinese subtitles.')
            string += line()
    # 空一行的任务交给if else 内了，因为不一定有字幕组
    return string

def comment(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        pyperclip.copy('')
        input('前往U2，复制中文评论（注意中英文之间之间半角空格），然后回车')
        com_ch = line(clean(pyperclip.paste().strip()))
        input('前往U2，复制英文评论，然后回车')
        com_en = line(clean(pyperclip.paste().strip()))
        pyperclip.copy('')
        input('前往U2，复制其他评论，然后回车，没有则直接回车')
        com_other = line(clean(pyperclip.paste().strip()))
        if com_other:
            string += (f'{com_ch}{com_en}{line()}{com_other}')
        else:
            string += (f'{com_ch}{com_en}')
        print('# 警告：如果段落较多，请手动检查段之间的空行<br>')

        string += line()
        string += '\n</p>\n<hr>\n'
        return string


def staff(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''
        string += '<p>'

        string += line(f'感谢所有参与制作者 / Thank to our participating members: ')
        pyperclip.copy('')
        input('前往U2，复制制作人员信息，然后回车')
        paste = clean(pyperclip.paste().strip())
        string += line(paste)

        string += line()
        return string

def source(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        string += line(f'感谢所有资源提供者 / Thank to all resource providers: ')
        pyperclip.copy('')
        input('前往U2，复制资源提供者信息，然后回车')
        paste = clean(pyperclip.paste().strip())
        string += line(paste)

        string += line()
        string += '\n</p>\n<hr>\n'
        return string

def miscellaneous(mobile_version, name_long):
    '''
    项目名过长提示
    WebP图片格式提示
    播放器教程
    '''
    string = ''
    string += '<p>'

    if name_long:
        string += line('本项目文件名较长，下载时请注意存放路径，以免发生无法下载的情况。')
        string += line('Please be mindful of long paths in this torrent to avoid download error. ')
        string += line()
    WebP = input('有WebP扫图吗？有则输入任意字符然后回车，没有直接回车：')
    if WebP:
        string += line('本资源扫图格式为 WebP，浏览详情请参见 <a href="https://vcb-s.com/archives/7949" target="_blank">https://vcb-s.com/archives/7949</a>。')
        string += line('Please refer to <a href="https://vcb-s.com/archives/7949" target="_blank">https://vcb-s.com/archives/7949</a> if you have trouble viewing WebP images. ')
        string += line()

    if mobile_version:
        string += line('基础播放器教程： <a href="https://vcb-s.com/archives/4384" target="_blank">PotPlayer</a> / <a href="https://vcb-s.com/archives/4407" target="_blank">MPC-HC</a> / <a href="https://vcb-s.com/archives/7159" target="_blank">IINA</a>')
        string += line('中文字幕分享区： <a href="http://bbs.vcb-s.com/forum-37-1.html" target="_blank">VCB-Studio 分享论坛</a>（请善用搜索）')
        string += line('项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a>（每月初更新）')
    else:
        string += line('基础播放器教程： <a href="https://vcb-s.com/archives/4384" target="_blank">PotPlayer</a> / <a href="https://vcb-s.com/archives/4407" target="_blank">MPC-HC</a> / <a href="https://vcb-s.com/archives/7159" target="_blank">IINA</a>')
        string += line('进阶播放器教程： <a href="https://vcb-s.com/archives/5610" target="_blank">madVR</a> / <a href="https://vcb-s.com/archives/7228" target="_blank">PotPlayer+madVR</a> / <a href="https://vcb-s.com/archives/7594" target="_blank">mpv</a>')
        string += line('中文字幕分享区： <a href="http://bbs.vcb-s.com/forum-37-1.html" target="_blank">VCB-Studio 分享论坛</a>（请善用搜索）')
        string += line('项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a>（每月初更新）')

    string += line()
    string += '\n</p>\n<hr>\n'
    return string

def screenshot(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        pyperclip.copy('')
        input('请到总监吐糟中，复制<a href>开头结尾的代码（从<p>Comparison开始），然后回车')
        string += pyperclip.paste().strip()
        return string

def comment_reseed():
    string = ''

    pyperclip.copy('')
    input('复制之前帖子上的中文评论（注意中英文之间之间半角空格），然后回车')
    com_ch = line(clean(pyperclip.paste().strip()))
    input('复制之前帖子上的英文评论，然后回车')
    com_en = line(clean(pyperclip.paste().strip()))

    string += (f'{com_ch}{com_en}')
    print('# 警告：如果段落较多，请手动检查段之间的空行<br>')

    string += line()
    string += '\n</p>\n<hr>\n'
    return string

def reseed_info():
    string = ''
    string += '<p>'

    string += line('重发修正：')
    pyperclip.copy('')
    input('复制中文的重发修正（注意中英文之间之间半角空格），然后回车')
    com_ch = line(clean(pyperclip.paste().strip()))
    string += line()
    string += line('Reseed comment:')
    pyperclip.copy('')
    input('复制英文的重发修正，然后回车')
    com_en = line(clean(pyperclip.paste().strip()))

    string += line()
    string += '\n</p>\n<hr>\n'

    #重发计划说明
    string += '<p>'

    string += line('这份发布来自 VCB-Studio 每月老番重发计划。')
    string += line('我们计划在每月月中和月末，重发 VCB-Studio 曾经发布过的合集。选择的合集有这些特点： ')
    string += line('1. 发布已久，公网已经或者几乎断种；')
    string += line('2. 存在制作错误或疏漏，尤其当存在补丁包修正；')
    string += line('3. 之前的发布为分卷或分季，适合补充一个系列合集。')
    print('# 重发时间范例：')
    print('# 2016 年 9 月，月中')
    reseed_date = input('输入本次重发时间（注意空格）：')
    string += line(reseed_date)

    string += line()
    string += '\n</p>\n<hr>\n'
    return string

def miscellaneous_reseed():
    string = ''
    string += '<p>'

    string += line('基础播放器教程： <a href="https://vcb-s.com/archives/4384" target="_blank">PotPlayer</a> / <a href="https://vcb-s.com/archives/4407" target="_blank">MPC-HC</a> / <a href="https://vcb-s.com/archives/7159" target="_blank">IINA</a>')
    string += line('进阶播放器教程： <a href="https://vcb-s.com/archives/5610" target="_blank">madVR</a> / <a href="https://vcb-s.com/archives/7228" target="_blank">PotPlayer+madVR</a> / <a href="https://vcb-s.com/archives/7594" target="_blank">mpv</a>')
    string += line('中文字幕分享区： <a href="http://bbs.vcb-s.com/forum-37-1.html" target="_blank">VCB-Studio 分享论坛</a>（请善用搜索）')
    string += line('项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a>（每月初更新）')

    string += line()
    string += '\n</p>\n<hr>\n'
    return string

'''
def screenshot_reseed():
    string = ''

    pyperclip.copy('')
    input('请到总监吐糟中，复制<a href>开头结尾的代码（从<p>Comparison开始），然后回车')

    string += pyperclip.paste().strip()
    return string
'''

# 新番/重发
def new_project():
    str_parts = []

    str_parts.append(poster())
    str_parts.append(recruit())
    global long
    long = input('番名长吗？长则输入任意字符然后回车，没有则直接回车：')
    str_parts.append(info(long))
    str_parts.append(collaboration())
    global mobile
    mobile = input('是小体积版吗？是则输入任意字符然后回车，没有直接回车：')
    str_parts.append(comment(mobile))
    str_parts.append(staff(mobile))
    str_parts.append(source(mobile))
    str_parts.append(miscellaneous(mobile, long))
    str_parts.append(screenshot(mobile))

    text = ''.join(str_parts)
    return text

def reseed():
    str_parts = []

    str_parts.append(poster())
    str_parts.append(recruit())
    global long
    long = input('番名长吗？长则输入任意字符然后回车，没有则直接回车：')
    str_parts.append(info(long))
    str_parts.append(collaboration())
    str_parts.append(comment_reseed())
    # 目前是reseed不考虑小体积版
    str_parts.append(reseed_info())
    str_parts.append(miscellaneous_reseed())
    # str_parts.append(screenshot_reseed()) # 不知道需不需要

    text = ''.join(str_parts)
    return text

#主程序
print('#本工具将生成 bangumi.moe 发布代码 txt 及预览 html')
print('#请注意区分“输入”和“复制”')
while True:
    project_type = input('新番（1）或重发项目（2）：')
    if project_type not in ['1', '2']:
        print('请输入数字"1"或"2"')
    else:
        if project_type == '1':
            output_text = new_project()
            break
        else:
            output_text = reseed()
            break
write_to_files(output_text)
input('（按回车退出）')

